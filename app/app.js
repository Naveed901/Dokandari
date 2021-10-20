
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
        .state('userlogin', {
            url : '/userlogin',
            templateUrl : '/user/userlogin/user_login.html',
            controller : 'UserloginController'
        })
        .state('shoplogin', {
            url : '/shoplogin',
            templateUrl : '/shop/shoplogin/shop_login.html',
            controller : 'LoginController'
        })
        .state('signup', {
            url : '/signup',
            templateUrl : '/user/usersignup/user_signup.html',
            controller : 'SignupController'
        })
        .state('userprofile', {
            url : '/userprofile',
            templateUrl : '/user/userprofile/user_profile.html',
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
            templateUrl : '/shop/shopprofile/shop_profile.html',
            controller : 'ShopprofileController'
        })
        .state('forgotpassword', {
            url : '/forgotpassword',
            templateUrl : 'forgot_password/forgot_password.html',
            controller : 'ForgotpasswordController'
        })
        .state('getnewpassword', {
            url : '/getnewpassword',
            templateUrl : 'get_new_password/get_new_password.html',
            controller : 'GetnewpasswordController'
        })
         .state('post', {
            url : '/post',
            templateUrl : 'shop/shopprofile/post/create_post.html',
            controller : 'PostController'
        })
        .state('home', {
            url : '/home',
            templateUrl : '/home_page/home.html',
            controller : 'HomeController'
        });
        $urlRouterProvider.otherwise('/home');
}]);
})();