import pytest
from requests import Session, HTTPError
from ffreedom_expenses.clients.gocardless import GoCardlessClient


def test_get_access_token_returns_parsed_json_on_success(monkeypatch):
    # Json response expected from the GoCardless API
    fake_payload = {
        "access": "tok1",
        "access_expires": 100,
        "refresh": "tok2",
        "refresh_expires": 200,
    }

    # Class to simulate a requests.Response object
    class FakeResp:
        status_code = 200

        def raise_for_status(self):
            pass

        def json(self):
            return fake_payload

    client = GoCardlessClient("https://api.example.com/", "id", "key")
    #  replace the client’s session with a fresh Session instance (ensures monkeypatch applies cleanly and doesn’t affect other tests or global state)
    client.session = Session()
    # override client.session.post to always return a new FakeResp. This prevents real HTTP calls and gives us predictable, fast tests.
    monkeypatch.setattr(client.session, "post", lambda *args, **kwargs: FakeResp())

    # Call the method under test
    result = client.get_access_token()

    # Check ...
    assert result == fake_payload


def test_get_access_token_raises_on_http_error(monkeypatch):
    class FakeResp:
        status_code = 401

        def raise_for_status(self):
            raise HTTPError("unauthorized")

    monkeypatch.setattr(Session, "post", lambda *args, **kwargs: FakeResp())

    client = GoCardlessClient("https://api.example.com", "id", "key")
    with pytest.raises(HTTPError):
        client.get_access_token()
