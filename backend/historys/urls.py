from django.urls import path
from historys.views import *

urlpatterns = [
    path("", set_history.as_view()),
    path("<int:history_id>/", update_history.as_view()),
]