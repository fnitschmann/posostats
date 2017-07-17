from ..accounts import facebook
from orator import Model
from orator.orm import belongs_to

class FacebookPost(Model):
    __table__ = "facebook_posts"
    __fillable__ = ["comments_count", "facebook_account_id",
            "facebook_created_at",
            "facebook_post_id", "reactions_count"]
    __guarded__ = ["id"]

    @belongs_to
    def account(self):
        return facebook.FacebookAccount

    def link(self):
        return "{}{}".format(self.account.link, self.facebook_post_id)
