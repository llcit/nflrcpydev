# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class Contacts(models.Model):
    contact_id = models.IntegerField(primary_key=True, db_column='Contact_ID') # Field name made lowercase.
    full_name = models.CharField(max_length=50L, db_column='Full_Name') # Field name made lowercase.
    title = models.ForeignKey('ContactsTitle', null=True, blank=True)
    title_deleteme = models.CharField(max_length=50L, db_column='Title_DELETEME', blank=True) # Field name made lowercase.
    last_name = models.CharField(max_length=20L, db_column='Last_Name', blank=True) # Field name made lowercase.
    department = models.CharField(max_length=80L, db_column='Department', blank=True) # Field name made lowercase.
    university = models.CharField(max_length=60L, db_column='University', blank=True) # Field name made lowercase.
    address = models.CharField(max_length=128L, db_column='Address', blank=True) # Field name made lowercase.
    city = models.CharField(max_length=20L, db_column='City', blank=True) # Field name made lowercase.
    state = models.CharField(max_length=15L, db_column='State', blank=True) # Field name made lowercase.
    zip = models.CharField(max_length=15L, db_column='Zip', blank=True) # Field name made lowercase.
    field10 = models.CharField(max_length=255L, db_column='Field10', blank=True) # Field name made lowercase.
    phone = models.CharField(max_length=40L, db_column='Phone', blank=True) # Field name made lowercase.
    fax = models.CharField(max_length=40L, db_column='Fax', blank=True) # Field name made lowercase.
    email = models.CharField(max_length=40L, db_column='Email', blank=True) # Field name made lowercase.
    url = models.CharField(max_length=80L, db_column='URL', blank=True) # Field name made lowercase.
    field15 = models.CharField(max_length=255L, db_column='Field15', blank=True) # Field name made lowercase.
    field16 = models.CharField(max_length=255L, db_column='Field16', blank=True) # Field name made lowercase.
    field17 = models.DateTimeField(null=True, db_column='Field17', blank=True) # Field name made lowercase.
    field18 = models.CharField(max_length=255L, db_column='Field18', blank=True) # Field name made lowercase.
    current_project = models.CharField(max_length=255L, db_column='Current_Project', blank=True) # Field name made lowercase.
    status = models.IntegerField(null=True, db_column='Status', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'contacts'

class ContactsTitle(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    listing_rank = models.DecimalField(null=True, max_digits=6, decimal_places=0, blank=True)
    title = models.CharField(max_length=50L, blank=True)
    class Meta:
        db_table = 'contacts_title'

class Project(models.Model):
    project_number = models.CharField(max_length=10L, primary_key=True, db_column='Project_Number') # Field name made lowercase.
    title = models.CharField(max_length=150L, db_column='Title', blank=True) # Field name made lowercase.
    grant_cycle = models.CharField(max_length=50L, db_column='Grant_Cycle', blank=True) # Field name made lowercase.
    status = models.CharField(max_length=30L, db_column='Status', blank=True) # Field name made lowercase.
    language = models.CharField(max_length=80L, db_column='Language', blank=True) # Field name made lowercase.
    director = models.TextField(db_column='Director', blank=True) # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True) # Field name made lowercase.
    skeywords = models.TextField(db_column='sKeywords', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'project'

class PersonProject(models.Model):
    contact_id = models.IntegerField(db_column='Contact_ID', primary_key=True) # Field name made lowercase.
    project_number = models.CharField(max_length=10L, db_column='Project_Number') # Field name made lowercase.
    status = models.IntegerField(null=True, db_column='Status', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'person_project'

class Publication(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    item_number = models.CharField(max_length=10L, db_column='Item_Number', blank=True) # Field name made lowercase.
    category = models.CharField(max_length=35L, db_column='Category', blank=True) # Field name made lowercase.
    title = models.CharField(max_length=200L, db_column='Title', blank=True) # Field name made lowercase.
    author = models.CharField(max_length=100L, db_column='Author', blank=True) # Field name made lowercase.
    year = models.CharField(max_length=12L, db_column='Year', blank=True) # Field name made lowercase.
    language = models.CharField(max_length=255L, db_column='Language', blank=True) # Field name made lowercase.
    price = models.FloatField(null=True, db_column='Price', blank=True) # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True) # Field name made lowercase.
    size = models.CharField(max_length=40L, db_column='Size', blank=True) # Field name made lowercase.
    url = models.CharField(max_length=250L, db_column='URL', blank=True) # Field name made lowercase.
    order_from = models.CharField(max_length=10L, db_column='Order_From', blank=True) # Field name made lowercase.
    skeywords = models.TextField(db_column='SKeywords', blank=True) # Field name made lowercase.
    image = models.CharField(max_length=100L, db_column='Image', blank=True) # Field name made lowercase.
    isbn = models.CharField(max_length=20L, db_column='ISBN', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'publication'

class PersonPublication(models.Model):
    contact_id = models.IntegerField(primary_key=True, db_column='Contact_ID', ) # Field name made lowercase.
    publication_id = models.IntegerField(db_column='Publication_ID') # Field name made lowercase.
    class Meta:
        db_table = 'person_publication'

class Prodev(models.Model):
    institute_id = models.IntegerField(primary_key=True, db_column='Institute_ID') # Field name made lowercase.
    title = models.CharField(max_length=200L, db_column='Title', blank=True) # Field name made lowercase.
    institute_date = models.CharField(max_length=50L, db_column='Institute_Date', blank=True) # Field name made lowercase.
    institute_type = models.CharField(max_length=30L, db_column='Institute_Type', blank=True) # Field name made lowercase.
    institute_language = models.CharField(max_length=100L, db_column='Institute_Language', blank=True) # Field name made lowercase.
    director = models.CharField(max_length=200L, db_column='Director', blank=True) # Field name made lowercase.
    facilitator = models.TextField(db_column='Facilitator', blank=True) # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True) # Field name made lowercase.
    related_publication = models.TextField(db_column='Related_Publication', blank=True) # Field name made lowercase.
    url = models.CharField(max_length=80L, db_column='URL', blank=True) # Field name made lowercase.
    skeywords = models.TextField(db_column='sKeywords', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'prodev'

class Resource(models.Model):
    resource_number = models.IntegerField(primary_key=True, db_column='Resource_Number') # Field name made lowercase.
    title = models.CharField(max_length=150L, db_column='Title', blank=True) # Field name made lowercase.
    url = models.TextField(db_column='URL', blank=True) # Field name made lowercase.
    site_type = models.CharField(max_length=60L, db_column='Site_Type', blank=True) # Field name made lowercase.
    language = models.CharField(max_length=200L, db_column='Language', blank=True) # Field name made lowercase.
    language_group = models.CharField(max_length=60L, db_column='Language_Group', blank=True) # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True) # Field name made lowercase.
    status = models.IntegerField(null=True, db_column='Status', blank=True) # Field name made lowercase.
    contact_email = models.CharField(max_length=60L, db_column='Contact_Email', blank=True) # Field name made lowercase.
    site_type2 = models.CharField(max_length=60L, db_column='Site_type2', blank=True) # Field name made lowercase.
    site_type1 = models.CharField(max_length=60L, db_column='Site_type1', blank=True) # Field name made lowercase.
    site_type3 = models.CharField(max_length=60L, blank=True)
    image = models.CharField(max_length=50L, db_column='Image', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'resource'

class Software(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True) # Field name made lowercase.
    title = models.CharField(max_length=200L, db_column='Title') # Field name made lowercase.
    content = models.CharField(max_length=1000L, db_column='Content', blank=True) # Field name made lowercase.
    languages = models.CharField(max_length=100L, db_column='Languages') # Field name made lowercase.
    skills = models.CharField(max_length=200L, db_column='Skills', blank=True) # Field name made lowercase.
    levels = models.CharField(max_length=100L, db_column='Levels', blank=True) # Field name made lowercase.
    age = models.CharField(max_length=100L, db_column='Age', blank=True) # Field name made lowercase.
    format = models.CharField(max_length=100L, db_column='Format', blank=True) # Field name made lowercase.
    platforms = models.CharField(max_length=300L, db_column='Platforms', blank=True) # Field name made lowercase.
    hardwares = models.CharField(max_length=1500L, db_column='Hardwares', blank=True) # Field name made lowercase.
    distributor = models.CharField(max_length=600L, db_column='Distributor', blank=True) # Field name made lowercase.
    telephone = models.CharField(max_length=100L, db_column='Telephone', blank=True) # Field name made lowercase.
    fax = models.CharField(max_length=100L, db_column='Fax', blank=True) # Field name made lowercase.
    infoemail = models.CharField(max_length=100L, db_column='InfoEmail', blank=True) # Field name made lowercase.
    saleemail = models.CharField(max_length=100L, db_column='SaleEmail', blank=True) # Field name made lowercase.
    geneemail = models.CharField(max_length=100L, db_column='GeneEmail', blank=True) # Field name made lowercase.
    www = models.CharField(max_length=200L, db_column='WWW', blank=True) # Field name made lowercase.
    price = models.CharField(max_length=200L, db_column='Price', blank=True) # Field name made lowercase.
    review = models.CharField(max_length=1000L, db_column='Review', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'software'


## UNUSED FOR NOW ###########################################################

# # UNKNOWN #
# class Spinstruction(models.Model):
#     id = models.IntegerField(db_column='ID', primary_key=True) # Field name made lowercase.
#     classid = models.CharField(max_length=50L, db_column='ClassID', blank=True) # Field name made lowercase.
#     activid = models.CharField(max_length=50L, db_column='ActivID', blank=True) # Field name made lowercase.
#     specinstrucation = models.TextField(db_column='SpecInstrucation', blank=True) # Field name made lowercase.
#     specinstrucsound = models.CharField(max_length=50L, db_column='SpecInstrucSound', blank=True) # Field name made lowercase.
#     activtitle = models.CharField(max_length=200L, db_column='ActivTitle', blank=True) # Field name made lowercase.
#     class Meta:
#         db_table = 'spinstruction'

# class Table05Sp(models.Model):
#     id = models.IntegerField(primary_key=True, db_column='Id') # Field name made lowercase.
#     classid = models.CharField(max_length=50L, db_column='ClassID', blank=True) # Field name made lowercase.
#     activid = models.CharField(max_length=10L, db_column='ActivID', blank=True) # Field name made lowercase.
#     quesid = models.IntegerField(null=True, db_column='QuesID', blank=True) # Field name made lowercase.
#     aenglish = models.CharField(max_length=500L, db_column='AEnglish', blank=True) # Field name made lowercase.
#     apinyin = models.TextField(db_column='APinyin', blank=True) # Field name made lowercase.
#     acorrectid = models.IntegerField(null=True, db_column='ACorrectID', blank=True) # Field name made lowercase.
#     acorrectsound = models.CharField(max_length=50L, db_column='ACorrectSound', blank=True) # Field name made lowercase.
#     awrongsound = models.CharField(max_length=50L, db_column='AWrongSound', blank=True) # Field name made lowercase.
#     benglish = models.CharField(max_length=500L, db_column='BEnglish', blank=True) # Field name made lowercase.
#     bpinyin = models.TextField(db_column='BPinyin', blank=True) # Field name made lowercase.
#     bcorrectid = models.IntegerField(null=True, db_column='BCorrectID', blank=True) # Field name made lowercase.
#     bcorrectsound = models.CharField(max_length=50L, db_column='BCorrectSound', blank=True) # Field name made lowercase.
#     bwrongsound = models.CharField(max_length=50L, db_column='BWrongSound', blank=True) # Field name made lowercase.
#     class Meta:
#         db_table = 'table05sp'

# # UNKNOWN #

# class Mmactivities(models.Model):
#     id = models.DecimalField(decimal_places=0, primary_key=True, db_column='ID', max_digits=19) # Field name made lowercase.
#     courseid = models.CharField(max_length=50L, db_column='CourseID', blank=True) # Field name made lowercase.
#     code = models.CharField(max_length=50L, db_column='Code') # Field name made lowercase.
#     name = models.CharField(max_length=100L, db_column='Name', blank=True) # Field name made lowercase.
#     type = models.CharField(max_length=100L, db_column='Type', blank=True) # Field name made lowercase.
#     instructions = models.CharField(max_length=4000L, db_column='Instructions', blank=True) # Field name made lowercase.
#     class Meta:
#         db_table = 'mmactivities'

# class Mmactivity1(models.Model):
#     quesid = models.DecimalField(decimal_places=0, primary_key=True, db_column='QuesID', max_digits=19) # Field name made lowercase.
#     questype = models.CharField(max_length=50L, db_column='QuesType', blank=True) # Field name made lowercase.
#     quesname = models.CharField(max_length=50L, db_column='QuesName', blank=True) # Field name made lowercase.
#     activityid = models.CharField(max_length=50L, db_column='ActivityID', blank=True) # Field name made lowercase.
#     groupno = models.DecimalField(decimal_places=0, null=True, max_digits=19, db_column='GroupNO', blank=True) # Field name made lowercase.
#     audiofile = models.CharField(max_length=50L, db_column='AudioFile', blank=True) # Field name made lowercase.
#     imagelists = models.CharField(max_length=2000L, db_column='ImageLists', blank=True) # Field name made lowercase.
#     captionlists = models.CharField(max_length=2000L, db_column='CaptionLists', blank=True) # Field name made lowercase.
#     imagekey = models.CharField(max_length=50L, db_column='ImageKey', blank=True) # Field name made lowercase.
#     answer = models.IntegerField(null=True, db_column='Answer', blank=True) # Field name made lowercase.
#     imageshow = models.CharField(max_length=2000L, db_column='ImageShow', blank=True) # Field name made lowercase.
#     class Meta:
#         db_table = 'mmactivity1'


# class Personnel(models.Model):
#     contact_id = models.IntegerField(primary_key=True, db_column='Contact_ID', blank=True) # Field name made lowercase.
#     last_name = models.CharField(max_length=20L, db_column='Last_Name', blank=True) # Field name made lowercase.
#     middle_name = models.CharField(max_length=20L, db_column='Middle_Name', blank=True) # Field name made lowercase.
#     first_name = models.CharField(max_length=20L, db_column='First_Name', blank=True) # Field name made lowercase.
#     personal_title = models.CharField(max_length=60L, db_column='Personal_Title', blank=True) # Field name made lowercase.
#     business_name = models.CharField(max_length=50L, db_column='Business_Name', blank=True) # Field name made lowercase.
#     business_street = models.CharField(max_length=30L, db_column='Business_Street', blank=True) # Field name made lowercase.
#     business_city = models.CharField(max_length=25L, db_column='Business_City', blank=True) # Field name made lowercase.
#     business_state = models.CharField(max_length=15L, db_column='Business_State', blank=True) # Field name made lowercase.
#     business_zipcode = models.CharField(max_length=15L, db_column='Business_ZipCode', blank=True) # Field name made lowercase.
#     business_title = models.CharField(max_length=60L, db_column='Business_Title', blank=True) # Field name made lowercase.
#     home_street = models.CharField(max_length=80L, db_column='Home_Street', blank=True) # Field name made lowercase.
#     home_city = models.CharField(max_length=25L, db_column='Home_City', blank=True) # Field name made lowercase.
#     home_state = models.CharField(max_length=15L, db_column='Home_State', blank=True) # Field name made lowercase.
#     home_zipcode = models.CharField(max_length=15L, db_column='Home_ZipCode', blank=True) # Field name made lowercase.
#     notes = models.TextField(db_column='Notes', blank=True) # Field name made lowercase.
#     phone_type = models.CharField(max_length=50L, db_column='Phone_Type', blank=True) # Field name made lowercase.
#     phone_number = models.CharField(max_length=50L, db_column='Phone_Number', blank=True) # Field name made lowercase.
#     email_address = models.CharField(max_length=60L, db_column='Email_Address', blank=True) # Field name made lowercase.
#     date_created = models.DateTimeField(null=True, db_column='Date_Created', blank=True) # Field name made lowercase.
#     date_modified = models.DateTimeField(null=True, db_column='Date_Modified', blank=True) # Field name made lowercase.
#     country = models.CharField(max_length=50L, db_column='Country', blank=True) # Field name made lowercase.
#     url = models.CharField(max_length=80L, db_column='URL', blank=True) # Field name made lowercase.
#     info = models.CharField(max_length=50L, db_column='Info', blank=True) # Field name made lowercase.
#     title = models.CharField(max_length=60L, db_column='Title', blank=True) # Field name made lowercase.
#     role = models.CharField(max_length=25L, db_column='Role', blank=True) # Field name made lowercase.
#     current_project = models.CharField(max_length=250L, db_column='Current_Project', blank=True) # Field name made lowercase.
#     class Meta:
#         db_table = 'personnel'

# # ONLINE ORDERING #

# class Customer(models.Model):
#     customer_number = models.IntegerField(primary_key=True, db_column='Customer_Number') # Field name made lowercase.
#     full_name = models.CharField(max_length=50L, db_column='Full_Name') # Field name made lowercase.
#     last_name = models.CharField(max_length=20L, db_column='Last_Name', blank=True) # Field name made lowercase.
#     department = models.CharField(max_length=75L, db_column='Department', blank=True) # Field name made lowercase.
#     institution = models.CharField(max_length=50L, db_column='Institution', blank=True) # Field name made lowercase.
#     address = models.CharField(max_length=80L, db_column='Address') # Field name made lowercase.
#     city = models.CharField(max_length=20L, db_column='City') # Field name made lowercase.
#     state = models.CharField(max_length=15L, db_column='State') # Field name made lowercase.
#     zip = models.CharField(max_length=15L, db_column='Zip') # Field name made lowercase.
#     country = models.CharField(max_length=20L, db_column='Country', blank=True) # Field name made lowercase.
#     phone = models.CharField(max_length=50L, db_column='Phone', blank=True) # Field name made lowercase.
#     fax = models.CharField(max_length=50L, db_column='Fax', blank=True) # Field name made lowercase.
#     email = models.CharField(max_length=50L, db_column='Email') # Field name made lowercase.
#     homepage_url = models.CharField(max_length=80L, db_column='Homepage_URL', blank=True) # Field name made lowercase.
#     billing_name = models.CharField(max_length=40L, db_column='Billing_Name', blank=True) # Field name made lowercase.
#     billing_address = models.CharField(max_length=60L, db_column='Billing_Address', blank=True) # Field name made lowercase.
#     billing_city = models.CharField(max_length=20L, db_column='Billing_City', blank=True) # Field name made lowercase.
#     billing_state = models.CharField(max_length=15L, db_column='Billing_State', blank=True) # Field name made lowercase.
#     billing_zip = models.CharField(max_length=15L, db_column='Billing_Zip', blank=True) # Field name made lowercase.
#     billing_country = models.CharField(max_length=20L, db_column='Billing_Country', blank=True) # Field name made lowercase.
#     password = models.CharField(max_length=10L, db_column='Password', blank=True) # Field name made lowercase.
#     comment = models.TextField(db_column='Comment', blank=True) # Field name made lowercase.
#     po_number = models.CharField(max_length=15L, db_column='PO_Number', blank=True) # Field name made lowercase.
#     class Meta:
#         db_table = 'customer'

# class OrderItem(models.Model):
#     order_number = models.IntegerField(db_column='Order_Number') # Field name made lowercase.
#     item_number = models.CharField(max_length=10L, db_column='Item_Number') # Field name made lowercase.
#     item_title = models.CharField(max_length=200L, db_column='Item_Title', blank=True) # Field name made lowercase.
#     quantity = models.IntegerField(null=True, db_column='Quantity', blank=True) # Field name made lowercase.
#     unit_price = models.FloatField(null=True, db_column='Unit_Price', blank=True) # Field name made lowercase.
#     class Meta:
#         db_table = 'order_item'

# class PublicationOrder(models.Model):
#     order_number = models.IntegerField(primary_key=True, db_column='Order_Number') # Field name made lowercase.
#     customer_number = models.IntegerField(null=True, db_column='Customer_Number', blank=True) # Field name made lowercase.
#     total_due = models.FloatField(null=True, db_column='Total_Due', blank=True) # Field name made lowercase.
#     author_discount = models.FloatField(null=True, db_column='Author_Discount', blank=True) # Field name made lowercase.
#     order_date = models.DateTimeField(null=True, db_column='Order_Date', blank=True) # Field name made lowercase.
#     po_number = models.CharField(max_length=30L, db_column='PO_Number', blank=True) # Field name made lowercase.
#     class Meta:
#         db_table = 'publication_order'

# class TempOrder(models.Model):
#     temp_order_number = models.IntegerField(null=True, db_column='Temp_Order_Number', blank=True) # Field name made lowercase.
#     item_number = models.CharField(max_length=10L, db_column='Item_Number', blank=True) # Field name made lowercase.
#     item_title = models.CharField(max_length=200L, db_column='Item_Title', blank=True) # Field name made lowercase.
#     quantity = models.IntegerField(null=True, db_column='Quantity', blank=True) # Field name made lowercase.
#     unit_price = models.FloatField(null=True, db_column='Unit_Price', blank=True) # Field name made lowercase.
#     class Meta:
#         db_table = 'temp_order'


# # UNKNOWN #
# class Userinfo(models.Model):
#     userid = models.IntegerField(db_column='UserID') # Field name made lowercase.
#     loginname = models.CharField(max_length=50L, db_column='LoginName') # Field name made lowercase.
#     password = models.TextField(db_column='Password', blank=True) # Field name made lowercase.
#     test = models.CharField(max_length=64L, unique=True, db_column='Test', blank=True) # Field name made lowercase.
#     class Meta:
#         db_table = 'userinfo'

# # UNKNOWN #
# class Counter(models.Model):
#     count_no = models.IntegerField()
#     category = models.IntegerField()
#     category_name = models.CharField(max_length=20L, blank=True)
#     class Meta:
#         db_table = 'counter'
