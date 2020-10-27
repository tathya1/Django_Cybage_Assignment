***Settings***
Library     SeleniumLibrary
Resource    Common.robot

**Test Cases***
DepartmentTest
    Open Browser                 ${DeptUrl}                                                                                               ${Browser}
    Maximize Browser Window
    Common.Login
    Sleep                        1
    Click Element                xpath://a[contains(text(),'Add department')]
    Sleep                        1
    #Add Department
    Select From List By Index    organization                                                                                             1
    Sleep                        1
    ${"DeptName"}                Set Variable                                                                                             id:id_departmentName
    Element Should Be Visible    ${"DeptName"}
    Element Should Be Enabled    ${"DeptName"}
    Input Text                   ${"DeptName"}                                                                                            testdept
    Sleep                        1
    #Save Department
    Click Element                xpath://body/div[@id='container']/div[@id='main']/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/input[1]
    Common.Test checkbox
    Common.Delete Entry
    Close Browser