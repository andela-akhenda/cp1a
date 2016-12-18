import unittest
from mock import patch
from amity.person import Person, Fellow, Staff


class TestPerson(unittest.TestCase):

    def setUp(self):
        self.fellow = Fellow("O'Neall")
        self.staff = Staff("Rodney")

    def test_child_class_instance(self):
        self.assertIsInstance(self.fellow, Person)
        self.assertIsInstance(self.staff, Person)

    @patch.dict('amity.person.Person.persons', {
                "Fellows": {},
                "Staff": {}
                })
    def test_add_person(self):
        jaffar = Staff("Teal'c")
        runner = Fellow("Ronon")
        colonel = Fellow("Samantha")
        self.assertEqual(jaffar.name, "Teal'c")
        self.assertEqual(runner.name, "Ronon")
        self.assertEqual(colonel.name, "Samantha")
        self.assertEqual(len(Person.persons['Staff'].keys()), 1)
        self.assertEqual(len(Person.persons['Fellows'].keys()), 2)

    def test_if_a_person_is_fellow_or_staff(self):
        self.assertEqual(self.staff.role, "Staff")
        self.assertEqual(self.fellow.role, "Fellow")

    @patch.dict('amity.person.Person.persons', {
                "Fellows": {},
                "Staff": {}
                })
    @patch.object(Person, "number_of_staff", 0)
    @patch.object(Person, "number_of_fellows", 0)
    @patch.object(Person, "total_persons", 0)
    @patch.object(Person, "error", "")
    def test_number_of_persons_increment_after_addition(self):
        Staff("Teal'c")
        Fellow("Ronon")
        Fellow("Samantha")
        self.assertEqual(Person.number_of_fellows, 2)
        self.assertEqual(Person.number_of_staff, 1)
        self.assertEqual(Person.total_persons, 3)
        self.assertEqual(len(Person.error), 0)

    @patch.dict('amity.person.Person.persons', {
                "Fellows": {
                    "f1": {
                        "uuid": "f1",
                        "Name": "Jack O'Neall",
                        "Role": "Fellow",
                        "Boarding": "Y"
                    }
                },
                "Staff": {}
                })
    def test_get_person(self):
        response = Person.get_person('f1')
        print response
        self.assertEqual(
            response,
            {
                "uuid": "f1",
                "Name": "Jack O'Neall",
                "Role": "Fellow",
                "Boarding": "Y"
            }
        )

    def test_get_person_with_invalid_uuid(self):
        response = Person.get_person('f2f3')
        self.assertEqual(
            response,
            "The person with UUID: f2f3 was not found"
        )

    def test_get_person_only_accepts_strings(self):
        response = Person.get_person(56)
        self.assertRaises(TypeError, response)
