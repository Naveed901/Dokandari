
var app = angular.module('myApp');
app.controller('UserloginController', function($scope, $rootScope, $stateParams, $state, LoginService) {
    $rootScope.title = "Login Page";
    $scope.formSubmit = function() {
        if(LoginService.login($scope.username, $scope.password, $scope.email, $scope.phonenumber )) {
            $rootScope.userName = $scope.username;
            $scope.error = '';
            $scope.username = '';
            $scope.password = '';
            $scope.email = '';
            $scope.phonenumber = '';
            $state.transitionTo('userprofile');
        } else {
            $scope.error = "Incorrect username/password !";
        }   
    };    
});