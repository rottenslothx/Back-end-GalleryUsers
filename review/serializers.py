from django.db.models import Count, Q
from rest_framework import serializers
from rest_framework.fields import CharField, IntegerField

from account.serializers import AccountSerializer
from review.models import Gallery, Review


#for admin Upload and see all posts
class AdminPowerSerializers(serializers.ModelSerializer):
    user_uploaded = AccountSerializer

    class Meta:
        model = Gallery
        fields = ['id', 'title', 'image', 'avg_rating', 'user_uploaded']
        extra_kwargs = {'image': {'read_only': True},
                        'user_uploaded': {}
                        }


class AdminCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ['title', 'image']


class ShowUserSerializers(serializers.ModelSerializer):
    username = CharField(source='Users.username')

    class Meta:
        model = Gallery
        fields = ['Image', 'username', 'user_uploaded']


#for user give some rating
class ReviewSerializers(serializers.ModelSerializer):
    rating = IntegerField(max_value=5, min_value=1)

    class Meta:
        model = Review
        fields = ['review_text', 'rating']


