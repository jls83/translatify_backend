# Generated by Django 2.0.4 on 2018-04-19 00:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PhraseRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cache_hit', models.BooleanField(default=False)),
                ('time_requested', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-time_requested',),
            },
        ),
        migrations.CreateModel(
            name='TranslatedPhrase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input_phrase', models.CharField(max_length=500)),
                ('input_language', models.CharField(max_length=25)),
                ('output_phrase', models.CharField(max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='phraserequest',
            name='requested_phrase',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='translatify_translate.TranslatedPhrase'),
        ),
        migrations.AddField(
            model_name='phraserequest',
            name='requesting_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]