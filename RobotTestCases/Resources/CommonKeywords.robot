***Settings***
Library     SeleniumLibrary
Resource    ../Resources/LoginKeywords.robot


***Keywords***
Open my browser
    [Arguments]                ${siteUrl}    ${browser}
    Open Browser               ${siteUrl}    ${browser}
    Maximize Browser Window

CLose my browser
    Close Browser

Enter Login Credentials
    LoginKeywords.Enter Username    ${user}
    LoginKeywords.Enter Password    ${pwd}
    LoginKeywords.Click login

Select unselect checkbox
    [Arguments]          ${checkbox1}    ${checkbox2}
    Select Checkbox      ${checkbox1}
    Select Checkbox      ${checkbox2}
    Unselect Checkbox    ${checkbox2}

Select delete from dropdown and delete
    [Arguments]          ${dropdown}    ${index}    ${delete}    ${confirm}
    Select From List By Index    ${dropdown}   ${index}    
    #Delete
    Click Element                ${delete}
    #Are you sure
    Click Element                ${confirm}