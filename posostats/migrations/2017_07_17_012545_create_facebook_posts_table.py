from orator.migrations import Migration

class CreateFacebookPostsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("facebook_posts") as table:
            table.increments("id")

            table.integer("facebook_account_id").unsigned()
            table.string("facebook_post_id").unique()
            table.string("facebook_created_at").nullable()
            table.integer("comments_count").default(0)
            table.integer("reactions_count").default(0)

            table.foreign("facebook_account_id").references("id").on("facebook_accounts")

            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("facebook_posts")
