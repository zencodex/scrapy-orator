from orator.migrations import Migration


class CreateNoi2018AwardsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('noi2018_awards') as table:
            table.increments('id')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('noi2018_awards')
