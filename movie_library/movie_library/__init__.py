from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Peliculas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('género', models.CharField(max_length=30)),
                ('director', models.CharField(max_length=30)),
                ('Año', models.DecimalField(decimal_places=4, max_digits=6)),
                ('Sinopsis', models.DecimalField(decimal_places=4, max_digits=6)),
            ],
        ),
    ]