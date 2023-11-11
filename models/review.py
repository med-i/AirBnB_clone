#!/usr/bin/python3
''' review class that inherit from BaseModel '''
from models.base_model import BaseModel


class Review(BaseModel):
    ''' review class that inherit from BaseModel '''

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        ''' Initializition. '''
        super().__init__(*args, **kwargs)
