import json


def read_json_file(filepath):
    return json.loads(open(filepath).read())


def update_json_file(filepath, new_info):
    """
    Add new data to existing JSON file, if exists, create new file otherwise
    :param filepath: JSON filepath
    :param new_info: new JSON fields to be added as a JSON file
    :return: True if success, False otherwise
    """

    updated_metadata = {}
    try:
        existing_metadata = json.loads(open(filepath).read())
        updated_metadata = existing_metadata
    except FileNotFoundError as eFNFE:
        pass

    for key in new_info.keys():
        updated_metadata[key] = new_info[key]

    with open(filepath, 'w') as outfile:
        json.dump(updated_metadata, outfile)


new_info = {
    "raincell": "MME"
}
update_json_file('/home/shadhini/dev/repos/shadhini/python_helpers/json_utils/run_meta2.json', new_info)
