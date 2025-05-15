from fastapi import Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from app.database import get_db
from app import schemas, models, utils, oauth2

router = APIRouter(tags=['Authentication'])       # the tags argument is to group all gateways from this script together when viewing it with swagger ui

@router.post('/login', response_model=schemas.Token)          # this is to login our users
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):


    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f'Invalid Credentials')

    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f'Invalid Credentials')
    
    access_token = oauth2.create_access_token(data = {"user_id": user.id})  # create a token
    # return token
    return{"access_token" : access_token, "token_type" : "bearer"}
