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
    Select From List By Index    ${emp_dept_list_name}    ${emp_dep_list_index_one} 
    Select From List By Index    ${emp_dept_list_name}    ${emp_dep_list_index_two}

Select Designation
    Select From List By Index    ${emp_des_drop_down_name}    ${emp_des_drop_down_index}

Enter Employee Bio
    [Arguments]    ${bio}
    Input Text     ${emp_bio}    ${bio}

Click Save
    Click Element    ${save_emp_button}