import os, sys

p = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if p not in sys.path:
    sys.path.append(p)

from flask import Blueprint
from utils import Singleton, SubController

class BaseController(Singleton):
    controller_prefix = None
    sub_controllers = []

    def __init__(self, app):
        self.app = app
        self.__create_blueprint()

    def register(self):
        self.app.register_blueprint(self.blueprint)
        self.__register_sub_controller_blueprints()

    def register_sub_controller(self, prefix):
        sub_controller = SubController(self.blueprint, prefix)

        if sub_controller not in self.sub_controllers:
            self.sub_controllers.append(sub_controller)

        return sub_controller

    # private

    def __create_blueprint(self):
        if self.controller_prefix.startswith("/"):
            self.blueprint = Blueprint(self.controller_prefix, __name__,
                url_prefix = self.controller_prefix)
        else:
            err_msg = "controller_prefix must start with a leading slash"
            raise ValueError(err_msg)

    def __register_sub_controller_blueprints(self):
        for controller in self.sub_controllers:
            self.app.register_blueprint(controller.blueprint)
