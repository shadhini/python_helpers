import os

local_file_path = "/home/shadhini/dev/repos/shadhini/python_helpers/gcloud_gsutils/temp.txt"
bucket_output_dir = "wrf_nfs/wrf/temp/"

os.system("gsutil cp {} gs://{}".format(local_file_path, bucket_output_dir))

# OR (if the above command doesn't work and gives a "gsutil comman not found error",
# give the absolute path to gsutil binaries in the command as follows)

os.system("/home/muditha/google-cloud-sdk/bin/gsutil cp {} gs://{}".format(local_file_path, bucket_output_dir))