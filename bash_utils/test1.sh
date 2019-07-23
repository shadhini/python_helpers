#!/usr/bin/env bash


trimQuotes() {
    tmp="${1%\"}"
    tmp="${tmp#\"}"
    echo ${tmp}
}
# replaceStringVariable <variableName> <replacingVariableName> <replacingVariableValue>
replaceStringVariable() {
    # E.g. Working example of replacing "${HEC_HMS_MODEL_DIR}/2008_2_Events_input.dss"
    # with HEC_HMS_MODEL_DIR="./2008_2_Events"
    #
    # if [[ "$DSS_INPUT_FILE" =~ ^\$\{(HEC_HMS_MODEL_DIR)\} ]]; then
    #     DSS_INPUT_FILE=${DSS_INPUT_FILE/\$\{HEC_HMS_MODEL_DIR\}/$HEC_HMS_MODEL_DIR}
    # fi

    if [[ "$1" =~ ^\$\{("$2")\} ]]; then
        echo ${1/\$\{$2\}/"$3"}
    else
        echo $1
    fi
}


ROOT_DIR="$(cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
INIT_DIR=$(pwd)
CONFIG_FILE=${ROOT_DIR}/CONFIG.json

# cd into bash script's root directory
cd ${ROOT_DIR}
echo "Current Working Directory set to -> $(pwd)"
if [ -z "$(find ${CONFIG_FILE} -name CONFIG.json)" ]; then
    echo "Unable to find $CONFIG_FILE file"
    exit 1
fi

INIT_STATE="True"

HEC_HMS_DIR="/home/uwcc-admin/hechms_hourly/hec-hms41"

current_date_time="`date +%Y-%m-%dT%H:%M:%S`";

output_dir="/home/uwcc-admin/hechms_hourly/output"

timeseries_start_date="`date +%Y-%m-%d -d "2 days ago"`"

HEC_HMS_MODEL_DIR="./2008_2_Events"
DSS_INPUT_FILE="./2008_2_Events/2008_2_Events_input.dss",
DSS_OUTPUT_FILE="./2008_2_Events/2008_2_Events_run.dss",
HEC_HMS_CONTROL="./2008_2_Events/Control_1.control",
HEC_HMS_RUN="./2008_2_Events/2008_2_Events.run",
HEC_HMS_GAGE="./2008_2_Events/2008_2_Events.gage",

forecast_date="`date '+%Y-%m-%d'`"
forecast_time="`date '+%H:00:00'`"
force_run=false

while getopts d:t:f: option
do
    case "${option}"
    in
        d) forecast_date=${OPTARG};;
        t) forecast_time=${OPTARG};;
        f) force_run=$OPTARG;;
    esac
done

echo "Run date = $forecast_date"
echo "Run time = $forecast_time"

daily_dir="${forecast_date}/${forecast_time}"

current_dir=${output_dir}/${daily_dir}

