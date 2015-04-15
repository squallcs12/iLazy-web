import time


class Wait5SecForLocalMiddleware(object):
    def process_response(self, request, response):
        if request.path.startswith('/api/') and request.META['REMOTE_ADDR'] == '127.0.0.1' \
                and getattr(response, 'accepted_media_type', None) == 'application/json':
            time.sleep(2)
        return response
