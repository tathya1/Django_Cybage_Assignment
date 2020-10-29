***Settings***
Library     SeleniumLibrary
Resource    ../Resources/CommonVariables.robot
Resource    ../Resources/CommonKeywords.robot
Resource    ../Resources/DeptKeywords.robot

**Test Cases***
DeptTest
    Open my browser                           ${DeptUrl}               ${Browser}
    Set Selenium Speed                        0.1 seconds
    Enter Login Credentials
    Click Add Department                      
    Select Organization                       ${org_drop_down_name}    ${org_drop_down_index}
    Enter Department Name                     ${dept}
    Click Save
    Select unselect checkbox                  ${first_checkbox}        ${second_checkbox}        
    Select delete from dropdown and delete    ${dropdown_name}         ${dropwon_index}          ${delete_button}    ${are_you_sure_button}
    CLose my browser