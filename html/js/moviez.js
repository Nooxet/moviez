angular.module('moviez', [])
.controller('getmovies', function($scope, $http) {
    $http.get('http://localhost:8080/movies').
        then(function(response) {
            $scope.movies = response.data;
        });
});
