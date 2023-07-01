
*** Settings ***
Library  Collections
Library  json
Library  OperatingSystem

Library           SeleniumLibrary

*** Variables ***
${url}            http://localhost/centaur/
${browser}        chrome
*** Test Cases ***
Centour
    insidecentour
Write data
   &{TESTS_DICT}=  Create Dictionary  FirstTestResults=PASS  SecondTestResult=FAIL
   ${JSON_CONTENT}=  json.dumps  ${TESTS_DICT}
   Create File  ${CURDIR}/data_file.json  content=${JSON_CONTENT}

*** Keywords ***
insidecentour
    Open Browser    ${url}    ${browser}
    Maximize Browser Window
    ##	login page
    # \ \ \ Input Text \ name:empid \ \ \ \ mis1011
    # \ \ \ Input Text \ name:password \ \ \ \ \ \ Q!W@e3r4t5
    # \ \ \ Sleep \ \ \ \ \ \ 1
    # \ \ \ Click Button \ \ \ class:btn-primary
    # \ \ \ Sleep \ \ \ \ \ \ 1
    ###	check in page
    # \ \ \ go to \ \ http://localhost/centaur/user/
    # \ \ \ Sleep \ \ \ \ \ \ 1
    # \ \ \ Input Text \ name:clientname \ \ \ \ Anuj choubey
    # \ \ \ Input Text \ name:discussion \ \ \ \ Samnapur seth deori
    # \ \ \ Input Text \ name:premise_image \ \ \ \ \ \ \ C://Users//Admin//Pictures//Screenshots//src.png.png
    # \ \ \ Click Button \ \ \ name:submit
    #
    # \ \ \ Sleep \ \ \ \ \ \ 2
    ###	checkout page
    # \ \ \ go to \ http://localhost/centaur/user/
    # \ \ \ Input Text \ name:expense_detail \ \ \ \ samnapur seth
    # \ \ \ Click Button \ \ \ class:btn-outline-primary
    # \ \ \ Input Text \ name:exp_image \ \ \ \ \ C://Users//Admin//Pictures//Screenshots//src.png.png
    # \ \ \ Click Button \ \ \ name:submit
    # \ \ \ Sleep \ \ \ \ \ \ 5
    # # \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \	logout
    # \ \ \ Click link \ \ \ xpath://body/div[2]/nav[1]/div[1]/ul[1]/li[4]/a[1]
    # \ \ \ sleep \ \ \ \ \ \ 3
    # \ \ \ #wrong password and id login
    go to    http://localhost/centaur/
    Input Text    name:empid    mis101
    Input Text    name:password    Q!W@e3r4t5
    Sleep    2
    Click Button    class:btn-primary
    Click Button    class:close
    Sleep    4
    ##	wrong password and id \	login
    go to    http://localhost/centaur/
    Input Text    name:empid    mis1011
    Input Text    name:password    Q!W@e3r4t
    Sleep    2
    Click Button    class:btn-primary
    Click Button    class:close
    Sleep    5
    ##	Right password and id login
    go to    http://localhost/centaur/
    Input Text    name:empid    mis1011
    Input Text    name:password    Q!W@e3r4t5
    Sleep    2
    Click Button    class:btn-primary
    # Click Button \ \ \ class:close
    Sleep    4
    # # \ \ \ Click Button \ \ \ class:close
    #Alert    class:alert-dismissible
    ##	logout
    #Click link    xpath://body/div[2]/nav[1]/div[1]/ul[1]/li[4]/a[1]
