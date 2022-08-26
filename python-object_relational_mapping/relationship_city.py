#!/usr/bin/python3
"""module for the cities table model"""

from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import State, Base


class City(Base):
    """State model class for the states table"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
