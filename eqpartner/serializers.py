#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from task.models import *
from django.contrib.auth.models import User

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ('id', 'name', 'address')
        
class UrgencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Urgency
        fields = ('id', 'name')

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ('id', 'tag', 'name')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'username')
        write_only_fields = ('password',)
        read_only_fields = ('is_staff', 'is_superuser', 'is_active', 'date_joined',)

class NotificationSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Notification
        fields = ('id', 'user', 'userN', 'ntype', 'task', 'read')

class NotificationSerializerWriter(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ('id', 'user', 'userN', 'ntype', 'task', 'read')

class TaskSerializerWriter(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = (
            'id', 'identificator', 'title', 'description', 'done', 'start_date', 'finish_date', 'client', 'user',
            'priority', 'urgency', 'estimation_hours', 'module', 'status', 'implementation_id')

class TaskSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    module = ModuleSerializer()
    status = StatusSerializer()
    client = UserSerializer()
    urgency = UrgencySerializer()
    class Meta:
        model = Task
        fields = (
            'id', 'identificator', 'title', 'description', 'done', 'start_date', 'finish_date', 'client', 'user',
            'priority', 'urgency', 'estimation_hours', 'module', 'status', 'implementation_id')

class TaskCommentSerializerWriter(serializers.ModelSerializer):
    class Meta:
        model = TaskComment
        fields = ('id', 'task', 'user', 'comment', 'docfile')

class TaskCommentSerializer(serializers.ModelSerializer):
    user = UserSerializer();
    class Meta:
        model = TaskComment
        fields = ('id', 'task', 'user', 'comment', 'docfile')

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'done', 'user', 'description', 'task', 'created_at', 'updated_at')

class UserClientSerializerWriter(serializers.ModelSerializer):
    class Meta:
        model = UserClient
        fields = ('id', 'user', 'userR', 'relation')

class UserClientSerializer(serializers.ModelSerializer):
    user = UserSerializer();
    userR = UserSerializer();

    class Meta:
        model = UserClient
        fields = ('id', 'user', 'userR', 'relation')

class UserProfileSerializerWriter(serializers.ModelSerializer):
    class Meta:
        model = UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer();

    class Meta:
        model = UserProfile

class MessageSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    client = UserSerializer()

    class Meta:
        model = Message
        fields = ('id', 'owner', 'receptor', 'message')

class MessageSerializerWriter(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'owner', 'receptor', 'message')