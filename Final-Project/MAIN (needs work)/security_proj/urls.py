
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('customer/',include('customer.urls')),
    path("accounts/", include("django.contrib.auth.urls")),
    path('logout/', auth_views.LogoutView.as_view(next_page= '/accounts/login/'), name = 'logout'),
]
