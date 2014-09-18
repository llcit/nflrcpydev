# views.py
from __future__ import unicode_literals
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from collections import OrderedDict
from itertools import chain
from operator import attrgetter

from django.db.models import Q
from django.utils.html import strip_tags

from nflrcapp.models import *


def home(request):
    featured1 = Publication.objects.filter(featured=True)
    featured2 = Project.objects.filter(featured=True)
    featured3 = Prodev.objects.filter(featured=True)
    featured4 = StoryPage.objects.filter(featured=True)
    featured = sorted(
        chain(featured1, featured2, featured3, featured4), key=attrgetter('featured_rank'))

    return render_to_response('index.html', {'featured': featured}, context_instance=RequestContext(request))


def about(request):
    kuleana_item = StoryPage.objects.filter(pk=1)
    history_item = StoryPage.objects.filter(pk=2)
    lrc_item = StoryPage.objects.filter(pk=3)
    menu_items = []
    menu_items.append(history_item[0])
    menu_items.append(kuleana_item[0])
    menu_items.append(lrc_item[0])

    staff = Contact.objects.filter(role='STAFF').order_by('listing_rank')
    collabs = Contact.objects.filter(role='COLLAB').order_by('listing_rank')
    advboard = Contact.objects.filter(role='ADVBOARD').order_by('listing_rank')
    return render_to_response('l2-about.html',
                              {'staff': staff,
                              'collabs': collabs,
                              'advboard': advboard,
                              'menu_items': menu_items},
                              context_instance=RequestContext(request))


def contact(request):
    staff = Contact.objects.filter(role='STAFF').order_by('listing_rank')
    collabs = Contact.objects.filter(role='COLLAB').order_by(
        'last_name').order_by('staff_role__list_rank')
    advboard = Contact.objects.filter(role='ADVBOARD').order_by('listing_rank')
    return render_to_response('l2-contact.html', {
        'staff': staff, 
        'collabs': collabs,
        'advboard': advboard
    }, context_instance=RequestContext(request))


def contactview(request, person):
    thehuman = Contact.objects.get(pk=person)
    return render_to_response('person-display.html', {
        'thehuman': thehuman
    }, context_instance=RequestContext(request))


def languages(request, tag):
    language_list = [
        'Austronesian', 'Czech', 'Danish', 'East Asian', 'English', 'French', 'German', 'Hawaiian', 'HCE', 'Hindi', 'Icelandic', 'Ilokano', 'Indonesian', 'Italian', 'Kiswahili',
         'Malay', 'Manchu', 'Maori', 'Middle East', 'Muang', 'Pacific Islands', 'Persian', 'Pingelapese', 'Russian', 'Russian', 'Southeast Asian ', 'Spanish', 'Swahili', 'Tagalog', 'Thai', 'Tongan', 'Vietnamese']
    if tag:
        publications = Publication.objects.filter(
            language__icontains=tag).order_by('-year')
        projects = Project.objects.filter(
            language__icontains=tag).order_by('-id')
        prodevs = Prodev.objects.filter(
            language__icontains=tag).order_by('-id')

        return render_to_response('l2-languages.html', {
            'language_name': tag,
            'publications': publications,
            'projects': projects,
            'prodevs': prodevs,
            'language_list': language_list
        }, context_instance=RequestContext(request))

    # Even though the Publication class is listed here, the query produces
    # featured items from all types.
    featured = Publication.objects.allfeatured()

    # Faster if request is language specific.
    return render_to_response('l2-languages.html',
                              {'featured': featured, 'language_list': language_list}, context_instance=RequestContext(request))


def prodev(request, tag):
    if tag:
        listing = Prodev.objects.filter(pdtype__icontains=tag).order_by('-id')
        if not listing:
            tag = ''
    else:
        listing = None

    featured = Prodev.objects.filter(featured=True).order_by('featured_rank')
            # listing = Prodev.objects.filter().order_by('pdtype', '-id')

    return render_to_response('l2-events.html', {
        'events': listing,
        'featured': featured,
        'pdtype_tag': tag
    }, context_instance=RequestContext(request))


def workshop_conf(request):
    listing = Prodev.objects.filter().order_by('-id', 'pdtype')
    featured = listing.filter(featured=True)
    return render_to_response('l2-workshop-confs.html', {
        'events': listing,
        'featured': featured
    }, context_instance=RequestContext(request))


def prodevview(request, item):
    try:
        displayitem = Prodev.objects.get(pk=item)
        language_list = displayitem.language.split(',')
    except ObjectDoesNotExist:
        raise Http404
    except ValueError:
        raise Http404

    return render_to_response('item-display.html', {
        'item': displayitem,
        'shortcuts': ITEM_TYPE_SHORTCUTS,
        'language_list': language_list
    }, context_instance=RequestContext(request))


