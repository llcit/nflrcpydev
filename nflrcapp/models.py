from __future__ import unicode_literals
from collections import OrderedDict
from django.core.urlresolvers import reverse
from django.db import models

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
    ('Conference', 'Conference'),
    ('Online Course', 'Online Course'),
    ('Summer Institute', 'Summer Institute'),
    ('Symposium', 'Symposium'),
    ('Workshop', 'Workshop'),
    ('Workshop/Symposium', 'Workshop/Symposium'),
    ('Other', 'Other'),
)

PUBLICATION_MEDIA_TYPES = (
    ('CD', 'CD'),
    ('DVD', 'DVD'),
    ('Language Teaching Material', 'Language Teaching Material'),
    ('Network', 'Network'),
    ('NFLRC Monograph', 'NFLRC Monograph'),
    ('PragmaticsI', 'PragmaticsI'),
    ('PragmaticsLL', 'PragmaticsLL'),
    ('Research Note', 'Research Note'),
    ('Videotape', 'Videotape'),
)


class Contact(models.Model):
    first_name = models.CharField(max_length=50L)
    title = models.CharField(max_length=50, choices=HUMAN_PREFIXES, default='', blank=True)
    last_name = models.CharField(max_length=20L, blank=True)
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

    def getuid(self):
        return self.id

    def properties(self):
        properties = [(field.name, field.value_to_string(self))
                      for field in Contact._meta.fields]
        return properties

    def get_absolute_url(self):
        return reverse('contactview', args=[str(self.id)])

    def __unicode__(self):
        return self.last_name


class StoryPage(models.Model):
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    skeywords = models.TextField(blank=True)
    image = models.CharField(max_length=100L, blank=True)
    featured = models.BooleanField(default=False)
    headline = models.BooleanField(default=False)

    def getuid(self):
        return self.id

    def get_absolute_url(self):
        return reverse('story', args=[str(self.id)])

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
    related_publication = models.TextField(blank=True)
    url = models.URLField()
    skeywords = models.TextField(blank=True)
    image = models.CharField(max_length=100L, blank=True)
    featured = models.BooleanField(default=False)
    headline = models.BooleanField(default=False)

    def classname(self):
        name = self.__class__.__name__
        return name.lower()

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
        return self.id

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
    skeywords = models.TextField(blank=True)
    image = models.CharField(max_length=100L, blank=True)
    featured = models.BooleanField(default=False)
    headline = models.BooleanField(default=False)

    def classname(self):
        name = self.__class__.__name__
        return name.lower() + 's'

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
    item_number = models.CharField(max_length=10L, blank=True)
    title = models.CharField(max_length=200L, blank=True)
    language = models.CharField(max_length=255L, blank=True)
    category = models.CharField(
        max_length=128, choices=PUBLICATION_MEDIA_TYPES)
    author = models.CharField(max_length=100L, blank=True)
    year = models.CharField(max_length=12L, blank=True)
    price = models.FloatField(null=True, blank=True)
    description = models.TextField(blank=True)
    size = models.CharField(max_length=40L, blank=True)
    url = models.CharField(max_length=250L, blank=True)
    order_from = models.CharField(max_length=10L, blank=True)
    skeywords = models.TextField(blank=True)
    image = models.CharField(max_length=100L, blank=True)
    isbn = models.CharField(max_length=20L, null=True, blank=True)
    featured = models.BooleanField(default=False)
    headline = models.BooleanField(default=False)

    def classname(self):
        name = self.__class__.__name__
        return name.lower() + 's'

    def properties(self):
        properties = [(field.name, field.value_to_string(self))
                      for field in Publication._meta.fields]
        return properties

    # method to return dictionary with meta information to display
    def customproperties(self):
        properties = [
            # 'uid' : self.item_number,
            ('category', self.category),
            ('author', self.author),
            ('year', self.year),
            ('url', '<a href=\"' + self.url + '\"/>vendors</a>'),
            ('order info', self.order_from),
            ('isbn', self.isbn)
        ]
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

# UNUSED FOR NOW ###########################################################

