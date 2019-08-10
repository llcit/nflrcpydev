# views.py
from __future__ import unicode_literals

import os
from itertools import chain
from urllib import urlencode
from operator import attrgetter

from django.conf import settings

from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.http import Http404, JsonResponse, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.contrib import messages
from django.shortcuts import render_to_response, redirect, get_object_or_404

from haystack.generic_views import SearchView
from sendfile import sendfile

from nflrcapp.models import *

grant_cycle_map = {'current':'2018-2022','2018-2022':'2018-2022', '2014-2018':'2014-2018', '2010-2014':'2010-2014','2006-2010':'2006-2010','2002-2006':'2002-2006','1999-2002':'1999-2002','1996-1999':'1996-1999','1993-1996':'1993-1996'}

def generate_search_query_url(qstring):
    queryparams = '?'+urlencode({'q': qstring})
    search_url = reverse('search_haystack')+queryparams
    return search_url

def cfm_global_handler(request, cfmtoken):
    """
        This view handles requests for older coldfusion request urls.
        E.g., /nnnn.cfm. Some requests are manually rerouted to their equivalent page
        on this site. Anything else is sent as a query to the search index.
    """

    if cfmtoken == 'aboutus':
        return redirect('about_index')

    elif cfmtoken == 'oj':
        return redirect(reverse('publications', args=['journals']))

    elif cfmtoken == 'projects':
        return redirect('projects_index')

    elif cfmtoken == 'publications':
        return redirect('publications_index')

    elif cfmtoken == 'prodev':
        return redirect('events_index')

    return redirect(generate_search_query_url(cfmtoken))

def cfm_publication_handler(request):
    """
        Handles requests from old coldfusion url queries.
        Example case:
        /get_publication.cfm?id=303&amp;scriptname=searchsite_pub&amp;keyword=MG09&amp;display_order=alphabetic
        will reroute to publications/view/MG09
    """

    item_key = request.GET.get('keyword', None)
    if item_key:
        #  First to retrieve object from keyword (e.g. MG09)
        try:
            Publication.objects.get(item_number=item_key)
            return redirect('pubview', item=item_key)

        #   Object does not exist force a search using keyword as query
        except ObjectDoesNotExist:
            return redirect(generate_search_query_url(item_key))

        #   Any other problems just show the search page.
        except:
            pass
    """ TODO: write a message about this to display in template """
    # msg = 'Sorry, but we could not find the resource you were requesting. Please try our search index!'
    # messages.add_message(request, messages.INFO, msg)
    return redirect('search_haystack')

def cfm_searchsite_handler(request):
    """
        Handles requests from old coldfusion url queries.
        Example case:
        /searchsite_pub.cfm?display_order=author&keyword=rshrp
        will reroute to search index for querying
    """
    item_key = request.GET.get('keyword', None)
    if item_key:
        try:
            return redirect(generate_search_query_url(item_key))
        except:
            pass
    """ TODO: write a message about this to display in template """
    return redirect('search_haystack')

def cfm_project_handler(request):
    try:

        item_key = request.GET.get('project_number', None)

        return redirect('projectview', item=item_key)  # Story page id for staffdocs index
    except:
        pass

    return render_to_response('index.html', {'featured': []}, context_instance=RequestContext(request))

@login_required
def nflrcprivate(request, f):
    priv_path = os.path.join(settings.SENDFILE_ROOT, f)
    return sendfile(request, priv_path)

def auth_download(request):
    if not download.is_user_allowed(request.user):
        return HttpResponseForbidden('Sorry, you cannot access this file')
    return sendfile(request, download.file.path)

def home(request):
    featured1 = Publication.objects.filter(featured=True)
    featured2 = Project.objects.filter(featured=True)
    featured3 = Prodev.objects.filter(featured=True)
    featured4 = StoryPage.objects.filter(featured=True)
    featured = sorted(
        chain(featured1, featured2, featured3, featured4), key=attrgetter('featured_rank'))

    return render_to_response('index.html', {'featured': featured}, context_instance=RequestContext(request))

def site_filter(request, tag):
    """View that filters all objects by querying the TaggedItem table"""
    if tag:
        tagged_items = TaggedItem.objects.filter(item_tag__tag=tag)
        listing = [t.content_object for t in tagged_items]
        # sort by featured(True/False) descending then by featured_rank ascending.
        # Do two sorts in reverse to get the above effect.
        # https://docs.python.org/2/howto/sorting.html#sortinghowto
        listing = sorted(listing, key=attrgetter('featured_rank'))  # sort by featured_rank
        listing = sorted(listing, key=attrgetter('featured'), reverse=True)  # then by True/False

        if not listing:
            return redirect(generate_search_query_url(tag))
    else:
        # No tag -- show all projects
        tag = None
        listing = None

    return render_to_response('index.html', {
        'featured': listing,
        'subpage': tag
    }, context_instance=RequestContext(request))

