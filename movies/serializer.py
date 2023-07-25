from rest_framework import serializers
from .models import Movie_ratings, Movie, MovieOrder
from users.serializer import UserSerializer, User


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10, allow_null=True, default=None)
    rating = serializers.ChoiceField(choices=Movie_ratings, default=Movie_ratings.Rated_G, allow_null=True)
    synopsis = serializers.CharField(allow_null=True, default=None)

    added_by = serializers.SerializerMethodField(method_name='get_addeb_by')

    user = UserSerializer(allow_null=True, default=None, write_only=True)

    def create(self, validated_data: dict) -> Movie:
        return Movie.objects.create(**validated_data)
    
    def get_addeb_by(self, obj: User):
        added_by = obj.user.email
        return added_by
    

class MovieOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    buyed_at = serializers.DateTimeField(read_only=True)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)

    buyed_by = serializers.SerializerMethodField(method_name='get_email_user')
    title = serializers.SerializerMethodField(method_name='get_movies_name')

    movie = MovieSerializer(allow_null=True, default=None, write_only=True)
    user = UserSerializer(allow_null=True, default=None, write_only=True)

    def create(self, validated_data: dict) -> MovieOrder:
        return MovieOrder.objects.create(**validated_data)
    
    def get_email_user(self, obj: MovieOrder):
        buyed_by = obj.user.email
        return buyed_by

    
    def get_movies_name(self, obj: MovieOrder):
        movies_title = obj.movie.title
        return movies_title