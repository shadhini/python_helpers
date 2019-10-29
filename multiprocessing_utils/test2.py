import multiprocessing_utils as mp
import traceback
from datetime import datetime, timedelta


def write_to_file(file_name, data, string):
    print(string)
    print(datetime.now())
    with open(file_name, 'w+') as f:
        f.write('\n'.join(data))
        f.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


wrf_systems_list = "A,C,E,SE".split(',')

try:
    mp_pool = mp.Pool(mp.cpu_count())

    wrf_results = mp_pool.starmap_async(extract_wrf_data,
                                        [(wrf_system, config_data, tms_meta) for wrf_system in wrf_systems_list]).get()

    print("wrf extraction results: ", wrf_results)
except Exception as e:
    msg = 'Multiprocessing error.'
    traceback.print_exc()
finally:
    mp_pool.close()
