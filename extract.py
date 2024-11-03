"""Extract data on NEOs and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the
command line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about
    near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    neos = []
    with open(neo_csv_path, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for neo in reader:
            designation = neo['pdes']
            name = neo['name'] if neo['name'] else None
            diameter = float(neo['diameter']) \
                if neo['diameter'] else float('nan')
            hazardous = neo['pha'] == 'Y'
            # Create a NEO instance and add to list
            neos.append(NearEarthObject(designation=designation, name=name,
                                        diameter=diameter,
                                        hazardous=hazardous))
    return neos


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about
    close approaches.
    :return: A collection of `CloseApproach`es.
    """
    approaches = []
    with open(cad_json_path, 'r') as file:
        contents = json.load(file)

        # Check if 'fields' exists and contains the required keys
        if 'fields' not in contents or not \
                all(key in contents['fields'] for key in
                    ['des', 'cd', 'dist', 'v_rel']):
            raise ValueError("Required fields are missing in the JSON data.")

        # Find indices of 'des', 'cd', 'v_rel' and 'dist' in the 'fields' list
        des_index = contents['fields'].index('des')
        cd_index = contents['fields'].index('cd')
        dist_index = contents['fields'].index('dist')
        v_rel_index = contents['fields'].index('v_rel')

        for cad in contents['data']:
            # Convert distance and velocity to float
            distance = float(cad[dist_index])\
                if cad[dist_index] else float('nan')
            velocity = float(cad[v_rel_index])\
                if cad[v_rel_index] else float('nan')

            # Create a CloseApproach instance and append to the list
            approaches.append(CloseApproach(
                designation=cad[des_index],
                cad_time=cad[cd_index],
                distance=distance,
                velocity=velocity
            ))

    return approaches
