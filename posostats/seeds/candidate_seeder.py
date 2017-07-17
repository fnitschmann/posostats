import os, sys, yaml

p = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if p not in sys.path:
    sys.path.append(p)

from models import Candidate, Party
from models.accounts.facebook import FacebookAccount
from models.accounts.twitter import TwitterAccount
from orator.seeds import Seeder

class CandidateSeeder(Seeder):
    def run(self):
        """
        This seeds file creates all candidates defined in ./candidates.yml
        """
        filepath = os.path.abspath(os.path.dirname(__file__))
        filepath = os.path.join(filepath, "candidates.yml")

        with open(filepath) as candidates_file:
            try:
                candidates = yaml.load(candidates_file)["candidates"]
                self.__create_all_candidates(candidates)
            except Exception as e:
                print(e)

    def __create_all_candidates(self, candidates = {}):
        with self.db.transaction():
            for candidate_attributes in candidates:
                if "party" in candidate_attributes:
                    short_name = candidate_attributes["party"]
                    party = Party.where("short_name", short_name).first()

                    if party:
                        self.__create_candidate(candidate_attributes, party)
                    else:
                        continue
                else:
                    continue

    def __create_candidate(self, attributes, party):
        first_name = attributes["first_name"]
        last_name = attributes["last_name"]

        candidate = Candidate.first_or_new(first_name = first_name, last_name = last_name)
        candidate.party_id = party.id

        if "title" in attributes and attributes["title"] is not None:
            candidate.title = attributes["title"]

        candidate.save()

        if "facebook_account" in attributes and attributes["facebook_account"] is not None:
            facebook_account = attributes["facebook_account"]
            self.__create_candidate_facebook_account(facebook_account,
                    candidate, party)

        if "twitter_account" in attributes and attributes["twitter_account"] is not None:
            twitter_account = attributes["twitter_account"]
            self.__create_candidate_twitter_account(twitter_account, candidate,
                    party)

    def __create_candidate_facebook_account(self, attributes, candidate, party):
        link = attributes["link"]
        page_name = attributes["page_name"]

        account = FacebookAccount.first_or_new(page_name = page_name)
        account.link = link
        account.candidate_id = candidate.id
        account.party_id = party.id

        account.save()
        account.fetch_and_set_likes_count()

    def __create_candidate_twitter_account(self, attributes, candidate, party):
        link = attributes["link"]
        screen_name = attributes["screen_name"]

        account = TwitterAccount.first_or_new(screen_name = screen_name)
        account.link = link
        account.candidate_id = candidate.id
        account.party_id = party.id

        account.save()
