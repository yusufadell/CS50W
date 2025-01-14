# Generated by Django 4.2.13 on 2024-09-06 15:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("encyclopedia", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="historicalarticle",
            options={
                "get_latest_by": ("history_date", "history_id"),
                "ordering": ("-history_date", "-history_id"),
                "verbose_name": "historical Article",
                "verbose_name_plural": "historical Articles",
            },
        ),
        migrations.AlterModelOptions(
            name="historicalmodification",
            options={
                "get_latest_by": ("history_date", "history_id"),
                "ordering": ("-history_date", "-history_id"),
                "verbose_name": "historical Modification",
                "verbose_name_plural": "historical Modifications",
            },
        ),
        migrations.RenameField(
            model_name="subcategory",
            old_name="subcategory_name",
            new_name="name",
        ),
        migrations.RemoveField(
            model_name="category",
            name="category_name",
        ),
        migrations.AddField(
            model_name="category",
            name="name",
            field=models.CharField(
                default="", max_length=128, verbose_name="Category name"
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="historicalarticle",
            name="history_date",
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name="historicalmodification",
            name="history_date",
            field=models.DateTimeField(db_index=True),
        ),
    ]