def home_prototype(request):
    featured1 = Publication.objects.filter(featured=True)
    featured2 = Project.objects.filter(featured=True)
    featured3 = Prodev.objects.filter(featured=True)
    featured4 = StoryPage.objects.filter(featured=True)
    featured = sorted(
        chain(featured3, featured4, featured2, featured1), key=attrgetter('featured_rank'))
    feature_flash = featured[0]
    featured = featured[1:]
    feature_sticky = featured[-3:] # last three ranked
    featured = featured[:-3] # all but last three


    return render_to_response('index-prototype.html', {'featured': featured, 'feature_flash': feature_flash, 'feature_sticky': feature_sticky}, context_instance=RequestContext(request))

@login_required
def staffdocs(request):
    return redirect('staffdocsview', item=8)  # Story page id for staffdocs index

def about(request):
    kuleana_item = StoryPage.objects.filter(pk=1)
    history_item = StoryPage.objects.filter(pk=2)
    lrc_item = StoryPage.objects.filter(pk=3)

    menu_items = []
    try:
        menu_items.append(history_item[0])
        menu_items.append(kuleana_item[0])
        menu_items.append(lrc_item[0])
    except:
        pass

    staff = Contact.objects.filter(role='STAFF').order_by('listing_rank')
    collabs = Contact.objects.filter(role='COLLAB').order_by('last_name')
    advboard = Contact.objects.filter(role='ADVBOARD').order_by('last_name')
    return render_to_response('l2-about.html',
                              {'staff': staff,
                              'collabs': collabs,
                              'advboard': advboard,
                              'menu_items': menu_items},
                              context_instance=RequestContext(request))

def aboutview(request, item):
    displayitem = StoryPage.objects.get(id=item)
    if displayitem.private:
        return redirect('staffdocsview', item=displayitem.id)

    return render_to_response('item-display.html', {
        'item': displayitem,
    }, context_instance=RequestContext(request))

@login_required
def privateview(request, item):
    displayitem = StoryPage.objects.get(id=item)

    return render_to_response('item-display.html', {
        'item': displayitem,
    }, context_instance=RequestContext(request))

def contact(request):
    staff = Contact.objects.filter(role='STAFF').order_by('listing_rank')
    collabs = Contact.objects.filter(role='COLLAB').order_by('last_name')
    advboard = Contact.objects.filter(role='ADVBOARD').order_by('last_name')
    return render_to_response('l2-contact.html', {
        'staff': staff,
        'collabs': collabs,
        'advboard': advboard
    }, context_instance=RequestContext(request))

def contactview(request, person):
    # thehuman = Contact.objects.get(pk=person)
    thehuman = get_object_or_404(Contact, pk=person)

    return render_to_response('person-display.html', {
        'thehuman': thehuman
    }, context_instance=RequestContext(request))

def languages(request, tag='featured'):
    tag = tag.replace('-', ' ')
    language_list = [
        'Austronesian', 'Czech', 'Danish', 'East Asian', 'English', 'French', 'German', 'Hawaiian', 'HCE', 'Hindi', 'Icelandic', 'Ilokano', 'Indonesian', 'Italian', 'Kiswahili',
         'Malay', 'Manchu', 'Maori', 'Middle East', 'Muang', 'Pacific Islands', 'Persian', 'Pingelapese', 'Russian', 'Russian', 'Southeast Asian ', 'Spanish', 'Swahili', 'Tagalog', 'Thai', 'Tongan', 'Vietnamese']
    if tag != 'featured':
        publications = Publication.objects.filter(language__icontains=tag).order_by('-year')
        projects = Project.objects.filter(language__icontains=tag).order_by('-id')
        prodevs = Prodev.objects.filter(language__icontains=tag).order_by('-id')

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
    return render_to_response('l2-languages.html', {
            'featured': featured,
            'language_list': language_list,
        }, context_instance=RequestContext(request))

