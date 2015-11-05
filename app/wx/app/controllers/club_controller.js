var clubController = angular.module('clubController', []);

clubController.controller('clubIndexController',
	['$scope', '$rootScope', '$location', '$routeParams', function($scope, $rootScope, $location, $routeParams){
		$scope.id = 12;
		$scope.name = "天天";
		$scope.head_img_url = "http://7xkdgg.com2.z0.glb.qiniucdn.com/561c84c322dad82d571cd734-small01";
		$scope.toUserInfo = function(){
		    $location.url("users/"+$scope.id+"/info");
		}

 }]);