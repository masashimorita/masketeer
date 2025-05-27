from starlette.middleware.base import BaseHTTPMiddleware
from .maskteer import Maskteer


class MaskteerMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, config_file=None):
        self.maskteer = Maskteer(config_file)
        super().__init__(app)

    async def dispatch(self, request, call_next):
        try:
          response = await call_next(request)
          body = await response.body()
          if body:
              response.body_iterator = iter([self.maskteer.mask_text(body.decode()).encode()])
        except Exception as e:
            print(f"Error masking response content: {e}")
        return response
  

def assign_maskteer_middleware(app, config_file=None):
    maskteer = Maskteer(config_file)

    @app.middleware("http")
    async def mask_response(request, call_next):
        try:
          response = await call_next(request)
          body = await response.body()
          if body:
            response.body_iterator = iter([maskteer.mask_text(body.decode()).encode()])
        except Exception as e:
            print(f"Error masking response content: {e}")
        return response
