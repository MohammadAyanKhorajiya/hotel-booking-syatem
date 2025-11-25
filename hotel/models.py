# hotel/models.py - Database models

from django.db import models

# कमरे की जानकारी के लिए model
class Room(models.Model):
    # कमरे के प्रकार
    ROOM_TYPES = [
        ('single', 'Single Room'),
        ('double', 'Double Room'),
        ('suite', 'Suite'),
    ]
    
    # कमरे का नाम
    name = models.CharField(max_length=100)
    
    # कमरे की description
    description = models.TextField()
    
    # कमरे का प्रकार
    room_type = models.CharField(max_length=20, choices=ROOM_TYPES)
    
    # रात भर का price
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    
    # कुल कमरों की संख्या
    total_rooms = models.IntegerField(default=1)
    
    # कमरे की image
    image = models.ImageField(upload_to='rooms/', null=True, blank=True)
    
    # सुविधाएं (जैसे WiFi, AC आदि)
    amenities = models.TextField(help_text="कमरे की सुविधाएं (comma से अलग करें)")
    
    # कमरा बनाया गया समय
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "कमरे"
    
    def __str__(self):
        return self.name
