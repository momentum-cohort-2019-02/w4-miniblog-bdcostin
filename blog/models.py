from django.db import models
import uuid
from django.urls import reverse

# Create your models here.
class BlogPost(models.Model):
    '''Model that represents a blog post'''
    title = models.CharField(max_length=200)

    # This application will assume blog post have only one author, e.g., ForeignKey
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    post = models.TextField()
    posted = models.DateField()
    summary = models.TextField(max_length=1000, help_text='Enter a description for the blog post')
    topic = models.ManyToManyField('Topic', help_text='Select a topic for this post')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular post across whole site')

    def __str__(self):
        """String for representing the Model object."""
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this blog post."""
        return reverse('blog-detail', args=[str(self.id)])

    class Meta:
        ordering = ['posted']

    def display_topic(self):
        """Create a string for the Topic. This is required to display genre in Admin."""
        return ', '.join(topic.name for topic in self.topic.all()[:3])
    
    display_topic.short_description = 'Topic'

class Topic(models.Model):
    '''Model represents the topics of each blog post'''
    name = models.CharField(max_length=200, help_text='Enter a blog topic (e.g. Django Basics)')

    def __str__ (self):
        '''String that represents the model'''
        return self.name

class Author(models.Model):
    '''Model represents an author'''
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        ordering = ['last_name', 'first_name']
    
    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'

class Comment(models.Model):
    pass
