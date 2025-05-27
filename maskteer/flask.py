from .maskteer import Maskteer

class MaskteerMiddleware:
    def __init__(self, app):
        self.app = app
        self.maskteer = Maskteer()

    def __call__(self, environ, start_response):
        response = self.app(environ, start_response)
        try:
            response.set_data(self.maskteer.mask_text(response.get_data(as_text=True)))
        except Exception as e:
            print(f"Error masking response content: {e}")
        return response


def assign_maskteer_middleware(app, config_file=None):
    maskteer = Maskteer(config_file)

    @app.after_request
    def mask_response(response):
        try:
            response.set_data(maskteer.mask_text(response.get_data(as_text=True)))
        except Exception as e:
            print(f"Error masking response content: {e}")
        return response
