Feature: We would like to check if about page contains most important elements:
1. Description with header
2. Leadership team memebers
3. Clients

Scenario: We can see company description
    Given we start at mainpage
    When we click at about page
    Then we should land on about page
    And we should see first company description

Scenario Outline: We can see leadership team members
    Given we start at mainpage
    When we click at about page
    Then we should land on about page
    And we should see leadership <name> and <postion>
    Examples:
      | name            | postion                             |
      | Craig Rundels   | Chief Executive Officer             |
      | Denis Larkin    | Chief Operating Officer             |
      | Devin Young     | Sr. Director of PMO                 |
      | Paul Houlders   | Sr. Director of Art                 |
      | Valeriy Dutchak | Sr. Director of Engineering         |
      | Anna Trofimova  | Sr. Director of Business Operations |
    
Scenario Outline: We can see our clients logos
    Given we start at mainpage
    When we click at about page
    Then we should land on about page
    And we should see <brand> logo
    Examples:
      | brand                           |
      | Ubisoft                         |
      | Warner Bros. Entertainment Inc. |
      | 343 Industries                  |
      | Electronic Arts, Inc            |
      | Riot Games                      |

            