import pytest
import requests


@pytest.fixture()
def default_url():
    return 'https://docs.microsoft.com/api/search/'


@pytest.mark.parametrize('payload', [{'search': 'LINQ', 'locale': 'ru-ru'},
                                     {'search': 'LINQ', 'locale': 'ru-ru', 'skip': 25}])
@pytest.mark.parametrize('id', [i for i in range(25)])
def test_API_search(default_url, payload, id):
    resp = requests.get(default_url, params=payload)
    resp_dict = resp.json()
    assert 'LINQ' in resp_dict['results'][id]['title'].upper()
