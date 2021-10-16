
import uuid
import datetime


class MadrasRest:
    def __init__(self, **kwargs):
        self.id = uuid.uuid4().__str__() if 'id' not in kwargs.keys() else kwargs['id']
        self.name = kwargs['name']
        self.creation_date = datetime.datetime.now().strftime("%d-%m-%y") \
            if 'creation_date' not in kwargs.keys() else kwargs['creation_date']
        self.status = 'draft' if 'status' not in kwargs.keys() else kwargs['status']
        self.username = '' if 'username' not in kwargs.keys() else kwargs['username']
        self.votes = 0 if 'votes' not in kwargs.keys() else kwargs['votes']

    def png(self):
        return self.name + '.png'

    def json(self):
        return self.name + '.json'

    def __repr__(self):
        return {'id': self.id,
                'name': self.name,
                'creation_date': self.creation_date,
                'status': self.status,
                'username': self.username,
                'votes': self.votes}

    def __str__(self):
        return self.__repr__().__str__()