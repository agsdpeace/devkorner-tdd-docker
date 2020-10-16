from django.urls import path

from .views import TeamList, TeamDetail, MessageList, DevkornerInfosList

urlpatterns = [
    path('api/team/', TeamList.as_view()),
    path('api/team/<int:pk>/', TeamDetail.as_view()),
    path('api/message/', MessageList.as_view()),
    path('api/devkorner-infos/', DevkornerInfosList.as_view()),
]
