from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
import  database
from sqlalchemy.orm import Session

from repository import login

router = APIRouter(tags=['Login']) 

@router.post('/login')
def login_users(request:OAuth2PasswordRequestForm = Depends(), db:Session = Depends(database.get_db)):

    return login.login_user(request, db)


