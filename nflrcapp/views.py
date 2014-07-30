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
    menu_items = []
    menu_items.append(history_item[0])
    menu_items.append(kuleana_item[0])

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
    collabs = Contact.objects.filter(role='COLLAB').order_by('last_name').order_by('-staff_role')
    return render_to_response('l2-contact.html', {
        'staff': staff, 'collabs': collabs
    }, context_instance=RequestContext(request))


def contactview(request, person):
    thehuman = Contact.objects.get(pk=person)
    return render_to_response('person-display.html', {
        'thehuman': thehuman
    }, context_instance=RequestContext(request))


def languages(request, tag):
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
        }, context_instance=RequestContext(request))

    featured = Publication.objects.allfeatured()

    # Faster if request is language specific.
    return render_to_response('l2-languages.html',
                              {'featured': featured}, context_instance=RequestContext(request))


def outreach(request):
    return render_to_response('index.html', {}, context_instance=RequestContext(request))


def prodev(request, tag):
    if tag:
        listing = Prodev.objects.filter(pdtype__icontains=tag).order_by('-id')
        if not listing:
            tag = ''
    else:
        listing= None

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
    except ObjectDoesNotExist:
        raise Http404
    except ValueError:
        raise Http404

    return render_to_response('item-display.html', {
        'item': displayitem,
        'shortcuts': ITEM_TYPE_SHORTCUTS
    }, context_instance=RequestContext(request))


def projects(request, tag):
    listing = Project.objects.all().order_by('-id')
    featured = listing.filter(featured=True)
    return render_to_response('l2-projects.html', {
        'items': listing,
        'featured': featured,
        'subpage': tag
    }, context_instance=RequestContext(request))


def projectview(request, item):
    # listing = Project.objects.filter(project_number=item)
    # people = PersonProject.objects.filter(project_number=tag).select_related('contact_id')
    try:
        displayitem = Project.objects.get(project_number=item)
    except ObjectDoesNotExist:
        raise Http404
    except ValueError:
        raise Http404

    return render_to_response('item-display.html', {
        'item': displayitem,
        'shortcuts': ITEM_TYPE_SHORTCUTS
    }, context_instance=RequestContext(request))


def publications(request, tag):
    featured = Publication.objects.filter(featured=1)
    listing = ""
    # Built-in queries on publication categories
    if tag == 'monographs':
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
    elif tag == 'listing':
        listing = Publication.objects.all()
    else:
        listing = featured

    listing = listing.order_by('category', '-year')

    return render_to_response('l2-publications.html', {
        'items': listing,
        'featured': featured,
        'subpage': tag
    }, context_instance=RequestContext(request))


def pubview(request, item):
    
    try:
        displayitem = Publication.objects.get(item_number=item)
    except ObjectDoesNotExist:
      raise Http404
    except ValueError:
      raise Http404

    return render_to_response('item-display.html', {
        'item': displayitem,
        'shortcut': ITEM_TYPE_SHORTCUTS[displayitem.category]
    }, context_instance=RequestContext(request))


def resources(request, tag):
    if tag:
        listing = Resource.objects.filter(resource_number=tag)
        return render_to_response('item-view.html',
                                  {'resources': listing},
                                  context_instance=RequestContext(request))

    listing = Resource.objects.all()
    return render_to_response('item-listing.html', {
        'items': listing,
        'item_type': 'resources'
    }, context_instance=RequestContext(request))


def search(request):
    query = request.GET['q']
    if query:
        publications = Publication.objects.filter(
            skeywords__icontains=query).order_by('-year')
        projects = Project.objects.filter(
            skeywords__icontains=query).order_by('-id')
        prodevs = Prodev.objects.filter(
            skeywords__icontains=query).order_by('-id')
        contacts = Contact.objects.filter(
            last_name__icontains=query).order_by('last_name')

        return render_to_response('search-results.html', {
            'query': query,
            'publications': publications,
            'projects': projects,
            'prodevs': prodevs,
            'people': contacts,
        }, context_instance=RequestContext(request))

    return render_to_response('search-results.html', {}, context_instance=RequestContext(request))


def software(request, tag):
    if tag:
        listing = Software.objects.filter(pk=tag)
        return render_to_response('item-view.html', {
            'software': listing
        }, context_instance=RequestContext(request))

    listing = Software.objects.all()
    return render_to_response('item-listing.html', {
        'items': listing,
        'item_type': 'software'
    }, context_instance=RequestContext(request))

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







# Use this stub to run development changes...
def dev_utility(request):
#     imgs = ["CD02","CD07","CD08","DVD01","DVD02","DVD03","KP01","KPiconTEMPLATE.png","LT03","LT09","LT25","LT25r","LT25t","LT26","LT28","LT29icon.jpg","LT30","LT31","LT31r","LT31t","LT33","LT34","LT34lg.png","LT34sm.png","LT35","LT36icon.jpg","LT36","LT38","LT3icon.jpg","LT40icon.jpg","LT40","LT41icon.jpg","LT41","MG00icon.jpg","MG00","MG01","MG02","MG03","MG04","MG05","MG06","MG07","MG09","MG09lg.png","MG0x","MI07icon.jpg","MI08","NW00","OJ01","OJ01lg.png","OJ01sm.png","OJ02","OJ03","PI01","PI02","PI03","PLL11","PLL12","PLL13","PROJECTSplaceholder","RN14","RN21","RN33","RN34","RN35","RN36","RN37","RN38","RN39","RN40","RN41","RN42","RN43","RN44","RN46","RN47","RN48","RN49","RN50x","RN51","TR05","TR06","TR07","TR08","TR09","TR10","TR11","TR12","TR13","TR14","TR15","TR16","TR17","TR18","TR19","TR20","TR21","TR22","TR23","TR24","TR25","TR26","VD03","VD04","VD05","VD06","VD07","VD08","VD09","VD10","VD11","VD12","VD14","VD15","VD16.png","VD17","VD18","VD19","VD20","VD21","VD22","VD23","VD24","VD25","WORKSHOPS-CONFERENCESplaceholder","XLT03-2icon.jpg","XLT03-2","XLT03icon.jpg","XLT03"
#     ]

    objs = Publication.objects.all()
    for i in objs:
        data = strip_tags(i.description)
        trimmed = (data[:137] + '...') if len(data) > 137 else data
        i.thumbnail_desc = trimmed
        i.save()

    objs = Prodev.objects.all()
    for i in objs:
        data = strip_tags(i.description)
        trimmed = (data[:137] + '...') if len(data) > 137 else data
        i.thumbnail_desc = trimmed
        i.save()

    objs = Project.objects.all()
    for i in objs:
        data = strip_tags(i.description)
        trimmed = (data[:137] + '...') if len(data) > 137 else data
        i.thumbnail_desc = trimmed
        i.save()
#     for i in objs:
#         if i.getuid() in imgs:
#             i.image = i.getuid() + 'icon.png'
#         else:
#             i.image = 'icon.png'
        
#         i.save()

#     objs = Project.objects.all()
#     for i in objs:
#         i.image = 'PROJECTSplaceholderIcon.png'
#         i.save()

#     objs = Prodev.objects.all()
#     for i in objs:
#         i.image = 'WORKSHOPS-CONFERENCESplaceholderIcon.png'
#         i.save()


    return render_to_response('index.html', {}, context_instance=RequestContext(request))
