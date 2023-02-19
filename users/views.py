from django.db.models import Count, Q, QuerySet
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from users.serializers import *


# ----------------------------------------------------------------
# Paginator
class Paginator(PageNumberPagination):
    """
    Custom pagination class
    """
    page_size: int = 4


# ----------------------------------------------------------------
# UserViewSet
class UserViewSet(ModelViewSet):
    queryset: QuerySet = User.objects.annotate(total_ads=Count(
        'advertisement',
        filter=Q(advertisement__is_published=True))).\
        order_by('username')
    default_serializer: UserDefaultSerializer = UserDefaultSerializer
    serializers: dict = {
        'list': UserListDetailSerializer,
        'retrieve': UserListDetailSerializer,
        'create': UserCreateSerializer,
        'update': UserChangeSerializer,
        'partial_update': UserChangeSerializer,
        'destroy': UserDeleteSerializer
    }
    pagination_class: Paginator = Paginator

    def get_serializer_class(self) -> UserDefaultSerializer:
        """
        Method to define serializer class
        :return: UserDefaultSerializer
        """
        return self.serializers.get(self.action, self.default_serializer)


# ----------------------------------------------------------------
# Location ViewSet
class LocationViewSet(ModelViewSet):
    queryset: QuerySet = Location.objects.all()
    serializer_class: LocationSerializer = LocationSerializer
    pagination_class: Paginator = Paginator
