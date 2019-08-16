# forms.py
from django.forms import ModelForm
from .models import Prodev, Publication, Project, StoryPage


class ProdevForm(ModelForm):
    class Meta:
        model = Prodev
        fields = ['featured', 'featured_rank', 'date', 'datestamp', 'pdtype', 'image', 'listing_rank',  'description']


class PublicationForm(ModelForm):
    class Meta:
        model = Publication
        fields = ['featured', 'featured_rank', 'listing_rank',  'description']


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['featured', 'featured_rank', 'listing_rank',  'description']


class StoryPageForm(ModelForm):
    class Meta:
        model = StoryPage
        fields = ['featured', 'featured_rank', 'listing_rank',  'description']

