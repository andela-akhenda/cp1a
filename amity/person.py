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

    def __init__(self, person_id, name, role):
        if role == "Fellow":
            role_key = role + "s"
        else:
            role_key = role
        self.persons[role_key][person_id] = {}
        self.persons[role_key][person_id]["person_id"] = person_id
        self.persons[role_key][person_id]["Name"] = name
        self.persons[role_key][person_id]["Role"] = role
        self.persons[role_key][person_id]["Boarding"] = "N"
        if role == "Fellow":
            Person.number_of_fellows += 1
        elif role == "Staff":
            Person.number_of_staff += 1
        Person.total_persons = Person.number_of_fellows + Person.number_of_staff
        Person.error = ""
        self.person_id = person_id
        self.role = role
        self.name = name

    @staticmethod
    def get_person(person_id):
        ''' This method is responsible for fetching all the
            Person's details.
        '''
        if not isinstance(person_id, str):
            return TypeError("This method only accepts a string as the input.")
        else:
            all_fellows = Person.persons["Fellows"]
            all_staff = Person.persons["Staff"]
            all_persons = dict(all_fellows, **all_staff)
            if person_id in all_persons.keys():
                return all_persons[person_id]
            else:
                return "The person with ID: " + person_id + " was not found"

    @staticmethod
    def get_person_id(name):
        ''' This method is responsible for fetching the Person's ID. '''
        person_ids = []
        if not isinstance(name, str):
            return TypeError("This method only accepts a string as the input.")
        else:
            people = dict(Person.persons["Fellows"], **Person.persons["Staff"])
            for person in people.itervalues():
                if person['Name'] == name:
                    person_ids.append(person['person_id'])
            if len(person_ids) == 1:
                return name + "'s ID is: " + person_ids[0]
            elif len(person_ids) > 1:
                return "Several persons with the name '" + name + "' exist.\n" + "\n".join(person_ids) + "\nFor more information, Print Allocations to see how they are allocated."
            else:
                return "The user, '" + name + "' was not found! Please ensure the person already exists in the system."


class Fellow(Person):
    ''' Fellow Class

        This is one of the Child Classes that inherits from the Person
        Super Class. It passes information to the Parent Constructor
        so as to dictate how the Person is created. It also handles
        other responsibilities related to a Fellow.
    '''

    def __init__(self, name):
        initializer(self, Fellow, name)


class Staff(Person):
    ''' Staff Class

        This is one of the Child Classes that inherits from the Person
        Super Class. It passes information to the Parent Constructor
        so as to dictate how the Person is created. It also handles
        other responsibilities related to a Staff.
    '''

    def __init__(self, name):
        initializer(self, Staff, name)


def initializer(this, role, name):
    if role.__name__ == "Fellow":
        number_of_persons = Person.number_of_fellows
    else:
        number_of_persons = Person.number_of_staff
    super(role, this).__init__(
        role.__name__[0].lower() + str(number_of_persons + 1),
        name,
        role.__name__
    )
