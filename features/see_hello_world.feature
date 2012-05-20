Feature: User can get "Hello world!" when accessing the root URI

Scenario: User accesses root URI
    Given I am on the root URI
    Then I should see "Hello world!"
