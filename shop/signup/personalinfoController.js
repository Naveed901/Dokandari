
var app = angular.module('myApp');
app.controller('PersonalinfoController', function($scope, $rootScope, $stateParams, $state, LoginService) {
    $rootScope.title = "Signup Page";
    $scope.formSubmit = function() {
        // if(LoginService.($scope.username, $scope.password)) {
        //     $rootScope.userName = $scope.username;
        //     $scope.error = '';
        //     $scope.username = '';
        //     $scope.password = '';
        //     $state.transitionTo('home');
        // } else {
        //     $scope.error = "Incorrect username/password !";
        // }   
    };    
});