# search_indexes.py
""" See http://django-haystack.readthedocs.org/en/latest/tutorial.html for more
	information about this setup.
"""
from haystack import indexes
from .models import Contact, Project, Prodev, Publication


class PublicationIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    item_number = indexes.CharField(model_attr='item_number')
    title = indexes.CharField(model_attr='title')
    author = indexes.CharField(model_attr='author')
    description = indexes.CharField(model_attr='description')
    language = indexes.CharField(model_attr='language')
    year = indexes.CharField(model_attr='year')

    def get_model(self):
        return Publication

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()

class ProjectIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    project_number = indexes.CharField(model_attr='project_number')
    title = indexes.CharField(model_attr='title')
    language = indexes.CharField(model_attr='language')
    grant_cycle = indexes.CharField(model_attr='grant_cycle')
    director = indexes.CharField(model_attr='director')
    description = indexes.CharField(model_attr='description')

    def get_model(self):
        return Project

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()

class ProdevIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    pdtype = indexes.CharField(model_attr='pdtype')
    description = indexes.CharField(model_attr='description')
    director = indexes.CharField(model_attr='director')
    language = indexes.CharField(model_attr='language')
    facilitator = indexes.CharField(model_attr='facilitator')

    def get_model(self):
        return Prodev

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()

class ContactIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    first_name = indexes.CharField(model_attr='first_name')
    last_name = indexes.CharField(model_attr='last_name')
    bio = indexes.CharField(model_attr='bio')
    university = indexes.CharField(model_attr='university')
    email = indexes.CharField(model_attr='email')

    def get_model(self):
        return Contact

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()