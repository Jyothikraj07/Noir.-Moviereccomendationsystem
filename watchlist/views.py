from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from django.contrib.auth.decorators import login_required

from .models import Watchlist
from .serializers import WatchlistSerializer
from django.shortcuts import render


class WatchlistView(generics.ListCreateAPIView):
    serializer_class = WatchlistSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Watchlist.objects.filter(
            user=self.request.user
        )

    def perform_create(self, serializer):

        movie = serializer.validated_data["movie"]

        exists = Watchlist.objects.filter(
            user=self.request.user,
            movie=movie
        ).exists()

        if exists:
            raise ValidationError(
                {"error": "Movie already in watchlist"}
            )

        serializer.save(
            user=self.request.user
        )


class WatchlistDeleteView(generics.DestroyAPIView):
    queryset = Watchlist.objects.all()
    serializer_class = WatchlistSerializer
    permission_classes = [IsAuthenticated]


def watchlist_page(request):
    return render(request, "watchlist.html")