from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Blog(Base):
    __tablename__ = 'blogs'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    body = Column(String(1000), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    # Relationship: blog.creator returns the User object
    creator = relationship("User", back_populates="blogs")


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False, index=True)
    password = Column(String(1000), nullable=False)

    # Relationship: user.blogs returns a list of Blog objects
    blogs = relationship("Blog", back_populates="creator", cascade="all, delete-orphan")
