import random, string

from orator.orm import Factory
from models import Party

factory = Factory()

@factory.define(Party)
def parties_factory(faker):
    char_set = string.ascii_uppercase + string.digits
    name = "".join(random.sample(char_set*10, 10))

    return {
            "full_name": name + " Party",
            "short_name": name
            }
