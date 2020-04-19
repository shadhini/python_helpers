#!"D:\curw_flo2d_data_manager\venv\Scripts\python.exe"

import os, json, traceback
# from db_adapter.curw_fcst.timeseries import insert_run_metadata
from db_adapter.constants import set_db_config_file_path
from db_adapter.constants import connection as con_params
from db_adapter.base import get_Pool

ROOT_DIRECTORY = 'D:\curw_flo2d_data_manager'

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData

def write_file(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)

def insert_run_metadata(pool, sim_tag, source_id, variable_id, fgt, metadata, template=None):
    """
    Insert new run info entry
    :param source_id:
    :param sim_tag:
    :param fgt:
    :param metadata:
    :return:
    """

    connection = pool.connection()
    try:

        sql_statement = "INSERT INTO `run_info` (`sim_tag`, `source`, `variable`, `fgt`, `metadata`) " \
                        "VALUES ( %s, %s, %s, %s, %s)"
        data = (sim_tag, source_id, variable_id, fgt, json.dumps(metadata))

        if template is not None:
            sql_statement = "INSERT INTO `run_info` (`sim_tag`, `source`, `variable`, `fgt`, `metadata`, `template`) " \
                                "VALUES ( %s, %s, %s, %s, %s, %s)"
            data = (sim_tag, source_id, variable_id, fgt, json.dumps(metadata), template)

        with connection.cursor() as cursor:
            cursor.execute(sql_statement, data)

        connection.commit()

        return True
    except Exception as exception:
        connection.rollback()
        traceback.print_exc()
        raise exception
    finally:
        if connection is not None:
            connection.close()

def read_template(pool, sim_tag, source_id, variable_id, fgt, output_file_path):

    connection = pool.connection()
    try:

        with connection.cursor() as cursor:
            sql_statement = "SELECT `template` FROM `run_info` WHERE `sim_tag`=%s and `source`=%s and `variable`=%s and `fgt`=%s"
            row_count = cursor.execute(sql_statement, (sim_tag, source_id, variable_id, fgt))
            if row_count > 0:
                template_data = cursor.fetchone()['template']
                write_file(data=template_data, filename=output_file_path)
            else:
                return None
    except Exception as exception:
        error_message = "Retrieving template failed."
        traceback.print_exc()
        raise exception
    finally:
        if connection is not None:
            connection.close()

set_db_config_file_path(os.path.join(ROOT_DIRECTORY, 'db_adapter_config.json'))

pool = get_Pool(host=con_params.CURW_FCST_HOST, port=con_params.CURW_FCST_PORT, db=con_params.CURW_FCST_DATABASE,
                        user=con_params.CURW_FCST_USERNAME, password=con_params.CURW_FCST_PASSWORD)

source_id = 1
variable_id = 1
sim_tag = "test"
fgt = "2020-04-20 00:00:00"
run_info= {"test": "test1"}
template_path = "D:\\flo2d_output\\flo2d_150\\2020-03-16\\02-00-08\\template.tar.gz"
template = convertToBinaryData(template_path)
insert_run_metadata(pool=pool, source_id=source_id, variable_id=variable_id, sim_tag=sim_tag, fgt=fgt,
                            metadata=run_info, template=template)

output_file_path = "D:\\event_sim\\test\\template.tar.gz"

read_template(pool=pool, source_id=source_id, variable_id=variable_id, sim_tag=sim_tag, fgt=fgt,
                              output_file_path=output_file_path)

