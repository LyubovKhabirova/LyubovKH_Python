from CompanyApi import Company


title = "autotest"


def test_add_project(api_token):
    api = Company(api_token)
    resp = api.create_project(title)
    assert resp.status_code == 201
    data = resp.json()
    assert len(data) > 0


def test_get_project(api_token):
    api = Company(api_token)
    list_project = api.get_project_list()
    id_project = list_project["content"][-1]["id"]

    resp = api.get_project_by_id(id_project)
    assert resp.status_code == 200
    title_project = resp.json()
    assert title_project["title"] == title


def test_update_project(api_token):
    api = Company(api_token)
    body = api.get_project_list()
    len_before = len(body["content"])

    id_project = body["content"][-1]["id"]

    update_project = api.update_project_by_id(id_project, deleted=True)
    assert update_project.status_code == 200

    body = api.get_project_list()
    len_after = len(body["content"])
    assert len_before - len_after == 1
