import pytest
import requests
from config import Config


@pytest.fixture(scope="session")
def company_id():
    creds = {
        "login": Config.LOGIN,
        "password": Config.PASSWORD,
        "name": Config.NAME_COMPANY
    }
    resp = requests.post(Config.REQUEST_URL + 'api-v2/auth/companies',
                         json=creds)
    assert resp.status_code == 200

    company = resp.json()
    id_company = company["content"][0]["id"]
    return id_company


@pytest.fixture
def api_token(company_id):
    creds = {
        "login": Config.LOGIN,
        "password": Config.PASSWORD,
        "companyId": company_id
    }
    resp = requests.post(Config.REQUEST_URL + 'api-v2/auth/keys/get',
                         json=creds)
    assert resp.status_code == 200
    return resp.json()[0]['key']
