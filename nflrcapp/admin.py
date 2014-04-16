from django.contrib import admin

from nflrcapp.models import *


# list_display = ('section', 'rank', 'text', 'getOptionTexts', 'guide')

class ExtraMedia:
    js = [
        '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
        '/static/js/tinymce_setup.js',
    ]

class ContactAdmin(admin.ModelAdmin):
	list_display = ('last_name', 'first_name', 'title', 'role', 'listing_rank')
	list_filter = ['role',]
	list_editable = ['role', 'title', 'listing_rank']	

class ProjectAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'featured', 'headline')
	list_filter = ['featured', 'headline']
	list_editable = ['featured', 'headline']

class PublicationAdmin(admin.ModelAdmin):
	list_display = ('item_number', 'title', 'featured', 'headline')
	list_filter = ['featured', 'headline']
	list_editable = ['featured', 'headline']

class ProdevAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'featured', 'headline')
	list_filter = ['featured', 'headline']
	list_editable = ['featured', 'headline']
	
admin.site.register(Contact, ContactAdmin, Media = ExtraMedia)
admin.site.register(Project, ProjectAdmin, Media = ExtraMedia)
# admin.site.register(PersonProject)
admin.site.register(Publication, PublicationAdmin, Media = ExtraMedia)
# admin.site.register(PersonPublication)
admin.site.register(Prodev, ProdevAdmin, Media = ExtraMedia)
admin.site.register(Resource, Media = ExtraMedia)
admin.site.register(Software, Media = ExtraMedia)
admin.site.register(StoryPage, Media = ExtraMedia)
