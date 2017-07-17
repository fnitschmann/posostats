from orator.migrations import Migration

class AddLikesCountColumn(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table("facebook_accounts") as table:
            table.integer("likes_count").default(0)

    def down(self):
        """
        Revert the migrations.
        """
        with self.schema.table("facebook_accounts") as table:
            table.drop_column("likes_count")
