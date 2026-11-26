from web import create_app


def test_storages_can_be_created_and_displayed():
    client = create_app().test_client()

    response = client.post("/storages", data={"name": "Apples", "size": "10"})
    assert response.status_code == 302
    response = client.post("/storages", data={"name": "Oranges", "size": "5"})
    assert response.status_code == 302

    response = client.get("/")
    assert response.status_code == 200
    assert b"Apples" in response.data
    assert b"Oranges" in response.data
    assert b"Size: 10.0" in response.data
    assert b"Balance: 0" in response.data


def test_items_can_be_added_and_removed():
    client = create_app().test_client()
    client.post("/storages", data={"name": "Apples", "size": "10"})

    response = client.post("/storages/Apples/add", data={"amount": "8"})
    assert response.status_code == 302
    response = client.post("/storages/Apples/remove", data={"amount": "3"})
    assert response.status_code == 302

    response = client.get("/")
    assert b"Balance: 5.0" in response.data


def test_addition_and_removal_respect_storage_limits():
    client = create_app().test_client()
    client.post("/storages", data={"name": "Apples", "size": "10"})

    client.post("/storages/Apples/add", data={"amount": "15"})
    response = client.get("/")
    assert b"Balance: 10.0" in response.data

    client.post("/storages/Apples/remove", data={"amount": "15"})
    response = client.get("/")
    assert b"Balance: 0.0" in response.data


def test_invalid_storage_is_rejected():
    client = create_app().test_client()

    response = client.post("/storages", data={"name": "Apples", "size": "-1"})
    assert response.status_code == 400
    response = client.post("/storages", data={"name": " ", "size": "10"})
    assert response.status_code == 400
