#!/usr/bin/python3
"""module for the states table model"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class State(Base):
    """State model class for the states table"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', order_by="asc(City.id)")
