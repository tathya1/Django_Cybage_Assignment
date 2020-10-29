***Settings***
Library      SeleniumLibrary
Variables    ../PageObjects/Locators.py

***Keywords***

Click Add Designation
    Click Element    ${add_des_button}

Enter Designation Name
    [Arguments]    ${designation}
    Input Text     ${des_name}    ${designation}

Click Save
    Click Element    ${save_des_button}
