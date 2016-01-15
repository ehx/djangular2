#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import filters, generics, routers
from django.conf.urls import include, url
from django.contrib import admin
from viewsets import *

router = routers.DefaultRouter()
router.register(r'task', TaskViewSet)
router.register(r'organization', OrganizationViewSet)
router.register(r'taskComment', TaskCommentViewSet)
router.register(r'users', UserViewSet)
router.register(r'notification', NotificationViewSet)
router.register(r'todo', TodoViewSet)
router.register(r'module', ModuleViewSet)
router.register(r'status', StatusViewSet)
router.register(r'urgency', UrgencyViewSet)
router.register(r'userClient', UserClientViewSet)
router.register(r'message', MessageViewSet)
router.register(r'userProfile', UserProfileViewSet)

urlpatterns = [
	url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^auth/', include('djoser.urls.authtoken'))
]