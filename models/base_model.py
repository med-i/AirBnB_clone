#!/usr/bin/env python3
''' the base of all other classes in this project '''
import uuid
from datetime import datetime
import models


class BaseModel():
    '''
    Bass class that defines all common attributes/methods for other classes
    '''

    def __init__(self, *args, **kwargs):
        ''' Initializes the data.
        Args:
        id: unique number.
        create_at: create datetime
        updated_at: update datetim.
        '''
        if kwargs:
            form = "%Y-%m-%dT%H:%M:%S.%f"
            kwargs['created_at'] = datetime.strptime(
                kwargs['created_at'], form)
            kwargs['updated_at'] = datetime.strptime(
                kwargs['updated_at'], form)
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        ''' print: [<class name>] (<self.id>) <self.__dict__> '''
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        ''' updates the public instance attribute with the current datetime '''
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        '''
        returns a dictionary containing all
        keys/values of __dict__ of the instance
        '''
        attr_dict = dict(self.__dict__)
        attr_dict['__class__'] = self.__class__.__name__
        attr_dict['created_at'] = self.__dict__['created_at'].isoformat()
        attr_dict['updated_at'] = self.__dict__['updated_at'].isoformat()
        return attr_dict
