
var app = angular.module('myApp');
app.factory('SignupService', function() {

    var isAuthenticated = false;
    return {
        signup : function(username, password, email, phonenumber) {
            // TODO call API of register
            // isAuthenticated = username === admin && password === pass && email === pass;
            return true;
        },
        isAuthenticated : function() {
            return isAuthenticated;
        }
    };
});
                                                                                                                                                                                                       
var app = angular.module('myApp');
app.factory('SignupService', function() {

    var isAuthenticated = false;
    return {
        signup : function(username, password, email, phonenumber) {
            // TODO call API of register
            // isAuthenticated = username === admin && password === pass && email === pass;
            return true;
        },
        isAuthenticated : function() {
            return isAuthenticated;
        }
    };
});
