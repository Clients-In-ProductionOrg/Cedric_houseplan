# Generated migration to remove display_on field

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_houseplan_display_section'),
    ]

    operations = [
        migrations.RunSQL(
            'ALTER TABLE core_houseplan DROP COLUMN IF EXISTS display_on;',
            reverse_sql='SELECT 1;',  # No reverse operation needed for drop
        ),
    ]
