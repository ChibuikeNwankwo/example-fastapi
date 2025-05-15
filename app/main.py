# importing impotant packages
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app import models
from app.database import engine
from app.routers import post, user, auth, vote
from app.config import settings




# models.Base.metadata.create_all(bind=engine)

# starts the whole process. # the variable name is most time called app
# we use uvicorn (filename):(variable name) --reload in the terminal to launch it
app = FastAPI()

origins = ["https://www.google.com"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
        
app.include_router(post.router) 
app.include_router(user.router)   
app.include_router(auth.router)  
app.include_router(vote.router)    

# this links to the homepage of any site. It's like the base or root and everything else is built on it 
@app.get("/")
def root():
    return  "Hello World!!!!!!!!"
