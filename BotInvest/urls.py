from django.urls import path, include

from admin_panel.admin import bot_admin

urlpatterns = [
    path('admin_panel/', include('admin_panel.urls', namespace='admin_panel')),
    path('', bot_admin.urls),
]
