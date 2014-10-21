from __future__ import unicode_literals
from collections import OrderedDict
from django.core.urlresolvers import reverse
from itertools import chain
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.contrib.syndication.views import Feed
from django.utils.html import strip_tags

from operator import attrgetter


HUMAN_PREFIXES = {
    ('DR', 'PhD.'),
    ('MR', 'Mr.'),
    ('MS', 'Ms.'),
}

ROLE_TYPES = {
    ('STAFF', 'NFLRC Staff'),
    ('ADVBOARD', 'Advisory Board'),
    ('COLLAB', 'Collaborator'),
}

PRODEV_TYPES = (
    ('conference', 'Conference'),
    ('online', 'Online Course'),
    ('institute', 'Summer Institute'),
    ('symposium', 'Symposium'),
    ('workshop', 'Workshop'),
    ('workshop_symposium', 'Workshop/Symposium'),
    ('other', 'Other'),
)

PUBLICATION_MEDIA_TYPES = (
    ('CD', 'CD'),
    ('DVD', 'DVD'),
    ('Journal', 'Journal'),
    ('Language Teaching Material', 'Language Teaching Material'),
    ('Network', 'Network'),
    ('NFLRC Monograph', 'NFLRC Monograph'),
    ('PragmaticsI', 'PragmaticsI'),
    ('PragmaticsLL', 'PragmaticsLL'),
    ('Research Note', 'Research Note'),
    ('Videotape', 'Videotape'),
)

ITEM_TYPE_SHORTCUTS = {
    'CD': 'media',
    'DVD': 'media',
    'Videotape': 'media',
    'NFLRC Monograph': 'monographs',
    'Network': 'networks',
    'Journal': 'journals',
    'Language Teaching Material': 'teaching-materials',
    'PragmaticsLL': 'pragmatics',
    'PragmaticsI': 'pragmatics',
    'Research Note': 'research-notes',
    'Workshop & Conferences': 'prodev',
}



class ItemsManager(models.Manager):

    def allfeatured(self, **kwargs):
        featured_publications = Publication.objects.filter(featured=1)
        featured_prodevs = Prodev.objects.filter(featured=1)
        featured_projects = Project.objects.filter(featured=1)
        featured_stories = StoryPage.objects.filter(featured=1)
        featured_items = sorted(
            chain(featured_publications, featured_prodevs, featured_projects, featured_stories), key=attrgetter('featured_rank'))
        
        return featured_items

    def get_tagged_items(self, **kwargs):
        tag = kwargs.pop('tag')
        item_type = kwargs.pop('item_type')
        taggeditems = TaggedItem.objects.filter(item_tag__tag=tag).filter(content_type__name=item_type)
        items = []
        for i in taggeditems:
            items.append(i.content_object)

        return items 

class ItemTag(models.Model):
    tag = models.CharField(max_length=180, unique=True)

    def __unicode__(self):
        return self.tag

class TaggedItem(models.Model):
    item_tag = models.ForeignKey(ItemTag)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    def __unicode__(self):
        return self.item_tag.tag

class ContactRole(models.Model):
    title = models.CharField(max_length=128)
    list_rank = models.IntegerField(blank=True, default=1000)

    def __unicode__(self):
        return self.title  

