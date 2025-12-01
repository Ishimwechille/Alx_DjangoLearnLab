class ContentSecurityPolicyMiddleware:
    """
    Simple CSP middleware to set Content-Security-Policy header.
    Adjust allowed sources as needed in production.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        # Minimal CSP - allow resources from self only, inline scripts/styles are blocked
        csp = "default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data:;"
        response['Content-Security-Policy'] = csp
        return response
