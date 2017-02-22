***Settings***
Resource    keywords/search.robot

***Test Cases***
Get Request - Search Keyword Through Google Search API
    [Tags]    RAT
    When User Sends A GET Request To Search "Robot"
    Then Response Contains Web Url "http://robotframework.org"
