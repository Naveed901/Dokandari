
var app = angular.module('myApp');
app.factory('LoginService', function() {
    var admin = 'admin';
    var pass = 'admin';
    var isAuthenticated = false;
    return {
        login : function(username, password, email) {
            isAuthenticated = username === admin && password === pass && email === pass;
            return isAuthenticated;
        },
        isAuthenticated : function() {
            return isAuthenticated;
        }
    };
});