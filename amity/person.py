class Person(object):
    ''' Person Class

        This is the Super Class that handles the creation of Persons
        in the Amity System. It relies heavily on the information it
        gets from it's Child Classes.
    '''
    number_of_fellows = 0
    number_of_staff = 0
    total_persons = 0
    persons = {"Fellows": {}, "Staff": {}}
    error = ""

    def __init__(self, uuid, name, role):
        if role == "Fellow":
            role = role + "s"
        self.persons[role][uuid] = {}
        self.persons[role][uuid]["uuid"] = uuid
        self.persons[role][uuid]["Name"] = name
        self.persons[role][uuid]["Role"] = role
        self.persons[role][uuid]["Boarding"] = "N"
        if role[:-1] == "Fellows":
            Person.number_of_fellows += 1
        elif role == "Staff":
            Person.number_of_staff += 1
        Person.total_persons = Person.number_of_fellows + Person.number_of_staff
        Person.error = ""
        self.uuid = uuid

    @staticmethod
    def get_person(uuid):
        ''' This method is responsible for fetching all the
            Person's details.
        '''
        if type(uuid) is not str:
            raise TypeError("This method only accepts a string as the input.")
        else:
            all_fellows = Person.persons["Fellows"]
            all_staff = Person.persons["Staff"]
            all_persons = dict(all_fellows, **all_staff)
            if uuid in all_persons.keys():
                return all_persons[uuid]
            else:
                return "The person with UUID: " + uuid + " was not found"


class Fellow(Person):
    ''' Fellow Class

        This is one of the Child Classes that inherits from the Person
        Super Class. It passes information to the Parent Constructor
        so as to dictate how the Person is created. It also handles
        other responsibilities related to a Fellow.
    '''

    def __init__(self, name):
        super(Fellow, self).__init__(
            "f" + str(Person.number_of_fellows + 1), name, "Fellow"
        )

    def is_allocated_room(self):
        pass


class Staff(Person):
    ''' Staff Class

        This is one of the Child Classes that inherits from the Person
        Super Class. It passes information to the Parent Constructor
        so as to dictate how the Person is created. It also handles
        other responsibilities related to a Staff.
    '''

    def __init__(self, name):
        super(Staff, self).__init__(
            "s" + str(Person.number_of_staff + 1), name, "Staff"
        )

    def is_allocated_room(self):
        pass
