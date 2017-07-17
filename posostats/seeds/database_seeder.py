from .candidate_seeder import CandidateSeeder
from .facebook_posts_seeder import FacebookPostsSeeder
from orator.seeds import Seeder
from .party_seeder import PartySeeder
from .twitter_posts_seeder import TwitterPostsSeeder

class DatabaseSeeder(Seeder):
    def run(self):
        """
        Run the database seeds.

        ATTENTION: NEVER(!) change the order of this Seeders
        """
        self.call(PartySeeder)
        self.call(CandidateSeeder)
        self.call(FacebookPostsSeeder)
        self.call(TwitterPostsSeeder)
