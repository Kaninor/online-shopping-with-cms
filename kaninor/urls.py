from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("main.urls")),
    path('cms/', include("cms.urls")),
    path('shop/', include("shop.urls")),
]
