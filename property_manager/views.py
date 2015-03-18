from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from property_manager.forms import PropertyForm, LoginForm
from property_manager.models import Property
from django.contrib.gis.measure import D
from django.contrib.auth import (
    login, logout, authenticate
)
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def home(request):
    return render(request, 'property_manager/index.html', {})

@login_required
def add_property(request):
    if request.method == 'GET':
        form = PropertyForm()
    else:
        form = PropertyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, "property_manager/add_property.html", {'form': form})


@login_required
def edit_property(request, id):
    property = get_object_or_404(
        Property,
        pk=id
    )
    form = PropertyForm(instance=property)
    if request.method == 'POST':
        form = PropertyForm(request.POST, instance=property)
        if form.is_valid():
            form.save()
            return render(request, "property_manager/edit_property.html", {'form': form, 'property':property, 'saved': True})
    return render(request, "property_manager/edit_property.html", {'form': form, 'property':property})



def property_detail(request, id):
    property = get_object_or_404(
        Property,
        pk=id
    )

    ref_location = property.geom
    distance = 20000  # 20km
    near = Property.objects.filter(geom__distance_lte=(ref_location, D(m=distance))).exclude(id=property.id)
    return render(request, "property_manager/property_detail.html", {'property': property, 'near' : near})


def user_login(request):
    if request.user.is_anonymous():
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                username = request.POST['username']
                password = request.POST['password']
                # This authenticates the user
                user = authenticate(username=username, password=password)
                if user is not None:
                    if user.is_active:
                        # This logs him in
                        login(request, user)
                        return HttpResponseRedirect(request.GET.get('next', reverse('home')))

                return render(request, "property_manager/login.html", {'form': form, 'error':True})
            else:
                return render(request, "property_manager/login.html", {'form': form})
        else:
            form = LoginForm()
            return render(request, "property_manager/login.html", {'form': form})
    return HttpResponseRedirect(reverse('home'))

# User Logout View
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
