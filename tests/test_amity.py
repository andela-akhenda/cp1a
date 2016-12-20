import os
import unittest
from mock import patch
from amity.amity import Amity
from amity.room import Room
from amity.person import Person


class TestAmity(unittest.TestCase):

    def setUp(self):
        self.amity = Amity()
        if os.path.exists('tests'):
            os.chdir('tests')

    def test_amity_class_instance(self):
        self.assertIsInstance(self.amity, Amity)

    def test_create_room_receives_list(self):
        response = self.amity.create_room('Abydos')
        self.assertRaises(TypeError, response)

    @patch.dict('amity.room.Room.rooms', {
                "Offices": {},
                "Living Spaces": {}
                })
    def test_create_room(self):
        response = self.amity.create_room(['Abydos'])
        self.assertEqual(response, "The Office has been successfully created")
        self.assertEqual(
            self.amity.create_room(['Daedalus', '-o']),
            "The Office has been successfully created"
        )

    @patch.dict('amity.room.Room.rooms', {
                "Offices": {
                    "abydos": {
                        "Room Name": "Abydos",
                        "Room ID": "abydos",
                        "Capacity": 6,
                        "Total Persons": 0,
                        "Occupants": []
                    }
                },
                "Living Spaces": {
                    "dakara": {
                        "Room Name": "Dakara",
                        "Room ID": "dakara",
                        "Capacity": 4,
                        "Total Persons": 0,
                        "Occupants": []
                    }
                }
                })
    @patch.dict('amity.person.Person.persons', {
                "Fellows": {
                    "f1": {
                        "person_id": "f1",
                        "Name": "Jaffa Teal'c",
                        "Role": "Fellow",
                        "Boarding": "Y"
                    }
                },
                "Staff": {}
                })
    @patch.object(Person, "number_of_staff", 0)
    @patch.object(Person, "number_of_fellows", 1)
    @patch.object(Person, "total_persons", 0)
    def test_add_person(self):
        self.assertRaises(TypeError, self.amity.add_person(123, 'Staff'))
        self.assertRaises(TypeError, self.amity.add_person('Jose A', 'Felow'))
        add = self.amity.add_person('General Hammond', 'Staff')
        add_fellow = self.amity.add_person('Ronon Dex', 'Fellow', 'N')
        add_staff = self.amity.add_person('Samantha Carter', 'Staff', 'Y')
        self.assertIn(
            'The Staff, General Hammond has been added successfuly',
            add
        )
        self.assertIn(
            'The Fellow, Ronon Dex has been added successfuly',
            add_fellow
        )
        self.assertIn(
            'Cannot allocate Staff a living space',
            add_staff
        )
        self.assertIn(
            "Allocate only accepts 'Y' or 'N'",
            self.amity.add_person('General Hammond', 'Staff', 'P')
        )
        self.assertIn(
            "The Fellow, Joseph Akhenda has been added successfuly",
            self.amity.add_person('Joseph Akhenda', 'Fellow', 'Y')
        )

    @patch.dict('amity.person.Person.persons', {
                "Fellows": {},
                "Staff": {}
                })
    @patch.object(Person, "number_of_staff", 0)
    @patch.object(Person, "number_of_fellows", 0)
    @patch.object(Person, "total_persons", 0)
    @patch('amity.amity.Amity.get_person_details')
    def test_if_a_person_is_fellow_or_staff(self, mock_get_person_details):
        mock_get_person_details.return_value = {
            "person_id": "s1",
            "Name": "General Hammond",
            "Role": "Staff",
            "Boarding": "N"
        }
        self.amity.add_person('General Hammond', 'Staff')
        # we should pass 'person_id' here
        response = mock_get_person_details('s1')
        self.assertEqual(response['Role'], "Staff")

    @patch.dict('amity.person.Person.persons', {
                "Fellows": {
                    "f1": {
                        "person_id": "f1",
                        "Name": "Jaffa Teal'c",
                        "Role": "Fellow",
                        "Boarding": "Y"
                    },
                    "f2": {
                        "person_id": "f2",
                        "Name": "Rodney McKay",
                        "Role": "Fellow",
                        "Boarding": "Y"
                    },
                    "f3": {
                        "person_id": "f3",
                        "Name": "Samantha Carter",
                        "Role": "Fellow",
                        "Boarding": "N"
                    }
                },
                "Staff": {
                    "s1": {
                        "person_id": "s1",
                        "Name": "Rodney McKay",
                        "Role": "Staff",
                        "Boarding": "N"
                    }
                }
                })
    def test_get_person_details_and_person_id(self):
        response = self.amity.get_person_details('f1')
        self.assertEqual(response['person_id'], "f1")
        self.assertEqual(response['Name'], "Jaffa Teal'c")
        self.assertEqual(response['Role'], "Fellow")
        self.assertEqual(response['Boarding'], "Y")
        self.assertEqual(
            self.amity.get_person_id('Samantha Carter'),
            "Samantha Carter's ID is: f3"
        )
        self.assertIn(
            "Several persons with the name 'Rodney McKay' exist.",
            self.amity.get_person_id('Rodney McKay')
        )
        self.assertIn(
            "The user, 'Rodney McKays' was not found",
            self.amity.get_person_id('Rodney McKays')
        )
        self.assertRaises(TypeError, self.amity.get_person_id(123))

    @patch.dict('amity.room.Room.rooms', {
                "Offices": {},
                "Living Spaces": {}
                })
    def test_create_multiple_rooms(self):
        response = self.amity.create_room(['Abydos', 'Chulak', 'Argos'])
        self.assertEqual(
            response,
            "Your 3 Offices have been successfully created"
        )

    @patch.dict('amity.room.Room.rooms', {
                "Offices": {},
                "Living Spaces": {
                    "dakara": {
                        "Room Name": "Dakara",
                        "Room ID": "dakara",
                        "Capacity": 4,
                        "Total Persons": 0,
                        "Occupants": []
                    }
                }
                })
    def test_cannot_add_duplicate_room(self):
        response = self.amity.create_room(['Dakara', 'Chulak', '-ls'])
        self.assertIn(
            "A room named 'Dakara' already exists. Please choose another name.",
            response
        )
        self.assertIn("Only 1 Living Space has been successfully created", response)
        self.assertIn(
            "No room was created",
            self.amity.create_room(['Dakara', 'Chulak', '-ls'])
        )
        self.assertIn(
            "Only 2 Living Spaces have been successfully created",
            self.amity.create_room(['Dakara', 'Argos', 'Hive', '-ls'])
        )

    @patch.dict('amity.room.Room.rooms', {
                "Offices": {
                    "abydos": {
                        "Room Name": "Abydos",
                        "Room ID": "abydos",
                        "Capacity": 6,
                        "Total Persons": 0,
                        "Occupants": []
                    }
                },
                "Living Spaces": {}
                })
    @patch.dict('amity.person.Person.persons', {
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

    @patch.dict('amity.room.Room.rooms', {
                "Offices": {},
                "Living Spaces": {
                    "chulak": {
                        "Room Name": "Chulak",
                        "Room ID": "chulak",
                        "Capacity": 4,
                        "Total Persons": 4,
                        "Occupants": ['f1', 'f2', 'f3', 'f4']
                    }
                }
                })
    @patch.dict('amity.person.Person.persons', {
                "Fellows": {
                    "f1": {
                        "person_id": "f1",
                        "Name": "Jack O'Neall",
                        "Role": "Fellow",
                        "Boarding": "Y"
                    },
                    "f2": {
                        "person_id": "f2",
                        "Name": "Rodney McKay",
                        "Role": "Fellow",
                        "Boarding": "Y"
                    },
                    "f3": {
                        "person_id": "f3",
                        "Name": "Ronon Dex",
                        "Role": "Fellow",
                        "Boarding": "Y"
                    },
                    "f4": {
                        "person_id": "f4",
                        "Name": "Daniel Jackson",
                        "Role": "Fellow",
                        "Boarding": "Y"
                    },
                    "f5": {
                        "person_id": "f5",
                        "Name": "Samantha Carter",
                        "Role": "Fellow",
                        "Boarding": "N"
                    }
                },
                "Staff": {}
                })
    def test_add_to_fully_occupied_room(self):
        response = self.amity.reallocate_person('f5', 'Chulak')
        self.assertEqual(
            response,
            "Chulak is fully booked. Try another room."
        )

    @patch.dict('amity.room.Room.rooms', {
                "Offices": {},
                "Living Spaces": {
                    "daedalus": {
                        "Room Name": "Daedalus",
                        "Room ID": "daedalus",
                        "Capacity": 4,
                        "Total Persons": 0,
                        "Occupants": []
                    }
                }
                })
    @patch.dict('amity.person.Person.persons', {
                "Fellows": {},
                "Staff": {
                    "s1": {
                        "person_id": "s1",
                        "Name": "General Hammond",
                        "Role": "Staff",
                        "Boarding": "N"
                    }
                }
                })
    def test_reallocate_staff_to_a_living_space(self):
        self.assertEqual(
            self.amity.reallocate_person('s1', 'Daedalus'),
            "Staff cannot be reallocated to a Living Space."
        )

    def test_reallocate_person_accepts_strings_only(self):
        self.assertRaises(TypeError, self.amity.reallocate_person('f5', 123))
        self.assertRaises(
            TypeError,
            self.amity.reallocate_person(['list'], 'Chulak')
        )

    @patch.dict('amity.room.Room.rooms', {
                "Offices": {
                    "argos": {
                        "Room Name": "Argos",
                        "Room ID": "argos",
                        "Capacity": 6,
                        "Total Persons": 0,
                        "Occupants": []
                    },
                    "daedalus": {
                        "Room Name": "Daedalus",
                        "Room ID": "daedalus",
                        "Capacity": 6,
                        "Total Persons": 1,
                        "Occupants": ['f1']
                    }
                },
                "Living Spaces": {}
                })
    @patch.dict('amity.person.Person.persons', {
                "Fellows": {
                    "f1": {
                        "person_id": "f1",
                        "Name": "Daniel Jackson",
                        "Role": "Fellow",
                        "Boarding": "Y"
                    }
                },
                "Staff": {}
                })
    def test_reallocate_person_to_an_office(self):
        response = self.amity.reallocate_person('f1', 'Argos')
        self.assertEqual(
            response,
            "Daniel Jackson has been successfuly re-allocated from Daedalus to Argos"
        )
        self.assertEqual(
            self.amity.reallocate_person('f1', 'Chulak'),
            "The room given does not exist"
        )

    @patch.dict('amity.room.Room.rooms', {
                "Offices": {},
                "Living Spaces": {}
                })
    @patch.dict('amity.person.Person.persons', {
                "Fellows": {},
                "Staff": {}
                })
    def test_reallocate_non_existent_person_id(self):
        response = self.amity.reallocate_person('d1', 'Dakara')
        self.assertEqual(
            response,
            "The given Person ID does not exist!"
        )

    @patch.dict('amity.room.Room.rooms', {
                "Offices": {},
                "Living Spaces": {}
                })
    @patch.dict('amity.person.Person.persons', {
                "Fellows": {},
                "Staff": {}
                })
    def test_response_on_no_rooms(self):
        response = self.amity.add_person("Samantha Carter", "Staff")
        self.assertIn(
            "The system has no Offices",
            response
        )

    @patch.dict('amity.room.Room.rooms', {
                "Offices": {
                    "daedalus": {
                        "Room Name": "Daedalus",
                        "Room ID": "daedalus",
                        "Capacity": 6,
                        "Total Persons": 0,
                        "Occupants": []
                    }
                },
                "Living Spaces": {}
                })
    @patch.dict('amity.person.Person.persons', {
                "Fellows": {},
                "Staff": {}
                })
    @patch.object(Person, "number_of_staff", 0)
    @patch.object(Person, "number_of_fellows", 0)
    @patch.object(Person, "total_persons", 0)
    @patch.object(Room, "number_of_offices", 0)
    @patch.object(Room, "number_of_living_spaces", 0)
    @patch.object(Room, "total_rooms", 0)
    def test_occupants_after_allocation(self):
        self.amity.add_person('Daniel Jackson', 'Fellow', 'Y')
        self.amity.add_person('General Hammond', 'Staff')
        occupants = self.amity.get_current_occupants('daedalus')
        # We ca also use Python's cmp() function below
        print occupants
        self.assertEqual(
            occupants,
            {
                "f1": {
                    "person_id": "f1",
                    "Name": "Daniel Jackson",
                    "Role": "Fellow",
                    "Boarding": "Y"
                },
                "s1": {
                    "person_id": "s1",
                    "Name": "General Hammond",
                    "Role": "Staff",
                    "Boarding": "N"
                }
            }
        )
        self.assertRaises(TypeError, self.amity.get_current_occupants(123))

    @patch.dict('amity.room.Room.rooms', {
                "Offices": {},
                "Living Spaces": {}
                })
    @patch.dict('amity.person.Person.persons', {
                "Fellows": {},
                "Staff": {}
                })
    def test_person_cannot_be_allocated_room_when_no_rooms_exist(self):
        self.amity.create_room(['Hive', '-ls'])
        response = self.amity.add_person('Tod Wraith', 'Staff')
        self.assertIn(
            "The system has no Offices",
            response
        )

    @patch.dict('amity.room.Room.rooms', {
                "Offices": {
                    "abydos": {
                        "Room Name": "Abydos",
                        "Room ID": "abydos",
                        "Capacity": 6,
                        "Total Persons": 2,
                        "Occupants": ['f1', 's1']
                    },
                    "chulak": {
                        "Room Name": "Chulak",
                        "Room ID": "chulak",
                        "Capacity": 6,
                        "Total Persons": 0,
                        "Occupants": []
                    }
                },
                "Living Spaces": {
                    "daedalus": {
                        "Room Name": "Daedalus",
                        "Room ID": "daedalus",
                        "Capacity": 4,
                        "Total Persons": 1,
                        "Occupants": ['f2']
                    }
                }
                })
    @patch.dict('amity.person.Person.persons', {
                "Fellows": {
                    "f1": {
                        "person_id": "f1",
                        "Name": "Jack O'Neall",
                        "Role": "Fellow",
                        "Boarding": "Y"
                    },
                    "f2": {
                        "person_id": "f2",
                        "Name": "Rodney McKay",
                        "Role": "Fellow",
                        "Boarding": "Y"
                    }
                },
                "Staff": {
                    "s1": {
                        "person_id": "s1",
                        "Name": "Ronon Dex",
                        "Role": "Staff",
                        "Boarding": "Y"
                    }
                }
                })
    def test_print_allocations(self):
        # os.chdir(sys.path[0] + '/tests')
        self.assertEqual(
            self.amity.print_allocations(None),
            "Successfuly printed the allocations"
        )
        self.assertEqual(
            self.amity.print_allocations('test.txt'),
            "Successfuly printed and saved the allocations to a file, test.txt in the '/data/outputs' directory."
        )

    @patch.dict('amity.room.Room.rooms', {
                "Offices": {},
                "Living Spaces": {}
                })
    @patch.dict('amity.person.Person.persons', {
                "Fellows": {},
                "Staff": {}
                })
    def test_print_allocations_with_no_previous_file(self):
        # os.chdir(sys.path[0] + '/tests')
        self.assertEqual(
            self.amity.print_allocations('no-test-file.txt'),
            "There is no data to print or save"
        )

    @patch.dict('amity.room.Room.rooms', {
                "Offices": {
                    "abydos": {
                        "Room Name": "Abydos",
                        "Room ID": "abydos",
                        "Capacity": 6,
                        "Total Persons": 2,
                        "Occupants": ['f5', 's4']
                    }
                },
                "Living Spaces": {
                    "daedalus": {
                        "Room Name": "Daedalus",
                        "Room ID": "daedalus",
                        "Capacity": 4,
                        "Total Persons": 1,
                        "Occupants": ['f7']
                    }
                }
                })
    @patch.dict('amity.person.Person.persons', {
                "Fellows": {
                    "f1": {
                        "person_id": "f1",
                        "Name": "Jack O'Neall",
                        "Role": "Fellow",
                        "Boarding": "N"
                    },
                    "f2": {
                        "person_id": "f2",
                        "Name": "Rodney McKay",
                        "Role": "Fellow",
                        "Boarding": "Y"
                    }
                },
                "Staff": {
                    "s1": {
                        "person_id": "s1",
                        "Name": "Ronon Dex",
                        "Role": "Staff",
                        "Boarding": "N"
                    }
                }
                })
    def test_print_unallocated(self):
        # os.chdir(sys.path[0] + '/tests')
        self.assertEqual(
            self.amity.print_unallocated(None),
            "Successfuly printed the unallocated"
        )
        self.assertEqual(
            self.amity.print_unallocated('test.txt'),
            "Successfuly printed and saved the unallocated to a file, test.txt in the '/data/outputs' directory."
        )

    @patch.dict('amity.room.Room.rooms', {
                "Offices": {},
                "Living Spaces": {}
                })
    @patch.dict('amity.person.Person.persons', {
                "Fellows": {},
                "Staff": {}
                })
    def test_print_unallocated_with_no_previous_file(self):
        # os.chdir(sys.path[0] + '/tests')
        self.assertEqual(
            self.amity.print_unallocated('no-test-file.txt'),
            "There is no data to print or save"
        )

    @patch.dict('amity.room.Room.rooms', {
                "Offices": {},
                "Living Spaces": {}
                })
    @patch.dict('amity.person.Person.persons', {
                "Fellows": {},
                "Staff": {}
                })
    @patch.object(Person, "number_of_staff", 0)
    @patch.object(Person, "number_of_fellows", 0)
    @patch.object(Person, "total_persons", 0)
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
                    "f1": {
                        "Boarding": "Y",
                        "Role": "Fellow",
                        "person_id": "f1",
                        "Name": "Jaffa Teal'c"
                    }
                }
            }
        )
        self.assertEqual(
            self.amity.print_room('daedalus'),
            "No room with the name 'Daedalus' exists!"
        )
        self.assertRaises(TypeError, self.amity.print_room(123))

    @patch.dict('amity.room.Room.rooms', {
                "Offices": {},
                "Living Spaces": {}
                })
    def test_print_empty_room(self):
        self.amity.create_room(['Daedalus', '-ls'])
        response = self.amity.print_room('daedalus')
        self.assertEqual(
            response,
            "Daedalus has no occupants"
        )

    # TODO: Add file usage Mock here
    @patch.dict('amity.room.Room.rooms', {
                "Offices": {},
                "Living Spaces": {}
                })
    @patch.dict('amity.person.Person.persons', {
                "Fellows": {},
                "Staff": {}
                })
    @patch.object(Person, "number_of_staff", 0)
    @patch.object(Person, "number_of_fellows", 0)
    @patch.object(Person, "total_persons", 0)
    def test_load_people_from_file(self):
        # os.chdir(sys.path[0] + '/tests')
        self.assertIn(
            "The given file does not exist.",
            self.amity.load_people('no_file.txt')
        )
        self.assertEqual(
            self.amity.load_people('test_people.txt'),
            "People have been successfuly added to the system."
        )
        self.assertRaises(TypeError, self.amity.load_people(123))

    # TODO: Add DB usage Mock here
    @patch.dict('amity.room.Room.rooms', {
                "Offices": {
                    "abydos": {
                        "Room Name": "Abydos",
                        "Room ID": "abydos",
                        "Capacity": 6,
                        "Total Persons": 2,
                        "Occupants": ['f5', 's4']
                    }
                },
                "Living Spaces": {
                    "daedalus": {
                        "Room Name": "Daedalus",
                        "Room ID": "daedalus",
                        "Capacity": 4,
                        "Total Persons": 1,
                        "Occupants": ['f7']
                    }
                }
                })
    @patch.dict('amity.person.Person.persons', {
                "Fellows": {
                    "f1": {
                        "person_id": "f1",
                        "Name": "Jack O'Neall",
                        "Role": "Fellow",
                        "Boarding": "N"
                    },
                    "f2": {
                        "person_id": "f2",
                        "Name": "Rodney McKay",
                        "Role": "Fellow",
                        "Boarding": "Y"
                    }
                },
                "Staff": {
                    "s1": {
                        "person_id": "s1",
                        "Name": "Ronon Dex",
                        "Role": "Staff",
                        "Boarding": "N"
                    }
                }
                })
    def test_save_state(self):
        # os.chdir(sys.path[0] + '/tests')
        self.assertIn(
            "You have successfuly persisted the state of the Application.",
            self.amity.save_state("test.db")
        )

    # TODO: Add DB usage Mock here
    @patch.object(Person, "persons", {"Fellows": {}, "Staff": {}})
    @patch.object(Room, "rooms", {"Offices": {}, "Living Spaces": {}})
    @patch.object(Person, "number_of_staff", 0)
    @patch.object(Person, "number_of_fellows", 0)
    @patch.object(Person, "total_persons", 0)
    @patch.object(Room, "number_of_offices", 0)
    @patch.object(Room, "number_of_living_spaces", 0)
    @patch.object(Room, "total_rooms", 0)
    def test_load_state(self):
        self.assertIn(
            "You have successfuly loaded a previously saved state.",
            self.amity.load_state("load_test.db")
        )

    def test_load_state_from_non_conforming_db(self):
        self.assertEqual(
            self.amity.load_state("non_conforming.db"),
            "No such table exists. Please check that you loaded the correct DB."
        )


if __name__ == '__main__':
    unittest.main()
