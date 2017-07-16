from orator.migrations import Migration

class CreateCandidatesTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("candidates") as table:
            table.increments("id")

            table.integer("party_id").unsigned()
            table.string("title", 4).nullable()
            table.string("first_name", 100)
            table.string("last_name", 100)

            table.foreign("party_id").references("id").on("parties")
            table.index("last_name")

            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("candidates")
