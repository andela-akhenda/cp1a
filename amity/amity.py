from person import Fellow, Staff
from room import Office, LivingSpace


class Amity(object):
    ''' Amity Class

        Amity is a class that models a room allocation system for one of
        Andela's facilities called Amity. Amity creates rooms which can
        be offices or living spaces. An office can occupy a maximum of 6
        people. A living space can inhabit a maximum of 4 people. It also
        creates and allocates a person rooms. A person to be allocated
        could be a fellow or staff. Staff cannot be allocated living
        spaces. Fellows have a choice to choose a living space or not.
        This system will be used to automatically allocate spaces to
        people at random.

        Attributes:
            rooms (list): This is a list of all Room IDs of rooms in the
            system.
            persons (list): This is a list of all UUIDs of persons in the
            system.
            total_rooms (int): This is an integer representing all the
            rooms in the system.
            total_persons (int): This is an integer representing all the
            persons in the system.
            room_allocations (dict): This is a dictionary that holds all
            the data on room allocations in the system.

    '''
    rooms = []
    persons = []
    total_rooms = 0
    total_persons = 0
    room_allocations = {}

    def __init__(self):
        pass

    def create_room(self, name):
        """
        Create a room in Amity.

        This method creates a room or multiple of rooms depending on the
        amount of items in the list it receives. So, it receives a list.
        This method should also check that no duplicate rooms can be created.

        Parameters
        ----------
        name : list
            This is a list of names for the rooms to be created.

        Returns
        -------
        dict
            This is a dictionary containing the details of the newly
            created rooms.

        """
        pass

    def add_person(self, name, role, allocate="N"):
        """
        Add Person and allocate random room.

        This method adds a person to the Amity System and immediately
        allocates the person a random room.

        Parameters
        ----------
        name : str
            This is a string representing the full name of the person.
        role : str
            This is a string of the person's role.
        allocate : str
            This is a boolean string that can either be "N" for "No"
            or "Y" for "Yes". It tells us if the person needs
            accommodation.

        Returns
        -------
        dict
            This is a dictionary containing the details of the newly
            added person.

        """
        pass

    def get_person_details(self, uuid):
        """
        Get Person details.

        This method fetches a Person's details using the provided id.

        Parameters
        ----------
        name : str
            This is a string representing the id of the person.

        Returns
        -------
        dict
            This is a dictionary containing the details of the
            a person.

        """
        pass

    def get_current_occupants(self, r_id):
        """
        Get specific Room occupants.

        This method fetches all the Persons in a particular room
        given the room ID.

        Parameters
        ----------
        r_id : str
            This is a string representing the id of the room.

        Returns
        -------
        dict
            This is a dictionary containing the details of the
            room together with all the occupants.

        """
        pass

    def reallocate_person(self, uuid, room_name):
        """
        Reallocate a Person.

        This method reallocates a Person from a room to another room
        given the destination room name and the Unique User ID (uuid)
        of the user.

        Parameters
        ----------
        uuid : str
            This is a string representing the unique id of the Person.
        room_name : str
            This is a string representing name of the room the Person
            is to be reallocated.

        Returns
        -------
        dict
            This is a dictionary containing the details of the room
            the Person has been reallocated to together with all the
            occupants.

        """
        pass

    def get_empty_rooms(self):
        """
        Get all empty room in the system.

        This method goes through the entire system and looks for all
        rooms that have not been allocated anyone. In other words, all
        empty rooms in the system.

        Returns
        -------
        dict
            This is a list of all the empty rooms in the system.

        """
        pass

    def print_allocations(self, param=None):
        """
        Print Room allocations.

        This method prints a list of allocations onto the screen.
        Specifying the optional -o option here outputs the registered
        allocations to a txt file.

        Parameters
        ----------
        param : str
            This is an optional string that specifies whether the
            output should be saved on a txt file.

        Returns
        -------
        dict
            This is a dictionary containing the details of all the
            allocation. The dictionary may be returned or saved in a
            file depending on the parameter passed.

        """
        pass

    def print_unallocated(self, param=None):
        """
        Print Room Unallocations.

        This method prints a list of unallocated people to the screen.
        Specifying the -o option here outputs the information to the
        txt file provided.

        Parameters
        ----------
        param : str
            This is an optional string that specifies whether the
            output should be saved on a txt file.

        Returns
        -------
        dict
            This is a dictionary containing the details of all the
            unallocated Persons. The dictionary may be returned or saved in a
            file depending on the parameter passed.

        """
        pass

    def print_room(self, r_id):
        """
        Print Room.

        This method prints all the details of a specific Room given
        the Room Id.

        Parameters
        ----------
        r_id : str
            This is a string representing the id of the Room to be
            printed.

        Returns
        -------
        dict
            This is a dictionary containing the details of the
            Room.

        """
        pass

    def save_state(self, outfile):
        """
        Persist State

        This method persists the state of the application by saving the
        current working data to a DB.

        Parameters
        ----------
        outfile : str
            This is a string representing the name of the DB to save the
            current state.

        Returns
        -------
        string
            his is a string representing a successful operation or
            a failure

        """
        pass

    def load_state(self, infile):
        """
        Load State

        This method loads a previously saved state for the application
        to resume fro that point the DB was created.

        Parameters
        ----------
        infile : str
            This is a string representing the name of the DB to load
            the state from.

        Returns
        -------
        string
            his is a string representing a successful operation or
            a failure

        """
        pass
