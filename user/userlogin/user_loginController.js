
var app = angular.module('myApp');
app.controller('UserloginController', function($scope, $rootScope, $stateParams, $state, UserloginService) {
    $rootScope.title = "Login Page";
    console.log('here');
    $scope.formSubmit = function() {
        console.log('formSubmit');
        if(UserloginService.login($scope.username, $scope.password, $scope.email, $scope.phonenumber )) {
            $rootScope.userName = $scope.username;
            $scope.error = '';
            $scope.username = '';
            $scope.password = '';
            $scope.email = '';
            $scope.phonenumber = '';
            console.log('here 2')
            console.log($state)
            $state.transitionTo('userprofile');
        } else {
            $scope.error = "Incorrect username/password !";
            console.log($scope.error);
        }   
    };    
});