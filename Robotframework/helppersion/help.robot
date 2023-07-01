*** Settings ***
Library           SeleniumLibrary

*** Variables ***
${url}            http://localhost:3000/
${browser}        chrome

*** Test Cases ***
Home page
    inside helpersin

*** Keywords ***
inside helpersin
    Open browser    ${url}    ${browser}
    Maximize Browser Window
    Sleep    3
    Input Text    class:ant-input    Dwarkadham bhopal
    Sleep    3
    Input Text    xpath://input[@id='distance']    5
    Sleep    2
    # \ \ \ Input Text \ \ \ class:ant-select-selection-item
    # \ \ \ Sleep \ \ \ 2
    Click Button    class:css-dev-only-do-not-override-10ed4xt
    Sleep    2
