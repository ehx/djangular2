'use strict';

angular.module('app').run(runFunction);

function runFunction($http, $cookies, $rootScope, $location, $cookieStore, editableOptions) {
  editableOptions.theme = 'bs3';

  $http.defaults.headers.common['X-CSRFToken'] = $cookies['csrftoken'];

  $rootScope.$on( "$routeChangeStart", function(event, next, current) {
    if ( $cookieStore.get('loggedIn') === '' ) {
      $location.path( "/login/" );
    }
  });
};