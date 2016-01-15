'use strict';

// Factoriza los resource para obtener datos de la api de django
angular.module('app').factory('moduleResource', function($resource) {
  return $resource('/module/:id', {
    id: '@id'
  }, {
    'query': {
      method: 'GET',
      isArray: true
    },
  });
})

angular.module('app').factory('urgencyResource', function($resource) {
  return $resource('/urgency/:id', {
    id: '@id'
  }, {
    'query': {
      method: 'GET',
      isArray: true
    },
  });
})

angular.module('app').factory('statusResource', function($resource) {
  return $resource('/status/:id', {
    id: '@id'
  }, {
    'query': {
      method: 'GET',
      isArray: true
    },
  });
})

angular.module('app').factory('configurationResource', function($resource) {
  return $resource('/userProfile/:id', {
    id: '@id'
  }, {
    'get': {
      method: 'GET',
      isArray: false
    },
    'save': {
      method: 'POST'
    },
    'update': {
      method: 'PATCH'
    },
    'query': {
      method: 'GET',
      isArray: true
    },
    'remove': {
      method: 'DELETE'
    },
    'delete': {
      method: 'DELETE'
    }
  });
})

angular.module('app').factory('taskResource', function($resource) {
  return $resource('/task/:id', {
    id: '@id'
  }, {
    'get': {
      method: 'GET',
      isArray: false
    },
    'save': {
      method: 'POST'
    },
    'update': {
      method: 'PATCH'
    },
    'query': {
      method: 'GET',
      isArray: true
    },
    'remove': {
      method: 'DELETE'
    },
    'delete': {
      method: 'DELETE'
    }
  });
})

angular.module('app').factory('UserClientResource', function($resource) {
  return $resource('/userClient/:id', {
    id: '@id'
  }, {
    'get': {
      method: 'GET',
      isArray: false
    },
    'save': {
      method: 'POST'
    },
    'update': {
      method: 'PATCH'
    },
    'query': {
      method: 'GET',
      isArray: true
    },
    'remove': {
      method: 'DELETE'
    },
    'delete': {
      method: 'DELETE'
    }
  });
})

angular.module('app').factory('organizationResource', function($resource) {
  return $resource('/organization/:id', {
    id: '@id'
  }, {
    'get': {
      method: 'GET',
      isArray: false
    },
    'save': {
      method: 'POST'
    },
    'update': {
      method: 'PUT'
    },
    'query': {
      method: 'GET',
      isArray: true
    },
    'remove': {
      method: 'DELETE'
    },
    'delete': {
      method: 'DELETE'
    }
  });
})

angular.module('app').factory('usersResource', function($resource) {
  return $resource('/users/:id', {
    id: '@id'
  }, {
    'get': {
      method: 'GET',
      isArray: false
    },
    'query': {
      method: 'GET',
      isArray: true
    },
  });
})

angular.module('app').factory('notificationResource', function($resource) {
  return $resource('/notification/:id', {
    id: '@id'
  }, {
    'get': {
      method: 'GET'
    },
    'save': {
      method: 'POST'
    },
    'update': {
      method: 'PUT'
    },
    'query': {
      method: 'GET',
      isArray: true
    },
    'remove': {
      method: 'DELETE'
    },
    'delete': {
      method: 'DELETE'
    },
    'markAsRead': {
      method: 'POST',
      isArray: true
    }
  });
})

angular.module('app').factory('taskCommentsResource', function($resource) {
  return $resource('/taskComment/:id', {
    id: '@id'
  }, {
    'get': {
      method: 'GET'
    },
    'save': {
      method: 'POST'
    },
    'update': {
      method: 'PUT'
    },
    'query': {
      method: 'GET',
      isArray: true
    },
    'remove': {
      method: 'DELETE'
    },
    'delete': {
      method: 'DELETE'
    }
  });
})

angular.module('app').factory('clientResource', function($resource) {
  return $resource('/client/:id', {
    id: '@id'
  }, {
    'get': {
      method: 'GET'
    },
    'save': {
      method: 'POST'
    },
    'update': {
      method: 'PUT'
    },
    'query': {
      method: 'GET',
      isArray: true
    },
    'remove': {
      method: 'DELETE'
    },
    'delete': {
      method: 'DELETE'
    }
  });
})

angular.module('app').factory('todoResource', function($resource) {
  return $resource('/todo/:id', {
    id: '@id'
  }, {
    'get': {
      method: 'GET'
    },
    'save': {
      method: 'POST'
    },
    'update': {
      method: 'PUT'
    },
    'query': {
      method: 'GET',
      isArray: true
    },
    'remove': {
      method: 'DELETE'
    },
    'delete': {
      method: 'DELETE'
    }
  });
})

angular.module('app').factory('loginResource', function($resource) {
  return $resource('/auth/login/:id', {
    id: '@id'
  }, {
    'get': {
      method: 'GET',
      isArray: false
    },
    'save': {
      method: 'POST'
    },
    'update': {
      method: 'PUT'
    },
    'query': {
      method: 'GET',
      isArray: true
    },
    'remove': {
      method: 'DELETE'
    },
    'delete': {
      method: 'DELETE'
    }
  });
})