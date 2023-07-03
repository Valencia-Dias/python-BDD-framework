Feature: Verify if books are added and deleted using library api

#53-54
  @library
  Scenario:  Verify AddBook api functionality
    Given Book details that need to be added to the library
    When We execute the AddBook PostAPI method
    Then Book has been added
    And Status code of the response should be 200

    #for parameterization-55
  @library
    Scenario Outline:  Verify AddBook api functionality
    Given Book details with <isbn> and <aisle>
    When We execute the AddBook PostAPI method
    Then Book has been added
      Examples:
        |  isbn| aisle |
        |  adfn| 3446 |
        |  radn| 6344  |


