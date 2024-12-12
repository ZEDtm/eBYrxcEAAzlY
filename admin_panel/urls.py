from django.urls import path

from . import views

app_name = 'tg'

urlpatterns = [
    path('mailing', views.mailing, name='mailing'),
    path('hook/', views.check_pay_view, name='webhook_pay'),
]