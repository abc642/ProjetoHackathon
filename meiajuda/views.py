
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string

from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode
from .forms import SignUpForm
from .tokens import account_activation_token

from django.shortcuts import render, redirect, get_object_or_404

from .models import Person
from .forms import PersonForm


def sou_mei(request):
    return render(request,'soumei.html')

def persons_list(request):
    persons = Person.objects.all()
    return render(request, 'person.html', {'persons': persons})



def persons_new(request):
    form = PersonForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'person_form.html', {'form': form})



def persons_update(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)

    if form.is_valid():
        form.save()
        return redirect('person_list')

    return render(request, 'person_form.html', {'form': form})



def persons_delete(request, id):
    person = get_object_or_404(Person, pk=id)

    if request.method == 'POST':
        person.delete()
        return redirect('home')

    return render(request, 'person_delete_confirm.html', {'person': person})

'''cadastro'''

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            '''campos do formulario'''
            user = form.save()
            user.refresh_from_db()
            user.profile.first_name = form.cleaned_data.get('nome')
            user.profile.last_name = form.cleaned_data.get('sobrenome')
            user.profile.email = form.cleaned_data.get('email')
            # itens p/ anuncio

            # default False
            user.is_active = True
            user.save()
            current_site = get_current_site(request)
            subject = 'Por favor ative sua conta'
            '''
            message = render_to_string('home',{
                'user':user,
                'domain':current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject,message)'''
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request,'singup.html', {'form': form})

def activate(request,uidb64,token):
    try:
        uid = force_text(urlsafe_base64_encode(uidb64))
        user = User.objtects.get(pk=uid)
    except(TypeError,ValueError,OverflowError,User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user,token):
        user.is_active=True
        user.profile.signup_confirmation = True
        user.save()
        login(request,user)
        return redirect('')
    else:
        return render(request,'activation_invalid.html')

def activation_sent_view(request):
    return render(request,'activations/activation_sent.html')




'''onde tiver 'home' era activations/activation_sent.html '''



