from orator.seeds import Seeder

from .party_seeder import PartySeeder

class DatabaseSeeder(Seeder):
    def run(self):
        """
        Executes the database seeders and sets up an default set of needed data

        ATTENTION: Never(!) change the order of the following executed seeders
        """
        self.call(PartySeeder)

