from django.shortcuts import render, redirect
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from translatify_translate.models import TranslatedPhrase, PhraseRequest
from translatify_translate.serializers import TranslatedPhraseSerializer, PhraseRequestSerializer
from translatify_translate.services import translate_phrase


class TranslatedPhraseList(APIView):
    """ View all translated phrases """
    def get(self, request, format=None):
        phrases = TranslatedPhrase.objects.all()
        serializer = TranslatedPhraseSerializer(phrases, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TranslatedPhraseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TranslatedPhraseDetail(APIView):
    """ Perform operations on a single TranslatedPhrase """
    def get_object(self, pk):
        try:
            return TranslatedPhrase.objects.get(pk=pk)
        except TranslatedPhrase.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        phrase = self.get_object(pk)
        serializer = TranslatedPhraseSerializer(phrase)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        phrase = self.get_object(pk)
        serializer = TranslatedPhraseSerializer(phrase, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        phrase = self.get_object(pk)
        phrase.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PhraseRequestList(APIView):
    """ View all requested translations

        TO DO:
            * Breakout language check after checking serializer.is_valid()

    """
    def get(self, request, format=None):
        phrases = PhraseRequest.objects.all()
        serializer = PhraseRequestSerializer(phrases, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PhraseRequestSerializer(data=request.data)
        if serializer.is_valid():
            try:
                translated_phrase = TranslatedPhrase.objects.get(input_phrase=serializer.validated_data['requested_phrase'])

                serializer.validated_data['cache_hit'] = True
            except TranslatedPhrase.DoesNotExist:
                translated_phrase = translate_phrase(serializer.validated_data['requested_phrase'])
                translated_phrase.save()
            tp_serialized = TranslatedPhraseSerializer(translated_phrase)
            serializer.save()
            return Response(tp_serialized.data, status=status.HTTP_302_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PhraseRequestDetail(APIView):
    """ Perform operations on a single PhraseRequest """
    def get_object(self, pk):
        try:
            return PhraseRequest.objects.get(pk=pk)
        except PhraseRequest.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        phrase = self.get_object(pk)
        serializer = PhraseRequestSerializer(phrase)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        phrase = self.get_object(pk)
        serializer = PhraseRequestSerializer(phrase, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        phrase = self.get_object(pk)
        phrase.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
