***Settings***
Library     SeleniumLibrary
Resource    ../Resources/CommonVariables.robot
Resource    ../Resources/CommonKeywords.robot
Resource    ../Resources/OrgKeywords.robot

**Test Cases***
OrgTest
    Open my browser                           ${OrgUrl}      ${Browser}
    Set Selenium Speed                        0.1 seconds
    Enter Login Credentials
    Click Add Organization
    Enter Organization Name                   ${org}
    Click Save
    Select unselect checkbox                  
    Select delete from dropdown and delete    
    CLose my browser