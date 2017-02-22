***Settings***
Library    GoogleApi.py

***Keywords***
Search By Keyword
    [Arguments]   ${keyword}
    ${res} =    Search Api    ${keyword}
    [Return]    ${res}
