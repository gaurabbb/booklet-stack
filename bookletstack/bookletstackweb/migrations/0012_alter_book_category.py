# Generated by Django 4.0.3 on 2023-06-06 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookletstackweb', '0011_alter_book_price_alter_comment_buyer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.CharField(choices=[('money', 'Money'), ('business', 'Business'), ('coding', 'Coding'), ('skills', 'Skills'), ('case_studies', 'Case Studies')], max_length=50),
        ),
    ]
