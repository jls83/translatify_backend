from django.shortcuts import render
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from translatify_translate.models import TranslatedPhrase, PhraseRequest
from translatify_translate.serializers import TranslatedPhraseSerializer, PhraseRequestSerializer


class PhraseList(APIView):
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


class PhraseDetail(APIView):
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

