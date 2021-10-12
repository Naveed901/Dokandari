
(function() {
var app = angular.module('myApp', ['ui.router']);
app.run(function($rootScope, $location, $state, LoginService) {
    console.clear();
    console.log('running');
    if(!LoginService.isAuthenticated()) {
        $state.transitionTo('home');
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
            templateUrl : '/profilepage/user/signup/signup.html',
            controller : 'SignupController'
        })
        .state('profile', {
            url : '/profile',
            templateUrl : '/profilepage/profile.html',
            controller : 'ProfileController'
        })   
        .state('market', {
            url : '/market',
            templateUrl : '/shop/signup/market.html',
            controller : 'MarketController'
        })
         .state('shopdetail', {
            url : '/shopdetail',
            templateUrl : '/shop/signup/shop detail.html',
            controller : 'ShopdetailController'
        })
        .state('personalinfo', {
            url : '/personalinfo',
            templateUrl : '/shop/signup/personal info.html',
            controller : 'personalinfoController'
        }) 
        .state('shopprofile', {
            url : '/shopprofile',
            templateUrl : '/shop/shopprofile.html',
            controller : 'ShopprofileController'
        }) 
        .state('home', {
            url : '/home',
            templateUrl : '/home_page/home.html',
            controller : 'HomeController'
        });
        $urlRouterProvider.otherwise('/home');
}]);
})();