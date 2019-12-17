import os

local_file_path = "/home/shadhini/dev/repos/shadhini/python_helpers/gcloud_gsutils/temp.txt"
bucket_output_dir = "wrf_nfs/wrf/temp/"

os.system("gsutil cp {} gs://{}".format(local_file_path, bucket_output_dir))