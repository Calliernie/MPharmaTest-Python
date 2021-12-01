Feature: Patient Creation

  Scenario: Adding a patient's details to the database
    Given I open the a browser and navigate to the URL
    When I type the patient's first name
    Then I type the patient's middle name
    Then I type the patient's last name
    Then I type the patient's phone number
    Then I type the patient's date of birth
    Then I type the patient's address
    When I click on the add new user button
    Then I should see the added patient's full name
    Then I should see the added patient's address
    Then I should see the added patient's date of birth