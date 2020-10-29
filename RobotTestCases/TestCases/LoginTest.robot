***Settings***
Library     SeleniumLibrary
Resource    ../Resources/CommonVariables.robot
Resource    ../Resources/CommonKeywords.robot
Resource    ../Resources/LoginKeywords.robot

**Test Cases***
LoginTest
    Open my browser            ${AdminLoginUrl}    ${Browser}
    Set Selenium Speed         0.1 seconds
    Enter Login Credentials
    CLose my browser
