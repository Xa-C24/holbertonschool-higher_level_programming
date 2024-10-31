#!/usr/bin/python3
"""
Defines a State class and an instance Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

# Création de la base de données
Base = declarative_base()

# Définition de la classe State
class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
