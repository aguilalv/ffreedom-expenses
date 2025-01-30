import pytest
from ffreedom_expenses import create_app


@pytest.fixture
def client():
    """
    Provide a Flask test client that can be used by multiple test files.
    """
    app = create_app()
    with app.test_client() as client:
        yield client