# UNKNOWN #
# class Spinstruction(models.Model):
# id = models.IntegerField(db_column='ID', primary_key=True) # Field name made lowercase.
# classid = models.CharField(max_length=50L, db_column='ClassID', blank=True) # Field name made lowercase.
# activid = models.CharField(max_length=50L, db_column='ActivID', blank=True) # Field name made lowercase.
# specinstrucation = models.TextField(db_column='SpecInstrucation', blank=True) # Field name made lowercase.
# specinstrucsound = models.CharField(max_length=50L, db_column='SpecInstrucSound', blank=True) # Field name made lowercase.
# activtitle = models.CharField(max_length=200L, db_column='ActivTitle', blank=True) # Field name made lowercase.
#     class Meta:
#         db_table = 'spinstruction'

# class Table05Sp(models.Model):
# id = models.IntegerField(primary_key=True, db_column='Id') # Field name made lowercase.
# classid = models.CharField(max_length=50L, db_column='ClassID', blank=True) # Field name made lowercase.
# activid = models.CharField(max_length=10L, db_column='ActivID', blank=True) # Field name made lowercase.
# quesid = models.IntegerField(null=True, db_column='QuesID', blank=True) # Field name made lowercase.
# aenglish = models.CharField(max_length=500L, db_column='AEnglish', blank=True) # Field name made lowercase.
# apinyin = models.TextField(db_column='APinyin', blank=True) # Field name made lowercase.
# acorrectid = models.IntegerField(null=True, db_column='ACorrectID', blank=True) # Field name made lowercase.
# acorrectsound = models.CharField(max_length=50L, db_column='ACorrectSound', blank=True) # Field name made lowercase.
# awrongsound = models.CharField(max_length=50L, db_column='AWrongSound', blank=True) # Field name made lowercase.
# benglish = models.CharField(max_length=500L, db_column='BEnglish', blank=True) # Field name made lowercase.
# bpinyin = models.TextField(db_column='BPinyin', blank=True) # Field name made lowercase.
# bcorrectid = models.IntegerField(null=True, db_column='BCorrectID', blank=True) # Field name made lowercase.
# bcorrectsound = models.CharField(max_length=50L, db_column='BCorrectSound', blank=True) # Field name made lowercase.
# bwrongsound = models.CharField(max_length=50L, db_column='BWrongSound', blank=True) # Field name made lowercase.
#     class Meta:
#         db_table = 'table05sp'

# UNKNOWN #

# class Mmactivities(models.Model):
# id = models.DecimalField(decimal_places=0, primary_key=True, db_column='ID', max_digits=19) # Field name made lowercase.
# courseid = models.CharField(max_length=50L, db_column='CourseID', blank=True) # Field name made lowercase.
# code = models.CharField(max_length=50L, db_column='Code') # Field name made lowercase.
# name = models.CharField(max_length=100L, db_column='Name', blank=True) # Field name made lowercase.
# type = models.CharField(max_length=100L, db_column='Type', blank=True) # Field name made lowercase.
# instructions = models.CharField(max_length=4000L, db_column='Instructions', blank=True) # Field name made lowercase.
#     class Meta:
#         db_table = 'mmactivities'

# class Mmactivity1(models.Model):
# quesid = models.DecimalField(decimal_places=0, primary_key=True, db_column='QuesID', max_digits=19) # Field name made lowercase.
# questype = models.CharField(max_length=50L, db_column='QuesType', blank=True) # Field name made lowercase.
# quesname = models.CharField(max_length=50L, db_column='QuesName', blank=True) # Field name made lowercase.
# activityid = models.CharField(max_length=50L, db_column='ActivityID', blank=True) # Field name made lowercase.
# groupno = models.DecimalField(decimal_places=0, null=True, max_digits=19, db_column='GroupNO', blank=True) # Field name made lowercase.
# audiofile = models.CharField(max_length=50L, db_column='AudioFile', blank=True) # Field name made lowercase.
# imagelists = models.CharField(max_length=2000L, db_column='ImageLists', blank=True) # Field name made lowercase.
# captionlists = models.CharField(max_length=2000L, db_column='CaptionLists', blank=True) # Field name made lowercase.
# imagekey = models.CharField(max_length=50L, db_column='ImageKey', blank=True) # Field name made lowercase.
# answer = models.IntegerField(null=True, db_column='Answer', blank=True) # Field name made lowercase.
# imageshow = models.CharField(max_length=2000L, db_column='ImageShow', blank=True) # Field name made lowercase.
#     class Meta:
#         db_table = 'mmactivity1'


