from person import Person, Fellow, Staff
from room import Room, Office, LivingSpace


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
        def create_rooms_from_list(names_list, room_type="o"):
            all_rooms = Room.total_rooms
            creation_errors = []
            msg = ''
            for name in names_list:
                if room_type == "ls":
                    LivingSpace(name)
                else:
                    Office(name)
                if Room.error:
                    creation_errors.append(Room.error)
            new_all_rooms = Room.total_rooms
            if creation_errors and new_all_rooms - all_rooms == 0:
                for item in creation_errors:
                    msg = msg + "\n" + item
                return "No room was created beacuse:" + msg
            if creation_errors and new_all_rooms - all_rooms >= 1:
                for item in creation_errors:
                    msg = msg + "\n" + item
                if new_all_rooms - all_rooms == 1:
                    msg2 = ' room has been'
                elif new_all_rooms - all_rooms > 1:
                    msg2 = ' rooms have been'
                return "Only " + str(new_all_rooms - all_rooms) + msg2 + " successfully created because:" + msg
            elif new_all_rooms - all_rooms > 1:
                return "Your " + str(new_all_rooms - all_rooms) + " rooms have been successfully created"
            else:
                return "The room has been successfully created"

        if type(name) is not list:
            raise TypeError("This method only accepts a list as the input.")
        else:
            if name[-1] != "-ls" and name[-1] != "-o":
                return create_rooms_from_list(name)
            else:
                if name[-1] == "-ls":
                    return create_rooms_from_list(name[:-1], "ls")
                elif name[-1] == "-o":
                    return create_rooms_from_list(name[:-1])

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
        if type(name) is not str and type(role) is not str and type(allocate) is not str:
            raise TypeError("This method only accepts strings as the input.")
        else:
            all_persons = Person.total_persons
            creation_errors = []
            msg = ''
            if allocate != "Y" and allocate != "N":
                creation_errors.append("Allocate only accepts 'Y' or 'N'")
            if role == "Staff":
                temp_staff = Staff(name)
                if allocate == "Y":
                    creation_errors.append("Cannot allocate Staff a living space")
                Room.add_person(temp_staff.uuid, "Staff", "Office")
                if Room.error:
                    creation_errors.append(Room.error)
            elif role == "Fellow":
                temp_fellow = Fellow(name)
                if allocate == "Y":
                    Room.add_person(temp_fellow.uuid, "Fellows", "Office")
                    if Room.error:
                        creation_errors.append(Room.error)
                    Room.add_person(temp_fellow.uuid, "Fellows", "Living Space")
                elif allocate == "N":
                    Room.add_person(temp_fellow.uuid, "Fellows", "Office")
                if Room.error:
                    creation_errors.append(Room.error)
            else:
                raise ValueError("Please check that the entered role is either 'Fellow' or 'Staff'")
            new_all_persons = Person.total_persons
            if creation_errors and new_all_persons - all_persons == 0:
                for item in creation_errors:
                    msg = msg + "\n" + item
                return "No person was added to the system beacuse:" + msg
            if creation_errors and new_all_persons - all_persons >= 1:
                for item in creation_errors:
                    msg = msg + "\n - " + item
                return "The person has been added successfuly but with the following problem(s):" + msg
            else:
                return "The " + role + " has been added successfuly"

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
        if type(r_id) is not str:
            raise TypeError("This method only accepts a string as the input.")
        else:
            occupants_dict = {}
            all_offices = Room.rooms["Offices"]
            all_living_spaces = Room.rooms["Living Spaces"]
            all_rooms = dict(all_offices, **all_living_spaces)
            if r_id in all_rooms.keys():
                occupants = all_rooms[r_id]['Occupants']
            for occupant in occupants:
                occupants_dict[occupant] = Person.get_person(occupant)
            return occupants_dict

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

# amity = Amity()
# amity.create_room(['Abydos'])
# amity.create_room(['Scala', 'Ruby', '-ls'])
# amity.create_room(['Hogwarts', 'Oculus', 'Valhalla', 'Ruby'])
# amity.create_room(['Oculus'])

# amity.create_room(['Dakara', 'Chulak', '-ls'])


# amity.add_person('General Hammond', 'Staff')
# amity.add_person("Jaffa Teal'c", 'Fellow', 'Y')
# amity.add_person('Samantha Carter', 'Staff', 'Y')

# print amity.get_current_occupants('scala')



