from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager

class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ('name',)

# Create your models here.
class Advert(models.Model):
    # CATEGORY_CHOICES = [
    #     ('Cars', 'Cars'),
	# 	('Stationery', 'Stationery'),
    #     ('Wears', 'Wears'),
    #     ('Cosmetics', 'Cosmetics'),
	# 	('Kitchen', 'Kitchen'),
    #     ('Baby Care', 'Baby Care'),
    #     ('Home', 'Home'),
    #     ('Garden', 'Garden'),
    #     ('Electronics', 'Electronics'),
    #     ('Pet', 'Pet'),
    #     ('Art and Craft', 'Art and Craft'),
    #     ('Sports', 'Sports'),
    #     ('Health', 'Health'),
    #     ('Fitness and Gym', 'Fitness and Gym'),
    # ]
    STATUS_CHOICES = [
        ('Approved', 'Approved'),
		('Rejected', 'Rejected'),
        ('Under review', 'Under review'),
    ]
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='adverts_category')
    slug = models.SlugField(max_length=255, unique_for_date='created', null=True)
    poster = models.ForeignKey('account.Person', null=True, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='adverts/%Y/%m/%d', blank=True, null=True)
    title = models.CharField(max_length=255, null=True)
    alt = models.CharField(max_length=255, blank=True, null=True)
    link = models.CharField(max_length=1000, null=True)
    article = models.TextField(max_length=5000, null=True)
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default="Under review", null=True)
    updated_by = models.ManyToManyField('account.Person', blank=True, related_name='adverts_updated')

    loves = models.PositiveIntegerField(default=0)
    edits = models.PositiveIntegerField(default=0)
    lovers = models.ManyToManyField('account.Person', blank=True, related_name='adverts_lovers')

    views = models.PositiveIntegerField(default=0)
    viewers = models.ManyToManyField('account.Person', blank=True, related_name='adverts_viewers')

    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    tags = TaggableManager()

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.created.year,
                                                 self.created.strftime('%m'),
                                                 self.created.strftime('%d'),
                                                 self.slug])
