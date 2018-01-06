# pasteRestApiServer
Python paste server servicing PUT/GET request with JSON response

/** Assume you have installed python3 python3-dev **/

#1. clone this repository:
git clone
git status
pip install bottle paste

#2. edit conf.xml and change ip, port params to your environment params

#3. run it:
python3 pasteRestApiServer

#4. If you use Chrome, chances are you have RESTclient add-on, 
    point browser to http://127.0.0.1:7777/restapionmark

    Else if yours is Firefox, search and allow add-on for RESTclient.  
    Then point the browser to http://[ip:port]/restapionmark or http://[ip:port]/action

et, voila!
