*** Settings ***
Library           SeleniumLibrary

*** Variables ***
${url}            http://localhost/centaur/
${browser}        chrome







*** Test Cases ***
Order report
    order

*** Keywords ***
order
    Open Browser    ${url}    ${browser}
    Maximize Browser Window

For
    ##	login page
    Input Text    name:empid    mis1011
    Input Text    name:password    Q!W@e3r4t5
    Sleep    1
    Click Button    class:btn-primary
    Sleep    1
    go to    http://localhost/centaur/user/OrdersReport
    Sleep    3
    Select From List By Index class:fs-3    2

End
