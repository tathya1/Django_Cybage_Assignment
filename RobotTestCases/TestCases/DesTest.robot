***Settings***
Library     SeleniumLibrary
Resource    ../Resources/CommonVariables.robot
Resource    ../Resources/CommonKeywords.robot
Resource    ../Resources/DesKeywords.robot

**Test Cases***
DesTest
    Open my browser                           ${DesUrl}            ${Browser}
    Set Selenium Speed                        0.1 seconds
    Enter Login Credentials
    Click Add Designation
    Enter Designation Name                    ${des}
    Click Save
    Select unselect checkbox                  ${first_checkbox}    ${second_checkbox}    
    Select delete from dropdown and delete    ${dropdown_name}     ${dropwon_index}      ${delete_button}    ${are_you_sure_button}
    CLose my browser