from .singleton import Singleton

class RoutesController(Singleton):
    """
    This class is just an simple wrapper for routing.
    It requires an instance of SubController during its' initialization
    """

    def __init__(self, controller):
        self.controller = controller

    def register_routes(self):
        """
        This method has to be implemented in each controller that inheritates
        from this class.
        All routes for this controller has to be definied here
        """
        pass
