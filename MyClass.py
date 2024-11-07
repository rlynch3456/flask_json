import uuid

class Person():
    '''
    Simple stub class that will be called from Flask
    '''
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.id = str(uuid.uuid4())

    def __str__(self):
        string = (f'Name: {self.name}\n'
                  f'Age: {self.age}\n'
                  f'ID: {self.id}\n'
        )
        return string