from sqlalchemy import Column, Integer, String
from .base import Base
from passlib import exc
from passlib.hash import argon2


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True)
    password = Column(String(255))

    def is_password_matched(self, raw_password: str) -> bool:
        if self.password is None or len(self.password) == 0:
            return False
        try:
            return argon2.verify(raw_password, self.password)
        except exc.MalformedHashError:
            return False

    @classmethod
    def convert_to_hash(cls, raw):
        return argon2.hash(raw)
