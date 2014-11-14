# Get or create a tag.
try:
	tag = ItemTag.objects.get(tag='summer-institute')
except ItemTag.DoesNotExist:
	tag = ItemTag(tag='summer-institute')
	tag.save()
	print 'new tag is ', tag

# get all prodev objects that currently have tag named 'institute':
ctype = ContentType.objects.get_for_model(Prodev)
institutes = TaggedItem.objects.filter(content_type__id=ctype.id).filter(item_tag__tag='institute')
# now add a new tag 'summer-institute' to each:
for i in institutes:
	tag = ItemTag.objects.get(tag='summer-institute')
	t = TaggedItem(content_object=i.content_object, item_tag=tag)
	t.save()

# Retrieve all prodev objects with a tag named 'summer-institute'
summers = TaggedItem.objects.filter(content_type__id=ctype.id).filter(item_tag__tag='summer-institute')


# Get all TaggedItems for an object:
event_item = Prodev.objects.get(pk=15)
tagged_items = event_item.tags.all()
for i in tagged_items:
	print i.content_object # the object instance
	print i.tag # the tag
