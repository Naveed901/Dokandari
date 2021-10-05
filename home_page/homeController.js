
var app = angular.module('myApp');
app.controller('HomeController', 
function($scope, $rootScope, $stateParams, $state, LoginService) {
	$rootScope.title = "Home Page";
	$scope.user = $rootScope.userName;
});