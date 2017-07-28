from abc import ABCMeta, abstractmethod
from flask import jsonify
from orator.orm.collection import Collection

from .singleton import Singleton

class RoutesController(Singleton, metaclass=ABCMeta):
    """
    This class is just an simple abstract wrapper for routing.
    It requires an instance of SubController during its' initialization
    """

    def __init__(self, controller):
        self.controller = controller

    @abstractmethod
    def register_routes(self):
        """
        This method has to be implemented in each controller that inheritates
        from this class.
        All routes for this controller have to be definied here
        """
        pass

    def json_response(self, obj = {}):
        return jsonify(obj)

    def serialized_json_api_obj(self, records = Collection()):
        """
        This method returns an single model or collection of models records
        serialized as JSONApi schema obj.

        NOTE: Currently just collection of the same model type are supported
        """
        result_obj = {}
        many = False
        schema = None

        if isinstance(records, Collection) and not records.is_empty():
            many = True
            schema = records.first().__class__.schema()
        elif callable(getattr(records.__class__, "schema")):
            many = False
            schema = records.__class__.schema()

        if schema:
            result_obj = self.__dump_schema(records=records, schema=schema, many=many)

        return result_obj

    def __dump_schema(self, records, schema, many):
        return schema.dump(records, many=many).data
