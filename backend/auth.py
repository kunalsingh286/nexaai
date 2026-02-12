from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext

SECRET_KEY = "nexaai-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 1440

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


def hash_password(password: str):

    # bcrypt limit protection
    password = password[:72]

    return pwd_context.hash(password)


def verify_password(password, hashed):

    password = password[:72]

    return pwd_context.verify(password, hashed)


def create_token(data: dict):

    expire = datetime.utcnow() + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    data.update({"exp": expire})

    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
