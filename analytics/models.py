from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.conf import settings


from .utils import get_client_ip
from .signals import object_viewed_signal

User = settings.AUTH_USER_MODEL
class ObjectViewed(models.Model):
    user           = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    ip_address     = models.CharField(max_length=220,blank=True,null=True,)
    content_type   = models.ForeignKey(ContentType,null=True,on_delete=models.CASCADE)
    object_id      = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type','object_id')
    timestamp      = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%sviewed%s" %(self.content_object, self.timestamp)

    class Meta:
        ordering = ['-timestamp']
        verbose_name = 'object viewed'
        verbose_name_plural = 'objects viewed'

def object_viewed_receiver(sender, instance, request, *args, **kwargs):
    c_type = ContentType.objects.get_for_model(sender)
    #print(sender)
    #print(instance)
    #print(request)
    #print(request.user)
    
    new_view_obj = ObjectViewed.objects.create(
        user = None,
        content_type = c_type,
        object_id = instance.id,
        ip_address = get_client_ip(request)
        
    )

object_viewed_signal.connect(object_viewed_receiver)

class Visitor(models.Model):
    ip_address     = models.CharField(max_length=220,blank=True,null=True,)
    timestamp      = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%svisited on%s" %(self.timestamp, self.ip_address)

    class Meta:
        ordering = ['-timestamp']
        verbose_name = 'visitor'
        verbose_name_plural = 'visitors'


class number_of_visits(models.Model):
    visits = models.PositiveIntegerField()

    def __str__(self):
        return str(self.visits)

    class Meta:
        verbose_name = 'visit'
        verbose_name_plural = 'visits'

