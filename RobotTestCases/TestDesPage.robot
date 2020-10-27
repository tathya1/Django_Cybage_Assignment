***Settings***
Library     SeleniumLibrary
Resource    Common.robot

**Test Cases***
DesignationTest
    Open Browser                 ${DesUrl}                                                                                                ${Browser}
    Maximize Browser Window
    Common.Login
    Sleep                        1
    Click Element                xpath://a[contains(text(),'Add designation')]
    Sleep                        1
    ${"DesName"}                 Set Variable                                                                                             id:id_designationName
    #Add Designation
    Element Should Be Visible    ${"DesName"}
    Element Should Be Enabled    ${"DesName"}
    Input Text                   ${"DesName"}                                                                                             testdes
    Sleep                        1
    #Save Designation
    Click Element                xpath://body/div[@id='container']/div[@id='main']/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/input[1]
    Common.Test checkbox
    Common.Delete Entry
    Close Browser
