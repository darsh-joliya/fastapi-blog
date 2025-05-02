from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
import schemas,  database
from repository import user

routers = APIRouter(
    prefix='/user',
    tags=['Users']
)



@routers.post('/',  response_model=schemas.ShowUser, status_code=status.HTTP_201_CREATED)
def users(request: schemas.User, db: Session=Depends(database.get_db)):
    
    return user.users(request,db)
    

@routers.get('/{id}',response_model=schemas.ShowUser)
def showuser(id:int, db:Session = Depends(database.get_db)):    
    return user.showuser(id,db)