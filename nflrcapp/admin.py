from django.contrib import admin
from django.contrib.contenttypes import generic

from nflrcapp.models import Contact, ContactRole, Project, Publication, Prodev, StoryPage, ItemTag, TaggedItem
from badge_site.models import Issuer, Badge, Award, Revocation
from badge_site.utils import genGuid, getRandomString



class ExtraMedia:
    js = [
        '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
        '/static/js/tinymce_setup.js',
    ]

# class ProjectAdminForm(forms.ModelForm):
#     class Meta:
#         model = Project

#         widgets = {
#             'director': forms.TextInput(attrs={'class': 'vTextField'})
#         }

class TaggedItemInline(generic.GenericTabularInline):
    model = TaggedItem

class ContactRoleAdmin(admin.ModelAdmin):
	list_display = ('id', 'list_rank', 'title')
	list_filter = ['title',]
	list_editable = ['list_rank','title']
	list_per_page = 200
	ordering = ['list_rank']

class ContactAdmin(admin.ModelAdmin):
	list_display = ('last_name', 'first_name', 'title', 'role', 'staff_role', 'listing_rank', 'image')
	list_filter = ['role',]
	list_editable = ['role', 'staff_role', 'listing_rank', 'image']
	list_per_page = 200
	search_fields = ['last_name', 'first_name', 'role', 'bio']
	ordering = ['listing_rank']
	inlines = [
        TaggedItemInline,
    ]

class ProjectAdmin(admin.ModelAdmin):
	# form = ProjectAdminForm
	list_display = ('getuid', 'project_number', 'grant_cycle', 'title', 'director', 'language', 'featured', 'featured_rank', 'headline', 'image')
	list_filter = ['featured', 'headline']
	list_editable = ['featured', 'featured_rank', 'headline']
	list_per_page = 200
	search_fields = ['project_number', 'title', 'language', 'thumbnail_desc', 'description']
	ordering = ['-project_number']
	inlines = [
        TaggedItemInline,
    ]

class PublicationAdmin(admin.ModelAdmin):
	list_display = ('getuid', 'item_number', 'category', 'title', 'description', 'language', 'featured', 'featured_rank', 'image')
	list_filter = ['featured', 'category']
	list_editable = ['featured', 'featured_rank', 'image']
	list_per_page = 200
	search_fields = ['item_number', 'title', 'language', 'thumbnail_desc', 'description']
	ordering = ['item_number', '-year']
	inlines = [
        TaggedItemInline,
    ]

class ProdevAdmin(admin.ModelAdmin):
	list_display = ('getuid', 'id', 'title', 'description', 'language', 'featured', 'featured_rank', 'headline', 'pdtype', 'image',)
	list_filter = ['featured', 'headline', 'pdtype']
	list_editable = ['featured', 'featured_rank', 'headline', 'pdtype']
	list_per_page = 200
	search_fields = ['id', 'title','language', 'thumbnail_desc', 'description']
	ordering = ['-id', 'title']
	inlines = [
        TaggedItemInline,
    ]

class StoryPageAdmin(admin.ModelAdmin):
	list_display = ('getuid', 'id', 'title', 'featured', 'featured_rank', 'headline', 'image' )
	list_filter = ['featured', 'headline',]
	list_editable = ['featured', 'featured_rank', 'headline']
	list_per_page = 200
	search_fields = ['id', 'title', 'thumbnail_desc', 'description']
	ordering = ['id', 'title',]
	inlines = [
        TaggedItemInline,
    ]


class IssuerAdmin(admin.ModelAdmin):
	list_display = ('initials', 'name', 'contact', 'jsonfile')
	list_filter = ['initials']
	readonly_fields = ('guid', 'jsonfile')

	# Override: Save the object, then over/write json file.
	def save_model(self, request, obj, form, change):
		if not change:
			# Set a one-time unique id
			obj.guid = genGuid()
			# Set url to the json file on intialization (first save)
			obj.jsonfile = obj.getIssuerUrl()

		obj.save()
		obj.writeIssuerFile()

class BadgeAdmin(admin.ModelAdmin):
	list_display = ('name', 'issuer', 'created', 'image', 'jsonfile', 'guid',)
	list_filter = ['issuer',]
	readonly_fields = ('guid','jsonfile')

	# Override: Save the object, then over/write json file.
	def save_model(self, request, obj, form, change):
		if not change:
			# Set a one-time unique id
			obj.guid = genGuid()
			# Set url to the json file on intialization (first save)
			obj.jsonfile = obj.getBadgeUrl()

		obj.save()
		obj.writeBadgeFile()

class AwardAdmin(admin.ModelAdmin):
	list_display = ('email', 'lastname', 'firstname', 'guid', 'badge', 'issuedOn', 'claimCode', 'jsonfile')
	list_filter = ['email', 'badge', 'badge__issuer']
	readonly_fields = ('guid', 'salt', 'claimCode', 'jsonfile')
	save_as = True

	# Override: Save the object, then over/write json file.
	def save_model(self, request, obj, form, change):
		if not change:
			# Set a one-time unique id, claimCode, and salt for this badge to random strings
			obj.guid = genGuid()
			obj.claimCode = getRandomString(size=10)
			obj.salt = getRandomString(size=10)
			obj.jsonfile = obj.getAssertionUrl()

		# Save the object, then over/write json file.
		obj.save()
		obj.writeAssertionFile()

	def delete_model(self, request, obj):
		obj.deleteAssertionFile()
		obj.delete()

admin.site.register(Contact, ContactAdmin, Media = ExtraMedia)
admin.site.register(ContactRole, ContactRoleAdmin)
admin.site.register(Project, ProjectAdmin, Media = ExtraMedia)
admin.site.register(Publication, PublicationAdmin, Media = ExtraMedia)
admin.site.register(Prodev, ProdevAdmin, Media = ExtraMedia)
admin.site.register(StoryPage, StoryPageAdmin, Media = ExtraMedia)
admin.site.register(ItemTag)
admin.site.register(TaggedItem)

admin.site.register(Issuer, IssuerAdmin)
admin.site.register(Badge, BadgeAdmin)
admin.site.register(Award, AwardAdmin)
admin.site.register(Revocation)
