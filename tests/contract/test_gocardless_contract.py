import pytest
from pact import Consumer, Provider
from ffreedom_expenses.clients.gocardless import GoCardlessClient

PACT_MOCK_HOST = "localhost"
PACT_MOCK_PORT = 1234


@pytest.fixture(scope="module")
def pact():
    """Set up a Pact mock server for contract testing.

    This fixture initializes the Pact mock server to simulate the GoCardless API.
    It starts the server before the first test in the module runs and stops it
    after all tests have completed. The mock server listens on localhost and
    verifies HTTP interactions between the client and the mocked provider.

    Yields:
        pact.Pact: The Pact object configured with the consumer and provider.
    """
    pact = Consumer("MyAppClient").has_pact_with(
        Provider("GoCardless"),
        host_name=PACT_MOCK_HOST,
        port=PACT_MOCK_PORT,
        pact_dir="./tests/contract/pacts",  # save pact files here
        log_dir="./tests/contract/logs",  # save log files here
    )
    pact.start_service()
    yield pact
    pact.stop_service()


def test_get_access_token(pact):
    """Contract test: Verify the access token request to GoCardless.

    This test ensures that the GoCardlessClient sends the correct HTTP request
    when requesting an access token, and that it can handle a successful
    response from the provider. The Pact mock server validates that the request
    matches the expected method, path, headers, and JSON body as defined in the
    interaction contract.

    Args:
        pact (pact.Pact): The Pact fixture providing the mock server and contract builder.

    Raises:
        AssertionError: If the client does not process the response as expected
        (optional, depending on whether response assertions are included).
    """
    expected_response = {
        "access_token": "test_access_token",
        "token_type": "bearer",
        "expires_in": 3600,
    }

    # The expected request body matches your client exactly
    expected_request_body = {"secret_id": "test_id", "secret_key": "test_secret"}

    pact.given("valid secret credentials").upon_receiving(
        "a request for an access token"
    ).with_request(
        method="post",
        path="/api/v2/token/new/",
        headers={"Accept": "application/json", "Content-Type": "application/json"},
        body=expected_request_body,
    ).will_respond_with(
        200, body=expected_response, headers={"Content-Type": "application/json"}
    )

    with pact:
        client = GoCardlessClient(
            base_url=f"http://{PACT_MOCK_HOST}:{PACT_MOCK_PORT}",
            secret_id="test_id",
            secret_key="test_secret",
        )
        client.get_access_token()
        # result = client.get_access_token()
        # The assertion below is not needed because unit tests for the client already test its behaviour (returns parsed json on 200)
        # This test is only testing the 'contract' and therefore pact will fail if the client is not making the request expected in the contract
        # assert result == expected_response
