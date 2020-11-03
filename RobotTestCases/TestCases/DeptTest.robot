***Settings***
Library     SeleniumLibrary
Resource    ../Resources/CommonVariables.robot
Resource    ../Resources/CommonKeywords.robot
Resource    ../Resources/DeptKeywords.robot

**Test Cases***
DeptTest
    Open my browser                           ${DeptUrl}     ${Browser}
    Set Selenium Speed                        0.1 seconds
    Enter Login Credentials
    Click Add Department                      
    Select Organization                       
    Enter Department Name                     ${dept}
    Click Save
    Select unselect checkbox                  
    Select delete from dropdown and delete    
    CLose my browser