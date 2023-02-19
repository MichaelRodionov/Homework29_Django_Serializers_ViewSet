from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from Homework29_Django_Serializers_ViewSet import settings
from ads.views import *
from users.views import *

# ----------------------------------------------------------------
# create SimpleRouter instance
router = SimpleRouter()


# ----------------------------------------------------------------
# register routers
router.register('ad', AdvertisementViewSet)
router.register('cat', CategoryViewSet)
router.register('user', UserViewSet)
router.register('location', LocationViewSet)


# ----------------------------------------------------------------
# urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns += router.urls


# ----------------------------------------------------------------
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)