import unittest

from amity.room import Room, Office, LivingSpace


class TestAmity(unittest.TestCase):

    def setUp(self):
        self.office = Office("Chulak")
        self.living_space = LivingSpace("Dakara")

    def test_child_class_instance(self):
        self.assertIsInstance(self.office, Room)
        self.assertIsInstance(self.living_space, Room)

    def test_create_room(self):
        daedalus = Office("Daedalus")
        abydos = LivingSpace("Abydos")
        self.assertEqual(daedalus.name, "Daedalus")
        self.assertEqual(daedalus.type, "Office")
        self.assertEqual(daedalus.max_persons, 6)
        self.assertEqual(abydos.name, "Abydos")
        self.assertEqual(abydos.type, "Living Space")
        self.assertEqual(abydos.max_persons, 4)

    def test_occupants_increment_on_allocation(self):
        self.office.add_person('f1')
        self.office.add_person('f2')
        self.assertEqual(
            len(self.office.allocated_persons),
            2
        )

    def test_add_to_fully_occupied_rooms(self):
        self.office.total_persons = 6
        response = self.office.add_person('f7')
        self.assertEqual(
            response,
            "Chulak is fully booked. Try another room."
        )

    def test_occupants_after_reallocation(self):
        self.living_space.add_person('f3')
        self.living_space.add_person('f4')
        self.assertIn('f4', self.living_space.allocated_persons)


if __name__ == '__main__':
    unittest.main()
