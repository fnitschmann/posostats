from ..accounts import twitter
from orator import Model
from orator.orm import belongs_to

class TwitterPost(Model):
    __table__ = "twitter_posts"
    __fillable__ = ["favorites_count", "retweets_count", "twitter_account_id",
            "twitter_created_at", "twitter_post_id"]
    __guarded__ = ["id"]

    @belongs_to
    def account(self):
        return twitter.TwitterAccount

    def link(self):
        return "{}{}".format(self.account.link, self.twitter_post_id)
