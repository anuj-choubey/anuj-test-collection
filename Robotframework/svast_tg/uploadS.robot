*** Settings ***
Library           SeleniumLibrary

*** Variables ***
${url}            http://localhost:4200/
${browser}        chrome
${email}          utkarsh@mistpl.com
${p/w}            Svast@1209
${file}           D://Users//Mohni Lakhera//All script 5600










*** Test Cases ***
Upload
    insideupload

*** Keywords ***
insideupload
    Open Browser    ${url}    ${browser}
    Maximize browser window
    set selenium speed    1 seconds
    Click Button    class:other-login
    Input Text    xpath://body/app-root[1]/div[1]/app-login[1]/app-layout[1]/div[1]/div[1]/div[1]/form[1]/div[1]/input[1]    ${email}
    Input Text    xpath://body/app-root[1]/div[1]/app-login[1]/app-layout[1]/div[1]/div[1]/div[1]/form[1]/div[2]/input[1]    ${p/w}
    Click Button    class:btn-primary
    go to    http://localhost:4200/#/admin/upload/file
    Choose File    xpath://body/app-root[1]/div[1]/app-upload-csv[1]/div[1]/div[2]/div[1]/input[1]    `${file}`
    Click Button    xpath://body/app-root[1]/div[1]/app-upload-csv[1]/div[1]/div[2]/div[1]/input[1]
    Sleep    3
