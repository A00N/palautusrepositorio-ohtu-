*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  testaajaeka
    Set Password  eioleolemassa1
    Set Confirm  eioleolemassa1
    Submit Credentials Register
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  te
    Set Password  eioleolemassa1
    Set Confirm  eioleolemassa1
    Submit Credentials Register
    Register Should Fail With Message  Invalid username

Register With Valid Username And Too Short Password
    Set Username  testaajatoka
    Set Password  1
    Set Confirm  1
    Submit Credentials Register
    Register Should Fail With Message  Invalid password

Register With Nonmatchin Password And Password Confirmation
    Set Username  testaajakolmas
    Set Password  eioleolemassa1
    Set Confirm  eioleol1
    Submit Credentials Register
    Register Should Fail With Message  Passwords not matching

Login After Succesful Registration
    Set Username  testaajaneljas
    Set Password  eioleolemassa1
    Set Confirm  eioleolemassa1
    Submit Credentials Register
    Register Should Succeed
    Go To Login Page
    Set Username  testaajaneljas
    Set Password  eioleolemassa1
    Submit Credentials
    Main Page Should Be Open

Login After Failed Registration
    Set Username  testaajaviides
    Set Password  1
    Set Confirm  1
    Submit Credentials Register
    Register Should Fail With Message  Invalid password
    Go To Login Page
    Set Username  testaajaviides
    Set Password  1
    Submit Credentials
    Login Should Fail With Message  Invalid username or password


*** Keywords ***
Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Create User And Go To Login Page
    Create User  kalle  kalle123
    Go To Login Page
    Login Page Should Be Open

Submit Credentials Register
    Click Button  Register

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Set Confirm
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}
