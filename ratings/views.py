from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Rating
from .serializers import RatingSerializer
from django.contrib.auth.decorators import login_required



class RatingView(generics.ListCreateAPIView):
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Rating.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class RatingDeleteView(generics.DestroyAPIView):
    queryset = Rating.objects.all()
    permission_classes = [IsAuthenticated]


def ratings_page(request):
    return render(request, "ratings.html")