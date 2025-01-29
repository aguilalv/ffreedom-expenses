import requests
from behave import given, when, then

@given("I target the hello world endpoint")
def step_impl(context):
    # We'll build the final URL from the base_url in environment.py
    context.endpoint_url = f"{context.base_url}/hello"

@when("I send a GET request")
def step_impl(context):
    context.response = requests.get(context.endpoint_url)

@then("the response status code should be 200")
def step_impl(context):
    assert context.response.status_code == 200, \
        f"Expected 200, got {context.response.status_code}"

@then('the response body should contain "Hello, World!"')
def step_impl(context):
    assert "Hello, World!" in context.response.text, \
        f"Expected 'Hello, World!' in response, got {context.response.text}"

