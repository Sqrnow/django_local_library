# Generated by Django 3.2.9 on 2021-11-30 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_alter_bookinstance_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['due_back'], 'permissions': (('can_mark_returned', 'Set book as returned'), ('canSeeAllBorrow', 'Can see all borrowed books'))},
        ),
    ]