class Contact(models.Model):
    first_name = models.CharField(max_length=50L)
    last_name = models.CharField(max_length=20L)
    title = models.CharField(
        max_length=50, choices=HUMAN_PREFIXES, blank=True, null=True)
    staff_role = models.ForeignKey(ContactRole, blank=True, null=True)
    bio = models.TextField(blank=True)
    department = models.CharField(max_length=256L, blank=True)
    university = models.CharField(max_length=60L, blank=True)
    address = models.CharField(max_length=128L, blank=True)
    city = models.CharField(max_length=20L, blank=True)
    state = models.CharField(max_length=15L, blank=True)
    zipcode = models.CharField(max_length=15L, blank=True)
    phone = models.CharField(max_length=40L, blank=True)
    fax = models.CharField(max_length=40L, blank=True)
    email = models.EmailField(blank=True)
    url = models.URLField(blank=True)
    image = models.CharField(max_length=100L, blank=True)
    current_project = models.CharField(max_length=255L, null=True, blank=True)
    nflrc_staff = models.BooleanField(blank=True)
    listing_rank = models.IntegerField(null=True, blank=True)
    role = models.CharField(
        max_length=30, choices=ROLE_TYPES, null=True, blank=True)

    tags = generic.GenericRelation(TaggedItem)
    
    def getuid(self):
        return self.id

    def properties(self):
        properties = [(field.name, field.value_to_string(self))
                      for field in Contact._meta.fields]
        return properties

    # method to return dictionary with meta information to display
    def customproperties(self):
        properties = [
            ('University', self.university),
            ('Role', self.staff_role),
            ('Current Project', self.current_project),
        ]
        return properties

    def get_absolute_url(self):
        return reverse('contactview', args=[str(self.id)])

    def __unicode__(self):
        return self.last_name

class StoryPage(models.Model):
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    thumbnail_desc = models.CharField(
        max_length=160, default='more...', null=True, blank=True, )
    skeywords = models.TextField(blank=True)
    image = models.CharField(max_length=100L, blank=True, default='icon.png',
                             verbose_name='Icon image name (jumbotron images are not specified here.)')
    featured = models.BooleanField(blank=True, default=False)
    featured_rank = models.IntegerField(blank=True, default=0, help_text='higher the number, lower the rank')
    headline = models.BooleanField(default=False)
    headline_tag = models.CharField(
        max_length=512, blank=True, null=True, default='')
    
    tags = generic.GenericRelation(TaggedItem)

    objects = ItemsManager()

    def classname(self):
        name = 'about'
        return name

    def displayname(self):
        name = 'About'
        return name

    def getuid(self):
        return 'story%s' % self.id

    def get_absolute_url(self):
        return reverse('aboutview', args=[str(self.id)])

    def __unicode__(self):
        return self.title


class Prodev(models.Model):
    title = models.CharField(max_length=200L, blank=True)
    language = models.CharField(max_length=100L, blank=True)
    date = models.CharField(max_length=50L, blank=True)
    pdtype = models.CharField(max_length=30L, blank=True, choices=PRODEV_TYPES)
    director = models.CharField(max_length=200L)
    facilitator = models.TextField(blank=True)
    description = models.TextField(blank=True)
    thumbnail_desc = models.CharField(
        max_length=160, null=True, blank=True, default='more...')
    related_publication = models.TextField(blank=True)
    url = models.URLField()
    skeywords = models.TextField(blank=True)
    image = models.CharField(max_length=100L, blank=True, default='icon.png',
                             verbose_name='Icon image name (jumbotron images are not specified here.)')
    featured = models.BooleanField(blank=True, default=False)
    featured_rank = models.IntegerField(blank=True, default=0, help_text='higher the number, lower the rank')
    headline = models.BooleanField(default=False)
    headline_tag = models.CharField(
        max_length=512, blank=True, null=True, default='')

    tags = generic.GenericRelation(TaggedItem)
    
    objects = ItemsManager()

    def classname(self):
        name = self.__class__.__name__
        return name.lower()

    def displayname(self):
        name = 'Events'
        return name

    def properties(self):
        properties = [(field.name, field.value_to_string(self))
                      for field in Prodev._meta.fields]
        return properties

    # method to return dictionary with meta information to display
    def customproperties(self):
        properties = [
            ('date', self.date),
            ('type', self.pdtype),
            ('director', self.director),
            ('facilitator(s)', self.facilitator),
            ('publications', self.related_publication),
            ('url', '<a href=\"' + self.url + '\"/>' + self.url + '</a>')
        ]
        return properties

    def getuid(self):
        return 'PD%s' % self.id

    def get_absolute_url(self):
        return reverse('prodevview', args=[str(self.id)])

    def __unicode__(self):
        return self.title


