import json
import os

import pytest

from src.etl.extract import get_all_circuits


@pytest.fixture
def mock_circuits():
    data_dir = os.path.join(os.path.dirname(__file__), "data")
    with open(f"{data_dir}/circuits.json", "r") as fp:
        return json.load(fp)


def test_extract(requests_mock, mock_circuits):
    requests_mock.get(
        "http://ergast.com/api/f1/circuits.json?limit=30&offset=0", json=mock_circuits
    )
    res = get_all_circuits()
    assert len(res) == 3
