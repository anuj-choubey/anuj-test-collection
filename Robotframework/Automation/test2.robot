*** Settings ***
Library           SeleniumLibrary

*** Variables ***
${url}            http://localhost/centaur/user/placedorders
${browser}        chrome




*** Test Cases ***
order


*** Keywords ***
insideorder
    Open Browser    ${url}    ${browser}
    Maximize Browser Window
    ##	login page
    Input Text    name:empid    mis1011
    Input Text    name:password    Q!W@e3r4t5
    Sleep    1
    Click Button    class:btn-primary
    Sleep    1
    go to    http://localhost/centaur/user/placedorders
    Sleep    3
    # \ \ \ Sleep \ \ \ \ \ \ 4
    Select From List By Index    Xpath://body/div[2]/div[1]/section[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/select[1]    2
    Sleep    2
    Select From List By Index    class:prd_name    1
    Sleep    2
    Select From List By Index    class:model    0
    Sleep    2
    Select From List By Index    class:wattage    1
    Sleep    1

    Select From List By Index    class:color    1
    Sleep    3
    Input Text    class:discount    40
    Input Text    class:quantity    30
    # \ \ \ Element should contain \ xpath://button[@id='order']
    Click Button    class:mb-3
    Sleep    8
    # \ \ \ Add client
    # \ \ \ Click Button \ \ \ class: mb-3
    # \ \ \ Sleep \ \ \ \ \ \ 2
