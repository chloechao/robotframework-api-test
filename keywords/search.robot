***Settings***
Resource    ../lib/search_api.robot

***Keywords***
User Sends A GET Request To Search ${keyword}
    ${res} =    Search By Keyword    ${keyword}
    Set Test Variable    ${RESPONSE}    ${res}

Response Contains Web Url ${web_url}
    Log    ${web_url}

Log The Url
    ${res} =    Get Url
    Log    ${res}
    Log Variables
