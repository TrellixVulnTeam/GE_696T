# Generated by Django 4.0.5 on 2022-06-26 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ge', '0022_remove_dstcolumn_pre_choice_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Category of Keyge'},
        ),
        migrations.AlterModelOptions(
            name='database',
            options={'verbose_name_plural': 'Database'},
        ),
        migrations.AlterModelOptions(
            name='dataset',
            options={'verbose_name_plural': 'Dataset'},
        ),
        migrations.AlterModelOptions(
            name='dstcolumn',
            options={'verbose_name_plural': 'Data Transformation'},
        ),
        migrations.AlterModelOptions(
            name='group',
            options={'verbose_name_plural': 'Group of Keyge'},
        ),
        migrations.AlterModelOptions(
            name='keyge',
            options={'verbose_name_plural': 'Keyge'},
        ),
        migrations.AlterModelOptions(
            name='keyhierarchy',
            options={'verbose_name_plural': 'Hierarchy of Keyge'},
        ),
        migrations.AlterModelOptions(
            name='keylink',
            options={'verbose_name_plural': 'Keyge Links'},
        ),
        migrations.AlterModelOptions(
            name='keyword',
            options={'verbose_name_plural': 'Keyge x Word'},
        ),
        migrations.AlterModelOptions(
            name='logscollector',
            options={'verbose_name_plural': 'Process Log'},
        ),
        migrations.AlterModelOptions(
            name='prefixopc',
            options={'verbose_name_plural': 'Prefix of Keyge'},
        ),
        migrations.AlterModelOptions(
            name='wfcontrol',
            options={'verbose_name_plural': 'Workflow Control'},
        ),
        migrations.AlterModelOptions(
            name='wordmap',
            options={'verbose_name_plural': 'Map of Word'},
        ),
    ]
