from django.shortcuts import render, get_object_or_404
from .models import Contact
from django.core.paginator import Paginator
from django.http import Http404


def index(request):
    contacts = Contact.objects.order_by('first_name').filter(is_visible=True)
    paginator = Paginator(contacts, 20)

    page = request.GET.get('page')

    contacts = paginator.get_page(page)
    return render(request, 'contacts/index.html',
                  {'contacts': contacts})


def single_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)

    if not contact.is_visible:
        raise Http404()

    return render(request, 'contacts/single_contact.html', {
        'contact': contact
    })
