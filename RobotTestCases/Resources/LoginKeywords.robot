***Settings***
Library      SeleniumLibrary
Variables    ../PageObjects/Locators.py

***Keywords***

Enter Username
    [Arguments]    ${username}
    Input Text     ${login_username}    ${username}

Enter Password
    [Arguments]    ${password}
    Input Text     ${login_password}    ${password}

Click login
    Click Element    ${login_button}






