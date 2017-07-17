import json, urllib.request, os, sys

p = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if p not in sys.path:
    sys.path.append(p)

from utils.url import *

def get_facebook_graph_api_response(path, params = {}):
    url = "https://graph.facebook.com/{path}?{params}".format(**{
        "path": path,
        "params": url_params_for_facebook(params)
        })

    return get_json_response(url)

def get_json_response(url):
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    return json.loads(response.read().decode("utf-8"))
