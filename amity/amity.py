class Amity(object):
    '''
        Amity is a class that models a room allocation system for one of
        Andela's facilities called Amity. Amity creates rooms which can
        be offices or living spaces. An office can occupy a maximum of 6
        people. A living space can inhabit a maximum of 4 people. It also
        creates and allocates a person rooms. A person to be allocated
        could be a fellow or staff. Staff cannot be allocated living
        spaces. Fellows have a choice to choose a living space or not.
        This system will be used to automatically allocate spaces to
        people at random.
    '''
    def __init__(self):
        pass

    def create_room(self, name):
        pass

    def add_person(self, name, role, allocate="No"):
        pass

    def get_person_details(self, name):
        pass