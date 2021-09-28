
var app = angular.module('myApp');
app.controller('ProfileController', 
function($scope, $rootScope, $stateParams, $state, ProfileService) {
	$rootScope.title = "Profile Page";
	$scope.user = $rootScope.userName;
});