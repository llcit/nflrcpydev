# search_indexes.py
""" See http://django-haystack.readthedocs.org/en/latest/tutorial.html for more
	information about this setup.
"""
from haystack import indexes
from .models import Contact, Project, Prodev, Publication


class PublicationIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
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