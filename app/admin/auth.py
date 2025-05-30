from typing import Optional

#from app.logger import logger
from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request
from starlette.responses import RedirectResponse
from starlette.status import HTTP_302_FOUND

from app.users.auth import authenticate_user, create_access_token
from app.users.dependencies import get_current_user


class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> RedirectResponse:
        form = await request.form()
        email, password = form["username"], form["password"]

        user = await authenticate_user(email, password)
        if user:
            access_token = create_access_token({"sub": str(user.id)})
            request.session.update({"token": access_token})
            return RedirectResponse(request.url_for("admin:index"), status_code=HTTP_302_FOUND)

        return RedirectResponse(request.url_for("admin:login"), status_code=HTTP_302_FOUND)

    async def logout(self, request: Request) -> bool:
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> Optional[RedirectResponse]:
        token = request.session.get("token")

        if not token:
            return RedirectResponse(request.url_for("admin:login"), status_code=302)

        user = await get_current_user(token)
        #logger.debug(f"{user=}")
        if not user:
            return RedirectResponse("/admin/login", status_code=302)
        return None


authentication_backend = AdminAuth(secret_key="...")