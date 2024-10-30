from app.backend.db import Base


import task
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship



class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True) # - целое число, первичный ключ, с индексом.
    username = Column(String) # - строка.
    firstname = Column(String) #- строка.
    lastname = Column(String) #- строка.
    age = Column(Integer) #- целое число.
    slug = Column(String, unique=True, index=True) #- строка, уникальная, с индексом.
    tasks = relationship('Task', back_populates='user') # - объект связи с таблицей с таблицей Task, где back_populates='user'.



from sqlalchemy.schema import CreateTable
print(CreateTable(User.__table__))