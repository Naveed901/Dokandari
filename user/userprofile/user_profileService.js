
var app = angular.module('myApp');
app.factory('ProfileService', function() {

    var isAuthenticated = false;
    return {
        getUserData : function(username, password) {
            // TODO call API of register
            // isAuthenticated = username === admin && password === pass;
            return true;
        },
        isAuthenticated : function() {
            return isAuthenticated;
        }
    };
});