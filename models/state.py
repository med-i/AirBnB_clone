#!/usr/bin/python3
''' state class that inherit from BaseModel '''
from models.base_model import BaseModel


class State(BaseModel):
    ''' stat class that inherit from BaseModel '''

    name = ""

    def __init__(self, *args, **kwargs):
        ''' Initializition. '''
        super().__init__(*args, **kwargs)