def prodev(request, tag=None):
    featured = None
    if tag:
        listing = Prodev.objects.filter(pdtype__icontains=tag).order_by('featured_rank', 'listing_rank')
        if not listing: # Retrieve items by tag
            listing = Prodev.objects.get_tagged_items(tag=tag, item_type='prodev')
    else:
        tag = 'upcoming'
        listing = Prodev.objects.get_tagged_items(tag=tag, item_type='prodev')
        # featured = Prodev.objects.filter(featured=True).order_by('featured_rank')

    return render_to_response('l2-events.html', {
        'events': listing,
        # 'featured': featured,
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

def projects(request, tag=None):
    """This view will accept a parameter (tag) that will filter on grant cycle or a any given tag.
    """
    
    if tag: # A tag is provided in the request url
        grant_cycle_tag = grant_cycle_map.get(tag)
        if grant_cycle_tag:
            listing = Project.objects.filter(grant_cycle__contains=grant_cycle_tag).order_by('featured_rank', 'listing_rank', '-grant_cycle')

        else: # Some other tag was submitted - query over tagged items for this type of content.
            item_type = ContentType.objects.get_for_model(Project)
            tagged_items = TaggedItem.objects.filter(content_type=item_type).filter(item_tag__tag=tag).order_by('-object_id')
            listing = [i.content_object for i in tagged_items]
    else:
        # No tag -- show all projects
        listing = Project.objects.all().order_by('-grant_cycle', 'listing_rank')
    
    
    return render_to_response('l2-projects.html', {
        'items': listing,
        'subpage': tag
    }, context_instance=RequestContext(request))

def projectview(request, item):
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

def publications(request, tag='featured'):
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

# See production settings file for additional info on setup.
class SearchHaystackView(SearchView):
    def get_queryset(self):
        queryset = super(SearchHaystackView, self).get_queryset()
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super(SearchHaystackView, self).get_context_data(*args, **kwargs)
        results = context['object_list']

        storage = messages.get_messages(self.request)
        context['searchmessages'] = []
        for message in storage:
            context['searchmessages'].append(message)

        context['people'] = [r for r in results if r.model_name == 'contact']
        context['stories'] = [r for r in results if r.model_name == 'storypage']
        context['publications'] = [r for r in results if r.model_name == 'publication']
        context['projects'] = [r for r in results if r.model_name == 'project']
        context['prodevs'] = [r for r in results if r.model_name == 'prodev']

        return context

# This brute force search view was deprecated in favor of the Haystack implementation for more comprehensive indexing.
def search(request):
    query = request.GET['q']

    if query:
        publications = Publication.objects.filter(
            Q(author__icontains=query) | Q(description__icontains=query) | Q(skeywords__icontains=query)
            ).order_by('-year')

        projects = Project.objects.filter(
            Q(description__icontains=query) | Q(skeywords__icontains=query)
            ).order_by('-id')
        prodevs = Prodev.objects.filter(
            Q(description__icontains=query) | Q(skeywords__icontains=query)
            ).order_by('-id')
        contacts = Contact.objects.filter(
              Q(last_name__icontains=query)
            | Q(first_name__icontains=query)
            | Q(email__icontains=query)
            ).order_by('last_name')
        stories = StoryPage.objects.filter(
            Q(description__icontains=query) | Q(title__icontains=query)
            ).order_by('title')

        return render_to_response('search-results.html', {
            'query': query,
            'publications': publications,
            'projects': projects,
            'prodevs': prodevs,
            'people': contacts,
            'stories': stories,
        }, context_instance=RequestContext(request))

    return render_to_response('search-results.html', {}, context_instance=RequestContext(request))

@login_required
def curator_view(request):        
    return render_to_response(
        'l2-curator.html', 
        {'featured': aggit(), }, 
        context_instance=RequestContext(request))

@login_required
def curator_update_rank_view(request):
    if request.method == 'POST':
        data = request.POST
        for key, rank in data.items():
            if key != 'csrfmiddlewaretoken':
                d = key.split('.')
                obj_nm = d[0]
                obj_pk = d[1]

                if obj_nm == 'projects':
                    obj = Project.objects.get(pk=obj_pk)
                elif obj_nm == 'prodev':
                    obj = Prodev.objects.get(pk=obj_pk)
                elif obj_nm == 'about':
                    obj = StoryPage.objects.get(pk=obj_pk)
                else:
                    obj = Publication.objects.get(pk=obj_pk)
                obj.featured_rank = rank
                obj.save()
    return HttpResponseRedirect(reverse('curator'))

def aggit():
    featured1 = Publication.objects.filter(featured=True)
    featured2 = Project.objects.filter(featured=True)
    featured3 = Prodev.objects.filter(featured=True)
    featured4 = StoryPage.objects.filter(featured=True)
    featured = sorted(
        chain(featured1, featured2, featured3, featured4), key=attrgetter('featured_rank'))
    
    return featured
