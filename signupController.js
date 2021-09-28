
var app = angular.module('myApp');
app.controller('SignupController', function($scope, $rootScope, $stateParams, $state, SignupService) {
    $rootScope.title = "Signup Page";
    $scope.formSubmit = function() {
        if(SignupService.signup($scope.username, $scope.password)) {
            $rootScope.userName = $scope.username;
            $scope.error = '';
            $scope.username = '';
            $scope.password = '';
            $state.transitionTo('home');
        } else {

        }   
    };    
});