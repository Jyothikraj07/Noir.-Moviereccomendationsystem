from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .services import ask_movie_bot


def chat_page(request):
    return render(request, "chat.html")


class ChatBotView(APIView):

    def post(self, request):

        message = request.data.get("message")

        result = ask_movie_bot(message)

        return Response({
            "response": result["text"],
            "movies": result["movies"]
        })