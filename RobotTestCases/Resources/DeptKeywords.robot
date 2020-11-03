***Settings***
Library      SeleniumLibrary
Variables    ../PageObjects/Locators.py

***Keywords***

Click Add Department
    Click Element    ${add_dept_button}

Select Organization
    Select From List By Index    ${org_drop_down_name}    ${org_drop_down_index}

Enter Department Name
    [Arguments]    ${department}
    Input Text     ${dept_name}        ${department}

Click Save
    Click Element    ${save_dept_button}