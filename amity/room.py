class Room(object):

    def __init__(self, name, type):
        self.total_persons = 0
        self.allocated_persons = []

    def add_person(self, uuid):
        pass

    def remove_person(self, uuid):
        pass


class Office(Room):
    number_of_offices = 0

    def __init__(self, name):
        Room.__init__(name, "Office")
        self.max_persons = 6


class LivingSpace(Room):
    number_of_living_spaces = 0

    def __init__(self, name):
        Room.__init__(name, "Living Space")
        self.max_persons = 4
