from django.urls import path
from historys.views import *

urlpatterns = [
    path("", History.as_view()),
    path("<int:history_id>/", Update_history.as_view()),
]