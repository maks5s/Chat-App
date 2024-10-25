from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from app.users.dao import UsersDAO
from app.users.dependencies import get_current_user
from app.users.models import User

router = APIRouter(prefix="/chat", tags=["Chat"])
templates = Jinja2Templates(directory="app/templates")


@router.get("/", response_class=HTMLResponse, summary="Chat Page")
async def get_chat_page(request: Request, user_data: User=Depends(get_current_user)):
    users_all = await UsersDAO.find_all()
    return templates.TemplateResponse("chat.html", {"request": request, "user": user_data, "users_all": users_all})
