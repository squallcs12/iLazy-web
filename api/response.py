from rest_framework.response import Response as OriginResponse


class Response(OriginResponse):
    def __init__(self, data=None, **kwargs):
        if isinstance(data, dict):
            if 'errors' in data:
                data['success'] = False
            else:
                data['success'] = True
        super(Response, self).__init__(data=data, **kwargs)
