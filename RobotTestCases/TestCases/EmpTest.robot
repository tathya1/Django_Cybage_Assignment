***Settings***
Library     SeleniumLibrary
Resource    ../Resources/CommonVariables.robot
Resource    ../Resources/CommonKeywords.robot
Resource    ../Resources/EmpKeywords.robot

**Test Cases***
EmpTest
    Open my browser                           ${EmpUrl}                    ${Browser}
    Set Selenium Speed                        0.1 seconds
    Enter Login Credentials
    Click Add Employee
    Enter Employee Name                       ${name}                  
    Enter Employee Email                      ${email}                 
    Select Department                         ${emp_dept_list_name}        ${emp_dep_list_index_one}     ${emp_dep_list_index_two}
    Select Designation                        ${emp_des_drop_down_name}    ${emp_des_drop_down_index}
    Enter Employee Bio                        ${bio}
    Click Save
    Select unselect checkbox                  ${first_checkbox}            ${second_checkbox}            
    Select delete from dropdown and delete    ${dropdown_name}             ${dropwon_index}              ${delete_button}             ${are_you_sure_button}
    CLose my browser