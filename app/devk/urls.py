from django.urls import path

from .views import TeamList, TeamDetail

urlpatterns = [
    path('api/team/', TeamList.as_view()),
    path('api/team/<int:pk>/', TeamDetail.as_view()),
]
