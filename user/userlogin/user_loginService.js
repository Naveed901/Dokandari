
var app = angular.module('myApp');
app.factory('UserloginService', function() {
    var admin = 'admin';
    var pass = 'admin';
    var isAuthenticated = false;
    return {
        login : function(username, password) {
            isAuthenticated = username === admin && password === pass ;
            console.log('user login service',isAuthenticated,username , admin , password , pass)
            return isAuthenticated;
        },
        isAuthenticated : function() {
            return isAuthenticated;
        }
    };
});