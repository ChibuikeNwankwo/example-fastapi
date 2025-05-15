from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
from pydantic.types import conint

# we create a class to specify the dtype or schema of our records/columns
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):      # if a class/schema we want to create has the same conditions as a previous one we can just put the class name as the argument and it'll automatically
    pass                         # inherit the conditions instead of us retyping it again and type in any other condition not present or pass if it's exactly the same conditions 

class UserOut(BaseModel):
    id: int
    email: EmailStr 
    created_at: datetime

    class config:
        orm_mode = True

class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    class config:                # when interacting with a database this class is to ensure it converts it using the orm
        orm_mode = True

class UserCreate(BaseModel):
    email: EmailStr
    password: str     

class PostOut(BaseModel):
    post: Post
    votes: int

    class config:                
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None


class Vote(BaseModel):
    post_id: int
    dir: conint(le=1) 