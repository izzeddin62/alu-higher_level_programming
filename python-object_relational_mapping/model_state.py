#!/usr/bin/python3
"""state model for states"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """State model class"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name =  Column(String(128), nullable=false)
