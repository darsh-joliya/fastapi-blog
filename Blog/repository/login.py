from fastapi import status, HTTPException
from sqlalchemy.orm import Session
import  models
from hashing import Hash
import token_utils
from fastapi.security import OAuth2PasswordRequestForm


def login_user(request: OAuth2PasswordRequestForm, db: Session):
    user = db.query(models.User).filter(models.User.email == request.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Credentials")
    
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect password")
    
    access_token = token_utils.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
