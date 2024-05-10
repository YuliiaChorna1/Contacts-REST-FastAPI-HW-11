from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, EmailStr, PastDate
from pydantic_extra_types.phone_numbers import PhoneNumber


class ContactBase(BaseModel):
    name: str = Field(max_length=50)
    surname: str = Field(max_length=80)
    email: EmailStr = Field(max_length=250)
    phone: PhoneNumber
    birthday: PastDate
    address: Optional[str] = Field(max_length=300)


class ContactResponse(ContactBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class ContactUpdate(BaseModel):
    name: Optional[str] = Field(None, max_length=50) 
    surname: Optional[str] = Field(None, max_length=80)
    email: Optional[EmailStr] = Field(None, max_length=250)
    phone: Optional[PhoneNumber] = None
    birthday: Optional[PastDate] = None
    address: Optional[str] = Field(None, max_length=300)

    @property
    def is_dirty(self) -> bool:
        return any(self.__dict__.values())
