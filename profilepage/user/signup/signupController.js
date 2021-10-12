
var app = angular.module('myApp');
app.controller('SignupController', function($scope, $rootScope, $stateParams, $state, SignupService) {
    $rootScope.title = "Signup Page";
    $scope.formSubmit = function() {
        if(SignupService.signup($scope.username, $scope.password ,$scope.email, $scope.phonenumber)) {
            $rootScope.userName = $scope.username;
            $scope.error = '';
            $scope.username = '';
            $scope.password = '';
            $scope.password = '';
            $scope.email = '';
            $scope.phonenumber = '';
            $state.transitionTo('home');
        } else {

        }   
    };    
});