*** Settings ***
Metadata          username    ${url}    # id
Metadata          password    ${p/w}    # passs
Library           SeleniumLibrary

*** Variables ***
${url}            http://localhost:4200/
${browser}        chrome
${email}          utkarsh@mistpl.com
${p/w}            Svast@1209

${emai}           anujchoubey@918gmail.com    #Wrong email

${pa/w}           svast@1209    #Wrong password
*** Test Cases ***
AccountType
    InsideaccountType

*** Keywords ***
InsideaccountType
    Open Browser    ${url}    ${browser}
    Maximize browser window
    set selenium speed    1 seconds
    Click Button    class:other-login
    Input Text    xpath://body/app-root[1]/div[1]/app-login[1]/app-layout[1]/div[1]/div[1]/div[1]/form[1]/div[1]/input[1]    ${email}
    Input Text    xpath://body/app-root[1]/div[1]/app-login[1]/app-layout[1]/div[1]/div[1]/div[1]/form[1]/div[2]/input[1]    ${p/w}
    Click Button    class:btn-primary
    Click Button    xpath://button[contains(text(),'Logout')]
    # \ \ \ Wrong Email
    set selenium speed    1 seconds
    Click Button    class:other-login
    Input Text    xpath://body/app-root[1]/div[1]/app-login[1]/app-layout[1]/div[1]/div[1]/div[1]/form[1]/div[1]/input[1]    ${emai}
    Input Text    xpath://body/app-root[1]/div[1]/app-login[1]/app-layout[1]/div[1]/div[1]/div[1]/form[1]/div[2]/input[1]    ${p/w}
    Click Button    class:btn-primary
    Element Text Should Be    xpath://span[contains(text(),'Invalid Credential!')]    Invalid Credential!
    # \ \ \ Wrong password
    go to    http://localhost:4200/
    # \ \ \ set selenium speed \ \ \ 1 seconds
    Click Button    class:other-login
    Input Text    xpath://body/app-root[1]/div[1]/app-login[1]/app-layout[1]/div[1]/div[1]/div[1]/form[1]/div[1]/input[1]    ${email}
    Input Text    xpath://body/app-root[1]/div[1]/app-login[1]/app-layout[1]/div[1]/div[1]/div[1]/form[1]/div[2]/input[1]    ${pa/w}
    Click Button    class:btn-primary
    Element Text Should Be    xpath://span[contains(text(),'Invalid Credential!')]    Invalid Credential!
    # \ \ \ set selenium speed \ \ \ 1 seconds
    go to    http://localhost:4200/
    Click Button    class:other-login
    Click Button    class:btn-primary
    # Element Text Should Be \ \ \ xpath://span[contains(text(),'Invalid Credential!')] \ \ \ Invalid Credential!
    # \ \ \ set selenium speed \ \ \ 1 seconds
    Element Text Should Be    xpath://small[contains(text(),'Username is required')]    Username is required
    Element Text Should Be    xpath://small[contains(text(),'Password is required')]    Password is required
    # Click Button \ \ \ class:btn-primary
    go to    http://localhost:4200/
    Click Button    class:other-login
#     \ \ \ set selenium speed \ \ \ 1 seconds
    Click Button    class:btn-primary
#    Element Text Should Be     xpath://span[contains(text(),'Invalid Credential!')]     Invalid Credential!
    Element Text Should Be    xpath://h4[contains(text(),'Login')]    Login
    set selenium speed    1 seconds
