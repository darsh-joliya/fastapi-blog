from pydantic import BaseModel
from typing import List, Optional

# --- BLOG MODELS ---

class Blog(BaseModel):
    title: str
    body: str

    class Config:
        orm_mode = True


class BlogResponse(Blog):
    id: int
    user_id: int

    class Config:
        orm_mode = True


# --- USER MODELS ---

class User(BaseModel):
    name: str
    email: str
    password: str


class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[BlogResponse]

    class Config:
        orm_mode = True


# --- COMBINED BLOG + USER RESPONSE MODEL ---

class ShowFullBlog(BlogResponse):
    creator: ShowUser

    class Config:
        orm_mode = True


# --- AUTHENTICATION MODELS ---

class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
