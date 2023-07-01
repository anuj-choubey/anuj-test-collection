*** Settings ***
Metadata          username    ${url}    # id
Metadata          password    ${p/w}    # passs
Library           SeleniumLibrary

*** Variables ***
${url}            https://instaapoll.com/
${browser}        chrome
${email}          anujchoubey918@gmail.com
${p/w}            123456

*** Test Cases ***
Login with correct Username and Password
    InsideLOType

*** Keywords ***
InsideLOType
    Open Browser    ${url}    ${browser}
    Maximize browser window
    set selenium speed    1 seconds
    Input Text          xpath:/html[1]/body[1]/app-root[1]/app-home[1]/div[1]/div[1]/div[1]/form[1]/div[1]/input[1]     ${email}
    Input Text          xpath://input[@id='exampleInputPassword1']      ${p/w}
    Click Buttton       xpath://button[@id='button']