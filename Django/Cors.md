### Contents
- CORS

### CORS - No 'Access-Control-Allow-Origin' header
I've set up
* React - Request(React library)
* Django API Server(with JWT)

There was a little problem when I send request from chrome browser with React.
I got message from developer console ``No 'Access-Control-Allow-Origin' header``
This is not a problem of client-side but of server.

* Solution
I've installed [``django-cors-headers``](https://github.com/ottoyiu/django-cors-headers/) by __ottoyiu__
