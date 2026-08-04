import pytest
from CompanyApi import Company


title = "autotest"


def test_add_project_empty_title(api_token):
    api = Company(api_token)
    resp = api.create_project("")
    assert resp.status_code == 400


def test_get_project_invalid_id_type(api_token):
    api = Company(api_token)
    with pytest.raises(TypeError):
        api.get_project_by_id(1234567890)


def test_update_project_not_found(api_token):
    api = Company(api_token)
    invalid_id = "00000000-0000-0000-0000-000000000000"
    resp = api.update_project_by_id(invalid_id, deleted=True)
    assert resp.status_code == 404
    data = resp.json()
    assert "message" in data
    assert "not found" in data["error"].lower()
