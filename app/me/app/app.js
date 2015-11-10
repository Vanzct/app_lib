/* App Module */
templates_root = '/wx/wx/app/templates/';

var clubApp = angular.module('clubApp', [
  'ngRoute',
  'baseController',
  'clubController'
]);

clubApp.config(['$routeProvider',
  function($routeProvider) {
    $routeProvider.
      when('/club/:id', {
        templateUrl: templates_root+'club_show.html',
        controller: 'clubIndexController'
      }).
      otherwise({
        //redirectTo: '404.html'
        templateUrl: templates_root+'404.html',
        controller: 'error404Controller'
      });
  }]);