import copy

from room import Room
from person import Person


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