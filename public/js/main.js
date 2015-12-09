var app=angular.module('app', [])

app.config(function($interpolateProvider) 
{
    $interpolateProvider.startSymbol('[[')
    $interpolateProvider.endSymbol(']]')
})

app.controller('ctrl', function($scope, $http)
{
	$scope.is_logged=false

	$scope.login=''
	$scope.password=''

	$scope.get_balance=function()
	{
		$http.get('get_balance?login='+$scope.login+'&password='+$scope.password).then(function(res)
		{
			if(res.data.status==="ok")
			{
				$scope.balance='Your balance is: '+res.data.balance+' BTC'
				$scope.is_logged=true
			}
			else
				$scope.balance=res.data.status
		})

		$scope.balance='loading...'
	}
})