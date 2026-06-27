from django.contrib import admin
from django.urls import path, include
from movies.frontend_views import home, login_page, register_page
from users.views import logout_view


urlpatterns = [
    path('', login_page, name='login'),
    path('register/', register_page, name='register'),
    path('admin/', admin.site.urls),
    path('logout/', logout_view), 
    path('users/', include('users.urls')),
    path('movies/', include('movies.urls')),
    path('ratings/', include('ratings.urls')),
    path('watchlist/', include('watchlist.urls')),
    path('recommendations/', include('recommendations.urls')),
]