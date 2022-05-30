from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from volunteer.forms import VolunteerForm
from django.views import View
from volunteer.models import Volunteer
from django.views import generic


class VolunteerFormView(View):

    def get(self, request):
        volunteer_form = VolunteerForm()
        return render(request, 'volunteer/register.html', context={'volunteer_form': volunteer_form})

    def post(self, request):
        volunteer_form = VolunteerForm(request.POST)

        if volunteer_form.is_valid():
            Volunteer.objects.create(**volunteer_form.cleaned_data)
            return HttpResponseRedirect('/volunteers')

        return render(request, 'volunteer/register.html', context={'volunteer_form': volunteer_form})

class VolunteerListView(generic.ListView):
    model = Volunteer
    template_name = 'volunteer_list.html'
    context_object_name = 'volunteer_list'

class VolunteerDetailView(generic.DetailView):
    model = Volunteer
