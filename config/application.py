import os, sys, yaml

p = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if p not in sys.path:
    sys.path.append(p)

from utils import Singleton

class ApplicationConfig(Singleton):
    ALLOWED_ENVS = ["development", "production", "test"]

    def __init__(self, environment = "development"):
        self.set_env(environment)

    def database_config(self):
        return self.database_config_for_env(self.environment)

    def database_config_for_env(self, environment):
        config = {}
        config_filepath = os.path.abspath(os.path.join(os.path.dirname(__file__),
            "database.yml"))

        with open(config_filepath, "r") as config_file:
            config = yaml.load(config_file)
            config = config[environment]

        return config

    def debug_mode_is_enabled(self):
        return self.environment == "development" or self.environment == "test"

    def set_env(self, environment):
        """
        NOTE: This function should never be called in production environments
        and be treated with care
        """
        if environment in self.ALLOWED_ENVS:
            self.environment = environment
        else:
            err_msg = "environment has to be one of {}".format(self.ALLOWED_ENVS)
            raise ValueError(err_msg)

