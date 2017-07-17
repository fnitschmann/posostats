from orator.migrations import Migration

class CreateTwitterPostsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("twitter_posts") as table:
            table.increments("id")

            table.integer("twitter_account_id").unsigned()
            table.string("twitter_post_id").unique()
            table.string("twitter_created_at").nullable()
            table.integer("favorites_count").default(0)
            table.integer("retweets_count").default(0)

            table.foreign("twitter_account_id").references("id").on("twitter_accounts")

            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("twitter_posts")
