'use strict';
var app = angular.module('app')

// muestra cuanto tiempo paso desde una fecha
app.filter('moment', function() {
  return function(dateString, format) {
    return moment(dateString).format(format);
	};
});

// convierte en html seguro
app.filter('rawHtml', ['$sce', function($sce){
  return function(val) {
    return $sce.trustAsHtml(val);
  };
}]);

app.filter('lastWord', ['$sce', function($sce){
  return function(txt) {
  	if(txt){
  		var txtCut = txt.split("/"); 
	    return txtCut[txtCut.length-1];
  	}else{
  		return false;	
  	}
  };
}]);

app.filter('extension', ['$sce', function($sce){
  return function(txt) {
    if(txt){
      var txtCut = txt.split(".");
      switch(txtCut[txtCut.length-1]){
        case 'doc':
          return 'fa fa-file-word-o'
          break;
        case 'pdf':
          return 'fa fa-file-pdf-o'
          break;
        case 'mln': 
          return 'fa fa-mail-forward'
          break;
        case 'png':
          return 'fa fa-picture-o'
          break;
        default:
          return 'fa fa-file-o'
      }
  	};
	}}
]);