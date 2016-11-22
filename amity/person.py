class Person(object):

    def __init__(self, uuid, name, role):
        self.allocated_rooms = []

    def print_person(self):
        pass


class Fellow(Person):
    number_of_fellows = 0

    def __init__(self, name):
        Person.__init__("f" + str(self.number_of_fellows + 1), name, "Fellow")

    def is_allocated_room(self):
        pass


class Staff(Person):
    number_of_staff = 0

    def __init__(self, name):
        Person.__init__("s" + str(self.number_of_staff + 1), name, "Staff")

    def is_allocated_room(self):
        pass
