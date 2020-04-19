#!"D:\curw_flo2d_data_manager\venv\Scripts\python.exe"
import sys
import os

file_names = ["ARF.DAT","CHAN.DAT","HYSTRUC.DAT","MANNINGS_N.DAT","RAIN.DAT","TOPO.DAT",
              "CADPTS.DAT","CONT.DAT","INFIL.DAT","NEIGHBORS.DAT","SUPPLEMENT.DAT","XSEC.DAT",
              "CHANBANK.DAT","FPLAIN.DAT","INFLOW.DAT","OUTFLOW.DAT","TOLER.DAT"]

source_file_dir = sys.argv[1]
zip_file_name =  "template.tar.gz"


def compress_multiple_files(file_names, source_file_dir, zip_file_name):

    # source_file_paths = []
    # for file_name in file_names:
    #     source_file_paths.append(os.path.join(source_file_dir, file_name))

    os.system("cd {} && tar -cvzf {} {}".format(source_file_dir, zip_file_name, " ".join(file_names)))

# source_file_paths = []
# for file_name in file_names:
#     source_file_paths.append(os.path.join(source_file_dir, file_name))

# os.system("cd {} && tar -cvzf {} {}".format(source_file_dir, zip_file_name, " ".join(file_names)))

compress_multiple_files(file_names=file_names, source_file_dir=source_file_dir, zip_file_name=zip_file_name)

