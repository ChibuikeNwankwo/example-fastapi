from passlib.context import CryptContext
pwd_context = CryptContext(schemes=['bcrypt'], deprecated = "auto")

def hash(password: str):         # this hash our paswords so that no one can access the original password
    return pwd_context.hash(password)

def verify(plain_password, hashed_password):              # this verifies whether the password entered is the same as the password already stored
    return pwd_context.verify(plain_password, hashed_password)