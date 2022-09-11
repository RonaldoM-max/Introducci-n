from django.urls import path,include
from .views import BlogListView,BlogCreateView,BlogDetailView,BlogDeleteView
app_name="blog"

urlpatterns =[
    path('', BlogListView.as_view(), name="home"),
    path('create/',BlogCreateView.as_view(), name="create"),
    path('<int:pk>/',BlogDetailView.as_view(), name="detail"),
    path('<int:pk>/update/',BlogDetailView.as_view(), name="update"),
    path('<int:pk>delete/',BlogDeleteView.as_view(), name="delete")

]