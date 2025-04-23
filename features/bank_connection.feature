Feature: Bank Connection
  As a user
  I want to connect my bank account
  So that I can track my expenses automatically

  Scenario: Successfully connect to a bank
    Given I am in the bank connection page
    When I click on "Connect Bank"
    Then I should see a list of available banks 