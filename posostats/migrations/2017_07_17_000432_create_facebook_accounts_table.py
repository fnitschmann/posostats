from orator.migrations import Migration

class CreateFacebookAccountsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('facebook_accounts') as table:
            table.increments("id")

            table.integer("candidate_id").unsigned().nullable()
            table.integer("party_id").unsigned()
            table.string("link", 200).unique()
            table.string("page_name", 100).unique()

            table.foreign("candidate_id").references("id").on("candidates")
            table.foreign("party_id").references("id").on("parties")
            table.index("page_name")

            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('facebook_accounts')
