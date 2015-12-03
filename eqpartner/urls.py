import django_filters
from rest_framework import filters
from rest_framework import generics

from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from task.models import *
from rest_framework.pagination import PageNumberPagination
from django.conf.urls import *
from django.db.models import Q

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100


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
        fields = ('first_name', 'last_name', 'email', 'username')
        write_only_fields = ('password',)
        read_only_fields = ('is_staff', 'is_superuser', 'is_active', 'date_joined',)


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ('id', 'user', 'ntype', 'notification', 'read')

'''
class ClientSerializerWriter(serializers.ModelSerializer):
    class Meta:
        model = Client
'''
'''
class ClientSerializer(serializers.ModelSerializer):
    organization = OrganizationSerializer()
    class Meta:
        model = Client
        fields = ('id', 'name', 'lastname', 'address', 'telephone', 'mail')
'''

class TaskSerializerWriter(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = (
            'id', 'sar', 'title', 'description', 'creation_date', 'done', 'start_date', 'finish_date', 'client', 'user',
            'priority', 'urgency', 'estimation_hours', 'module', 'status')


class TaskSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    module = ModuleSerializer()
    status = StatusSerializer()
    #client = ClientSerializer()
    client = UserSerializer() #nuevo
    urgency = UrgencySerializer()
    class Meta:
        model = Task
        fields = (
            'id', 'sar', 'title', 'description', 'creation_date', 'done', 'start_date', 'finish_date', 'client', 'user',
            'priority', 'urgency', 'estimation_hours', 'module', 'status')


class TaskCommentSerializerWriter(serializers.ModelSerializer):
    class Meta:
        model = TaskComment
        fields = ('id', 'task', 'user', 'comment', 'creation_date', 'docfile')


class TaskCommentSerializer(serializers.ModelSerializer):
    user = UserSerializer();
    class Meta:
        model = TaskComment
        fields = ('id', 'task', 'user', 'comment', 'creation_date', 'docfile')


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'done', 'user', 'description', 'task')


class UserClientSerializerWriter(serializers.ModelSerializer):
    class Meta:
        model = UserClient
        fields = ('id', 'user', 'userR')

class UserClientSerializer(serializers.ModelSerializer):
    task = TaskSerializer();
    user = UserSerializer();
    client = UserSerializer();

    class Meta:
        model = UserClient
        fields = ('id', 'user', 'userR')

class UserProfileSerializerWriter(serializers.ModelSerializer):
    class Meta:
        model = UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer();

    class Meta:
        model = UserProfile

class ModuleViewSet(viewsets.ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    filter_backends = (filters.DjangoFilterBackend,)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (filters.DjangoFilterBackend,)


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('user', 'online')

    def get_serializer_class(self):
        # get one task
        if self.action == 'retrieve':
            return UserProfileSerializer
        if self.action == 'list':
            return UserProfileSerializer
        return UserProfileSerializerWriter

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    pagination_class = StandardResultsSetPagination
    filter_fields = ('notification', 'user', 'read')

    def get_queryset(self):
        user = self.request.user
        return Notification.objects.filter(user=user)


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('priority')
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('id', 'title', 'done', 'user', 'client')

    def get_serializer_class(self):
        # get one task
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
        # get one task
        if self.action == 'retrieve':
            return ClientSerializer
        if self.action == 'list':
            return ClientSerializer
        return ClientSerializerWriter


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    filter_backends = (filters.DjangoFilterBackend,)


class TaskCommentViewSet(viewsets.ModelViewSet):
    queryset = TaskComment.objects.all().order_by('-creation_date')
    serializer_class = TaskCommentSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('id', 'task', 'user', 'docfile')
    pagination_class = StandardResultsSetPagination

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
    filter_fields = ('id', 'user', 'userR')

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return UserClientSerializer
        if self.action == 'list':
            return UserClientSerializer
        return UserClientSerializerWriter


class MessageSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    #client = ClientSerializer()
    client = UserSerializer() # nuevo

    class Meta:
        model = Message
        fields = ('id', 'owner', 'receptor', 'message')

class MessageSerializerWriter(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'owner', 'receptor', 'message')


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


router = routers.DefaultRouter()
router.register(r'task', TaskViewSet)
#router.register(r'client', ClientViewSet)
router.register(r'organization', OrganizationViewSet)
router.register(r'taskComment', TaskCommentViewSet)
router.register(r'user', UserViewSet)
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