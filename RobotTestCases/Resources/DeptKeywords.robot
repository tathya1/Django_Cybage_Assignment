***Settings***
Library      SeleniumLibrary
Variables    ../PageObjects/Locators.py

***Keywords***

Click Add Department
    Click Element    ${add_dept_button}

Select Organization
    [Arguments]                  ${drop_down_name}    ${drop_down_index}
    Select From List By Index    ${drop_down_name}    ${drop_down_index}

Enter Department Name
    [Arguments]    ${department}
    Input Text     ${dept_name}        ${department}

Click Save
    Click Element    ${save_dept_button}