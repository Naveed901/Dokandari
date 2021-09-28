
var app = angular.module('myApp');
app.factory('SignupService', function() {

    var isAuthenticated = false;
    return {
        signup : function(username, password) {
            // TODO call API of register
            // isAuthenticated = username === admin && password === pass;
            return true;
        },
        isAuthenticated : function() {
            return isAuthenticated;
        }
    };
});