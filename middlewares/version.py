from alloff_backoffice_server.settings import COMMIT_SHA


def version_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = get_response(request)

        # Code to be executed for each request/response after
        # the view is called.
        response["API-Version"] = COMMIT_SHA
        return response

    return middleware
