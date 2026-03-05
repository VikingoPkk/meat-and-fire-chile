from django.db import models

class EventSection(models.Model):
    SECTION_TYPES = (
        ('HERO', 'Hero/Portada'),
        ('INFO', 'Información General'),
        ('TICKETS', 'Sección de Tickets'),
    )
    type = models.CharField(max_length=10, choices=SECTION_TYPES, unique=True)
    title = models.CharField(max_length=200)
    subtitle = models.TextField(blank=True)
    # Campo de video configurado para aceptar .mov y .mp4
    video_file = models.FileField(upload_to='videos/', blank=True, null=True)
    background_image = models.ImageField(upload_to='sections/', blank=True)
    
    def __str__(self):
        return self.get_type_display()

class Chef(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chefs/')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name

class Ticket(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=20)
    info = models.TextField(help_text="Lo que incluye")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name