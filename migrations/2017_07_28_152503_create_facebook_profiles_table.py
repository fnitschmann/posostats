from orator.migrations import Migration


class CreateFacebookProfilesTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('facebook_profiles') as table:
            table.increments('id')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('facebook_profiles')
