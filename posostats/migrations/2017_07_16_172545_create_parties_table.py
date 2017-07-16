from orator.migrations import Migration

class CreatePartiesTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("parties") as table:
            table.increments("id")
            table.string("short_name", 10).unique()
            table.string("full_name", 100).nullable()

            table.index("short_name")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("parties")
