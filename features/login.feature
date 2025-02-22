    Feature: Login Functionality

        Scenario: User should be logged in to Swag Labs
            Given user is on login page
            When user enters the valid username
            When user enters the valid password
            When user clicks on login button
            Then user should be landed on dashboard page