from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import CustomUser, Produce, Note, Suggestion, SeasonLocation, Resource


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)
        token['location'] = user.location
        return token
    
class CustomUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    username = serializers.CharField()
    password = serializers.CharField(min_length=8, write_only=True)
    location = serializers.CharField()
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password', 'location')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)  # as long as the fields are the same, we can just use this
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class UserSerializer(serializers.HyperlinkedModelSerializer):
    notes = serializers.HyperlinkedRelatedField(
        view_name = 'note_detail',
        many=True,
        read_only=True
    )
    suggestions = serializers.HyperlinkedRelatedField(
        view_name = 'suggestion_detail',
        many=True,
        read_only=True
    )
    user_url = serializers.ModelSerializer.serializer_url_field(
        view_name = 'user_detail'
    )
    class Meta:
        model = CustomUser
        fields=('id','user_url','username', 'password', 'location', 'notes', 'suggestions' )


class ProduceSerializer(serializers.HyperlinkedModelSerializer):
    seasonlocations = serializers.HyperlinkedRelatedField(
        view_name = 'season_location_detail',
        many=True,
        read_only=True
    )
    produce_url = serializers.ModelSerializer.serializer_url_field(
        view_name = 'produce_detail'
    )

    class Meta:
        model = Produce
        fields=('id','produce_url','name', 'category', 'image_url', 'description', 'seasonlocations')

class NoteSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(
        view_name = 'user_detail',
        read_only=True
    )
    produce = serializers.HyperlinkedRelatedField(
        view_name = 'produce_detail',
        read_only=True
    )
    note_url = serializers.ModelSerializer.serializer_url_field(
        view_name = 'note_detail'
    )


    class Meta:
        model = Note
        fields=('id','note_url', 'content', 'produce', 'user')



class SuggestionSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(
        view_name = 'user_detail',
        read_only=True
    )

    suggestion_url = serializers.ModelSerializer.serializer_url_field(
        view_name = 'suggestion_detail'
    )


    class Meta:
        model = Suggestion
        fields=('id','suggestion_url', 'content', 'category', 'user')


class SeasonLocationSerializer (serializers.HyperlinkedModelSerializer):
    seasonlocation_url = serializers.ModelSerializer.serializer_url_field(
        view_name = 'seasonlocation_detail'
    )
    class Meta:
        model = SeasonLocation
        fields=('id','seasonlocation_url','season', 'location', 'combo')


class ResourceSerializer (serializers.HyperlinkedModelSerializer):
    resource_url = serializers.ModelSerializer.serializer_url_field(
        view_name = 'resource_detail'
    )
    class Meta:
        model = Resource
        fields=('id','resource_url','title','category', 'small_img', 'main_img', 'content', 'opt_link')
