from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='ordenes:lista', permanent=False)),
    path('admin/', admin.site.urls),
    path('ordenes/', include('ordenes.urls')),
]
