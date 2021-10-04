(function() {
var app = angular.module('myApp', ['ui.router']);
app.run(function($rootScope, $location, $state, LoginService) {
    console.clear();
    console.log('running');
    if(!LoginService.isAuthenticated()) {
        $state.transitionTo('login');
    }
});
app.config(['$stateProvider', '$urlRouterProvider', 
function($stateProvider, $urlRouterProvider) {
    $stateProvider
    .state('login', {
        url : '/login',
        templateUrl : '/login/login.html',
        controller : 'LoginController'
    })
    .state('signup', {
        url : '/signup',
        templateUrl : '/login/signup.html',
        controller : 'SignupController'
    })
    .state('profile', {
        url : '/profile',
        templateUrl : '/profilepage/profile.html',
        controller : 'ProfileController'
    })
    .state('home', {
        url : '/home',
        templateUrl : '/home_page/home.html',
        controller : 'HomeController'
    });
    $urlRouterProvider.otherwise('/login');
}]);
})();