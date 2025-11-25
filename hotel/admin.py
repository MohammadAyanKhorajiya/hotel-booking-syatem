# hotel/admin.py - Django admin में models को दिखाना

from django.contrib import admin
from .models import Room

# Room model को admin में register करता है
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    # List view में कौन से fields दिखाने हैं
    list_display = ('name', 'room_type', 'price_per_night', 'total_rooms')
    
    # कौन से fields search में शामिल हों
    search_fields = ('name', 'description')
    
    # कौन से fields से filter करें
    list_filter = ('room_type', 'created_at')
    
    # Form में fields की order
    fieldsets = (
        ('बुनियादी जानकारी', {
            'fields': ('name', 'description', 'room_type')
        }),
        ('मूल्य और सुविधाएं', {
            'fields': ('price_per_night', 'total_rooms', 'amenities')
        }),
        ('तस्वीर', {
            'fields': ('image',)
        }),
    )
