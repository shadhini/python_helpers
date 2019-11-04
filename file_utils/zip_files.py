import os
from datetime import datetime, timedelta

###################################################################################
# create tar file from multiple directories withoud retaining directory structure #
###################################################################################
FLO2D_250_RFIELD_DIR = "rain/rfields/flo2d_250"
FLO2D_250_RFIELD_BUCKET_DIR = "/mnt/disks/wrf_nfs/flo2d_raincells/250/rfield"

day_0 = (datetime.now() + timedelta(hours=5, minutes=30)).date()

start = day_0 - timedelta(days=3)
end = day_0 + timedelta(days=2)

delta = end - start  # as timedelta

rfield_locations = ""

for i in range(delta.days + 1):
    day = start + timedelta(days=i)
    dir_path = "{}/{}".format(FLO2D_250_RFIELD_DIR, day.strftime("%Y-%m-%d"))
    if os.path.isdir(dir_path):
        rfield_locations += " {}/*".format(dir_path)

print("{} : ####### Push FLO2D 250 rfields to google bucket".format(datetime.now()))
os.system("tar --transform 's/.*\///g' -czf {}/{}.tar.gz{}".format(FLO2D_250_RFIELD_BUCKET_DIR,
                                                   day_0, rfield_locations))