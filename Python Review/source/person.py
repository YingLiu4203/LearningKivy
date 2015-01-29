class Person:
    def __init__(self, name):
        self._name = name
    
    def get_name(self):
        return self._name
     
    def set_name(self, name):
        self._name = name
    
    # define the property
    name = property(get_name, set_name)
    
person = Person('Alice')
print person.name
person.name = 'Bob'
print person.name