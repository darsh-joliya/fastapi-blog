from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
import schemas, database, auth
from repository import blog
import models

routers = APIRouter(
    prefix='/blog',
    tags=['Blogs']
)

# Get all blogs
@routers.get('/', response_model=List[schemas.BlogResponse])
def view_blog(
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    return blog.get_all(db)

# Get a single blog by ID
@routers.get('/{id}', response_model=schemas.BlogResponse, status_code=200)
def show(
    id: int,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    return blog.show(id, db)

# Create a new blog
@routers.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.BlogResponse)
def create(
    request: schemas.Blog,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    return blog.create(request, db)

# Delete a blog by ID
@routers.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(
    id: int,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    return blog.delete(id, db)

# Update a blog by ID
@routers.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(
    id: int,
    request: schemas.Blog,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    return blog.update(id, request, db)
