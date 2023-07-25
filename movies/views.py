from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Request, Response, status
from users.models import User
from .models import Movie
from .serializer import MovieSerializer, MovieOrderSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import isAdminOrReadOnly
from rest_framework.permissions import IsAuthenticated


class MovieView(APIView, PageNumberPagination ):
    authentication_classes = [JWTAuthentication]
    permission_classes = [isAdminOrReadOnly]


    def get(self, request: Request) -> Response:
        movies = Movie.objects.get_queryset().order_by('id')
        result_page = self.paginate_queryset(movies, request)

        serializer = MovieSerializer(result_page, many=True)

        return self.get_paginated_response(serializer.data)
    
    def post(self, request: Request) -> Response:
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save(user=request.user)

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class MovieDatailsView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [isAdminOrReadOnly]

    def get(self, resquest: Request, movie_id:int) -> Response:
        movie = get_object_or_404(Movie, id=movie_id)
        serializer = MovieSerializer(movie)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def delete(self, resquest: Request, movie_id:int) -> Response:   
        
        movie = get_object_or_404(Movie, id=movie_id)
        movie.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

class MovieOrdenView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


    def post(self, resquest: Request, movie_id:int) -> Response:
        movie = get_object_or_404(Movie, id=movie_id)

        serializer = MovieOrderSerializer(data=resquest.data)
        serializer.is_valid(raise_exception=True)

        print(movie, resquest.user)
        serializer.save(movie=movie, user=resquest.user)

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