class Project(models.Model):
    project_number = models.CharField(max_length=10L)
    title = models.CharField(max_length=150L, blank=True)
    language = models.CharField(max_length=80L, blank=True)
    grant_cycle = models.CharField(max_length=50L, blank=True)
    status = models.CharField(max_length=30L, blank=True)
    director = models.TextField(blank=True)
    description = models.TextField(blank=True)
    thumbnail_desc = models.CharField(
        max_length=160, null=True, blank=True, default='more...')
    skeywords = models.TextField(blank=True)
    image = models.CharField(max_length=100L, blank=True, default='icon.png',
                             verbose_name='Icon image name (jumbotron images are not specified here.)')
    featured = models.BooleanField(blank=True, default=False)
    featured_rank = models.IntegerField(blank=True, default=0, help_text='higher the number, lower the rank')
    headline = models.BooleanField(default=False)
    headline_tag = models.CharField(
        max_length=512, blank=True, null=True, default='')
    tags = generic.GenericRelation(TaggedItem)

    objects = ItemsManager()

    def classname(self):
        name = self.__class__.__name__
        return name.lower() + 's'

    def displayname(self):
        name = 'Projects'
        return name

    def properties(self):
        properties = [(field.name, field.value_to_string(self))
                      for field in Project._meta.fields]
        return properties

    # method to return dictionary with meta information to display
    def customproperties(self):
        properties = [
            ('grant period', self.grant_cycle),
            ('director', self.director)
        ]
        return properties

    def getuid(self):
        return self.project_number

    def get_absolute_url(self):
        return reverse('projectview', args=[str(self.project_number)])

    def __unicode__(self):
        return self.title


class PersonProject(models.Model):
    contact_id = models.ForeignKey(Contact)
    project_number = models.ForeignKey(Project)
    status = models.IntegerField(null=True, blank=True)


class Publication(models.Model):
    item_number = models.CharField(max_length=10L, help_text='Follows coding/id system in place for other publications. Example: MGnn is a Monograph with id nn.')
    title = models.CharField(max_length=200L)
    author = models.CharField(
        max_length=100L, help_text='Enter one or more authors.')
    description = models.TextField(help_text='A description of the resource.')
    category = models.CharField(
        max_length=128, choices=PUBLICATION_MEDIA_TYPES, help_text='Category for this publication.')
    image = models.CharField('icon', max_length=100L, default='icon.png', help_text='Icon for this item. <br>Format = ITEM_NUMBERicon.png . Default is icon.png')
    language = models.CharField(
        max_length=255L, blank=True, help_text='(Optional)')
    year = models.CharField(max_length=12L, blank=True)
    thumbnail_desc = models.CharField(max_length=160, null=True, blank=True,
                                      default='more...', help_text='140 characters or less. Appears on the item blocks.')
    is_oer = models.BooleanField(
        'is this an Open Educational Resource?', default=False, blank=True,
        help_text='Check this ON if the publication is an Open Educational Resource')
    url = models.CharField(max_length=250L, blank=True,
                           help_text='(Optional) Specify the address at which the resource can be accessed.')
    ext_url = models.CharField(
        max_length=250L, blank=True, help_text='(Optional) Specify the address at which additional information about the resource is located.')
    oclc_url = models.CharField(
        max_length=250L, blank=True, help_text='(Optional) Specify the OCLC url if it exists.')
    order_from = models.CharField(
        max_length=250L, blank=True, help_text='(Optional) Specify URL where item may be purchased.')
    size = models.CharField(
        max_length=40L, blank=True, help_text='(Optional) Number of pages.')
    skeywords = models.TextField(
        blank=True, help_text='(Optional) List keywords for this item separated by commas.')
    featured = models.BooleanField('feature this item?', blank=True, default=False, help_text='(Optional) Check this ON to force the item to display in featured lists.')
    featured_rank = models.IntegerField(blank=True, default=0, help_text='higher the number, lower the rank')
    hidden = models.BooleanField(default=False, help_text='Prevent this item from displaying on the site. Currently not implemented.')
    isbn = models.CharField(max_length=20L, null=True, blank=True, editable=False) # no longer used.
    price = models.FloatField(editable=False, null=True, blank=True)  # no longer used.
    headline = models.BooleanField(editable=False, default=False, help_text='(Optional) Check this ON to force the item to display as headline. Currently not implemented.' )
    headline_tag = models.CharField(editable=False, max_length=512, blank=True, null=True, default='', help_text='(Optional) Show tagline in headline. Currently not implemented.')

    tags = generic.GenericRelation(TaggedItem)
    
    objects = ItemsManager()

    class Meta:
        ordering = ['-year', 'item_number']

    def displayname(self):
        name = 'Publications'
        return name

    def classname(self):
        name = self.__class__.__name__
        return name.lower() + 's'

    def properties(self):
        properties = [(field.name, field.value_to_string(self))
                      for field in Publication._meta.fields]
        return properties

    # method to return dictionary with meta information to display
    def customproperties(self):
        properties = {}
        access_list = {}
        access_list['access'] = self.url

        if self.ext_url:
            access_list['ext_url'] = self.ext_url
        if self.oclc_url:
            access_list['oclc'] = self.oclc_url
        if self.order_from:
            access_list['order_from'] = self.oclc_url

        access_list['oer'] = self.is_oer

        properties['author(s)'] = self.author
        properties['year'] = self.year
        properties['access_list'] = access_list

        return properties

    def getuid(self):
        return self.item_number

    def get_absolute_url(self):
        return reverse('pubview', args=[str(self.item_number)])

    def __unicode__(self):
        return self.title


