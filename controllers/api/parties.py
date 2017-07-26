import os, sys

p = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if p not in sys.path:
    sys.path.append(p)

from utils import RoutesController

class PartiesController(RoutesController):
    def register_routes(self):
        controller = self.controller

        @controller.route("/", methods=["GET"])
        def index():
            return "All parties"
