import unittest
from mock import patch
from amity.room import Room, Office, LivingSpace
from amity.person import Fellow


class TestRoom(unittest.TestCase):

    def setUp(self):
        self.office = Office("Chulak")
        self.living_space = LivingSpace("Dakara")
        Fellow("Magarita Nangoma")
        Fellow("Sabina Ingwe")
        Fellow("Anne Anyiru")
        Fellow("Sparkle Val")
        Fellow("Matty Kate")

    def test_child_class_instance(self):
        self.assertIsInstance(self.office, Room)
        self.assertIsInstance(self.living_space, Room)

    @patch.dict('amity.room.Room.rooms', {
                "Offices": {},
                "Living Spaces": {}
                })
    def test_create_room(self):
        daedalus = Office("Daedalus")
        abydos = LivingSpace("Abydos")
        self.assertEqual(daedalus.name, "Daedalus")
        self.assertEqual(daedalus.room_type, "Office")
        self.assertEqual(daedalus.capacity, 6)
        self.assertEqual(abydos.name, "Abydos")
        self.assertEqual(abydos.room_type, "Living Space")
        self.assertEqual(abydos.capacity, 4)

    @patch.dict('amity.room.Room.rooms', {
                "Offices": {
                    "chulak": {
                        "Room Name": "Chulak",
                        "Room ID": "chulak",
                        "Capacity": 6,
                        "Total Persons": 0,
                        "Occupants": []
                    }
                },
                "Living Spaces": {}
                })
    def test_create_duplicate_room(self):
        chulak = Office("Chulak")
        self.assertEqual(
            chulak.error,
            "A room named 'Chulak' already exists. Please choose another name."
        )
        del(chulak)

    @patch.dict('amity.room.Room.rooms', {
                "Offices": {
                    "chulak": {
                        "Room Name": "Chulak",
                        "Room ID": "chulak",
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
                "Staff": {}
                })
    def test_occupants_increment_on_allocation(self):
        Room.add_person('f1', 'Fellows', 'Office', 'Y')
        Room.add_person('f2', 'Fellows', 'Office', 'Y')
        self.assertEqual(
            Room.rooms['Offices']['chulak']['Total Persons'],
            2
        )

    @patch.dict('amity.room.Room.rooms', {
                "Offices": {},
                "Living Spaces": {}
                })
    @patch.dict('amity.person.Person.persons', {
                "Fellows": {},
                "Staff": {}
                })
    def test_add_to_fully_occupied_rooms(self):
        self.ruby = Office("Ruby")
        Room.rooms['Offices']['ruby']['Occupants'] = ['s1', 's2', 's3', 's4', 'f7', 'f6']
        Room.rooms['Offices']['ruby']['Total Persons'] = 6
        response = self.office.add_person('f5', 'Fellows', 'Office', 'Y')
        self.assertIn(
            "There are currently no Offices available.",
            response
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
    @patch.dict('amity.person.Person.persons', {
                "Fellows": {
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
                    }
                },
                "Staff": {}
                })
    def test_occupants_after_reallocation(self):
        Room.add_person('f3', 'Fellows', 'Living Space', 'Y')
        Room.add_person('f4', 'Fellows', 'Living Space', 'Y')
        self.assertIn('f4', Room.rooms['Living Spaces']['dakara']['Occupants'])
