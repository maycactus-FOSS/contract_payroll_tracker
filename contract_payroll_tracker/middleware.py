# contract_payroll_tracker/middleware.py

class FlushSessionOnPageChangeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get the current base URL from the request
        current_path = request.path

        # Get the stored base URL from the session
        stored_path = request.session.get('stored_path')

        # If the current base URL is different from the stored base URL, flush the relevant session data
        if current_path != stored_path:
            request.session.pop('sort_column', None)
            request.session.pop('sort_order', None)

        # Update the stored base URL in the session
        request.session['stored_path'] = current_path

        response = self.get_response(request)
        return response
