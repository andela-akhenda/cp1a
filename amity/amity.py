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
            rooms (dict): This is a dict of all Room IDs of rooms in the
            system.
            persons (dict): This is a dict of all UUIDs of persons in the
            system.
            total_rooms (int): This is an integer representing all the
            rooms in the system.
            total_persons (int): This is an integer representing all the
            persons in the system.
            room_allocations (dict): This is a dictionary that holds all
            the data on room allocations in the system.

    '''
    rooms = {"Offices": {}, "Living Spaces": {}}
    persons = {"Fellows": {}, "Staff": {}}
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
        Another thing to be noted is that this method will create an Office by
        default unless the last string in the arguments is "-ls" which will
        create Living Spaces

        Parameters
        ----------
        name : list
            This is a list of names for the rooms to be created.

        Returns
        -------
        string
            This is a string showing success or failure of the operation.

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
        string
            This is a string showing success or failure of the operation.

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
            This is a dictionary containing the details of
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
            This is a dictionary containing the details of
            current occupants.

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
        string
            This is a string showing success or failure of the operation.

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
        list
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
        string
            This is a string showing success or failure of the operation.

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
        string
            This is a string showing success or failure of the operation.

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

    def load_people(self, infile):
        """
        Load People

        This method load people from a text file and adds them to the
        Amity System.

        Parameters
        ----------
        infile : str
            This is a string representing the name of the file that
            contains the people to be loaded.

        Returns
        -------
        string
            This is a string representing a successful operation or
            a failure

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
            This is a string representing a successful operation or
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
            This is a string representing a successful operation or
            a failure

        """
        pass
