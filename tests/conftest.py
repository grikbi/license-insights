"""Definition of fixtures for static data, sessions etc. used by unit tests."""

import pytest

from src.rest_api import *
from starlette.testclient import TestClient

@pytest.fixture
def client():
    """Provide the client session used by tests."""
    with TestClient(app) as client:
        yield client
