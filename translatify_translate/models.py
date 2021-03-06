from django.db import models
from django.contrib.auth.models import User


class TranslatedPhrase(models.Model):
    input_phrase = models.CharField(max_length=500)
    input_language = models.CharField(max_length=25)
    output_phrase = models.CharField(max_length=500)

    class Meta:
        unique_together = (('input_phrase', 'input_language'),)


class PhraseRequest(models.Model):
    requested_phrase = models.CharField(max_length=500)
    requesting_user = models.ForeignKey('auth.User', related_name='phrase_requests', on_delete=models.CASCADE)
    cache_hit = models.BooleanField(default=False)
    time_requested = models.DateTimeField(auto_now_add=True)
    translated_phrase = models.ForeignKey(TranslatedPhrase, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ('-time_requested',)



