***Settings***
Library    SeleniumLibrary
Resource     Common.robot

**Test Cases***
LoginTest
    Open Browser               ${AdminLoginUrl}    ${Browser}
    Maximize Browser Window
    Login
    Sleep                2
    Close Browser

InputBoxTest
    ${"UserName"}                Set Variable         id:id_username
    ${"Password"}                Set Variable         id:id_password
    Open Browser                 ${AdminLoginUrl}    ${Browser}
    Maximize Browser Window
    Element Should Be Visible    ${"UserName"}
    Element Should Be Enabled    ${"UserName"}
    Element Should Be Visible    ${"Password"}
    Element Should Be Enabled    ${"Password"}

    Input Text            ${"UserName"}    testuser
    Sleep                 1
    Clear Element Text    ${"UserName"}
    Input Text            ${"Password"}    123456
    Sleep                 1
    Clear Element Text    ${"Password"}
    Close Browser         
