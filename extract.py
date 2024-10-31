"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    # TODO: Load NEO data from the given CSV file.
    neos = []
    with open(neo_csv_path, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for neo in reader:
            neos.append(NearEarthObject(designation=neo['pdes'], name=neo['name'], diameter = neo['diameter'], hazardous=neo['pha']))
    return neos


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    # TODO: Load close approach data from the given JSON file.
    approaches = []
    with open(cad_json_path, 'r') as file:
        contents = json.load(file)
        # Find the indices of 'des' and 'orbit_id' in the 'fields' list
        des_index = contents['fields'].index('des')
        cd_index = contents['fields'].index('cd')
        dist_index = contents['fields'].index('dist')
        v_rel_index = contents['fields'].index('v_rel')
        
        for cad in contents['data']:
            approaches.append(CloseApproach(designation=cad[des_index], cad_time=cad[cd_index],\
                distance=cad[dist_index],velocity=cad[v_rel_index]))

    return approaches
