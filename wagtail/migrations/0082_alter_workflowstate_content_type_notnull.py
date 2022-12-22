# Generated by Django 4.2.dev20221212151407 on 2022-12-12 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("wagtailcore", "0081_populate_workflowstate_content_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="workflowstate",
            name="base_content_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="contenttypes.contenttype",
            ),
        ),
        migrations.AlterField(
            model_name="workflowstate",
            name="content_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="contenttypes.contenttype",
            ),
        ),
    ]