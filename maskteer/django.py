from .maskteer import Maskteer

class MaskteerMiddleware:
    def __init__(self, get_response):
        self.maskteer = Maskteer()
        self.get_response = get_response

    def __call__(self, request):
        try:
            response = self.get_response(request)
            if response.content:
                response.content = self.maskteer.mask_text(response.content.decode()).encode()
        except Exception as e:
            print(f"Error masking response content: {e}")
        return response
