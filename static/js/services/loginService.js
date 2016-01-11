'use strict';

angular.module('app').factory('loginService', loginService);

function loginService($http, $location, localStorageService, toaster) {
  return {
    login : login,
    getUser : getUser,
    getUserId : getUserId,
    getUsername : getUsername,
    resetPassword : resetPassword,
    logout : logout
  };

  function login() {
    var data_login = localStorageService.get('data_login');

    $http.post('http://localhost:8000/auth/login/', data_login).then(function(result){
      localStorageService.remove('data_login');

      // obtengo token de auth
      $http.defaults.headers.common.Authorization = 'Token ' + result.data.auth_token;

      // obtengo datos del usuario y los guardo en un storage local
      $http.get('http://localhost:8000/auth/me/').then(function(user){
        localStorageService.set('user', user);
        // redirigo la ruta
        return $location.path( "/" );
      });
    }, function() {
    	// login erroneo , muestra error
      return toaster.pop({
        type: 'error',
        title: 'Error',
        body: 'Los datos ingresados son incorrectos.',
        showMethod: 'fadeIn',
        hideMethod: 'fadeOut',
        positionClass: 'toast-top-full-width'
      });
    });
  }

  function getUser(){
    var user = localStorageService.get('user');
    return user.data;
  }

  function getUserId() {
    var user = localStorageService.get('user');
    return user.data.id;
  }

  function getUsername() {
    var user = localStorageService.get('user');
    return user.data.username;
  }

  //TODO
  function resetPassword(){
     $http.post('http://localhost:8000/auth/logout/').then(function(){
      localStorageService.remove('user');
      return toaster.pop({
        type: 'info',
        title: 'Reset password',
        body: 'Se envio un mail con el reseteo del password.',
        showMethod: 'fadeIn',
        hideMethod: 'fadeOut',
        positionClass: 'toast-top-full-width'
      });
    })
  }

  function logout(){
    $http.post('http://localhost:8000/auth/logout/').then(function(){
      localStorageService.remove('user');
      return $location.path( "/login" );
    })
  }
}