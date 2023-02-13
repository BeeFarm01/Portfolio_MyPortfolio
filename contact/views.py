from django.shortcuts import render
from django.views.generic import CreateView
from .models import Contact
from .forms import ContactForm

# Create your views here.
class contactView(CreateView):
	form_class = ContactForm
	model = Contact
	queryset = Contact.objects.all()
	success_url = '/'
	template_name = 'contact.html'  

def contact(request, *args, **kwargs):
    data = request.POST
    form = ContactForm(data)
    if form.is_valid():
        form.save()

        Contact.objects.create(
            name = data.get('name'),
            email = data.get('email'),
            subjece = data.get('subject'),
            message = data.get('message'),
        )
        return render(request, 'index.html',)

    
