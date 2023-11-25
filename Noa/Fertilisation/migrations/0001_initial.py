# Generated by Django 4.0.4 on 2023-08-23 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fertilisation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom_Commercial', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='photos/%y/%m/%d')),
                ('QuantiteTotal', models.FloatField()),
                ('Quantite_H', models.FloatField()),
                ('N', models.DecimalField(decimal_places=2, max_digits=5)),
                ('K2O', models.DecimalField(decimal_places=2, max_digits=5)),
                ('P2O5', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Pour_Plante', models.BooleanField(default=False)),
                ('Pour_Arbre', models.BooleanField(default=False)),
                ('Pour_Semis', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Modéle_Variante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categorie', models.CharField(choices=[('plante', 'Plante'), ('arbre', 'Arbre'), ('semis', 'Semis')], max_length=20)),
                ('sous_categorie', models.CharField(max_length=200)),
                ('nom_variante', models.CharField(max_length=200)),
                ('nombre_etape', models.IntegerField()),
                ('description', models.TextField()),
                ('debut_saison', models.DateField()),
                ('fin_saison', models.DateField()),
            ],
        ),
    ]