main() {
#    local forecastStatus=$(alreadyForecast ${ROOT_DIR}/${STATUS_FILE} ${forecast_date})
#    if [ ${FORCE_RUN} == true ]; then
#        forecastStatus=0
#    fi
    forecastStatus=0
    echo "forecastStatus $forecastStatus"

    if [ ${forecastStatus} == 0 ]; then
        mkdir ${output_dir}
        # HACK: There is an issue with running HEC-HMS model, it gave a sudden value change after 1 day
        # We discovered that, this issue on 3.5 version, hence upgrade into 4.1
        # But with 4.1, it runs correctly when the data are saved by the HEC-HMS program
        # After run the model using the script, it can't reuse for a correct run again
        # Here we reuse a corrected model which can run using the script
        echo "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx--${HEC_HMS_MODEL_DIR}"
        if [ ! -d "$HEC_HMS_MODEL_DIR" ]; then
            mkdir ${HEC_HMS_MODEL_DIR}
        fi
        yes | cp -R 2008_2_Events_Hack/* ${HEC_HMS_MODEL_DIR}

        # Remove .dss files in order to remove previous results
        rm ${DSS_INPUT_FILE}
        rm ${DSS_OUTPUT_FILE}
        # Read Avg precipitation, then create .dss input file for HEC-HMS model
        ./dssvue/hec-dssvue.sh CSVTODSS.py --date ${forecast_date} --time ${forecast_time} \
            `[[ -z ${HEC_HMS_MODEL_DIR} ]] && echo "" || echo "--hec-hms-model-dir $HEC_HMS_MODEL_DIR"`

        # Change HEC-HMS running time window
        ./Update_HECHMS.py -d ${forecast_date} -t ${forecast_time} \
            `[[ ${INIT_STATE} == true ]] && echo "-i" || echo ""` \
            #`[[ ${CONTROL_INTERVAL} == 0 ]] && echo "" || echo "-c $CONTROL_INTERVAL"` \
            #`[[ -z ${HEC_HMS_MODEL_DIR} ]] && echo "" || echo "--hec-hms-model-dir $HEC_HMS_MODEL_DIR"`

        # Run HEC-HMS model
        HEC_HMS_SCRIPT_PATH=${HEC_HMS_MODEL_DIR}/2008_2_Events.script
        # TODO: Check python3 availability
        echo "zzzzzzzzzzzzzzzzzzzzzzzzzz : $HEC_HMS_SCRIPT_PATH"
        #HEC_HMS_SCRIPT_RELATIVE_PATH=$(python3 -c "import os.path; print(os.path.relpath('$HEC_HMS_SCRIPT_PATH', '$HEC_HMS_DIR'))")
        HEC_HMS_SCRIPT_RELATIVE_PATH="../2008_2_Events/2008_2_Events.script"
        cd ${HEC_HMS_DIR}
        #if [ -z "$(find ${HEC_HMS_SCRIPT_RELATIVE_PATH} -name 2008_2_Events.script)" ]; then
        #    echo "Unable to find $HEC_HMS_SCRIPT_RELATIVE_PATH file"
        #    exit 1
        #fi
        # Set FLO2D model path
        #HEC_HMS_PROJECT_RELATIVE_PATH=$(python3 -c "import os.path; print(os.path.relpath('$HEC_HMS_MODEL_DIR', '$HEC_HMS_DIR'))")
        HEC_HMS_PROJECT_RELATIVE_PATH="../2008_2_Events"
        HEC_HMS_PROJECT_NAME="2008_2_Events$([[ -z ${TAG} ]] && echo "" || echo "")" # Do nothing
        HEC_HMS_PROJECT_TXT="OpenProject(\"$HEC_HMS_PROJECT_NAME\", \"$HEC_HMS_PROJECT_RELATIVE_PATH\")"

        sed -i "/OpenProject/c\\$HEC_HMS_PROJECT_TXT" ${HEC_HMS_SCRIPT_RELATIVE_PATH}

        ./HEC-HMS.sh -s ${HEC_HMS_SCRIPT_RELATIVE_PATH}
        ret=$?
        if [ ${ret} -ne 0 ]; then
             echo "Error in running HEC-HMS Model"
             exit 1
        fi
        cd ${ROOT_DIR}
        # Read HEC-HMS result, then extract Discharge into .csv
        ./dssvue/hec-dssvue.sh DSSTOCSV.py --date ${forecast_date} --time ${forecast_time} \
            `[[ -z ${HEC_HMS_MODEL_DIR} ]] && echo "" || echo "--hec-hms-model-dir $HEC_HMS_MODEL_DIR"`
    else
        echo "WARN: Already run the forecast. Quit"
        exit 1
    fi
}

alreadyForecast() {
    local forecasted=0
    while IFS='' read -r line || [[ -n "$line" ]]; do
        if [ $2 == ${line} ]; then
            forecasted=1
            break
        fi
    done < "$1"
    echo ${forecasted}
}

main "$@"

# End of Forecast.sh