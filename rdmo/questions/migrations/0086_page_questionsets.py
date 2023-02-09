# Generated by Django 3.2.14 on 2023-01-10 14:05

import django.db.models.deletion
from django.db import migrations, models


def run_data_migration(apps, schema_editor):
    QuestionSet = apps.get_model('questions', 'QuestionSet')
    PageQuestionSet = apps.get_model('questions', 'PageQuestionSet')

    for questionset in QuestionSet.objects.exclude(page=None):
        PageQuestionSet(
            page=questionset.page,
            questionset=questionset,
            order=questionset.order,
        ).save()


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0085_section_pages'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageQuestionSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=0)),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='page_questionsets', to='questions.page')),
                ('questionset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questionset_pages', to='questions.questionset')),
            ],
            options={
                'ordering': ('page', 'order'),
            },
        ),
        # remove the related_name='questionsets' from QuestionSet.page
        migrations.AlterField(
            model_name='questionset',
            name='page',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='questions.Page'),
        ),
        migrations.AddField(
            model_name='page',
            name='questionsets',
            field=models.ManyToManyField(blank=True, help_text='The question sets of this page.', related_name='pages', through='questions.PageQuestionSet', to='questions.QuestionSet', verbose_name='Question sets'),
        ),
        migrations.RunPython(run_data_migration),
        migrations.RemoveField(
            model_name='questionset',
            name='page',
        )
    ]
