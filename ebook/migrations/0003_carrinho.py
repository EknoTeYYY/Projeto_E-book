# Generated by Django 4.0.3 on 2022-05-01 20:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ebook', '0002_livros_nota_livros_porcentagem_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrinho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('total', models.IntegerField()),
                ('livros', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ebook.livros')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Carrinho',
            },
        ),
    ]