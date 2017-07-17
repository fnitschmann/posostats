from .candidate_seeder import CandidateSeeder
from .facebook_posts_seeder import FacebookPostsSeeder
from orator.seeds import Seeder
from .party_facebook_account_seeder import PartyFacebookAccountSeeder
from .party_twitter_account_seeder import PartyTwitterAccountSeeder
from .party_seeder import PartySeeder

class DatabaseSeeder(Seeder):
    def run(self):
        """
        Run the database seeds.

        ATTENTION: NEVER(!) change the order of this Seeders
        """
        self.call(PartySeeder)
        self.call(PartyFacebookAccountSeeder)
        self.call(PartyTwitterAccountSeeder)
        self.call(CandidateSeeder)
        self.call(FacebookPostsSeeder)
