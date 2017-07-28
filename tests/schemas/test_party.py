import unittest

from orator.orm import Factory

from schemas import PartySchema
from tests.factories.parties_factory import *
from tests.support.database_helper import *

class TestPartySchema(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        init_test_db_connection(cls)

    @classmethod
    def tearDownClass(cls):
        close_test_db_connection(cls)

    def setUp(self):
        self.party = factory(Party).create()
        self.data = PartySchema().dump(self.party).data

    def test_basic_structure(self):
        self.assertIsInstance(self.data, dict)
        self.assertIn("data", self.data.keys())
        self.assertIsInstance(self.data["data"], dict)
        self.assertIn("attributes", self.data["data"].keys())
        self.assertIsInstance(self.data["data"]["attributes"], dict)
        self.assertIn("id", self.data["data"].keys())
        self.assertIn("type", self.data["data"].keys())

    def test_data_structure(self):
        data = self.data["data"]

        self.assertEqual(int(data["id"]), self.party.id)
        self.assertEqual(data["type"], "parties")

    def test_attributes_structure(self):
        attributes = self.data["data"]["attributes"]

        self.assertEqual(attributes["full_name"], self.party.full_name)
        self.assertEqual(attributes["short_name"], self.party.short_name)
        self.assertEqual(attributes["created_at"], str(self.party.created_at))
        self.assertEqual(attributes["updated_at"], str(self.party.updated_at))
