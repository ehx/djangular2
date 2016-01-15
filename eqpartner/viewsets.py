#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from task.models import *
from task.permissions import IsOwnerOrReadOnly
from django.db.models import Q
from .serializers import *

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100

class ModuleViewSet(viewsets.ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    filter_backends = (filters.DjangoFilterBackend,)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (filters.DjangoFilterBackend,)

    def get_queryset(self):
        queryset = super(UserViewSet, self).get_queryset() 
        user_query = self.request.query_params.get('ne', None)
        if user_query:
            return queryset.filter(~Q(id=user_query))
        return queryset

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('user', 'online')

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return UserProfileSerializer
        if self.action == 'list':
            return UserProfileSerializer
        return UserProfileSerializerWriter

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    pagination_class = StandardResultsSetPagination
    filter_fields = ('task', 'user', 'userN', 'read')

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return NotificationSerializer
        if self.action == 'list':
            return NotificationSerializer
        return NotificationSerializerWriter

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('priority')
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('id', 'title', 'done', 'user', 'client')
    permission_classes = (IsOwnerOrReadOnly, IsAuthenticated)

    def get_queryset(self):
        queryset = super(TaskViewSet, self).get_queryset()
        user_client = self.request.query_params.get('user_client', None)
        if user_client:
            return queryset.filter(Q(client=user_client) | Q(user=user_client))
        return queryset

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return TaskSerializer
        if self.action == 'list':
            return TaskSerializer
        return TaskSerializerWriter

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('id', 'name', 'lastname')

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ClientSerializer
        if self.action == 'list':
            return ClientSerializer
        return ClientSerializerWriter

class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('id', 'name', 'address')

class TaskCommentViewSet(viewsets.ModelViewSet):
    queryset = TaskComment.objects.all().order_by('-created_at')
    serializer_class = TaskCommentSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('id', 'task', 'user', 'docfile')
    pagination_class = StandardResultsSetPagination
    permission_classes = (IsOwnerOrReadOnly, IsAuthenticated)

    def get_queryset(self):
        queryset = super(TaskCommentViewSet, self).get_queryset() 
        if self.request.query_params.get('attachment', None):
            return queryset.filter(~Q(docfile=''))
        return queryset

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return TaskCommentSerializer
        if self.action == 'list':
            return TaskCommentSerializer
        return TaskCommentSerializerWriter

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('id', 'done', 'user', 'task')

    def get_queryset(self):
        queryset = super(TodoViewSet, self).get_queryset() 
        if self.request.query_params.get('task_is_null', None):
            return queryset.filter(task_id__isnull=True)
        return queryset        

class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('id', 'name')
    
class UrgencyViewSet(viewsets.ModelViewSet):
    queryset = Urgency.objects.all()
    serializer_class = UrgencySerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('id', 'name')

class UrgencyViewSet(viewsets.ModelViewSet):
    queryset = Urgency.objects.all()
    serializer_class = UrgencySerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('id', 'name')

class UserClientViewSet(viewsets.ModelViewSet):
    queryset = UserClient.objects.all()
    serializer_class = UserClientSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('id', 'user', 'userR', 'relation')

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return UserClientSerializer
        if self.action == 'list':
            return UserClientSerializer
        return UserClientSerializerWriter

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('id', 'owner', 'receptor')

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return MessageSerializer
        if self.action == 'list':
            return MessageSerializer
        return MessageSerializerWriter