# class Personnel(models.Model):
# contact_id = models.IntegerField(primary_key=True, db_column='Contact_ID', blank=True) # Field name made lowercase.
# last_name = models.CharField(max_length=20L, db_column='Last_Name', blank=True) # Field name made lowercase.
# middle_name = models.CharField(max_length=20L, db_column='Middle_Name', blank=True) # Field name made lowercase.
# first_name = models.CharField(max_length=20L, db_column='First_Name', blank=True) # Field name made lowercase.
# personal_title = models.CharField(max_length=60L, db_column='Personal_Title', blank=True) # Field name made lowercase.
# business_name = models.CharField(max_length=50L, db_column='Business_Name', blank=True) # Field name made lowercase.
# business_street = models.CharField(max_length=30L, db_column='Business_Street', blank=True) # Field name made lowercase.
# business_city = models.CharField(max_length=25L, db_column='Business_City', blank=True) # Field name made lowercase.
# business_state = models.CharField(max_length=15L, db_column='Business_State', blank=True) # Field name made lowercase.
# business_zipcode = models.CharField(max_length=15L, db_column='Business_ZipCode', blank=True) # Field name made lowercase.
# business_title = models.CharField(max_length=60L, db_column='Business_Title', blank=True) # Field name made lowercase.
# home_street = models.CharField(max_length=80L, db_column='Home_Street', blank=True) # Field name made lowercase.
# home_city = models.CharField(max_length=25L, db_column='Home_City', blank=True) # Field name made lowercase.
# home_state = models.CharField(max_length=15L, db_column='Home_State', blank=True) # Field name made lowercase.
# home_zipcode = models.CharField(max_length=15L, db_column='Home_ZipCode', blank=True) # Field name made lowercase.
# notes = models.TextField(db_column='Notes', blank=True) # Field name made lowercase.
# phone_type = models.CharField(max_length=50L, db_column='Phone_Type', blank=True) # Field name made lowercase.
# phone_number = models.CharField(max_length=50L, db_column='Phone_Number', blank=True) # Field name made lowercase.
# email_address = models.CharField(max_length=60L, db_column='Email_Address', blank=True) # Field name made lowercase.
# date_created = models.DateTimeField(null=True, db_column='Date_Created', blank=True) # Field name made lowercase.
# date_modified = models.DateTimeField(null=True, db_column='Date_Modified', blank=True) # Field name made lowercase.
# country = models.CharField(max_length=50L, db_column='Country', blank=True) # Field name made lowercase.
# url = models.CharField(max_length=80L, db_column='URL', blank=True) # Field name made lowercase.
# info = models.CharField(max_length=50L, db_column='Info', blank=True) # Field name made lowercase.
# title = models.CharField(max_length=60L, db_column='Title', blank=True) # Field name made lowercase.
# role = models.CharField(max_length=25L, db_column='Role', blank=True) # Field name made lowercase.
# current_project = models.CharField(max_length=250L, db_column='Current_Project', blank=True) # Field name made lowercase.
#     class Meta:
#         db_table = 'personnel'

# ONLINE ORDERING #

