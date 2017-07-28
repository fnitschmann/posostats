import os, sys

p = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if p not in sys.path:
    sys.path.append(p)

from models import Party
from utils import RoutesController

class PartiesController(RoutesController):
    def register_routes(self):
        controller = self.controller

        @controller.route("/", methods=["GET"])
        def index():
            result_obj = self.serialized_json_api_obj(Party.all())
            return self.json_response(result_obj)

        @controller.route("/<int:party_id>", methods=["GET"])
        def show_party(party_id):
            party = Party.find_or_fail(party_id)
            result_obj = self.serialized_json_api_obj(party)
            return self.json_response(result_obj)
