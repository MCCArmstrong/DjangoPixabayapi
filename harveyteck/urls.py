
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import serve
from pixabay.views import searchImage, result, index



urlpatterns = [
    # path('admin/', admin.site.urls),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    path('', include('pixabay.urls')),
    path('make-search/', searchImage),
    path('upload-file/', include('pixabay.urls')),
    path('image-processing/', include('pixabay.urls')),
    path('result/', result, include('pixabay.urls')),
    path('get-pixabay-content/', include('pixabay.urls')),
    path('get-pixabay/', include('pixabay.urls')),
    path('<int:pk>file-edit/', include('pixabay.urls')),
    path('<int:pk>file-delete/', include('pixabay.urls')),
]
