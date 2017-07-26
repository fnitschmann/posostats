class SubController(object):
    """
    This class offers modular and nested route controller structures for Flask
    blueprints
    """
    def __init__(self, blueprint, prefix):
        super(SubController, self).__init__()
        self.blueprint = blueprint
        self.prefix = "/" + prefix

    def route(self, rule, **options):
        rule = self.prefix + rule
        return self.blueprint.route(rule, **options)
