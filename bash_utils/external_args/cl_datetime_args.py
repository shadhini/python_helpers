import getopt
import sys
import traceback
from datetime import datetime, timedelta


def usage():
    usageText = """

    -h  --help          Show usage
    -r  --run           GFS run. e.g: d0 (for yesterday gfs data), d1 (for today gfs data) 
    -D  --date          Run date. e.g.: 2019-10-07 (date of the directory containing the wrf output to be used)

    """
    print(""+ usageText)


if __name__ == "__main__":

    try:

        gfs_run = None
        date = None

        try:
            opts, args = getopt.getopt(sys.argv[1:], "h:r:D:",
                                       ["help", "run=", "date="])
        except getopt.GetoptError:
            usage()
            sys.exit(2)
        for opt, arg in opts:
            if opt in ("-h", "--help"):
                usage()
                sys.exit()
            elif opt in ("-r", "--run"):
                gfs_run = arg.strip()
            elif opt in ("-D", "--date"):
                date = arg.strip()

        print("Data received: ", gfs_run, date)
        print(datetime.strptime(date, "%Y-%m-%d %H:%M:%S") + timedelta(days=1))

    except Exception as e:
        traceback.print_exc()
    finally:
        print("Process finished!")
