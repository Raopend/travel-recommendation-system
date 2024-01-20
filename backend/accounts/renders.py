from rest_framework.renderers import BaseRenderer
from rest_framework.utils import json


class ApiRenderer(BaseRenderer):
    media_type = 'application/json'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        status_code = renderer_context["response"].status_code
        response = {
            "code": status_code,
            "data": data,
            "msg": None,
        }
        print(data)
        if not str(status_code).startswith("2"):
            errors_msg = data.get("errors", None)
            response["msg"] = errors_msg
            response["data"] = None
        else:
            response["msg"] = "success"

        return json.dumps(response)
