from http.client import HTTPException
from typing import List

import requests


def get_all_circuits() -> List[dict]:
    """Gets information about all circuits that hosted F1 races

    Raises:
        HTTPException: if status_code is greater or equal than 400

    Returns:
        List[dict]: a list of circuits
    """
    limit = 30
    offset = 0
    circuits = []
    while True:
        res = requests.get(
            f"http://ergast.com/api/f1/circuits.json?limit={limit}&offset={offset}"
        )
        if res.status_code >= 400:
            raise HTTPException("Could not get data from the API!")
        response = res.json()
        total = int(response["MRData"]["total"])
        circuits.extend(response["MRData"]["CircuitTable"]["Circuits"])
        if total < (limit + offset * limit):
            break
    return circuits
