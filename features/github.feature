Feature: Github API validation


  Scenario: Check session management
    Given  I have github auth credentials
    When I hit getRepo API of github
    Then Status code of the response should be 200