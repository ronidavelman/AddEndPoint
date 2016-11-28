# AddEndPoint
Easily add an endpoint for an Angular Rest application using Angular Init
https://github.com/ronidavelman/Angular-Init

### Creating an endpoint

python AddEndPoint.py <ModuleName> <Endpoint>
python AddEndPoint.py HomeMod GetProducts

This is based on Angular-Init, which uses the following anatomy: 

- Modules / <ModPrefix>Mod
  - <ModPrefix>Ctrl.js
  - <ModPrefix>Service.js
  
- Backend / API.php
  - case '<Endpoint>':
        require('<ModPrefix>/<Endpoint>.php');
        break;

An endpoint consists of a call to the service in the controller, an $http request in the service, and a php file in <ModPrefix>/<Endpoint>
