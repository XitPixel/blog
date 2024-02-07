from django.urls import path


from . import views


urlpatterns = [
    path('', views.home_view, name='home'),
    path('categories/<int:category_id>/', views.get_category_articles_views, name='category_articles'),
    path('login/', views.login_view, name='login'),
    path('registration/', views.registration_view, name='registration'),
    path('test_detail/', views.test_detail, name='test_detail')
]