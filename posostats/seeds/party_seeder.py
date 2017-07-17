import os, sys, yaml

p = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if p not in sys.path:
    sys.path.append(p)

from models import Party
from models.accounts.facebook import FacebookAccount
from models.accounts.twitter import TwitterAccount
from orator.seeds import Seeder

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

        if "facebook_account" in attributes and attributes["facebook_account"] is not None:
            facebook_account = attributes["facebook_account"]
            self.__create_party_facebook_account(facebook_account, party)

        if "twitter_account" in attributes and attributes["twitter_account"] is not None:
            twitter_account = attributes["twitter_account"]
            self.__create_party_twitter_account(twitter_account, party)


    def __create_party_facebook_account(self, attributes, party):
        link = attributes["link"]
        page_name = attributes["page_name"]

        account = FacebookAccount.first_or_new(page_name = page_name)
        account.link = link
        account.party_id = party.id

        account.save()
        account.fetch_and_set_likes_count()

    def __create_party_twitter_account(self, attributes, party):
        link = attributes["link"]
        screen_name = attributes["screen_name"]

        account = TwitterAccount.first_or_new(screen_name = screen_name)
        account.link = link
        account.party_id = party.id

        account.save()
        account.fetch_and_set_followers_count()
