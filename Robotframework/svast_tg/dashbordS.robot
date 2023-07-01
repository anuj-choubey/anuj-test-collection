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
DashBord
    insidedashboard

*** Keywords ***
insidedashboard
    Open Browser    ${url}    ${browser}
    Maximize browser window
    set selenium speed    1 seconds
    Click Button    class:other-login
    Input Text    xpath://body/app-root[1]/div[1]/app-login[1]/app-layout[1]/div[1]/div[1]/div[1]/form[1]/div[1]/input[1]    ${email}
    Input Text    xpath://body/app-root[1]/div[1]/app-login[1]/app-layout[1]/div[1]/div[1]/div[1]/form[1]/div[2]/input[1]    ${p/w}
    Click Button    class:btn-primary
    go to   http://localhost:4200//admin
    execute javascript   window.scrollTo(1,document.body.scrollHeight)
    # \ \ \ Element Text Should Be \ \ \ \ \ xpath://td[contains(text(),'Preethila Priyadharshini')] \ \ \ \ Preethila Priyadharshini
    Click Button         xpath://tbody/tr[10]/td[7]/button[1]
    Input Text        xpath://body/app-root[1]/div[1]/app-users[1]/div[1]/div[1]/div[1]/form[1]/div[1]/input[1] \ \ \ \ \ \ Anuj choubey
    Input Text        xpath://body/app-root[1]/div[1]/app-users[1]/div[1]/div[1]/div[1]/form[1]/div[2]/input[1] \ \ \ \ \ \ 0987654321
    Input Text        xpath://body/app-root[1]/div[1]/app-users[1]/div[1]/div[1]/div[1]/form[1]/div[3]/input[1] \ \ \ \ \ \ Assjs777@gmail.com
    select from list by index     xpath://body/app-root[1]/div[1]/app-users[1]/div[1]/div[1]/div[1]/form[1]/div[4]/select[1] \ \ \ \ \ 3
    Click Button      xpath://button[contains(text(),'Submit')]
    Sleep     2
    go to    http://localhost:4200/#/admin
    Run Keyword And Ignore Error    Scroll Element Into View    /html/body/section/div[3]/div
    execute javascript    window.scrollTo(8,document.body.scrollHeight)
