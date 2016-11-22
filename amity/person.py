class Person(object):
    ''' Person Class

        This is the Super Class that handles the creation of Persons
        in the Amity System. It relies heavily on the information it
        gets from it's Child Classes.
    '''
    def __init__(self, uuid, name, role):
        self.uuid = uuid
        self.name = name
        self.role = role
        self.allocated_rooms = []

    def print_person(self):
        ''' This method is responsible for printing all the
            Person's details.
        '''
        pass


class Fellow(Person):
    ''' Fellow Class

        This is one of the Child Classes that inherits from the Person
        Super Class. It passes information to the Parent Constructor
        so as to dictate how the Person is created. It also handles
        other responsibilities related to a Fellow.
    '''
    number_of_fellows = 0

    def __init__(self, name):
        Person.__init__("f" + str(self.number_of_fellows + 1), name, "Fellow")

    def is_allocated_room(self):
        pass


class Staff(Person):
    ''' Staff Class

        This is one of the Child Classes that inherits from the Person
        Super Class. It passes information to the Parent Constructor
        so as to dictate how the Person is created. It also handles
        other responsibilities related to a Staff.
    '''
    number_of_staff = 0

    def __init__(self, name):
        Person.__init__("s" + str(self.number_of_staff + 1), name, "Staff")

    def is_allocated_room(self):
        pass
