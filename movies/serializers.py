from django.db.models import Avg
from rest_framework import serializers
from actors.serializers import ActorSerializer
from movies.models import Movie
from genres.models import Genre
from genres.serializers import GenreSerializer

# class MovieSerializer(serializers.Serializer):
#     title = serializers.CharField()
#     genre = serializers.PrimaryKeyRelatedField(
#         queryset = Genre.objects.all(),
#     )
#     release_date = serializers.DateField()
#     actors = serializers.PrimaryKeyRelatedField(
#         queryset = Actor.objects.all(),
#         many=True
#     )


class MovieModelSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']

        if rate:
            return round(rate, 1)

        return None
        
        # reviews = obj.reviews.all()
        # if reviews:
        #     sum_reviews = 0
        #     for review in reviews:
        #         sum_reviews += review.stars
        #     reviews_count = reviews.count()
        #     return round(sum_reviews / reviews_count, 1)
        
        # return None

    def validate_release_date(self, value):
        if value.year < 1900:
            raise serializers.ValidationError('A data de lançamento não pode ser anterior a 1990.')
        return value
    
    def validate_resume(self, value):
        if len(value) > 500:
            raise serializers.ValidationError('Resumo não de ser maior que 200 caracteres.')
        
        
class MovieStatsSerializer(serializers.Serializer):
    total_movies = serializers.IntegerField(),
    movies_by_genre = serializers.ListField(),
    total_reviews = serializers.IntegerField(),
    average_stars = serializers.FloatField()


class MovieListDetailSerializer:
    actors = ActorSerializer(many=True)
    genre = GenreSerializer()
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'actors', 'release_date', 'rate', 'resume']
        
    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']

        if rate:
            return round(rate, 1)

        return None
    


