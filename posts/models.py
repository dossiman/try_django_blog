from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify


def upload_location(instance, filename):
    # filebase, extension = filename.split('.')
    # return '{}/{}.{}'.format(instance.id, instance.id, filename)
    return '{}/{}'.format(instance.id, filename)


class Post(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    image = models.ImageField(null=True, blank=True,
                              upload_to=upload_location,
                              width_field='width_field',
                              height_field='height_field')
    width_field = models.IntegerField(default=0)
    height_field = models.IntegerField(default=0)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts:detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-id', '-timestamp', '-updated']


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        # Create a slug with a incremental number suffixed
        slug = slugify(instance.title)
        new_slug = slug
        x = 0
        while Post.objects.filter(slug=new_slug).exists():
            x = x + 1
            new_slug = '{}-{}'.format(slug, x)
        instance.slug = new_slug


pre_save.connect(pre_save_post_receiver, sender=Post)
