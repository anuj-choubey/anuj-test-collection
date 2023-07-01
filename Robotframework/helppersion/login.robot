*** Settings ***
Library           SeleniumLibrary

*** Variables ***
${url}            http://localhost:3000/
${browser}        chrome
${Sleep}        10
*** Test Cases ***
Login
    insidelogin

*** Keywords ***
insidelogin
    Open browser    ${url}    ${browser}
    Maximize Browser Window
    Set Selenium Implicit Wait    10seconds
    Click Button    xpath://header/div[1]/div[3]/div[1]/button[1]
    Set Selenium Implicit Wait    10seconds
    Clear Element Text    name:email
    Set Selenium Implicit Wait    10seconds
    Input Text    name:email    info@mistpl.com
    Set Selenium Implicit Wait    10seconds
    Clear Element Text    name:password
    Set Selenium Implicit Wait    10seconds
    Input Text    name:password    Q!W@e3r4t5
    Set Selenium Implicit Wait    10seconds
    Click Button    class:css-iegovm-MuiButtonBase-root-MuiButton-root
    Wait Until Element Is Visible    xpath://body/div[10]/div[3]/p[1]/button[1]
#    Click Button    Delete
#    Wait Until Element Is Enabled    xpath://body/div[10]/div[3]/p[1]/button[1]
    Set Selenium Implicit Wait    10seconds
# xpath://body/div[10]/div[3]/p[1]/button[1]

