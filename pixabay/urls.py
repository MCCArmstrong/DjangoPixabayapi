
from django.urls import path, include
from . import views
app_name = 'pixabay'

urlpatterns = [
    path('', views.BaseHome.as_view(), name='basehome'),
    path('upload-file/', views.FileUpload.as_view(), name='upload'),
    path('image-processing/', views.ImageList.as_view(), name='image-panel'),
    # path('get-pixabay-content/', views.PixabaySearch.as_view(), name='bay-search'),
    path('<int:pk>file-edit/', views.UpdateFile.as_view(), name='edit'),
    path('get-pixabay-content/', views.index, name='index'),
    path('result/', views.result, name='result'),
    path('<int:pk>file-delete/', views.FileDelete.as_view(), name='delete'),
]