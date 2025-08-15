from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/',include('shop.urls')), # include forwards the urls to respective urls files
    path('blog/',include('blog.urls')),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
