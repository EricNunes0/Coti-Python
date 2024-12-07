from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('estoque/', include('appestoque.urls', namespace='estoque'))
]