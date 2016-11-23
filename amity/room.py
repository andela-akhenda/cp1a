class Room(object):
    ''' Room Class

        This is the Super Class that handles the creation of Rooms
        in the Amity System. It relies heavily on the information it
        gets from it's Child Classes.
    '''

    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.total_persons = 0
        self.allocated_persons = []

    def add_person(self, uuid):
        ''' This method is responsible for adding a person to a room. '''
        pass

    def remove_person(self, uuid):
        ''' This method is responsible for removing a person from a room. '''
        pass


class Office(Room):
    ''' Office Class

        This is one of the Child Classes that inherits from the Room
        Super Class. It passes information to the Parent Constructor
        so as to dictate how the Room is created. It also handles
        other activities related to a Office.
    '''
    number_of_offices = 0

    def __init__(self, name):
        super(Office, self).__init__(name, "Office")
        self.max_persons = 6


class LivingSpace(Room):
    ''' LivingSpace Class

        This is one of the Child Classes that inherits from the Room
        Super Class. It passes information to the Parent Constructor
        so as to dictate how the Room is created. It also handles
        other activities related to a Living Space.
    '''
    number_of_living_spaces = 0

    def __init__(self, name):
        super(LivingSpace, self).__init__(name, "Living Space")
        self.max_persons = 4
