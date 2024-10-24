from fastapi import HTTPException, status
from pydantic import EmailStr
import re

def validate_email(email: str):
    try:
        EmailStr.validate(email)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Invalid email format")

def sanitize_input(input_string: str):
    # Remove any potentially harmful characters
    return re.sub(r'[<>&\'"()]', '', input_string)