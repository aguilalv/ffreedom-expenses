def test_hello_endpoint_returns_200(client):
    """
    Check that the hello endpoint returns HTTP 200.
    """
    response = client.get("/hello")
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"


def test_hello_endpoint_returns_correct_body(client):
    """
    Check that the hello endpoint returns the expected "Hello, World!" text.
    """
    response = client.get("/hello")
    expected_text = "Hello, World!"
    # Flask test client returns bytes in response.data
    # so compare against a bytes string, or decode first
    assert (
        expected_text in response.data.decode()
    ), f"Expected '{expected_text}', got {response.data}"
