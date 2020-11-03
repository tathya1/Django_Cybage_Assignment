***Settings***
Library     SeleniumLibrary
Resource    ../Resources/LoginKeywords.robot
Resource    CommonVariables.robot


***Keywords***
Open my browser
    [Arguments]                ${siteUrl}    ${browser}
    Open Browser               ${siteUrl}    ${browser}
    Maximize Browser Window

CLose my browser
    Close Browser

Enter Login Credentials
    Enter Username    ${user}
    Enter Password    ${pwd}
    Click login

Select unselect checkbox

    Select Checkbox      ${first_checkbox}
    Select Checkbox      ${second_checkbox}
    Unselect Checkbox    ${second_checkbox}

Select delete from dropdown and delete
    Select From List By Index    ${dropdown_name}   ${dropwon_index}    
    #Delete
    Click Element                ${delete_button}
    #Are you sure
    Click Element                ${are_you_sure_button}