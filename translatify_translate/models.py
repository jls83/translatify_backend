from django.db import models
from django.contrib.auth.models import User


class TranslatedPhrase(models.Model):
    """
    TO DO:
        * UniqueKey input_phrase

    """
    input_phrase = models.CharField(max_length=500)
    input_language = models.CharField(max_length=25)
    output_phrase = models.CharField(max_length=500)


class PhraseRequest(models.Model):
    requested_phrase = models.CharField(max_length=500)
    requesting_user = models.ForeignKey(User, on_delete=models.CASCADE)
    cache_hit = models.BooleanField(default=False)
    time_requested = models.DateTimeField(auto_now_add=True)
    translated_phrase = models.ForeignKey(TranslatedPhrase, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ('-time_requested',)



