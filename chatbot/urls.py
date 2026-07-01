from django.urls import path
from .views import ChatBotView, chat_page

urlpatterns = [
    path("ui/", chat_page, name="chat-ui"),
    path("", ChatBotView.as_view(), name="chat-api"),
]