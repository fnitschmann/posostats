from .candidate_seeder import CandidateSeeder
from orator.seeds import Seeder
from .party_facebook_account_seeder import PartyFacebookAccountSeeder
from .party_seeder import PartySeeder

class DatabaseSeeder(Seeder):
    def run(self):
        """
        Run the database seeds.

        ATTENTION: NEVER(!) change the order of this Seeders
        """
        self.call(PartySeeder)
        self.call(PartyFacebookAccountSeeder)
        self.call(CandidateSeeder)
