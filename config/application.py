import os, sys, yaml

p = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if p not in sys.path:
    sys.path.append(p)

from utils import Singleton

class ApplicationConfig(Singleton):
    ALLOWED_ENVS = ["development", "production"]

    def __init__(self, environment = "development"):
        if environment in self.ALLOWED_ENVS:
            self.environment = environment
        else:
            err_msg = "environment has to be one of {}".format(self.ALLOWED_ENVS)
            raise ValueError(err_msg)

    def database_config(self):
        config = {}
        config_filepath = os.path.abspath(os.path.join(os.path.dirname(__file__),
            "database.yml"))

        with open(config_filepath, "r") as config_file:
            config = yaml.load(config_file)
            config = config[self.environment]

        return config

    def debug_mode_is_enabled(self):
        return self.environment == "development"
