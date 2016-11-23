import unittest

from amity.person import Person, Fellow, Staff


class TestAmity(unittest.TestCase):

    def setUp(self):
        self.fellow = Fellow("O'Neall")
        self.staff = Staff("Rodney")

    def test_child_class_instance(self):
        self.assertIsInstance(self.fellow, Person)
        self.assertIsInstance(self.staff, Person)

    def test_add_person(self):
        jaffar = Staff("Teal'c")
        runner = Fellow("Ronon")
        self.assertEqual(jaffar.uuid, "s1")
        self.assertEqual(jaffar.name, "Teal'c")
        self.assertEqual(runner.uuid, "f1")
        self.assertEqual(runner.name, "Ronon")

    def test_if_a_person_is_fellow_or_staff(self):
        self.assertEqual(self.staff.role, "Staff")
        self.assertEqual(self.fellow.role, "Fellow")


if __name__ == '__main__':
    unittest.main()
