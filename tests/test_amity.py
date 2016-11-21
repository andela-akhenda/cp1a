import unittest
from mock import mock_open, patch

from amity.amity import Amity


class TestAmity(unittest.TestCase):

    def setUp(self):
        self.amity = Amity()

    def test_amity_class_instrance(self):
        self.assertIsInstance(self.amity, Amity)

    def test_create_room(self):
        response = self.amity.create_room('Abydos')
        self.assertEqual(response, "The room has been successfully created")

    @patch.dict('amity.amity.Amity.rooms', {"Offices": ['o1'], "Living Spaces": ['ls1']})
    @patch.dict('amity.amity.Amity.persons', {"Fellows": ['f1'], "Staff": []})
    def test_add_person(self):
        add = self.amity.add_person('General Hammond', 'Staff', 'N')
        duplicate_add = self.amity.add_person('Daniel Jackson', 'Fellow', 'Y')
        add_staff = self.amity.add_person('Samantha Carter', 'Staff', 'Y')
        self.assertEqual(add['msg'], 'The Staff member has been added successfuly')
        self.assertEqual(duplicate_add['msg'], 'There already exists a person with the name "Daniel Jackson"!')
        self.assertEqual(add_staff['msg'], 'Cannot allocate Staff a living space')

    def test_if_a_person_is_fellow_or_staff(self):
        add = self.amity.add_person('General Hammond', 'Staff', 'N')
        response = self.amity.get_person_details('s1') # we should pass add['uuid'] here
        self.assertEqual(response['role'], "Staff")

    def test_create_multiple_rooms(self):
        response = self.amity.create_room('Abydos', 'Chulak', 'Argos')
        self.assertEqual(response, "Your 3 rooms have been successfully created")

    def test_cannot_add_duplicate_room(self):
        response = self.amity.create_room('Abydos', 'Chulak')
        response = self.amity.create_room('Abydos', 'Argos')
        assertEqual(response, "Abydos room alredy exists. Plaese choose another name.")

    def test_occupants_increment_on_allocation(self):
        pass

    def test_add_to_fully_occupied_rooms(self):
        pass

    def test_get_empty_rooms(self):
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
