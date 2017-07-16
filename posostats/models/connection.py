import yaml, os

from orator import DatabaseManager, Model

db = None
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
config_filepath = os.path.join(root_dir, "config/orator.yml")

with open(config_filepath, "r") as config_file:
    try:
        config = yaml.load(config_file)
        db = DatabaseManager(config["databases"])
    except Exception as e:
        print(e)

Model.set_connection_resolver(db)
