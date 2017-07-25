import os, yaml

class ApplicationConfig:
    ALLOWED_ENVS = ["development", "production"]

    singleton = None

    def __new__(cls, *args, **kwargs):
        if not cls.singleton:
            cls.singleton = object.__new__(ApplicationConfig)
        return cls.singleton

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
