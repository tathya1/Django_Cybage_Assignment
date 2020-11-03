***Settings***
Library     SeleniumLibrary
Resource    ../Resources/CommonVariables.robot
Resource    ../Resources/CommonKeywords.robot
Resource    ../Resources/EmpKeywords.robot

**Test Cases***
EmpTest
    Open my browser                           ${EmpUrl}      ${Browser}
    Set Selenium Speed                        0.1 seconds
    Enter Login Credentials
    Click Add Employee
    Enter Employee Name                       ${name}        
    Enter Employee Email                      ${email}       
    Select Department                         
    Select Designation                        
    Enter Employee Bio                        ${bio}
    Click Save
    Select unselect checkbox                  
    Select delete from dropdown and delete    
    CLose my browser