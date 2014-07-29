from django.contrib import admin
from django.contrib.contenttypes import generic
from nflrcapp.models import Contact, Project, Publication, Prodev, StoryPage#, TaggedItem

class ExtraMedia:
    js = [
        '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
        '/static/js/tinymce_setup.js',
    ]

# class TaggedItemInline(generic.GenericTabularInline):
#     model = TaggedItem

class ContactAdmin(admin.ModelAdmin):
	list_display = ('last_name', 'first_name', 'title', 'role', 'listing_rank')
	list_filter = ['role',]
	list_editable = ['role', 'title', 'listing_rank']	
	list_per_page = 200
	search_fields = ['last_name', 'first_name', 'role']
	ordering = ['listing_rank']

class ProjectAdmin(admin.ModelAdmin):
	list_display = ('getuid', 'project_number', 'title', 'featured', 'featured_rank', 'headline', 'image')
	list_filter = ['featured', 'headline']
	list_editable = ['featured', 'featured_rank', 'headline']
	list_per_page = 200
	search_fields = ['project_number', 'title']
	ordering = ['-project_number']

class PublicationAdmin(admin.ModelAdmin):
	list_display = ('getuid', 'item_number', 'category', 'title', 'featured', 'featured_rank', 'image',)
	list_filter = ['featured', 'category']
	list_editable = ['featured', 'featured_rank', 'image']
	list_per_page = 200
	search_fields = ['item_number', 'title']
	ordering = ['item_number', '-year']

class ProdevAdmin(admin.ModelAdmin):
	list_display = ('getuid', 'id', 'title', 'featured', 'featured_rank', 'headline', 'pdtype', 'image',)
	list_filter = ['featured', 'headline', 'pdtype']
	list_editable = ['featured', 'featured_rank', 'headline', 'pdtype']
	list_per_page = 200
	search_fields = ['id', 'title']
	ordering = ['-id', 'title']

class StoryPageAdmin(admin.ModelAdmin):
	list_display = ('getuid', 'id', 'title', 'featured', 'featured_rank', 'headline', 'image')
	list_filter = ['featured', 'headline',]
	list_editable = ['featured', 'featured_rank', 'headline']
	list_per_page = 200
	search_fields = ['id', 'title']
	ordering = ['id', 'title',]
	# inlines = [
 #        TaggedItemInline,
 #    ]

admin.site.register(Contact, ContactAdmin, Media = ExtraMedia)
admin.site.register(Project, ProjectAdmin, Media = ExtraMedia)
admin.site.register(Publication, PublicationAdmin, Media = ExtraMedia)
admin.site.register(Prodev, ProdevAdmin, Media = ExtraMedia)
admin.site.register(StoryPage, StoryPageAdmin, Media = ExtraMedia)
# admin.site.register(TaggedItem)