class PersonPublication(models.Model):
    contact_id = models.ForeignKey(Contact)
    publication_id = models.ForeignKey(Publication)


class Resource(models.Model):
    resource_number = models.IntegerField()
    title = models.CharField(max_length=150L, blank=True)
    url = models.URLField(blank=True)
    site_type = models.CharField(max_length=60L, blank=True)
    language = models.CharField(max_length=200L, blank=True)
    language_group = models.CharField(max_length=60L, blank=True)
    description = models.TextField(blank=True)
    status = models.IntegerField(null=True, blank=True)
    contact_email = models.CharField(max_length=60L, null=True, blank=True)
    site_type1 = models.CharField(max_length=60L, blank=True)
    site_type2 = models.CharField(max_length=60L, blank=True)
    site_type3 = models.CharField(max_length=60L, blank=True)
    image = models.CharField(max_length=50L, blank=True)
    featured = models.BooleanField(default=False)

    def classname(self):
        return self.__class__.__name__


class Software(models.Model):
    title = models.CharField(max_length=200L,)
    content = models.CharField(max_length=1000L, blank=True)
    languages = models.CharField(max_length=100L)
    skills = models.CharField(max_length=200L, blank=True)
    levels = models.CharField(max_length=100L, blank=True)
    age = models.CharField(max_length=100L, blank=True)
    format = models.CharField(max_length=100L, blank=True)
    platforms = models.CharField(max_length=300L, blank=True)
    hardwares = models.CharField(max_length=1500L, blank=True)
    distributor = models.CharField(max_length=600L, blank=True)
    telephone = models.CharField(max_length=100L, blank=True)
    fax = models.CharField(max_length=100L, blank=True)
    infoemail = models.EmailField(blank=True)
    saleemail = models.EmailField(blank=True)
    geneemail = models.EmailField(blank=True)
    www = models.URLField(blank=True)
    price = models.CharField(max_length=200L, blank=True)
    review = models.CharField(max_length=1000L, blank=True)
    featured = models.BooleanField(default=False)

    def classname(self):
        return self.__class__.__name__

class NflrcNewsFeed(Feed):
    title = "NFLRC News"
    link = "/"
    description = "The latest and greatest from the National Foreign Language Resource Center."
    title_template = "feeds/title.html"
    description_template = "feeds/newswire.html"

    def items(self):
        return StoryPage.objects.get_tagged_items(tag='news', item_type='story page')

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return strip_tags(item.description)

    def get_context_data(self, **kwargs):
        context = super(NflrcNewsFeed, self).get_context_data(**kwargs)
        try:
            context['blurb'] = kwargs.pop('item').thumbnail_desc
        except:
            context['blurb'] = 'News Flash'
        return context

    # def item_link(self, item):
    #     print 'NEWS', item;
    #     return reverse('news-wire', args=[item.pk])
