import hashlib
import json

def generate_timeseries_id(meta_data):
    # def generate_timeseries_id(meta_data: object) -> object:

    """
    Generate the event id for given metadata
    Only 'sim_tag', 'latitude', 'longitude', 'model', 'version', 'variable', 'unit', 'unit_type'
    are used to generate the id (i.e. hash value)

    :param meta_data: Dict with 'sim_tag', 'latitude', 'longitude', 'model', 'version', 'variable',
    'unit', 'unit_type' keys
    :return: str: sha256 hash value in hex format (length of 64 characters)
    """

    sha256 = hashlib.sha256()
    hash_data = {
        'sim_tag': '',
        'latitude': '',
        'longitude': '',
        'model': '',
        'version': '',
        'variable': '',
        'unit': '',
        'unit_type': ''
    }

    for key in hash_data.keys():
        hash_data[key] = meta_data[key]

    sha256.update(json.dumps(hash_data, sort_keys=True).encode("ascii"))
    event_id = sha256.hexdigest()
    return event_id

meta_data_flo2d_250 = {
        'sim_tag': 'hourly_run',
        'latitude': '6.936840',
        'longitude': '79.985100',
        'model': 'FLO2D',
        'version': '150',
        'variable': 'WaterLevel',
        'unit': 'm',
        'unit_type': 'Instantaneous'
    }

print(generate_timeseries_id(meta_data_flo2d_250))
# 250
# abf71d2d674a0b55ae6600990414ad9133a97d22233533a83e4745e64f736639
# 41c09277e997a53ef5998cd023594e37294090b8779d902371f0d78953fd5099
# 150
# f6fadbaadff1f1ebfde4469a2fd2eed9108eba869a6d7267b9d3efc2582f0d71
# a7b6a8476c9441c6fb5ee08fa913af452ac3a14ec36bb1b8a13c532cf3ac9719
