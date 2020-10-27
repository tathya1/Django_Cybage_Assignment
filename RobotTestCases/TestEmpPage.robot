***Settings***
Library     SeleniumLibrary
Resource    Common.robot

**Test Cases***
EmployeeTest
    Open Browser               ${EmpUrl}                                     ${Browser}
    Maximize Browser Window
    Common.Login
    Sleep                      1
    Click Element              xpath://a[contains(text(),'Add employee')]
    Sleep                      1
    ${"Name"}                  Set Variable                                  id:id_name
    ${"Email"}                 Set Variable                                  id:id_email
    ${"Department"}            Set Variable                                  id:id_department
    ${"Designation"}           Set Variable                                  id:id_department
    ${"Bio"}                   Set Variable                                  id:id_form-0-bio

    Element Should Be Visible    ${"Name"}
    Element Should Be Enabled    ${"Name"}
    Element Should Be Visible    ${"Email"}
    Element Should Be Enabled    ${"Email"}
    Element Should Be Visible    ${"Department"}
    Element Should Be Enabled    ${"Department"}
    Element Should Be Visible    ${"Designation"}
    Element Should Be Enabled    ${"Designation"}
    Element Should Be Visible    ${"Bio"}
    Element Should Be Enabled    ${"Bio"}
    #Add Employee
    Input Text                   ${"Name"}           testname
    Sleep                        1
    Input Text                   ${"Email"}          test@email.com
    Sleep                        1
    Select From List By Index      department                                                                                               0
    Select From List By Index      department                                                                                               1
    Select From List By Index      department                                                                                               2
    Sleep                          1
    Unselect From List By Index    department                                                                                               1
    Sleep                          1
    Select From List By Index      designation                                                                                              1
    Sleep                          1
    Input Text                     ${"Bio"}                                                                                                 testbio
    Sleep                          1
    #Save Employee
    Click Element                  xpath://body/div[@id='container']/div[@id='main']/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/input[1]
    Sleep                          1
    Common.Test checkbox
    Common.Delete Entry
    Close Browser

















