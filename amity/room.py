from random import choice
from person import Person


class Room(object):
    ''' Room Class

        This is the Super Class that handles the creation of Rooms
        in the Amity System. It relies heavily on the information it
        gets from it's Child Classes.
    '''
    number_of_offices = 0
    number_of_living_spaces = 0
    total_rooms = 0
    rooms = {"Offices": {}, "Living Spaces": {}}
    error = ""

    def __init__(self, name, room_type, capacity):
        room_key = room_type + "s"
        room_id = name.lower()
        all_room_ids = Room.rooms['Offices'].keys() + Room.rooms['Living Spaces'].keys()
        if name.lower() in all_room_ids:
            Room.error = "A room named '" + name + "' already exists. Please choose another name."
        else:
            self.rooms[room_key][room_id] = {}
            self.rooms[room_key][room_id]["Room Name"] = name
            self.rooms[room_key][room_id]["Room ID"] = room_id
            self.rooms[room_key][room_id]["Capacity"] = capacity
            self.rooms[room_key][room_id]["Total Persons"] = 0
            self.rooms[room_key][room_id]["Occupants"] = []
            if room_type == "Office":
                Room.number_of_offices += 1
            elif room_type == "Living Space":
                Room.number_of_living_spaces += 1
            Room.total_rooms = Room.number_of_offices + Room.number_of_living_spaces
            Room.error = ""
        self.name = name
        self.room_type = room_type
        self.capacity = capacity

    @staticmethod
    def add_person(uuid, role, room_type, allocate="N"):
        ''' Add Person Method

            This method is responsible for adding a person to a random room.
            It also checks if the system has any rooms before adding a person
            or if the rooms available are not fully occupied before assigning
            the person a random room.
        '''
        room_key = room_type + "s"
        all_rooms = Room.rooms[room_key].keys()
        if len(all_rooms) == 0:
            Room.error = "The system has no rooms. Please add rooms before adding persons."
            return Room.error
        available_rooms = []
        for room in all_rooms:
            if Room.rooms[room_key][room]['Total Persons'] < Room.rooms[room_key][room]['Capacity']:
                available_rooms.append(room)
        if len(available_rooms) == 0:
            Room.error = "There are currently no rooms available. All rooms are booked."
            return Room.error
        random_room = choice(available_rooms)
        Room.rooms[room_key][random_room]['Occupants'].append(uuid)
        Person.persons[role][uuid]['Boarding'] = allocate

        # if type(Room.rooms[room_key][random_room]['Total Persons']) is not str:
        #     Room.rooms[room_key][random_room]['Total Persons'] += 1
        # else:
        #     Room.rooms[room_key][random_room]['Total Persons'] = 0

        ''' Uncomment the above lines if the import from DB messes the Total
            Persons field. Remember to also delete the line below. '''
        Room.rooms[room_key][random_room]['Total Persons'] += 1
        Room.error = ""


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
