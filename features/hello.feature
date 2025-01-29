Feature: Hello World Endpoint
  As a user of the service
  I want to see a successful "Hello, World!" response
  So that I know the server is working properly

  Scenario: GET /hello
    Given I target the hello world endpoint
    When I send a GET request
    Then the response status code should be 200
    And the response body should contain "Hello, World!"

