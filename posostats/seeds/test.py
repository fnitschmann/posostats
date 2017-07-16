import os, sys

p = os.path.abspath("..")
if p not in sys.path:
    sys.path.append(p)

import models
# from version import VERSION

# print(VERSION)

# from PythonClient.hashes.hash_function import hash_function
# from ..version import VERSION
