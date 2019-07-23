import getopt
import sys
import os


def usage():

    usageText = """
Usage: ./EXTRACTFLO2DTOWATERLEVEL.py [-d YYYY-MM-DD] [-t HH:MM:SS] [-p -o -h] [-S YYYY-MM-DD] [-T HH:MM:SS]

-h  --help          Show usage
-f  --forceInsert   Force Insert into the database. May override existing values.
-F  --flo2d_config  Configuration for FLO2D model run
-d  --date          Model State Date in YYYY-MM-DD. Default is current date.
-t  --time          Model State Time in HH:MM:SS. If -d passed, then default is 00:00:00. Otherwise Default is current time.
-S  --start_date    Base Date of FLO2D model output in YYYY-MM-DD format. Default is same as -d option value.
-T  --start_time    Base Time of FLO2D model output in HH:MM:SS format. Default is set to 00:00:00
-p  --path          FLO2D model path which include HYCHAN.OUT
-o  --out           Suffix for 'water_level-<SUFFIX>' and 'water_level_grid-<SUFFIX>' output directories.
                    Default is 'water_level-<YYYY-MM-DD>' and 'water_level_grid-<YYYY-MM-DD>' same as -d option value.
-n  --name          Name field value of the Run table in Database. Use time format such as 'Cloud-1-<%H:%M:%S>' to replace with time(t).
-u  --utc_offset    UTC offset of current timestamps. "+05:30" or "-10:00". Default value is "+00:00".
"""
    print(usageText)


date = ''
time = ''
path = ''
output_suffix = ''
start_date = ''
start_time = ''
flo2d_config = ''
run_name_default = 'Cloud-1'
runName = ''
utc_offset = ''
forceInsert = False
try:
    opts, args = getopt.getopt(sys.argv[1:], "hF:d:t:p:o:S:T:fn:u:",
            ["help", "flo2d_config=", "date=", "time=", "path=", "out=", "start_date=",
             "start_time=", "name=", "forceInsert", "utc_offset="])
except getopt.GetoptError:
    usage()
    sys.exit(2)
for opt, arg in opts:
    if opt in ("-h", "--help"):
        usage()
        sys.exit()
    elif opt in ("-F", "--flo2d_config"):
        flo2d_config = arg
    elif opt in ("-d", "--date"):
        date = arg
    elif opt in ("-t", "--time"):
        time = arg
    elif opt in ("-p", "--path"):
        path = arg.strip()
    elif opt in ("-o", "--out"):
        output_suffix = arg.strip()
    elif opt in ("-S", "--start_date"):
        start_date = arg.strip()
    elif opt in ("-T", "--start_time"):
        start_time = arg.strip()
    elif opt in ("-n", "--name"):
        runName = arg.strip()
    elif opt in ("-f", "--forceInsert"):
        forceInsert = True
    elif opt in ("-u", "--utc_offset"):
        utc_offset = arg.strip()