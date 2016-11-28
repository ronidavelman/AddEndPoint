import os
import sys

module_name = sys.argv[1] #HomeMod
module_prefix =  module_name.replace("Mod", "") #Home
endpoint_name = sys.argv[2] #GetProducts
#File Paths
ctrl_path = "Modules/"+module_name+"/"+module_prefix+"Ctrl.js"
service_path = "Modules/"+module_name+"/"+module_prefix+"Service.js"

indent = "    " #spaces
api_path = "Backend/API.php"

def AddEndPoint(file, find_string, prepend_string):
    with open(file, "r") as in_file:
        buf = in_file.readlines()

    with open(file, "w") as out_file:
        for line in buf:
            if find_string in line :
                line = prepend_string + line
            out_file.write(line)

#Ctrl
AddEndPoint(ctrl_path, "}]);", indent+module_prefix+"Service."+endpoint_name+"($scope); \n")
#Service
service_string = """  this."""+endpoint_name+""" = function($scope,Store_ID){
    var params = {requestType:'"""+endpoint_name+"""'};
    $http({
    url: "/Backend/API.php",
      method: "POST",
      headers: {'Content-Type': 'application/x-www-form-urlencoded'},
      data: $httpParamSerializerJQLike(params)
    }).success(function(data, status, headers, config) {
      console.log(data);
      $timeout(function () {$scope.$apply($scope."""+endpoint_name+""" = data);}, 0);
    });
  }
"""
AddEndPoint(service_path, "}]);", service_string)
#API
api_string = """    case '"""+endpoint_name+"""':
        require('"""+module_prefix+"""/"""+endpoint_name+""".php');
        break;
"""
AddEndPoint(api_path, "default:", api_string)
