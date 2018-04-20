from django.contrib.auth.models import User
from rest_framework import serializers
from translatify_translate.models import TranslatedPhrase, PhraseRequest


class TranslatedPhraseSerializer(serializers.ModelSerializer):

    class Meta:
        model = TranslatedPhrase
        fields = ('id', 'input_phrase', 'input_language', 'output_phrase')


class PhraseRequestSerializer(serializers.ModelSerializer):
    requesting_user = serializers.ReadOnlyField(source='requesting_user.username')

    class Meta:
        model = PhraseRequest
        fields = ('id', 'requested_phrase', 'requesting_user', 'cache_hit', 'time_requested')


class UserSerializer(serializers.ModelSerializer):
    phrase_requests = serializers.PrimaryKeyRelatedField(many=True, queryset=PhraseRequest.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'phrase_requests')
