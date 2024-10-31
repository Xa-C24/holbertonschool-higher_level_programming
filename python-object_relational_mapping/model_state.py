#!/usr/bin/python3
"""
Write a python file that contains the class definition 
of a State and an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Création de la base
Base = declarative_base()

# Définition d'une classe
class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
