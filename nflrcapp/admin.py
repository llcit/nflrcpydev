from django.contrib import admin
from django import forms
from django.contrib.contenttypes import generic
from nflrcapp.models import Contact, ContactRole, Project, Publication, Prodev, StoryPage, ItemTag, TaggedItem

class ExtraMedia:
    js = [
        '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
        '/static/js/tinymce_setup.js',
    ]

class ProjectAdminForm(forms.ModelForm):
    class Meta:
        model = Project
        widgets = {
            'director': forms.TextInput(attrs={'class': 'vTextField'})
        }

class TaggedItemInline(generic.GenericTabularInline):
    model = TaggedItem

class ContactRoleAdmin(admin.ModelAdmin):
	list_display = ('id', 'list_rank', 'title')
	list_filter = ['title',]
	list_editable = ['list_rank','title']	
	list_per_page = 200	
	ordering = ['list_rank']

class ContactAdmin(admin.ModelAdmin):
	list_display = ('last_name', 'first_name', 'title', 'role', 'staff_role', 'listing_rank', 'image',)
	list_filter = ['role',]
	list_editable = ['role', 'staff_role', 'listing_rank','image']	
	list_per_page = 200
	search_fields = ['last_name', 'first_name', 'role']
	ordering = ['listing_rank']
	inlines = [
        TaggedItemInline,
    ]

class ProjectAdmin(admin.ModelAdmin):
	form = ProjectAdminForm
	list_display = ('getuid', 'project_number', 'title', 'director', 'language', 'featured', 'featured_rank', 'headline', 'image', 'tags')
	list_filter = ['featured', 'headline']
	list_editable = ['featured', 'featured_rank', 'headline']
	list_per_page = 200
	search_fields = ['project_number', 'title']
	ordering = ['-project_number']
	inlines = [
        TaggedItemInline,
    ]

class PublicationAdmin(admin.ModelAdmin):
	list_display = ('getuid', 'item_number', 'category', 'title', 'language', 'featured', 'featured_rank', 'image',)
	list_filter = ['featured', 'category']
	list_editable = ['featured', 'featured_rank', 'image']
	list_per_page = 200
	search_fields = ['item_number', 'title']
	ordering = ['item_number', '-year']
	inlines = [
        TaggedItemInline,
    ]

class ProdevAdmin(admin.ModelAdmin):
	list_display = ('getuid', 'id', 'title', 'language', 'featured', 'featured_rank', 'headline', 'pdtype', 'image',)
	list_filter = ['featured', 'headline', 'pdtype']
	list_editable = ['featured', 'featured_rank', 'headline', 'pdtype']
	list_per_page = 200
	search_fields = ['id', 'title']
	ordering = ['-id', 'title']
	inlines = [
        TaggedItemInline,
    ]

class StoryPageAdmin(admin.ModelAdmin):
	list_display = ('getuid', 'id', 'title', 'featured', 'featured_rank', 'headline', 'image')
	list_filter = ['featured', 'headline',]
	list_editable = ['featured', 'featured_rank', 'headline']
	list_per_page = 200
	search_fields = ['id', 'title']
	ordering = ['id', 'title',]
	inlines = [
        TaggedItemInline,
    ]

admin.site.register(Contact, ContactAdmin, Media = ExtraMedia)
admin.site.register(ContactRole, ContactRoleAdmin)
admin.site.register(Project, ProjectAdmin, Media = ExtraMedia)
admin.site.register(Publication, PublicationAdmin, Media = ExtraMedia)
admin.site.register(Prodev, ProdevAdmin, Media = ExtraMedia)
admin.site.register(StoryPage, StoryPageAdmin, Media = ExtraMedia)
admin.site.register(ItemTag)
admin.site.register(TaggedItem)
