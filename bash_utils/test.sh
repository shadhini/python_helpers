#!/usr/bin/env bash

HEC_HMS_MODEL_DIR="./2008_2_Events",
DSS_INPUT_FILE="./2008_2_Events/2008_2_Events_input.dss",
HEC_HMS_DIR="/home/uwcc-admin/hechms_hourly/hec-hms41"

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

current_date_time="`date +%Y-%m-%dT%H:%M:%S`";

output_dir="/home/uwcc-admin/hechms_hourly/output"

timeseries_start_date="`date +%Y-%m-%d -d "2 days ago"`"

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

daily_dir="${forecast_date}/${forecast_time}"

current_dir=${output_dir}/${daily_dir}

main() {

    # variable assigning
    forecastStatus=0
    echo "forecastStatus $forecastStatus"

    # if condition on variable value
    if [ ${forecastStatus} == 0 ]; then
        # create directory
        mkdir ${output_dir}

        # check whether a given directory existis
        if [ ! -d "$HEC_HMS_MODEL_DIR" ]; then
            mkdir ${HEC_HMS_MODEL_DIR}
        fi
        yes | cp -R 2008_2_Events_Hack/* ${HEC_HMS_MODEL_DIR} # Copy SOURCE to DEST, or multiple SOURCE(s) to DIRECTORY.
                                                              # -R, -r, --recursive      copy directories recursively

        # Remove file
        rm ${DSS_INPUT_FILE}

        ##########################################################
        # Read Avg precipitation, then create .dss input file for HEC-HMS model
        ./dssvue/hec-dssvue.sh CSVTODSS.py --date ${forecast_date} --time ${forecast_time} \
            `[[ -z ${HEC_HMS_MODEL_DIR} ]] && echo "" || echo "--hec-hms-model-dir $HEC_HMS_MODEL_DIR"`


        # move inside to directory
        cd ${HEC_HMS_DIR}

        HEC_HMS_PROJECT_RELATIVE_PATH="../2008_2_Events"
        HEC_HMS_PROJECT_NAME="2008_2_Events$([[ -z ${TAG} ]] && echo "" || echo "")" # Do nothing
        HEC_HMS_PROJECT_TXT="OpenProject(\"$HEC_HMS_PROJECT_NAME\", \"$HEC_HMS_PROJECT_RELATIVE_PATH\")"

        sed -i "/OpenProject/c\\$HEC_HMS_PROJECT_TXT" ${HEC_HMS_PROJECT_RELATIVE_PATH}

        ./HEC-HMS.sh -s ${HEC_HMS_PROJECT_RELATIVE_PATH}

        # $? is the exit status of the last executed command.
        # For example the command true always returns a status of 0 and false always returns a status of 1:
        ret=$?
        if [ ${ret} -ne 0 ]; then
             echo "Error in running HEC-HMS Model"
             exit 1
        fi

    else
        echo "WARN: Already run the forecast. Quit"
        exit 1
    fi
}

# The $@ variable expands to all the parameters used when calling the function
# If not used inside a function, it specifies all parameters used when calling the script
main "$@"

