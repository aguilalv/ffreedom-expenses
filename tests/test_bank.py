def test_bank_connect_root_returns_200(client):
    """
    Check that the root endpoint returns HTTP 200.
    """
    resp = client.get("/bank/connect")
    assert resp.status_code == 200, "/bank/connect endpoint should return OK"


def test_root_has_connect_to_bank_link(client):
    """
    Check that the bank/connect root endpoint shows a link to connect your bank.
    """
    resp = client.get("/bank/connect")
    body = resp.data.decode("utf-8")

    # basic substring check
    assert '<a href="/connect"' in body
    assert "Connect to your Bank" in body
