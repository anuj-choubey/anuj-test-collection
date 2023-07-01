*** Settings ***
Metadata          username    ${url}    # id
Metadata          password    ${p/w}    # passs
Library           SeleniumLibrary

*** Variables ***
${url}            http://localhost:4200/
${browser}        chrome
${email}          utkarsh@mistpl.com
${p/w}            Svast@1209













*** Test Cases ***
workbench
    insideworkbench

*** Keywords ***
insideworkbench
    Open Browser    ${url}    ${browser}
    Maximize browser window
    set selenium speed    1 seconds
    Click Button    class:other-login
    Input Text    xpath://body/app-root[1]/div[1]/app-login[1]/app-layout[1]/div[1]/div[1]/div[1]/form[1]/div[1]/input[1]    ${email}
    Input Text    xpath://body/app-root[1]/div[1]/app-login[1]/app-layout[1]/div[1]/div[1]/div[1]/form[1]/div[2]/input[1]    ${p/w}
    Click Button    class:btn-primary
    go to    http://localhost:4200/#/agent/workbench
    click Element    Xpath:/html/body/app-root/div/app-work-data/div/div[1]/p-table/div/div[1]/div/div/p-dropdown/div/div[2]/span
    click Element    Xpath://span[normalize-space()='By Service Date ASC']    # By Service Date ASC
    sleep    2 seconds
#    execute javascript    window.scrollTo(0,-document.body.scrollHeight)
#    execute javascript    window.scrollTo(0,document.body.scrollHeight)
#    Click Element    xpath:/html/body/app-root/div/app-clients/div/div[3]/p-paginator/div/p-dropdown/div/div[2]/span
#    Click Element    xpath://span[normalize-space()='20']
#    execute javascript    window.scrollTo(0,-document.body.scrollHeight
    Input Text    xpath://body/app-root[1]/div[1]/app-work-data[1]/div[1]/div[1]/p-table[1]/div[1]/div[1]/div[1]/form[1]/input[1]    anuj choubey
    Click Button    xpath://body/app-root[1]/div[1]/app-work-data[1]/div[1]/div[1]/p-table[1]/div[1]/div[1]/div[1]/form[1]/button[1]/span[1]
    Click Button    xpath://thead/tr[2]/th[4]/input[1]    anuj
    Click Button    xpath://thead/tr[2]/th[5]/input[1]    choubey
