import unittest
from mock import patch

from amity.amity import Amity


class TestAmity(unittest.TestCase):

    def setUp(self):
        self.amity = Amity()

    def test_amity_class_instrance(self):
        self.assertIsInstance(self.amity, Amity)

    @patch.dict('amity.amity.Amity.rooms', {
                "Offices": {},
                "Living Spaces": {}
                })
    def test_create_room(self):
        response = self.amity.create_room(['Abydos'])
        self.assertEqual(response, "The room has been successfully created")

    @patch.dict('amity.amity.Amity.rooms', {
                "Offices": {
                    "abydos": {
                        "Room Name": "Abydos",
                        "Room ID": "abydos",
                        "Capacity": 6,
                        "Total Persons": 0,
                        "Occupants": {}
                    }
                },
                "Living Spaces": {}
                })
    @patch.dict('amity.amity.Amity.persons', {
                "Fellows": {
                    "f1": {
                        "uuid": "f1",
                        "Name": "Jaffa Teal'c",
                        "Role": "Fellow",
                        "Wants Accommodation": "Y"
                    }
                },
                "Staff": {}
                })
    def test_add_person(self):
        add = self.amity.add_person('General Hammond', 'Staff')
        duplicate_add = self.amity.add_person("Jaffa Teal'c", 'Fellow', 'Y')
        add_staff = self.amity.add_person('Samantha Carter', 'Staff', 'Y')
        self.assertEqual(
            add,
            'The Staff member has been added successfuly'
        )
        self.assertEqual(
            duplicate_add,
            'There already exists a person with the name "Jaffa Teal\'c"!'
        )
        self.assertEqual(
            add_staff,
            'Cannot allocate Staff a living space'
        )

    @patch.dict('amity.amity.Amity.persons', {
                "Fellows": {},
                "Staff": {}
                })
    @patch('amity.amity.Amity.get_person_details')
    def test_if_a_person_is_fellow_or_staff(self, mock_get_person_details):
        mock_get_person_details.return_value = {
            "uuid": "s1",
            "Name": "General Hammond",
            "Role": "Staff",
            "Wants Accommodation": "N"
        }
        self.amity.add_person('General Hammond', 'Staff')
        # we should pass 'uuid' here
        response = mock_get_person_details('s1')
        self.assertEqual(response['Role'], "Staff")

    @patch.dict('amity.amity.Amity.rooms', {
                "Offices": {},
                "Living Spaces": {}
                })
    def test_create_multiple_rooms(self):
        response = self.amity.create_room(['Abydos', 'Chulak', 'Argos'])
        self.assertEqual(
            response,
            "Your 3 rooms have been successfully created"
        )

    @patch.dict('amity.amity.Amity.rooms', {
                "Offices": {},
                "Living Spaces": {
                    "dakara": {
                        "Room Name": "Dakara",
                        "Room ID": "dakara",
                        "Capacity": 4,
                        "Total Persons": 0,
                        "Occupants": {}
                    }
                }
                })
    def test_cannot_add_duplicate_room(self):
        response = self.amity.create_room(['Dakara', 'Chulak', '-ls'])
        self.assertEqual(
            response,
            "A room named 'Dakara' already exists. Please choose another name."
        )

    @patch.dict('amity.amity.Amity.rooms', {
                "Offices": {
                    "abydos": {
                        "Room Name": "Abydos",
                        "Room ID": "abydos",
                        "Capacity": 6,
                        "Total Persons": 0,
                        "Occupants": {}
                    }
                },
                "Living Spaces": {}
                })
    @patch.dict('amity.amity.Amity.persons', {
                "Fellows": {},
                "Staff": {}
                })
    def test_occupants_increment_on_allocation(self):
        prev_occupants = self.amity.get_current_occupants('abydos')
        self.amity.add_person('Daniel Jackson', 'Fellow', 'Y')
        new_occupants = self.amity.get_current_occupants('abydos')
        self.assertEqual(
            len(prev_occupants.keys()) + 1,
            len(new_occupants.keys())
        )

    @patch.dict('amity.amity.Amity.rooms', {
                "Offices": {},
                "Living Spaces": {
                    "chulak": {
                        "Room Name": "Chulak",
                        "Room ID": "chulak",
                        "Capacity": 4,
                        "Total Persons": 0,
                        "Occupants": {}
                    }
                }
                })
    @patch.dict('amity.amity.Amity.persons', {
                "Fellows": {
                    "f1": {
                        "uuid": "f1",
                        "Name": "Colonel Jack O'Neall",
                        "Role": "Fellow",
                        "Wants Accommodation": "Y"
                    },
                    "f2": {
                        "uuid": "f2",
                        "Name": "Dr. Rodney McKay",
                        "Role": "Fellow",
                        "Wants Accommodation": "Y"
                    },
                    "f3": {
                        "uuid": "f3",
                        "Name": "Ronon Dex",
                        "Role": "Fellow",
                        "Wants Accommodation": "Y"
                    },
                    "f4": {
                        "uuid": "f4",
                        "Name": "Dr. Daniel Jackson",
                        "Role": "Fellow",
                        "Wants Accommodation": "Y"
                    },
                    "f5": {
                        "uuid": "f5",
                        "Name": "Colonel Samantha Carter",
                        "Role": "Fellow",
                        "Wants Accommodation": "N"
                    },
                },
                "Staff": {}
                })
    def test_add_to_fully_occupied_rooms(self):
        response = self.amity.reallocate_person('f5', 'Chulak')
        self.assertEqual(
            response,
            "Chulak is fully booked. Try another room."
        )

    @patch.dict('amity.amity.Amity.rooms', {
                "Offices": {
                    "abydos": {
                        "Room Name": "Abydos",
                        "Room ID": "abydos",
                        "Capacity": 6,
                        "Total Persons": 0,
                        "Occupants": {}
                    },
                    "chulak": {
                        "Room Name": "Chulak",
                        "Room ID": "chulak",
                        "Capacity": 6,
                        "Total Persons": 0,
                        "Occupants": {}
                    },
                    "argos": {
                        "Room Name": "Argos",
                        "Room ID": "argos",
                        "Capacity": 6,
                        "Total Persons": 0,
                        "Occupants": {}
                    },
                },
                "Living Spaces": {}
                })
    def test_get_empty_rooms(self):
        self.assertEqual(
            self.amity.get_empty_rooms(),
            sorted(['Abydos', 'Chulak', 'Argos'])
        )

    @patch.dict('amity.amity.Amity.rooms', {
                "Offices": {},
                "Living Spaces": {}
                })
    @patch.dict('amity.amity.Amity.persons', {
                "Fellows": {},
                "Staff": {}
                })
    def test_response_on_no_rooms(self):
        response = self.amity.add_person("Colonel Samantha Carter", "Staff")
        self.assertEqual(
            response,
            "There are currently no rooms available"
        )

    @patch.dict('amity.amity.Amity.rooms', {
                "Offices": {
                    "daedalus": {
                        "Room Name": "Daedalus",
                        "Room ID": "daedalus",
                        "Capacity": 6,
                        "Total Persons": 0,
                        "Occupants": {}
                    }
                },
                "Living Spaces": {}
                })
    @patch.dict('amity.amity.Amity.persons', {
                "Fellows": {},
                "Staff": {}
                })
    def test_occupants_after_reallocation(self):
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

    @patch.dict('amity.amity.Amity.rooms', {
                "Offices": {},
                "Living Spaces": {}
                })
    @patch.dict('amity.amity.Amity.persons', {
                "Fellows": {},
                "Staff": {}
                })
    def test_staff_cannot_be_allocated_living_space(self):
        self.amity.create_room(['Wraith', '-ls'])
        response = self.amity.add_person('Tod The Wraith', 'Staff')
        self.assertEqual(
            response,
            "Staff cannot be allocated Living Space"
        )

    @patch.dict('amity.amity.Amity.rooms', {
                "Offices": {
                    "abydos": {
                        "Room Name": "Abydos",
                        "Room ID": "abydos",
                        "Capacity": 6,
                        "Total Persons": 0,
                        "Occupants": {
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
                    }
                },
                "Living Spaces": {
                    "daedalus": {
                        "Room Name": "Daedalus",
                        "Room ID": "daedalus",
                        "Capacity": 4,
                        "Total Persons": 0,
                        "Occupants": {
                            "Slot 1": {
                                "uuid": "f2",
                                "Name": "Jack O'Neall",
                                "Role": "Fellow",
                                "Wants Accommodation": "Y"
                            }
                        }
                    }
                }
                })
    def test_print_allocations(self):
        self.assertEqual(
            self.amity.print_allocations,
            "Successfuly printed and saved the allocations to a file"
        )

    @patch.dict('amity.amity.Amity.persons', {
                "Fellows": {
                    "f1": {
                        "uuid": "f1",
                        "Name": "Colonel Jack O'Neall",
                        "Role": "Fellow",
                        "Wants Accommodation": "N"
                    },
                    "f2": {
                        "uuid": "f2",
                        "Name": "Dr. Rodney McKay",
                        "Role": "Fellow",
                        "Wants Accommodation": "Y"
                    }
                },
                "Staff": {
                    "s1": {
                        "uuid": "s1",
                        "Name": "Ronon Dex",
                        "Role": "Staff",
                        "Wants Accommodation": "N"
                    }
                }
                })
    def test_print_unallocated(self):
        self.assertEqual(
            self.amity.print_unallocated,
            "Successfuly printed and saved all the unallocated people"
        )

    @patch.dict('amity.amity.Amity.rooms', {
                "Offices": {},
                "Living Spaces": {}
                })
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

    # TODO: Add file usage Mock here
    def test_load_people_from_file(self):
        response = self.amity.load_people("test_people.txt")
        self.assertEqual(
            response,
            "People have been successfuly added to the system."
        )

    # TODO: Add DB usage Mock here
    def test_save_state(self):
        self.assertEqual(
            self.amity.save_state("test.db"),
            "You have successfuly persisted the state of the Application."
        )

    # TODO: Add DB usage Mock here
    def test_load_state(self):
        self.assertEqual(
            self.amity.load_state("test.db"),
            "You have successfuly a previously saved state."
        )


if __name__ == '__main__':
    unittest.main()
