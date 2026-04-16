from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from crud import get_user_by_email, create_user
from api.schema.user_schema import UserRegister, UserLogin, TokenResponse
from api.core.security import hash_password, verify_password, create_access_token

router = APIRouter()


@router.post("/register")
def register(user: UserRegister, db: Session = Depends(get_db)):

    existing_user = get_user_by_email(db, user.email)

    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_pw = hash_password(user.password)
    new_user = create_user(db, user.email, hashed_pw)

    return {"message": "User registered successfully", "email": new_user.email}



@router.post("/login", response_model=TokenResponse)
def login(user: UserLogin, db: Session = Depends(get_db)):

    db_user = get_user_by_email(db, user.email)

    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    if not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    token = create_access_token({"sub": db_user.email})

    return {"access_token": token, "token_type": "bearer"}
