class Room(object):
    ''' Room Class

        This is the Super Class that handles the creation of Rooms
        in the Amity System. It relies heavily on the information it
        gets from it's Child Classes.
    '''
    number_of_offices = 0
    number_of_living_spaces = 0
    rooms = {"Offices": {}, "Living Spaces": {}}

    def __init__(self, name, room_type, capacity):
        room_key = room_type + "s"
        room_id = name.lower()
        self.rooms[room_key][room_id] = {}
        self.rooms[room_key][room_id]["Room Name"] = name
        self.rooms[room_key][room_id]["Room ID"] = room_id
        self.rooms[room_key][room_id]["Capacity"] = capacity
        self.rooms[room_key][room_id]["Total Persons"] = 0
        self.rooms[room_key][room_id]["Occupants"] = {}
        if room_type == "Office":
            Room.number_of_offices += 1
        elif room_type == "Living Space":
            Room.number_of_living_spaces += 1
        # print self.rooms

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

    def __init__(self, name):
        super(Office, self).__init__(name, "Office", 6)


class LivingSpace(Room):
    ''' LivingSpace Class

        This is one of the Child Classes that inherits from the Room
        Super Class. It passes information to the Parent Constructor
        so as to dictate how the Room is created. It also handles
        other activities related to a Living Space.
    '''

    def __init__(self, name):
        super(LivingSpace, self).__init__(name, "Living Space", 4)


office = LivingSpace("Narnia")
ofe = LivingSpace("Dojo")

print Room.rooms