# class Customer(models.Model):
# customer_number = models.IntegerField(primary_key=True, db_column='Customer_Number') # Field name made lowercase.
# full_name = models.CharField(max_length=50L, db_column='Full_Name') # Field name made lowercase.
# last_name = models.CharField(max_length=20L, db_column='Last_Name', blank=True) # Field name made lowercase.
# department = models.CharField(max_length=75L, db_column='Department', blank=True) # Field name made lowercase.
# institution = models.CharField(max_length=50L, db_column='Institution', blank=True) # Field name made lowercase.
# address = models.CharField(max_length=80L, db_column='Address') # Field name made lowercase.
# city = models.CharField(max_length=20L, db_column='City') # Field name made lowercase.
# state = models.CharField(max_length=15L, db_column='State') # Field name made lowercase.
# zip = models.CharField(max_length=15L, db_column='Zip') # Field name made lowercase.
# country = models.CharField(max_length=20L, db_column='Country', blank=True) # Field name made lowercase.
# phone = models.CharField(max_length=50L, db_column='Phone', blank=True) # Field name made lowercase.
# fax = models.CharField(max_length=50L, db_column='Fax', blank=True) # Field name made lowercase.
# email = models.CharField(max_length=50L, db_column='Email') # Field name made lowercase.
# homepage_url = models.CharField(max_length=80L, db_column='Homepage_URL', blank=True) # Field name made lowercase.
# billing_name = models.CharField(max_length=40L, db_column='Billing_Name', blank=True) # Field name made lowercase.
# billing_address = models.CharField(max_length=60L, db_column='Billing_Address', blank=True) # Field name made lowercase.
# billing_city = models.CharField(max_length=20L, db_column='Billing_City', blank=True) # Field name made lowercase.
# billing_state = models.CharField(max_length=15L, db_column='Billing_State', blank=True) # Field name made lowercase.
# billing_zip = models.CharField(max_length=15L, db_column='Billing_Zip', blank=True) # Field name made lowercase.
# billing_country = models.CharField(max_length=20L, db_column='Billing_Country', blank=True) # Field name made lowercase.
# password = models.CharField(max_length=10L, db_column='Password', blank=True) # Field name made lowercase.
# comment = models.TextField(db_column='Comment', blank=True) # Field name made lowercase.
# po_number = models.CharField(max_length=15L, db_column='PO_Number', blank=True) # Field name made lowercase.
#     class Meta:
#         db_table = 'customer'

# class OrderItem(models.Model):
# order_number = models.IntegerField(db_column='Order_Number') # Field name made lowercase.
# item_number = models.CharField(max_length=10L, db_column='Item_Number') # Field name made lowercase.
# item_title = models.CharField(max_length=200L, db_column='Item_Title', blank=True) # Field name made lowercase.
# quantity = models.IntegerField(null=True, db_column='Quantity', blank=True) # Field name made lowercase.
# unit_price = models.FloatField(null=True, db_column='Unit_Price', blank=True) # Field name made lowercase.
#     class Meta:
#         db_table = 'order_item'

# class PublicationOrder(models.Model):
# order_number = models.IntegerField(primary_key=True, db_column='Order_Number') # Field name made lowercase.
# customer_number = models.IntegerField(null=True, db_column='Customer_Number', blank=True) # Field name made lowercase.
# total_due = models.FloatField(null=True, db_column='Total_Due', blank=True) # Field name made lowercase.
# author_discount = models.FloatField(null=True, db_column='Author_Discount', blank=True) # Field name made lowercase.
# order_date = models.DateTimeField(null=True, db_column='Order_Date', blank=True) # Field name made lowercase.
# po_number = models.CharField(max_length=30L, db_column='PO_Number', blank=True) # Field name made lowercase.
#     class Meta:
#         db_table = 'publication_order'

# class TempOrder(models.Model):
# temp_order_number = models.IntegerField(null=True, db_column='Temp_Order_Number', blank=True) # Field name made lowercase.
# item_number = models.CharField(max_length=10L, db_column='Item_Number', blank=True) # Field name made lowercase.
# item_title = models.CharField(max_length=200L, db_column='Item_Title', blank=True) # Field name made lowercase.
# quantity = models.IntegerField(null=True, db_column='Quantity', blank=True) # Field name made lowercase.
# unit_price = models.FloatField(null=True, db_column='Unit_Price', blank=True) # Field name made lowercase.
#     class Meta:
#         db_table = 'temp_order'


# UNKNOWN #
# class Userinfo(models.Model):
# userid = models.IntegerField(db_column='UserID') # Field name made lowercase.
# loginname = models.CharField(max_length=50L, db_column='LoginName') # Field name made lowercase.
# password = models.TextField(db_column='Password', blank=True) # Field name made lowercase.
# test = models.CharField(max_length=64L, unique=True, db_column='Test', blank=True) # Field name made lowercase.
#     class Meta:
#         db_table = 'userinfo'

# UNKNOWN #
# class Counter(models.Model):
#     count_no = models.IntegerField()
#     category = models.IntegerField()
#     category_name = models.CharField(max_length=20L, blank=True)
#     class Meta:
#         db_table = 'counter'
