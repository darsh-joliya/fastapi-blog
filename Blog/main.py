from fastapi import FastAPI
import models
from database import engine

from routers import blog,user,login

app = FastAPI()

models.Base.metadata.create_all(engine)


app.include_router(blog.routers)
app.include_router(user.routers)
app.include_router(login.router)