def projects(request, tag):
    prebuilt_filter = None
    if tag:
        if tag == 'current':
            prebuilt_filter = '2010-2014'
        elif tag == '2006-2010':
            prebuilt_filter = tag
        elif tag == '2002-2006':
            prebuilt_filter = tag
        elif tag == '1999-2002':
            prebuilt_filter = tag
        elif tag == '1996-1999':
            prebuilt_filter = tag
        elif tag == '1993-1996':
            prebuilt_filter = tag

        if prebuilt_filter:
            listing = Project.objects.filter(grant_cycle=prebuilt_filter)

        else:
            if tag == 'online-learning':
                tag = 'online learning'

            item_type = ContentType.objects.get_for_model(Project)
            tagged_items = TaggedItem.objects.filter(content_type=item_type).filter(
                item_tag__tag=tag).order_by('-object_id')
            listing = []
            for i in tagged_items:
                listing.append(i.content_object)
    else:
        # No tag -- show all projects
        tag = None
        listing = Project.objects.all().order_by('-grant_cycle')

    return render_to_response('l2-projects.html', {
        'items': listing,
        'subpage': tag
    }, context_instance=RequestContext(request))


def projectview(request, item):
    # listing = Project.objects.filter(project_number=item)
    # people = PersonProject.objects.filter(project_number=tag).select_related('contact_id')


    try:
        displayitem = Project.objects.get(project_number=item)
        language_list = displayitem.language.split(',')
    except ObjectDoesNotExist:
        raise Http404
    except ValueError:
        raise Http404

    return render_to_response('item-display.html', {
        'item': displayitem,
        'shortcuts': ITEM_TYPE_SHORTCUTS,
        'tags': displayitem.tags.all(),
        'language_list': language_list
    }, context_instance=RequestContext(request))


def publications(request, tag):
    featured = Publication.objects.filter(featured=1)

    
    # Prebuilt queries on publication categories
    if tag == 'digital-archives':
        listing = Publication.objects.filter(
            Q(category='Research Note') | Q(category='Network')).order_by('-year')
    elif tag == 'monographs':
        listing = Publication.objects.filter(category='NFLRC Monograph')
    elif tag == 'journals':
        listing = Publication.objects.filter(category='Journal')
    elif tag == 'teaching-materials':
        listing = Publication.objects.filter(
            category='Language Teaching Material')
    elif tag == 'research-notes':
        listing = Publication.objects.filter(category='Research Note')
    elif tag == 'pragmatics':
        listing = Publication.objects.filter(category__startswith='Pragmatics')
    elif tag == 'networks':
        listing = Publication.objects.filter(category='Network')
    elif tag == 'media':
        listing = Publication.objects.filter(
            Q(category='DVD') | Q(category='Videotape') | Q(category='CD'))
    ## First test of tag search
    elif tag == 'heritage':
        listing = Publication.objects.get_tagged_items(tag=tag, item_type='publication')
    elif tag == 'listing':
        listing = Publication.objects.all()
    else:
        tag = 'featured'
        listing = featured

    # listing = listing.order_by('category', '-year')

    return render_to_response('l2-publications.html', {
        'items': listing,
        'featured': featured,
        'subpage': tag
    }, context_instance=RequestContext(request))


def pubview(request, item):

    try:
        displayitem = Publication.objects.get(item_number=item)
        language_list = displayitem.language.split(',')
    except ObjectDoesNotExist:
        raise Http404
    except ValueError:
        raise Http404

    return render_to_response('item-display.html', {
        'item': displayitem,
        'shortcut': ITEM_TYPE_SHORTCUTS[displayitem.category],
        'language_list': language_list
    }, context_instance=RequestContext(request))


def search(request):
    query = request.GET['q']
    # Q(category='Research Note') | Q(category='Network')
    if query:
        publications = Publication.objects.filter(
            skeywords__icontains=query).order_by('-year')
        projects = Project.objects.filter(
            skeywords__icontains=query).order_by('-id')
        prodevs = Prodev.objects.filter(
            skeywords__icontains=query).order_by('-id')
        contacts = Contact.objects.filter(
              Q(last_name__icontains=query)
            | Q(first_name__icontains=query)
            | Q(email__icontains=query)
            ).order_by('last_name')

        return render_to_response('search-results.html', {
            'query': query,
            'publications': publications,
            'projects': projects,
            'prodevs': prodevs,
            'people': contacts,
        }, context_instance=RequestContext(request))

    return render_to_response('search-results.html', {}, context_instance=RequestContext(request))


def stories(request):
    listing = StoryPage.objects.all().order_by('title')
    featured = listing.filter(featured=1)

    return render_to_response('l2-stories.html', {
        'items': listing,
        'featured': featured,
    }, context_instance=RequestContext(request))


def storyview(request, item):
    # listing = Publication.objects.filter(item_number=item)
    displayitem = StoryPage.objects.get(id=item)
    # tags = displayitem.tags.all()
    # try:
    #
    # except ObjectDoesNotExist:
    #   raise Http404
    # except ValueError:
    #   raise Http404

    return render_to_response('item-display.html', {
        'item': displayitem,
    }, context_instance=RequestContext(request))
