***Settings***
Library      SeleniumLibrary
Variables    ../PageObjects/Locators.py

***Keywords***

Click Add Employee
    Click Element    ${add_emp_button}

Enter Employee Name
    [Arguments]    ${name}
    Input Text     ${emp_name}    ${name}

Enter Employee Email
    [Arguments]    ${email}
    Input Text     ${emp_email}    ${email}

Select Department
    [Arguments]                  ${drop_down_name}    ${drop_down_index_1}     ${drop_down_index_2}
    Select From List By Index    ${drop_down_name}    ${drop_down_index_1} 
    Select From List By Index    ${drop_down_name}    ${drop_down_index_2}

Select Designation
    [Arguments]                  ${drop_down_name}    ${drop_down_index}
    Select From List By Index    ${drop_down_name}    ${drop_down_index}

Enter Employee Bio
    [Arguments]    ${bio}
    Input Text     ${emp_bio}    ${bio}

Click Save
    Click Element    ${save_emp_button}