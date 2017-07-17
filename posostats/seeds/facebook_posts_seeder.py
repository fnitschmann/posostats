import os, sys, threading

p = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if p not in sys.path:
    sys.path.append(p)

from fetchers.posts.facebook import FacebookPostsFetcher
from models.accounts.facebook import FacebookAccount
from orator.seeds import Seeder

class FacebookPostsSeeder(Seeder):
    def run(self):
        """
        This seeds file imports all posts for parties' and candidates' Facebook
        pages since 10 days
        """
        with self.db.transaction():
            accounts = FacebookAccount.all()

            for account in accounts:
                t = threading.Thread(target=self.__run_fetch, args=(account,))
                t.start()

    def __run_fetch(self, account):
        print("started Facebook post fetch for {}".format(account.link))
        FacebookPostsFetcher(account = account, since_days = 10).run()
        print("finished Facebook post fetch for {}".format(account.link))
