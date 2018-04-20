from rest_framework import serializers
from translatify_translate.models import TranslatedPhrase, PhraseRequest


class TranslatedPhraseSerializer(serializers.ModelSerializer):

    class Meta:
        model = TranslatedPhrase
        fields = ('id', 'input_phrase', 'input_language', 'output_phrase')


class PhraseRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = PhraseRequest
        fields = ('id', 'requested_phrase', 'requesting_user', 'cache_hit', 'time_requested')
