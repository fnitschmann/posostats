import os, sys, threading

p = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if p not in sys.path:
    sys.path.append(p)

from fetchers.posts.twitter import TwitterPostsFetcher
from models.accounts.twitter import TwitterAccount
from orator.seeds import Seeder

class TwitterPostsSeeder(Seeder):
    def run(self):
        """
        This seeds file imports all last 50 posts for parties' and candidates' Twitter
        profile
        """
        with self.db.transaction():
            accounts = TwitterAccount.all()

            for account in accounts:
                t = threading.Thread(target=self.__run_fetch, args=(account,))
                t.start()

    def __run_fetch(self, account):
        print("started Twitter post fetch for {}".format(account.link))
        TwitterPostsFetcher(account = account, count = 50).run()
        print("finished Twitter post fetch for {}".format(account.link))
