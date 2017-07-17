from orator.migrations import Migration

class AddFollowersCountToTwitterAccounts(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table("twitter_accounts") as table:
            table.integer("followers_count").default(0)

    def down(self):
        """
        Revert the migrations.
        """
        with self.schema.table("twitter_accounts") as table:
            table.drop_column("followers_count")
