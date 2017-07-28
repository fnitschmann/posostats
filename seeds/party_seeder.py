import os, sys, yaml

p = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if p not in sys.path:
    sys.path.append(p)

from orator.seeds import Seeder

from models import Party

class PartySeeder(Seeder):
    def run(self):
        """
        This seeds file creates all parties defined in ./parties.yml
        """
        filepath = os.path.abspath(os.path.dirname(__file__))
        filepath = os.path.join(filepath, "parties.yml")

        with open(filepath, "r") as parties_file:
            try:
                parties = yaml.load(parties_file)["parties"]

                with self.db.transaction():
                    for party in parties:
                        self.__create_party(party)
            except Exception as e:
                print(e)

    def __create_party(self, attributes = {}):
        party = Party.first_or_create(short_name = attributes["short_name"])

        if "full_name" in attributes and attributes["full_name"] is not None:
            party.full_name = attributes["full_name"]
            party.save()
