import os, sys, yaml

p = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if p not in sys.path:
    sys.path.append(p)

from models import Candidate, Party
from models.accounts.twitter import TwitterAccount
from orator.seeds import Seeder

class PartyTwitterAccountSeeder(Seeder):
    def run(self):
        """
        This seeds file creates all facebook account for a party defined in
        ./party_twitter_accounts.yml
        """
        filepath = os.path.abspath(os.path.dirname(__file__))
        filepath = os.path.join(filepath, "party_twitter_accounts.yml")

        with open(filepath) as accounts_file:
            try:
                accounts = yaml.load(accounts_file)["accounts"]
                self.__create_all_accounts(accounts)
            except Exception as e:
                print(e)


    def __create_all_accounts(self, accounts = {}):
        with self.db.transaction():
            for account_attributes in accounts:
                if "party" in account_attributes:
                    short_name = account_attributes["party"]
                    party = Party.where("short_name", short_name).first()

                    if party:
                        self.__create_account(account_attributes, party)
                    else:
                        continue
                else:
                    continue

    def __create_account(self, attributes, party):
        link = attributes["link"]
        screen_name = attributes["screen_name"]

        account = TwitterAccount.first_or_new(screen_name = screen_name)
        account.link = link
        account.party_id = party.id

        account.save()
