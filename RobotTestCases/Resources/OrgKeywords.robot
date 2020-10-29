***Settings***
Library      SeleniumLibrary
Variables    ../PageObjects/Locators.py

***Keywords***

Click Add Organization
    Click Element    ${add_org_button}

Enter Organization Name
    [Arguments]    ${organization}
    Input Text     ${org_name}    ${organization}

Click Save
    Click Element    ${save_org_button}

    