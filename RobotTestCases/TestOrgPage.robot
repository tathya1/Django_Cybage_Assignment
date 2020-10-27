***Settings***
Library     SeleniumLibrary
Resource    Common.robot

**Test Cases***
OrganizationTest
    Open Browser                 ${OrgUrl}                                                                                                ${Browser}
    Maximize Browser Window
    Common.Login
    Sleep                        1
    #Add Organization
    Click Element                xpath://a[contains(text(),'Add organization')]
    ${"OrgName"}                 Set Variable                                                                                             id:id_organizationName
    Element Should Be Visible    ${"OrgName"}
    Element Should Be Enabled    ${"OrgName"}
    Input Text                   ${"OrgName"}                                                                                             testorg
    Sleep                        1
    #Save Organization
    Click Element                xpath://body/div[@id='container']/div[@id='main']/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/input[1]
    Common.Test checkbox
    Common.Delete Entry
    Close Browser
