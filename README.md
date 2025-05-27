# Maskteer

Automatically mask sensitive information from logs or outputs for Django, Flask, and FastAPI applications.


## Installation

```bash
pip install maskteer
```

## Usage

### Django

In `settings.py`:
```python
MIDDLEWARE = [
    ...,
    'maskteer.django.MaskteerMiddleware',
]
```


### Flask

- Using maskteer as WSGI Middleware

  ```python
  from flask import Flask
  from maskteer.flask import MaskteerMiddleware

  app = Flask(__name__)
  app.wsgi_app = MaskteerMiddleware(app.wsgi_app) 
  ```

- Using maskteer as middleware function

  ```python
  from flask import Flask
  from maskteer.flask import assign_maskteer_middleware

  app = Flask(__name__)
  assign_maskteer_middleware(app)
  ```


### FastAPI

- Using maskteer as Middleware class

  ```python
  from fastapi import FastAPI
  from maskteer.fastapi import MaskteerMiddleware

  app = FastAPI()
  app.add_middleware(MaskteerMiddleware)
  ```

- Using maskteer as middleware function

  ```python
  from fastapi import FastAPI
  from maskteer.fastapi import assign_maskteer_middleware

  app = FastAPI()
  assign_maskteer_middleware(app)
  ```

## Configuration

You can configure via `maskteer.yaml` or environment variables:
```yaml
patterns:
  - "\\b[\\w.-]+@[\\w.-]+\\.\\w+\\b"
  - "(?i)password=[^\\s]+"
mask: "[REDACTED]"
```

Environment Variables:
```bash
export MASKTEER_PATTERNS="token=[^\\s]+,api_key=[^\\s]+"
export MASKTEER_MASK="[HIDDEN]"
```

## License

MIT License
