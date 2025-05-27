import pytest


def test_abc():
    assert 1 == 1


@pytest.mark.parametrize("email, password, status_code", [
    ("cat@dog.com", "catodog", 200),
    ("cat@dog.com", "cat0dog", 409),
    ("catdogcom", "cat0dog", 422),
                         ])
async def test_register_user(email, password, status_code, async_client):
    response = await async_client.post("/auth/register", json={
        "email": email,
        "password": password,
    })

    assert response.status_code == status_code


@pytest.mark.parametrize("email, password, status_code", [
    ("test@test.com", "test", 200),
    ("artem@example.com", "artem", 200),
    ("diman@example.com", "diman", 401),
                         ])
async def test_login_user(email, password, status_code, async_client):
    response = await async_client.post("/auth/login", json={
        "email": email,
        "password": password,
    })

    assert response.status_code == status_code
