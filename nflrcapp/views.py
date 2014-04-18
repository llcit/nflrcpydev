# views.py
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from itertools import chain

from django.db.models import Q


from nflrcapp.models import *


def home(request):
    featured1 = Publication.objects.filter(featured=True)
    featured2 = Project.objects.filter(featured=True)
    featured3 = Prodev.objects.filter(featured=True)
    featured4 = StoryPage.objects.filter(featured=True)
    featured = list(chain(featured1, featured2, featured3, featured4))

    headliner1 = Publication.objects.filter(headline=True)
    headliner2 = Project.objects.filter(headline=True)
    headliner3 = Prodev.objects.filter(headline=True)
    headliner4 = StoryPage.objects.filter(headline=True)
    headliners = list(chain(headliner1, headliner2, headliner3, headliner4))
    return render_to_response('index.html', {'headliners': headliners, 'featured': featured}, context_instance=RequestContext(request))


def about(request):
    staff = Contact.objects.filter(role='STAFF').order_by('listing_rank')
    collabs = Contact.objects.filter(role='COLLAB').order_by('listing_rank')
    advboard = Contact.objects.filter(role='ADVBOARD').order_by('listing_rank')
    return render_to_response('l2-about.html',
                              {'staff': staff, 'collabs':
                               collabs, 'advboard': advboard},
                              context_instance=RequestContext(request))


def contact(request):
    staff = Contact.objects.filter(role='STAFF').order_by('listing_rank')
    collabs = Contact.objects.filter(role='COLLAB').order_by('listing_rank')

    return render_to_response('l2-contact.html', {
        'staff': staff, 'collabs': collabs
    }, context_instance=RequestContext(request))


def contactview(request, person):
    thehuman = Contact.objects.get(pk=person)
    return render_to_response('person-display.html', {
        'thehuman': thehuman
    }, context_instance=RequestContext(request))


def journals(request):
    journals = Publication.objects.filter(item_number__in=['OJ01','OJ02','OJ03'])
    featured = journals.filter(featured=1)

    return render_to_response('l2-journals.html', {
        'journals': journals,
        'featured': featured
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

    # Faster if request is language specific.
    return render_to_response('l2-languages.html',
                              {}, context_instance=RequestContext(request))


def outreach(request):
    return render_to_response('index.html', {}, context_instance=RequestContext(request))


def prodev(request, tag):
    listing = Prodev.objects.all().order_by('-id')
    featured = listing.filter(featured=1)
    return render_to_response('l2-prodev.html', {
        'items': listing,
        'featured': featured,
        'subpage' : tag
    }, context_instance=RequestContext(request))


def prodevview(request, item):
    try:
        displayitem = Prodev.objects.get(pk=item)
    except ObjectDoesNotExist:
        raise Http404
    except ValueError:
        raise Http404

    return render_to_response('item-display.html', {
        'item': displayitem
    }, context_instance=RequestContext(request))


def projects(request, tag):
    listing = Project.objects.all().order_by('-id')
    featured = listing.filter(featured=True)
    return render_to_response('l2-projects.html', {
        'items': listing,
        'featured': featured,
        'subpage' : tag
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
        'item': displayitem
    }, context_instance=RequestContext(request))


def publications(request, tag):
    listing = ""
    # Built-in queries on publication categories
    if tag == 'monographs':
        listing = Publication.objects.filter(category='NFLRC Monograph')
    elif tag == 'teaching-materials':
        listing = Publication.objects.filter(
            category='Language Teaching Material')
    elif tag == 'research-notes':
        listing = Publication.objects.filter(category='Research Note')
    elif tag == 'pragmatics':
        listing = Publication.objects.filter(category__startswith='Pragmatics')
    elif tag == 'networks':
        listing = Publication.objects.filter(category='Network')
    elif tag == 'cd':
        listing = Publication.objects.filter(category='CD')
    elif tag == 'dvd':
        listing = Publication.objects.filter(category='DVD')
    elif tag == 'videotape':
        listing = Publication.objects.filter(category='Videotape')
    else:
        listing = Publication.objects.all()

    listing = listing.order_by('-year')

    featured = Publication.objects.filter(featured=True)

    return render_to_response('l2-publications.html', {
        'items': listing,
        'featured': featured,
        'subpage' : tag
    }, context_instance=RequestContext(request))


def pubview(request, item):
    # listing = Publication.objects.filter(item_number=item)
    displayitem = Publication.objects.get(item_number=item)
    # try:
    #
    # except ObjectDoesNotExist:
    # 	raise Http404
    # except ValueError:
    # 	raise Http404

    return render_to_response('item-display.html', {
        'item': displayitem
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


def search(request, query):
    if query:
        publications = Publication.objects.filter(
            skeywords__icontains=query).order_by('-year')
        projects = Project.objects.filter(
            skeywords__icontains=query).order_by('-id')
        prodevs = Prodev.objects.filter(
            skeywords__icontains=query).order_by('-id')

        return render_to_response('search.html', {
            'publications': publications,
            'projects': projects,
            'prodevs': prodevs,
        }, context_instance=RequestContext(request))

    return render_to_response('search.html', {}, context_instance=RequestContext(request))


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


def storyview(request, item):
    # listing = Publication.objects.filter(item_number=item)
    displayitem = StoryPage.objects.get(id=item)
    # try:
    #
    # except ObjectDoesNotExist:
    # 	raise Http404
    # except ValueError:
    # 	raise Http404

    return render_to_response('item-display.html', {
        'item': displayitem
    }, context_instance=RequestContext(request))


def workshop_conf(request):
    listing = Prodev.objects.filter().order_by('pdtype', 'date')
    featured = listing.filter(featured=True)
    return render_to_response('l2-workshop-confs.html', {
        'events': listing,
        'featured': featured
        }, context_instance=RequestContext(request))
