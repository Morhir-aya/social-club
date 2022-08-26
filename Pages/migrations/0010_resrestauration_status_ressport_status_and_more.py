# Generated by Django 4.1 on 2022-08-21 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0009_alter_resrestauration_typeres_alter_ressport_typeres'),
    ]

    operations = [
        migrations.AddField(
            model_name='resrestauration',
            name='status',
            field=models.CharField(choices=[('Acceptée', 'Acceptée'), ('Refusée', 'Refusée')], default='En cours de traitement', max_length=100),
        ),
        migrations.AddField(
            model_name='ressport',
            name='status',
            field=models.CharField(choices=[('Acceptée', 'Acceptée'), ('Refusée', 'Refusée')], default='En cours de traitement', max_length=100),
        ),
        migrations.AlterField(
            model_name='ressport',
            name='activite',
            field=models.CharField(choices=[('Football', 'Football'), ('Tennis', 'Tennis'), ('Natation', 'Natation'), ('Basket', 'Basket'), ('Salle de Sport', 'Salle de Sport')], max_length=100),
        ),
    ]
