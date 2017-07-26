import os, sys

p = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if p not in sys.path:
    sys.path.append(p)

from base import BaseController
from .parties import PartiesController

class ApiController(BaseController):
    controller_prefix = "/api"

    def register(self):
        self.__register_parties_controller()
        super().register()

    def __register_parties_controller(self):
        PartiesController(self.register_sub_controller("parties")).register_routes()
