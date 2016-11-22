import unittest
from mock import patch

from amity.amity import Amity


class TestAmity(unittest.TestCase):

    def setUp(self):
        self.amity = Amity()

    def test_amity_class_instrance(self):
        self.assertIsInstance(self.amity, Amity)

    def test_create_room(self):
        response = self.amity.create_room(['Abydos'])
        self.assertEqual(response, "The room has been successfully created")

    @patch.dict('amity.amity.Amity.rooms', {
                "Offices": ['o1'],
                "Living Spaces": ['ls1']
                })
    @patch.dict('amity.amity.Amity.persons', {
                "Fellows": ['f1'],
                "Staff": []
                })
    def test_add_person(self):
        add = self.amity.add_person('General Hammond', 'Staff')
        duplicate_add = self.amity.add_person("Jaffa Teal'c", 'Fellow', 'Y')
        add_staff = self.amity.add_person('Samantha Carter', 'Staff', 'Y')
        self.assertEqual(
            add['msg'],
            'The Staff member has been added successfuly'
        )
        self.assertEqual(
            duplicate_add['msg'],
            'There already exists a person with the name "Daniel Jackson"!'
        )
        self.assertEqual(
            add_staff['msg'],
            'Cannot allocate Staff a living space'
        )

    def test_if_a_person_is_fellow_or_staff(self):
        self.amity.add_person('General Hammond', 'Staff')
        # we should pass add['uuid'] here
        response = self.amity.get_person_details('s1')
        self.assertEqual(response['role'], "Staff")

    def test_create_multiple_rooms(self):
        response = self.amity.create_room(['Abydos', 'Chulak', 'Argos'])
        self.assertEqual(
            response,
            "Your 3 rooms have been successfully created"
        )

    def test_cannot_add_duplicate_room(self):
        response = self.amity.create_room(['Dakara', 'Chulak'])
        response = self.amity.create_room(['Dakara', 'Argos'])
        self.assertEqual(
            response,
            "Dakara room already exists. Please choose another name."
        )

    def test_occupants_increment_on_allocation(self):
        self.amity.create_room(['Abydos'])
        prev_occupants = self.amity.get_current_occupants('abydos')
        self.amity.add_person('Daniel Jackson', 'Fellow', 'Y')
        new_occupants = self.amity.get_current_occupants('abydos')
        self.assertEqual(
            len(prev_occupants.keys()) + 1,
            len(new_occupants.keys())
        )

    def test_add_to_fully_occupied_rooms(self):
        self.amity.create_room(['Chulak', '-ls'])
        self.amity.add_person("Colonel Jack O'Neal", 'Fellow', 'Y')
        self.amity.add_person("Dr. Rodney Mc'Kay", 'Fellow', 'Y')
        self.amity.add_person('Ronan Decks', 'Fellow', 'Y')
        self.amity.add_person('Dr. Daniel Jackson', 'Fellow', 'Y')
        add = self.amity.add_person('Colonel Samantha Carter', 'Fellow', 'Y')
        response = self.amity.reallocate_person(add['uuid'], 'Chulak')
        self.assertEqual(response, "Rejected! Chulak is fully booked.")

    def test_get_empty_rooms(self):
        self.amity.create_room(['Abydos', 'Chulak', 'Argos'])
        response = self.amity.get_empty_rooms()
        self.assertEqual(
            sorted(response),
            sorted(['Abydos', 'Chulak', 'Argos'])
        )

    def test_response_on_no_rooms(self):
        response = self.amity.add_person("Colonel Samantha Carter", "Staff")
        self.assertEqual(
            response['msg'],
            "There are currently no rooms available"
        )

    def test_occupants_after_reallocation(self):
        self.amity.create_room(['Daedalus'])
        self.amity.add_person('Daniel Jackson', 'Fellow', 'Y')
        self.amity.add_person('General Hammond', 'Staff')
        occupants = self.amity.get_current_occupants('daedalus')
        # We ca also use Python's cmp() function below
        self.assertEqual(
            occupants,
            {
                "Slot 1": {
                    "uuid": "f1",
                    "Name": "Daniel Jackson",
                    "Role": "Fellow",
                    "Wants Accommodation": "Y"
                },
                "Slot 2": {
                    "uuid": "s1",
                    "Name": "General Hammond",
                    "Role": "Staff",
                    "Wants Accommodation": "N"
                }
            }
        )

    def test_staff_cannot_be_allocated_living_space(self):
        self.amity.create_room(['Wraith', '-ls'])
        response = self.amity.add_person('Tod The Wraith', 'Staff')
        self.assertEqual(
            response['msg'],
            "Staff cannot be allocated Living Space"
        )

    def test_print_allocations(self):
        pass

    def test_print_unallocated(self):
        pass

    def test_print_room(self):
        self.amity.create_room(['Dakara', '-ls'])
        self.amity.add_person("Jaffa Teal'c", 'Fellow', 'Y')
        response = self.amity.print_room('dakara')
        self.assertEqual(
            response,
            {
                "Room Name": "Dakara",
                "Room ID": "dakara",
                "Capacity": 4,
                "Total Persons": 1,
                "Occupants": {
                    "Slot 1": {
                        "uuid": "f1",
                        "Name": "Jaffa Teal'c",
                        "Role": "Fellow",
                        "Wants Accommodation": "Y"
                    }
                }
            }
        )

    def test_load_people_from_file(self):
        response = self.amity.load_people("test_people.txt")
        self.assertEqual(
            response,
            "People have been successfuly added to the system."
        )

    def test_save_state(self):
        pass

    def test_load_state(self):
        pass


if __name__ == '__main__':
    unittest.main()
