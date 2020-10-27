**Variables***
${Browser}          chrome
${Host}             127.0.0.1:8000
${AdminLoginUrl}    http://${Host}/admin/login/?next=/admin/
${OrgUrl}           http://${Host}/admin/employee_app/organization/
${DeptUrl}          http://${Host}/admin/employee_app/department/
${DesUrl}           http://${Host}/admin/employee_app/designation/
${EmpUrl}           http://${Host}/admin/employee_app/employee/

***Keywords***
Login
    Input Text       id:id_username                                                                                    tathyak
    Input Text       id:id_password                                                                                    tathya123
    Click Element    xpath://body/div[@id='container']/div[@id='main']/div[1]/div[1]/div[1]/form[1]/div[3]/input[1]

Test checkbox
    #Checkboxes
    Select Checkbox      xpath://tbody/tr[1]/td[1]/input[1]
    Select Checkbox      xpath://tbody/tr[2]/td[1]/input[1]
    Sleep                1
    Unselect Checkbox    xpath://tbody/tr[2]/td[1]/input[1]
    Sleep                1

Delete Entry
    #From Drop Down
    Select From List By Index    action                                                                                     1 
    #Delete
    Click Element                xpath://button[contains(text(),'Go')]
    #Are you sure
    Click Element                xpath://body/div[@id='container']/div[@id='main']/div[1]/div[1]/form[1]/div[1]/input[4]
    Sleep                        1
