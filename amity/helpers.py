import copy

from room import Room
from person import Person


def reallocate_person(self, uuid, room_name):
    """
    Reallocate a Person.

    This function reallocates a Person from a room to another room
    given the destination room name and the Unique User ID (uuid)
    of the user.

    filenameeters
    ----------
    uuid : str
        This is a string representing the unique id of the Person.
    room_name : str
        This is a string representing name of the room the Person
        is to be reallocated.

    Returns
    -------
    string
        This is a string showing success or failure of the operation.

    """
    if not isinstance(uuid, str) or not isinstance(room_name, str):
        return TypeError("This method only accepts strings as the input.")
    else:
        current_rooms = []
        previous_room = ''
        type_of_reallocation = ''
        uuid = uuid.lower()
        r_id = room_name.lower()
        all_offices = Room.rooms["Offices"]
        all_living_spaces = Room.rooms["Living Spaces"]
        rooms = dict(Room.rooms["Offices"], **Room.rooms["Living Spaces"])
        rooms = copy.deepcopy(rooms)
        for room in rooms:
            if uuid in rooms[room]['Occupants']:
                current_rooms.append(room)
        if r_id in all_offices:
            type_of_reallocation = "Offices"
        elif r_id in all_living_spaces:
            type_of_reallocation = "Living Spaces"
        else:
            return "The room given does not exist"
        for room in current_rooms:
            if room in Room.rooms[type_of_reallocation]:
                previous_room = room
        # Now, let's remove the user from the previous room
        Room.rooms[type_of_reallocation][previous_room]['Occupants'].remove(uuid)
        # Let's not forget to decrement the number of Total Persons
        Room.rooms[type_of_reallocation][previous_room]['Total Persons'] -= 1
        # Now, let's reallocate the user to the given room
        if Room.rooms[type_of_reallocation][r_id]['Total Persons'] < Room.rooms[type_of_reallocation][r_id]['Capacity']:
            Room.rooms[type_of_reallocation][r_id]['Occupants'].append(uuid)
            Room.rooms[type_of_reallocation][r_id]['Total Persons'] += 1
            return "The person has been successfuly re-allocated to " + room_name
        elif Room.rooms[type_of_reallocation][r_id]['Total Persons'] == Room.rooms[type_of_reallocation][r_id]['Capacity']:
            return room_name + " is fully booked. Try another room."


def get_current_occupants(r_id):
    """
    Get specific Room occupants.

    This function fetches all the Persons in a particular room
    given the room ID.

    filenameeters
    ----------
    r_id : str
        This is a string representing the id of the room.

    Returns
    -------
    dict
        This is a dictionary containing the details of
        current occupants.

    """
    if not isinstance(r_id, str):
        return TypeError("This method only accepts a string as the input.")
    else:
        occupants = []
        occupants_dict = {}
        rooms = dict(Room.rooms["Offices"], **Room.rooms["Living Spaces"])
        rooms = copy.deepcopy(rooms)
        if r_id in rooms.keys():
            occupants = rooms[r_id]['Occupants']
        for occupant in occupants:
            occupants_dict[occupant] = Person.get_person(occupant)
        return occupants_dict
