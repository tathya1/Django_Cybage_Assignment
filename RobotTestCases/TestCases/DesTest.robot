***Settings***
Library     SeleniumLibrary
Resource    ../Resources/CommonVariables.robot
Resource    ../Resources/CommonKeywords.robot
Resource    ../Resources/DesKeywords.robot

**Test Cases***
DesTest
    Open my browser                           ${DesUrl}      ${Browser}
    Set Selenium Speed                        0.1 seconds
    Enter Login Credentials
    Click Add Designation
    Enter Designation Name                    ${des}
    Click Save
    Select unselect checkbox                  
    Select delete from dropdown and delete    
    CLose my browser