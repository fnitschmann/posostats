import os, sys

p = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if p not in sys.path:
    sys.path.append(p)

from config.social_networks import FACEBOOK_APP_ID, FACEBOOK_APP_SECRET
from urllib.parse import urlencode

def url_params_for_facebook(params = {}):
    params["access_token"] = "{}|{}".format(FACEBOOK_APP_ID, FACEBOOK_APP_SECRET)
    return urlencode(params)
