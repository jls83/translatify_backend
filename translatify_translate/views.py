from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from translatify_translate.models import TranslatedPhrase, PhraseRequest
from translatify_translate.serializers import TranslatedPhraseSerializer, PhraseRequestSerializer



@csrf_exempt
def phrase_list(request):
    """ View all translated phrases """
    if request.method == 'GET':
        phrases = TranslatedPhrase.objects.all()
        serializer = TranslatedPhraseSerializer(phrases, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TranslatedPhraseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

def phrase_detail(request, pk):
    """ Perform operations on a single TranslatedPhrase """
    try:
        phrase = TranslatedPhrase.objects.get(pk=pk)
    except TranslatedPhrase.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TranslatedPhraseSerializer(phrase)
        return JsonResponse(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TranslatedPhraseSerializer(phrase, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        phrase.delete()
        return HttpResponse(status=204)



