# Generated by Django 3.1.1 on 2021-05-24 21:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=45)),
                ('subtitle', models.CharField(max_length=45)),
                ('limit_date', models.DateField()),
                ('description', models.TextField()),
                ('state', models.CharField(choices=[('PC', 'por_comenzar'), ('EP', 'en_proceso'), ('FN', 'finalizada')], default='PC', max_length=2)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.usuarios')),
            ],
        ),
    ]
