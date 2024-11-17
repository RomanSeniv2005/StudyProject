from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('clients/', include('frontend.urls')),
    path('welcome/', include('frontend.urls')),
    path('', RedirectView.as_view(url='/welcome/', permanent=False)),  # Перенаправлення на клієнти
]
