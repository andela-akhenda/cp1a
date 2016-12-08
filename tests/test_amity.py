import sys
import os.path
import unittest
from mock import patch
from amity.amity import Amity
from amity.room import Room, LivingSpace, Office
from amity.person import Person, Fellow, Staff

# sys.path.insert(0,os.path.abspath(__file__+"/../.."))
# os.path.isfile = lambda path: path == '/tests/'


class TestAmity(unittest.TestCase):

    def setUp(self):
        self.amity = Amity()
        os.chdir(sys.path[0])

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
        self.assertEqual(response, "The room has been successfully created")
        self.assertEqual(
            self.amity.create_room(['Daedalus', '-o']),
            "The room has been successfully created"
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
                "Fellows": {
                    "f1": {
                        "uuid": "f1",
                        "Name": "Jaffa Teal'c",
                        "Role": "Fellow",
                        "Boarding": "Y"
                    }
                },
                "Staff": {}
                })
    @patch.object(Person, "number_of_staff", 0)
    @patch.object(Person, "number_of_fellows", 0)
    @patch.object(Person, "total_persons", 0)
    def test_add_person(self):
        self.assertRaises(TypeError, self.amity.add_person(123, 'Staff'))
        self.assertRaises(TypeError, self.amity.add_person('Jose A', 'Felow'))
        add = self.amity.add_person('General Hammond', 'Staff')
        add_fellow = self.amity.add_person('Ronon Dex', 'Fellow', 'N')
        add_staff = self.amity.add_person('Samantha Carter', 'Staff', 'Y')
        self.assertEqual(
            add,
            'The Staff has been added successfuly'
        )
        self.assertEqual(
            add_fellow,
            'The Fellow has been added successfuly'
        )
        self.assertIn(
            'Cannot allocate Staff a living space',
            add_staff
        )
        self.assertIn(
            "Allocate only accepts 'Y' or 'N'",
            self.amity.add_person('General Hammond', 'Staff', 'P')
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
            "uuid": "s1",
            "Name": "General Hammond",
            "Role": "Staff",
            "Boarding": "N"
        }
        self.amity.add_person('General Hammond', 'Staff')
        # we should pass 'uuid' here
        response = mock_get_person_details('s1')
        self.assertEqual(response['Role'], "Staff")

    @patch.dict('amity.person.Person.persons', {
                "Fellows": {
                    "f1": {
                        "uuid": "f1",
                        "Name": "Jaffa Teal'c",
                        "Role": "Fellow",
                        "Boarding": "Y"
                    }
                },
                "Staff": {}
                })
    def test_get_person_details(self):
        response = self.amity.get_person_details('f1')
        self.assertEqual(response['uuid'], "f1")
        self.assertEqual(response['Name'], "Jaffa Teal'c")
        self.assertEqual(response['Role'], "Fellow")
        self.assertEqual(response['Boarding'], "Y")

    @patch.dict('amity.room.Room.rooms', {
                "Offices": {},
                "Living Spaces": {}
                })
    def test_create_multiple_rooms(self):
        response = self.amity.create_room(['Abydos', 'Chulak', 'Argos'])
        self.assertEqual(
            response,
            "Your 3 rooms have been successfully created"
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
        self.assertIn("Only 1 room has been successfully created", response)
        self.assertIn(
            "No room was created",
            self.amity.create_room(['Dakara', 'Chulak', '-ls'])
        )
        self.assertIn(
            "Only 2 rooms have been successfully created",
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
                    },
                    "daedalus": {
                        "Room Name": "Daedalus",
                        "Room ID": "daedalus",
                        "Capacity": 4,
                        "Total Persons": 0,
                        "Occupants": ['f5']
                    }
                }
                })
    @patch.dict('amity.person.Person.persons', {
                "Fellows": {
                    "f1": {
                        "uuid": "f1",
                        "Name": "Jack O'Neall",
                        "Role": "Fellow",
                        "Boarding": "Y"
                    },
                    "f2": {
                        "uuid": "f2",
                        "Name": "Rodney McKay",
                        "Role": "Fellow",
                        "Boarding": "Y"
                    },
                    "f3": {
                        "uuid": "f3",
                        "Name": "Ronon Dex",
                        "Role": "Fellow",
                        "Boarding": "Y"
                    },
                    "f4": {
                        "uuid": "f4",
                        "Name": "Daniel Jackson",
                        "Role": "Fellow",
                        "Boarding": "Y"
                    },
                    "f5": {
                        "uuid": "f5",
                        "Name": "Samantha Carter",
                        "Role": "Fellow",
                        "Boarding": "N"
                    }
                },
                "Staff": {}
                })
    def test_add_to_fully_occupied_rooms(self):
        response = self.amity.reallocate_person('f5', 'Chulak')
        self.assertEqual(
            response,
            "Chulak is fully booked. Try another room."
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
                        "Total Persons": 0,
                        "Occupants": ['f1']
                    }
                },
                "Living Spaces": {}
                })
    @patch.dict('amity.person.Person.persons', {
                "Fellows": {
                    "f1": {
                        "uuid": "f1",
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
            "The person has been successfuly re-allocated to Argos"
        )
        self.assertEqual(
            self.amity.reallocate_person('f1', 'Chulak'),
            "The room given does not exist"
        )

    @patch.dict('amity.room.Room.rooms', {
                "Offices": {
                    "abydos": {
                        "Room Name": "Abydos",
                        "Room ID": "abydos",
                        "Capacity": 6,
                        "Total Persons": 0,
                        "Occupants": []
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
                    "argos": {
                        "Room Name": "Argos",
                        "Room ID": "argos",
                        "Capacity": 4,
                        "Total Persons": 0,
                        "Occupants": []
                    }
                }
                })
    def test_get_empty_rooms(self):
        response = self.amity.get_empty_rooms()
        self.assertIn(
            'abydos',
            response['Offices']
        )
        self.assertIn(
            'chulak',
            response['Offices']
        )
        self.assertIn(
            'argos',
            response['Living Spaces']
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
            "The system has no rooms",
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
                    "uuid": "f1",
                    "Name": "Daniel Jackson",
                    "Role": "Fellow",
                    "Boarding": "Y"
                },
                "s1": {
                    "uuid": "s1",
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
            "The system has no rooms",
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
                        "uuid": "f1",
                        "Name": "Jack O'Neall",
                        "Role": "Fellow",
                        "Boarding": "Y"
                    },
                    "f2": {
                        "uuid": "f2",
                        "Name": "Rodney McKay",
                        "Role": "Fellow",
                        "Boarding": "Y"
                    }
                },
                "Staff": {
                    "s1": {
                        "uuid": "s1",
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
            "Successfuly printed and saved the allocations to a file"
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
                        "uuid": "f1",
                        "Name": "Jack O'Neall",
                        "Role": "Fellow",
                        "Boarding": "N"
                    },
                    "f2": {
                        "uuid": "f2",
                        "Name": "Rodney McKay",
                        "Role": "Fellow",
                        "Boarding": "Y"
                    }
                },
                "Staff": {
                    "s1": {
                        "uuid": "s1",
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
            "Successfuly printed the unallocations"
        )
        self.assertEqual(
            self.amity.print_unallocated('test.txt'),
            "Successfuly printed and saved the unallocated to a file"
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
                        "uuid": "f1",
                        "Name": "Jaffa Teal'c"
                    }
                }
            }
        )
        self.assertRaises(TypeError, self.amity.print_room(123))

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
        response = self.amity.load_people('test_people.txt')
        self.assertEqual(
            response,
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
                        "uuid": "f1",
                        "Name": "Jack O'Neall",
                        "Role": "Fellow",
                        "Boarding": "N"
                    },
                    "f2": {
                        "uuid": "f2",
                        "Name": "Rodney McKay",
                        "Role": "Fellow",
                        "Boarding": "Y"
                    }
                },
                "Staff": {
                    "s1": {
                        "uuid": "s1",
                        "Name": "Ronon Dex",
                        "Role": "Staff",
                        "Boarding": "N"
                    }
                }
                })
    def test_save_state(self):
        # os.chdir(sys.path[0] + '/tests')
        self.assertEqual(
            self.amity.save_state("test.db"),
            "You have successfuly persisted the state of the Application."
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
        self.assertEqual(
            self.amity.load_state("load_test.db"),
            "You have successfuly loaded a previously saved state."
        )


if __name__ == '__main__':
    unittest.main()
