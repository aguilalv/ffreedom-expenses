import requests


class GoCardlessClient:
    def __init__(self, base_url, secret_id, secret_key):
        # Normalize base URL to avoid double-slashes
        self.base_url = base_url.rstrip("/")
        self.secret_id = secret_id
        self.secret_key = secret_key

        # Use a session for connection pooling and default headers
        self.session = requests.Session()
        self.session.headers.update(
            {
                "accept": "application/json",
                "Content-Type": "application/json",
            }
        )

    def get_access_token(self):
        """
        Request an access token from GoCardless.
        Returns the parsed JSON response as a dict.
        Raises HTTPError on non-2xx responses.
        """
        url = f"{self.base_url}/api/v2/token/new/"
        payload = {
            "secret_id": self.secret_id,
            "secret_key": self.secret_key,
        }
        response = self.session.post(url, json=payload)

        response.raise_for_status()
        return response.json()
