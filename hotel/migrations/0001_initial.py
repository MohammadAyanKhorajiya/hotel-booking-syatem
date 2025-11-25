# hotel/migrations/0001_initial.py

from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('room_type', models.CharField(choices=[('single', 'Single Room'), ('double', 'Double Room'), ('suite', 'Suite')], max_length=20)),
                ('price_per_night', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_rooms', models.IntegerField(default=1)),
                ('image', models.ImageField(blank=True, null=True, upload_to='rooms/')),
                ('amenities', models.TextField(help_text='कमरे की सुविधाएं (comma से अलग करें)')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'कमरे',
            },
        ),
    ]
