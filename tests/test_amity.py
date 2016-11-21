import unittest

from amity.amity import Amity


class TestAmity(unittest.TestCase):

    def setUp(self):
        self.amity = Amity()

    def test_create_room(self):
        pass

    def test_add_person(self):
        pass

    def test_if_a_person_is_fellow_or_staff(self):
        pass

    def test_create_multiple_rooms(self):
        pass

    def test_cannot_add_duplicate_room(self):
        pass

    def test_occupants_increment_on_allocation(self):
        pass

    def test_add_to_fully_occupied_rooms(self):
        pass

    def test_empty_rooms(self):
        pass

    def test_response_on_no_rooms(self):
        pass

    def test_occupants_after_relallocation(self):
        pass

    def test_staff_cannot_be_allocated_living_space(self):
        pass

    def test_print_allocations(self):
        pass

    def test_print_unallocated(self):
        pass

    def test_print_room(self):
        pass

    def test_load_people_from_file(self):
        pass

    def test_save_state(self):
        pass

    def test_load_state(self):
        pass


if __name__ == '__main__':
    unittest.main()
