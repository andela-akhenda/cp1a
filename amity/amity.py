import os
import copy
import sqlite3 as db

from person import Person, Fellow, Staff
from room import Room, Office, LivingSpace

if os.path.exists('amity'):
    os.chdir('amity')


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
            persons (dict): This is a dict of all IDs of persons in the
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
        self.current_state = ''

    @staticmethod
    def create_room(name):
        """
        Create a room in Amity.

        This method creates a room or multiple of rooms depending on the
        amount of items in the list it receives. So, it receives a list.
        This method should also check that no duplicate rooms can be created.
        Another thing to be noted is that this method will create an Office by
        default unless the last string in the arguments is "-ls" which will
        create Living Spaces

        filenameeters
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
            if room_type == 'o':
                room_type_str = 'Office'
            elif room_type == 'ls':
                room_type_str = 'Living Space'
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
                    msg2 = ' ' + room_type_str + ' has been'
                elif new_all_rooms - all_rooms > 1:
                    msg2 = ' ' + room_type_str + 's have been'
                return "Only " + str(new_all_rooms - all_rooms) + msg2 + " successfully created because:" + msg
            elif new_all_rooms - all_rooms > 1:
                return "Your " + str(new_all_rooms - all_rooms) + " " + room_type_str + "s have been successfully created"
            else:
                return "The " + room_type_str + " has been successfully created"

        if not isinstance(name, list):
            return TypeError("This method only accepts a list as the input.")
        else:
            if name[-1] != "-ls" and name[-1] != "-o":
                return create_rooms_from_list(name)
            else:
                if name[-1] == "-ls":
                    return create_rooms_from_list(name[:-1], "ls")
                elif name[-1] == "-o":
                    return create_rooms_from_list(name[:-1])

    @staticmethod
    def add_person(name, role, allocate="N"):
        """
        Add Person and allocate random room.

        This method adds a person to the Amity System and immediately
        allocates the person a random room.

        filenameeters
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
        if not isinstance(name, str) or not isinstance(role, str) or not isinstance(allocate, str):
            return TypeError("This method only accepts strings as the input.")
        else:
            all_persons = Person.total_persons
            creation_errors = []
            msg = ''
            given_office = ''
            given_ls = ''
            if allocate != "Y" and allocate != "N":
                creation_errors.append("Allocate only accepts 'Y' or 'N'")
            if role == "Staff":
                temp_staff = Staff(name)
                if allocate == "Y":
                    creation_errors.append("Cannot allocate Staff a living space")
                given_office = Room.add_person(temp_staff.person_id, "Staff", "Office")
                if Room.error:
                    creation_errors.append(Room.error)
            elif role == "Fellow":
                temp_fellow = Fellow(name)
                if allocate == "Y":
                    Person.persons["Fellows"][temp_fellow.person_id]['Boarding'] = 'Y'
                    given_office = Room.add_person(temp_fellow.person_id, "Fellows", "Office", "Y")
                    if Room.error:
                        creation_errors.append(Room.error)
                    given_ls = Room.add_person(temp_fellow.person_id, "Fellows", "Living Space", "Y")
                elif allocate == "N":
                    given_office = Room.add_person(temp_fellow.person_id, "Fellows", "Office")
                if Room.error:
                    creation_errors.append(Room.error)
            else:
                return TypeError(
                    "Please check that the entered role is either 'Fellow' or 'Staff'"
                )
            new_all_persons = Person.total_persons
            # if creation_errors and new_all_persons - all_persons == 0:
            #     for item in creation_errors:
            #         msg = msg + "\n" + item
            #     return "No person was added to the system beacuse:" + msg
            if creation_errors and new_all_persons - all_persons >= 1:
                for item in creation_errors:
                    msg = msg + "\n- " + item
                return "\nThe " + role + ", " + name + " has been added successfuly but with the following problem(s):" + msg
            else:
                msg = "\nThe " + role + ", " + name + " has been added "
                msg += "successfuly and given the following "
                if given_ls:
                    msg += "rooms:-"
                else:
                    msg += "room:-"
                msg += "\n1. Office       --> " + given_office.capitalize()
                if given_ls:
                    msg += "\n2. Living Space --> " + given_ls.capitalize()
                msg += "\n"
                return msg

    @staticmethod
    def get_person_details(person_id):
        """
        Get Person details.

        This method fetches a Person's details using the provided id.

        filenameeters
        ----------
        person_id : str
            This is a string representing the id of the person.

        Returns
        -------
        dict
            This is a dictionary containing the details of
            a person.

        """
        return Person.get_person(person_id)

    @staticmethod
    def get_person_id(name):
        """
        Get Person ID.

        This method fetches a Person's ID using the provided name.

        filenameeters
        ----------
        name : str
            This is a string representing the name of the person.

        Returns
        -------
        str
            This is a string containing the ID of the person.

        """
        return Person.get_person_id(name)

    @staticmethod
    def get_current_occupants(r_id):
        """
        Get specific Room occupants.

        This method fetches all the Persons in a particular room
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

    def reallocate_person(self, person_id, room_name):
        """
        Reallocate a Person.

        This method reallocates a Person from a room to another room
        given the destination room name and the Unique User ID (person_id)
        of the user.

        filenameeters
        ----------
        person_id : str
            This is a string representing the unique id of the Person.
        room_name : str
            This is a string representing name of the room the Person
            is to be reallocated.

        Returns
        -------
        string
            This is a string showing success or failure of the operation.

        """
        if not isinstance(person_id, str) or not isinstance(room_name, str):
            return TypeError("This method only accepts strings as the input.")
        else:
            current_rooms = []
            previous_room = ''
            type_of_reallocation = ''
            person_id = person_id.lower()
            r_id = room_name.lower()
            all_offices = Room.rooms["Offices"]
            all_living_spaces = Room.rooms["Living Spaces"]
            rooms = dict(Room.rooms["Offices"], **Room.rooms["Living Spaces"])
            persons = dict(Person.persons["Fellows"], **Person.persons["Staff"])
            rooms = copy.deepcopy(rooms)
            if person_id not in persons.keys():
                return "The given Person ID does not exist!"
            for room in rooms:
                if person_id in rooms[room]['Occupants']:
                    current_rooms.append(room)
            if r_id in all_offices:
                type_of_reallocation = "Offices"
            elif r_id in all_living_spaces:
                type_of_reallocation = "Living Spaces"
                if Person.get_person(person_id)['Role'] == 'Staff':
                    return "Staff cannot be reallocated to a Living Space"
            else:
                return "The room given does not exist"
            for room in current_rooms:
                if room in Room.rooms[type_of_reallocation]:
                    previous_room = room
            # Now, let's remove the user from the previous room
            # Handle the bug pointed out by @andela-jmuli
            if previous_room:
                Room.rooms[type_of_reallocation][previous_room]['Occupants'].remove(person_id)
                # Let's not forget to decrement the number of Total Persons
                Room.rooms[type_of_reallocation][previous_room]['Total Persons'] -= 1
            # Now, let's reallocate the user to the given room
            if Room.rooms[type_of_reallocation][r_id]['Total Persons'] < Room.rooms[type_of_reallocation][r_id]['Capacity']:
                Room.rooms[type_of_reallocation][r_id]['Occupants'].append(person_id)
                Room.rooms[type_of_reallocation][r_id]['Total Persons'] += 1
                return self.get_person_details(person_id)['Name'] + " has been successfuly re-allocated from " + previous_room.capitalize() + " to " + room_name.capitalize()
            elif Room.rooms[type_of_reallocation][r_id]['Total Persons'] == Room.rooms[type_of_reallocation][r_id]['Capacity']:
                return room_name.capitalize() + " is fully booked. Try another room."

    @staticmethod
    def get_empty_rooms():
        """
        Get all empty room in the system.

        This method goes through the entire system and looks for all
        rooms that have not been allocated anyone. In other words, all
        empty rooms in the system.

        Returns
        -------
        dict
            This is a dictionary of all the empty rooms in the system.

        """
        empty_rooms = {"Offices": [], "Living Spaces": []}
        all_offices = Room.rooms["Offices"]
        all_living_spaces = Room.rooms["Living Spaces"]
        for room, details in all_offices.iteritems():
            if details['Total Persons'] == 0 and len(details['Occupants']) == 0:
                empty_rooms["Offices"].append(room)
        for room, details in all_living_spaces.iteritems():
            if details['Total Persons'] == 0 and len(details['Occupants']) == 0:
                empty_rooms["Living Spaces"].append(room)
        return empty_rooms

    @staticmethod
    def print_allocations(filename=None):
        """
        Print Room allocations.

        This method prints a list of allocations onto the screen.
        Specifying the optional -o option here outputs the registered
        allocations to a txt file.

        filenameeters
        ----------
        filename : str
            This is an optional string that specifies whether the
            output should be saved on a txt file.

        Returns
        -------
        string
            This is a string showing success or failure of the operation.

        """
        all_offices = {}
        all_living_spaces = {}

        def print_rooms(rooms, rooms_type, filename=None):
            all_members = []
            misc_variable = 1
            title_header = "=" * 30 + "\n"
            title_header += " " * 9 + rooms_type + "\n"
            title_header += "=" * 30 + "\n\n"
            print(title_header)
            for room_details in rooms[rooms_type].itervalues():
                if room_details['Total Persons'] > 0:
                    for person_id in room_details['Occupants']:
                        occupant = Person.get_person(person_id)
                        all_members.append(occupant['Name'].upper())
                    all_members_len = 0
                    count = 0
                    for member in all_members:
                        all_members_len += len(member)
                        dashes = all_members_len + count
                        count += 2
                    print room_details['Room Name'].upper()
                    print "-" * dashes
                    print ", ".join(all_members)
                    print "\n"
                    if filename is not None and isinstance(filename, str):
                        with open('data/outputs/allocations/' + filename, 'a') as f:
                            if misc_variable == 1:
                                f.write(title_header)
                            output = room_details['Room Name'].upper()
                            output += "\n" + "-" * dashes + "\n"
                            output += ", ".join(all_members)
                            output += "\n\n"
                            f.write(output)
                            misc_variable = 0
                    all_members = []
            print "\n\n\n"

        if filename is not None and isinstance(filename, str):
            try:
                os.remove('data/outputs/allocations/' + filename)
            except OSError:
                pass
        all_offices["Offices"] = Room.rooms["Offices"]
        all_living_spaces["Living Spaces"] = Room.rooms["Living Spaces"]
        if all_offices["Offices"] == {} and all_living_spaces["Living Spaces"] == {}:
            return "There is no data to print or save"
        print_rooms(all_offices, 'Offices', filename)
        print_rooms(all_living_spaces, 'Living Spaces', filename)
        if filename:
            return "Successfuly printed and saved the allocations to a file, " + filename + " in the '/data/outputs' directory."
        else:
            return "Successfuly printed the allocations"

    @staticmethod
    def print_unallocated(filename=None):
        """
        Print Room Unallocations.

        This method prints a list of unallocated people to the screen.
        Specifying the -o option here outputs the information to the
        txt file provided.

        filenameeters
        ----------
        filename : str
            This is an optional string that specifies whether the
            output should be saved on a txt file.

        Returns
        -------
        string
            This is a string showing success or failure of the operation.

        """
        def print_people(person_ids, title, filename=None):
            misc_variable = 1
            title_header = "=" * 30 + "\n"
            title_header += "Without " + title + "\n"
            title_header += "=" * 30 + "\n"
            print title_header
            for person_id in person_ids:
                person = Person.get_person(person_id)
                print person['person_id'].upper(),
                if title == "Living Spaces":
                    print "(" + person['Boarding'] + ")",
                print "\t" + person['Name'].upper() + "\n"
                if filename is not None and isinstance(filename, str):
                    with open('data/outputs/unallocations/' + filename, 'a') as f:
                        if misc_variable == 1:
                            f.write(title_header)
                        output = person['person_id'].upper()
                        if title == "Living Spaces":
                            output += "(" + person['Boarding'] + ")"
                        output += "\t" + person['Name'].upper() + "\n"
                        if person_id == person_ids[-1]:
                            output += "\n\n"
                        f.write(output)
                        misc_variable = 0
            print "\n\n\n"

        if filename is not None and isinstance(filename, str):
            try:
                os.remove('data/outputs/unallocations/' + filename)
            except OSError:
                pass
        persons = dict(Person.persons["Fellows"], **Person.persons["Staff"])
        person_ids = []
        for person_details in persons.itervalues():
            person_ids.append(person_details['person_id'])

        all_offices = Room.rooms["Offices"]
        ids_in_offices = []
        for room_details in all_offices.itervalues():
            for occupant in room_details['Occupants']:
                ids_in_offices.append(occupant)
        unallocated_o = [person_id for person_id in person_ids if person_id not in ids_in_offices]

        all_living_spaces = Room.rooms["Living Spaces"]
        ids_in_ls = []
        for room_details in all_living_spaces.itervalues():
            for occupant in room_details['Occupants']:
                ids_in_ls.append(occupant)
        temp_unallocated_ls = [person_id for person_id in person_ids if person_id not in ids_in_ls]
        unallocated_ls = [person_id for person_id in temp_unallocated_ls if person_id[0] != 's']

        if unallocated_o == [] and unallocated_ls == []:
            return "There is no data to print or save"
        print_people(unallocated_o, 'Offices', filename)
        print_people(unallocated_ls, 'Living Spaces', filename)
        if filename:
            return "Successfuly printed and saved the unallocated to a file, " + filename + " in the '/data/outputs' directory."
        else:
            return "Successfuly printed the unallocated"

    def print_room(self, r_id):
        """
        Print Room.

        This method prints all the details of a specific Room given
        the Room Id.

        filenameeters
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
        if not isinstance(r_id, str):
            return TypeError("This method only accepts a string as the input.")
        else:
            room = {}
            r_name = r_id.capitalize()
            rooms = dict(Room.rooms["Offices"], **Room.rooms["Living Spaces"])
            rooms = copy.deepcopy(rooms)
            if r_id in rooms.keys():
                rooms[r_id]['Occupants'] = self.get_current_occupants(r_id)
                room = rooms[r_id]
            else:
                return "No room with the name '" + r_name + "' exists!"
            if len(room['Occupants']) == 0:
                return r_name + " has no occupants"
            else:
                print room['Room Name'].upper()
                print "-" * 25
            for occupant in room['Occupants']:
                print room['Occupants'][occupant]['person_id'].upper() + "\t",
                print room['Occupants'][occupant]['Boarding'].upper() + "\t",
                print room['Occupants'][occupant]['Name'].upper()
            return room

    def load_people(self, infile):
        """
        Load People

        This method load people from a text file and adds them to the
        Amity System.

        filenameeters
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
        if not isinstance(infile, str):
            return TypeError("This method only accepts a string as the input.")
        elif infile is not None:
            if os.path.exists('data/inputs/' + infile):
                with open('data/inputs/' + infile, 'r') as f:
                    for person_details in f:
                        person_details = person_details.rstrip('\n')
                        person_list = person_details.split(" ")
                        for i, item in enumerate(person_list):
                            person_list[i] = item.capitalize()
                        person_name = person_list[0] + " " + person_list[1]
                        person_role = person_list[2]
                        if len(person_list) > 3:
                            person_allocate = person_list[3]
                        else:
                            person_allocate = "N"
                        print self.add_person(person_name, person_role, person_allocate)
            else:
                return "The given file does not exist. \nPlease make sure "\
                        "'" + infile + "' is a valid filename and it exists "\
                        "in the 'data/inputs' directory"
        return "People have been successfuly added to the system."

    def save_state(self, outfile=None):
        """
        Persist State

        This method persists the state of the application by saving the
        current working data to a DB.

        filenameeters
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
        def db_looper(items, category):
            for item in items:
                i = items[item]
                if category == "Office" or category == "Living Space":
                    cursor.execute('''INSERT INTO Rooms (Id, Name, Type, \
                        Capacity, 'Total Persons', Occupants) VALUES(?, ?, ?,\
                        ?, ?, ?)''', (i['Room ID'], i['Room Name'], category, i['Capacity'], i['Total Persons'], ', '.join(i['Occupants'])))
                elif category == "Fellow" or category == "Staff":
                    cursor.execute('''INSERT INTO Persons ('Person ID', Name, Role,\
                        Boarding) VALUES(?, ?, ?, ?)''', (i['person_id'], i['Name'], i['Role'], i['Boarding']))

        self.dbError = False
        # if outfile is None:
        #     outfile = 'latest.db'
        conn = db.connect('data/states/' + outfile)
        with conn:
            # With the 'with' keyword, the Python interpreter automatically
            # releases the resources. It also provides error handling. Using the
            # with keyword, the changes are automatically committed. Otherwise,
            # we would have to commit them manually.
            print "Opened database successfully"
            cursor = conn.cursor()
            cursor.executescript('''
                    DROP TABLE IF EXISTS Rooms;
                    DROP TABLE IF EXISTS Persons;
                    CREATE TABLE Rooms(Id TEXT PRIMARY KEY NOT NULL UNIQUE,
                    Name TEXT NOT NULL, Type TEXT NOT NULL,
                    Capacity INT NOT NULL, 'Total Persons' INT NOT NULL,
                    Occupants TEXT);
                    CREATE TABLE Persons('Person ID' TEXT PRIMARY KEY NOT NULL,
                    Name TEXT NOT NULL, Role TEXT NOT NULL,
                    Boarding TEXT NOT NULL);
                    ''')
            print "Table created successfully"
            rooms = Room.rooms
            persons = Person.persons
            db_looper(rooms["Offices"], 'Office')
            db_looper(rooms["Living Spaces"], 'Living Space')
            db_looper(persons["Fellows"], 'Fellow')
            db_looper(persons["Staff"], 'Staff')
            if not self.dbError:
                return_msg = "You have successfuly persisted the state of the"
                return_msg += " Application."
                return_msg += "\nThe state was saved to '" + outfile + "' file"
                return_msg += " in the 'data/states' directory."
                return return_msg

    def load_state(self, infile):
        """
        Load State

        This method loads a previously saved state for the application
        to resume fro that point the DB was created.

        filenameeters
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
        def db_looper(table, category):
            output = []
            output_dict = {}
            old_category = category
            if category != "Staff":
                category += "s"
            output_dict[category] = {}
            try:
                cursor.execute("SELECT * from " + table)
            except db.OperationalError:
                self.dbError = True
                self.e_msg = "No such table exists. Please check that you loaded the correct DB."
            all_rows = cursor.fetchall()
            count = 0
            for row in all_rows:
                if str(row[2]) == old_category and table == "Rooms":
                    output_dict[category][str(row[0])] = {}
                    output_dict[category][str(row[0])]['Room Name'] = str(row[1])
                    output_dict[category][str(row[0])]['Room ID'] = str(row[0])
                    output_dict[category][str(row[0])]['Capacity'] = row[3]
                    output_dict[category][str(row[0])]['Total Persons'] = row[4]
                    if len(row[5]) != 0:
                        output_dict[category][str(row[0])]['Occupants'] = str(row[5]).split(', ')
                    else:
                        output_dict[category][str(row[0])]['Occupants'] = []
                    count += 1
                elif str(row[2]) == old_category and table == "Persons":
                    output_dict[category][str(row[0])] = {}
                    output_dict[category][str(row[0])]['person_id'] = str(row[0])
                    output_dict[category][str(row[0])]['Name'] = str(row[1])
                    output_dict[category][str(row[0])]['Role'] = str(row[2])
                    output_dict[category][str(row[0])]['Boarding'] = str(row[3])
                    count += 1
            output.append(output_dict)
            output.append(count)
            return output

        self.dbError = False
        self.e_msg = ""
        conn = db.connect('data/states/' + infile)
        with conn:
            print "Opened database successfully"
            cursor = conn.cursor()
            offices = db_looper('Rooms', 'Office')
            living_spaces = db_looper('Rooms', 'Living Space')
            fellows = db_looper('Persons', 'Fellow')
            staff = db_looper('Persons', 'Staff')
            if len(self.e_msg) > 0 and self.dbError:
                return self.e_msg
            rooms = dict(offices[0], **living_spaces[0])
            persons = dict(fellows[0], **staff[0])
            total_rooms = offices[1] + living_spaces[1]
            total_persons = fellows[1] + staff[1]
            Room.rooms = rooms
            Room.total_rooms = total_rooms
            Room.number_of_offices = offices[1]
            Room.number_of_living_spaces = living_spaces[1]
            Person.persons = persons
            Person.total_persons = total_persons
            Person.number_of_fellows = fellows[1]
            Person.number_of_staff = staff[1]
            print "Operation done successfully"
            if not self.dbError:
                return_msg = "You have successfuly loaded a previously saved "
                return_msg += "state.\n"
                return_msg += "The state was loaded from '" + infile + "' file"
                return_msg += " in the 'data/states' directory."
                return return_msg
