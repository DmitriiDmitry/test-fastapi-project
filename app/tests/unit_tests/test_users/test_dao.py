import pytest

from app.users.dao import UsersDAO


@pytest.mark.parametrize("user_id, email, is_present", [
    (1, "test@test.com", True),
    (2, "artem@example.com", True),
    (4, "email@email.com", False)
])
async def test_find_user_by_id(user_id, email, is_present):
    user = await UsersDAO.find_by_id(user_id)

    if is_present:
        assert user
        assert user.email == email
        assert user.id == user_id
    else:
        assert not user

