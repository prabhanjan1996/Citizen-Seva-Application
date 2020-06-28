from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse, redirect
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.http import HttpResponse, HttpResponseRedirect, request
from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, UpdateView
from django.views.generic import CreateView
from django_school.settings import EMAIL_HOST_USER
from citizen.forms import EmailForm, TalukaForms, HobaliForms, CircleForms, VillageCityForms, PoliceStationForms, \
    PartDetailsForms, PollingStationForms, ConstituencyTypeForms, ConstituencyForms, PressReportersForms, \
    PressReportersConstForms, PartyForms, MembersTypeForms, MembersForms, EventForms, ProjectsForms, PartyworkersForms, \
    CommitteeStructureForms, CommitteeForms, CommitteeMembersForms
from django.urls import reverse, reverse_lazy
from django.core.mail import send_mail
from django.conf import settings
import smtplib
from django.contrib import messages
from .forms import StateForms, DistrictForms, ContactForm
from .models import State, District, Taluka, Hobali, Circle, VillageCity, PoliceStation, PartDetails, PollingStation, \
    ConstituencyType, Constituency, PressReporters, PressReporterConstituency, PressReporterConstituency123, Party, \
    Party123, MembersType, Members, Events123, Event, Projects, PartyWorkers, CommitteeStructure, CommitteeStructure123, \
    Committee123, CommitteeMembers123

from classroom.models import  Quiz

from django.core.mail import send_mail, BadHeaderError

from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)


def admin_index(request):
    return render(request, 'citizen/index.html')


def about(request):
    return render(request, 'citizen/About.html')


def seen(request):
    if request.method == 'GET':
        return render(request, 'citizen/login.html')
    else:
        validate_user = authenticate(
            username=request.POST['username'],
            password=request.POST['password'])
        if validate_user:
            login(request, validate_user)
            return render(request, 'citizen/index.html')
        else:
            return render(request, 'citizen/login.html')


def index_contact(request):
    title = 'Contact Form'
    form = ContactForm(request.POST or None)
    confirm_message = None
    if form.is_valid():
        Email = form.cleaned_data['Email']
        Name = form.cleaned_data['Name']
        Comment = form.cleaned_data['Comment']
        subject = 'Message From Citizens'
        message = 'Message from :%s \n Citizen Name: %s \n Message: %s' % (Email, Name, Comment)
        emailFrom = form.cleaned_data['Email']
        emailTo = [settings.EMAIL_HOST_USER]
        send_mail(subject, message, emailFrom, emailTo, fail_silently=True)
        title = "Thanks!"
        confirm_message = " Thanks for message, will get back you."
        form = None

    context = {'title': title, 'form': form, 'confirm_message': confirm_message}
    template = 'citizen/Contacts.html'
    return render(request, template, context)


def HomePage(request):
    return render(request, "Email_Attachment.html")


def send_mail_plain_with_file(request):
    message = request.POST.get('message', '')
    subject = request.POST.get('subject', '')
    mail_id = request.POST.get('email', '')
    email = EmailMessage(subject, message, EMAIL_HOST_USER, [mail_id])
    email.content_subtype = 'html'

    file = request.FILES['file']
    email.attach(file.name, file.read(), file.content_type)

    email.send()
    return HttpResponse("Mail Sent Successfully")
    return render(request, "Email_Attachment.html")


def create_state(request):
    form = StateForms(request.POST)
    counts = State.objects.all().count()
    if form.is_valid():
        form.save()
        return redirect('citizen:create_state')
    return render(request, 'citizen/State.html',
                  {'form': form, 'counts': counts, 'users': State.objects.all().order_by('State')})


def edit_state(request, id):
    id = State.objects.get(id=id)
    form = StateForms(request.POST or None, instance=id)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('citizen:create_state'))
    return render(request, 'citizen/State.html', {'form': form,
                                                  'users': State.objects.all().order_by('State')})


def delete_state(request, id):
    user = State.objects.get(id=id)
    user.delete()
    return HttpResponseRedirect(reverse('citizen:create_state'))


def create_district(request):
    form = DistrictForms(request.POST)
    names1 = District.objects.all().count()
    if form.is_valid():
        form.save()
        return redirect('citizen:create_district')
    return render(request, 'citizen/District.html',
                  {'form': form, 'names1': names1, 'Dist': District.objects.all().order_by('Name')})


def update_district(request, id):
    id = District.objects.get(id=id)
    form = DistrictForms(request.POST or None, instance=id)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('citizen:create_district'))
    return render(request, 'citizen/District.html', {'form': form,
                                                     'Dist': District.objects.all().order_by('State', 'Code', 'Name')})


def delete_district(request, id):
    user = District.objects.get(id=id)
    user.delete()
    return HttpResponseRedirect(reverse('citizen:create_district'))


# def create_taluka(request):
#     form = TalukaForms(request.POST)
#
#     if form.is_valid():
#         form.save()
#         return redirect('create_taluka')
#     return render(request, 'citizen/Taluka.html',
#                   {'form': form, 'Taluk': Taluka.objects.all().order_by('State', 'District', 'Code', 'Name')})
#
#
# def update_taluka(request, id):
#     id = Taluka.objects.get(id=id)
#     form = TalukaForms(request.POST or None, instance=id)
#     if form.is_valid():
#         form.save()
#         return HttpResponseRedirect(reverse('create_taluka'))
#     return render(request, 'citizen/Taluka.html', {'form': form,
#                                                    'Taluk': Taluka.objects.all().order_by(
#                                                        'Name')})
#
#


def talukacreate(request):
    form = TalukaForms(request.POST)
    counts = Taluka.objects.all().count()
    if form.is_valid():
        form.save()
        return redirect('citizen:talukacreate')
    return render(request, 'citizen/Taluka_form.html',
                  {'form': form, 'counts': counts, 'taluks': Taluka.objects.all().order_by('Name')})


class TalukaUpdateView(UpdateView):
    model = Taluka
    form_class = TalukaForms
    success_url = reverse_lazy('citizen:talukacreate')


def delete_taluka(request, id):
    tl = Taluka.objects.get(id=id)
    tl.delete()
    return HttpResponseRedirect(reverse('citizen:talukacreate'))


def load_District(request):
    State_id = request.GET.get('State')
    Districts = District.objects.filter(State_id=State_id).order_by('State')
    return render(request, 'citizen/city_dropdown_list_options.html', {'District': Districts})


def hobalicreate(request):
    form = HobaliForms(request.POST)

    if form.is_valid():
        form.save()
        return redirect('citizen:hobalicreate')
    return render(request, 'citizen/Hobali_form.html',
                  {'form': form, 'hobali': Hobali.objects.all().order_by('Name')})


class HobaliUpdateView(UpdateView):
    model = Hobali
    form_class = HobaliForms
    template_name = 'citizen/Hobali_update.html'
    success_url = reverse_lazy('citizen:hobalicreate')


def delete_hobali(request, id):
    tl = Hobali.objects.get(id=id)
    tl.delete()
    return HttpResponseRedirect(reverse('citizen:hobalicreate'))


def load_Taluka(request):
    State_id = request.GET.get('State')
    District_id = request.GET.get('District')
    Districts = District.objects.filter(State_id=State_id).order_by('State')
    Talukas = Taluka.objects.filter(District_id=District_id).order_by('Name')
    context = {'District': Districts, 'Taluka': Talukas}
    return render(request, 'citizen/Taluka_dropdown_list_option.html', context)


def circlecreate(request):
    form = CircleForms(request.POST)

    if form.is_valid():
        form.save()
        return redirect('citizen:circlecreate')
    return render(request, 'citizen/Circle_form.html',
                  {'form': form, 'circle': Circle.objects.all().order_by('Name')})


def update_circle(request, id):
    context = {}

    obj = get_object_or_404(Circle, id=id)
    form = CircleForms(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/" + id)

        # add form dictionary to context
    context["form"] = form

    return HttpResponseRedirect(reverse('citizen:circlecreate'), context)


def delete_circle(request, id):
    tl = Circle.objects.get(id=id)
    tl.delete()
    return HttpResponseRedirect(reverse('citizen:circlecreate'))


def load_Hobali(request):
    State_id = request.GET.get('State')
    District_id = request.GET.get('District')
    Taluka_id = request.GET.get('Taluka')
    Districts = District.objects.filter(State_id=State_id).order_by('State')
    Talukas = Taluka.objects.filter(District_id=District_id).order_by('Name')
    Hobalis = Hobali.objects.filter(Taluka_id=Taluka_id).order_by('Name')
    context = {'District': Districts, 'Taluka': Talukas, 'Hobali': Hobalis}
    return render(request, 'citizen/Hobali_dropdown_list_option.html', context)


def villagecreate(request):
    form = VillageCityForms(request.POST)

    if form.is_valid():
        form.save()
        return redirect('citizen:villagecreate')
    return render(request, 'citizen/VillageCity_form.html',
                  {'form': form, 'village': VillageCity.objects.all().order_by('Name')})


def edit_village(request, id):
    users = VillageCity.objects.get(id=id)
    context = {'users': users}
    return render(request, 'citizen/village_edit.html', context)


def update_village(request, id):
    id = VillageCity.objects.get(id=id)
    form = VillageCityForms(request.POST or None, instance=id)
    form.save()
    return HttpResponseRedirect(reverse('citizen:villagecreate'))


def delete_village(request, id):
    tl = VillageCity.objects.get(id=id)
    tl.delete()
    return HttpResponseRedirect(reverse('citizen:villagecreate'))


def load_Circle(request):
    State_id = request.GET.get('State')
    District_id = request.GET.get('District')
    Taluka_id = request.GET.get('Taluka')
    Hobali_id = request.GET.get('Hobali')
    Districts = District.objects.filter(State_id=State_id).order_by('State')
    Talukas = Taluka.objects.filter(District_id=District_id).order_by('Name')
    Hobalis = Hobali.objects.filter(Taluka_id=Taluka_id).order_by('Name')
    Circles = Circle.objects.filter(Hobali_id=Hobali_id).order_by('Name')
    context = {'District': Districts, 'Taluka': Talukas, 'Hobali': Hobalis, 'Circle': Circles}
    return render(request, 'citizen/Circle_dropdown_list_option.html', context)


def policestationcreate(request):
    form = PoliceStationForms(request.POST)

    if form.is_valid():
        form.save()
        return redirect('citizen:policestationcreate')
    return render(request, 'citizen/PoliceStation_form.html',
                  {'form': form, 'policestation': PoliceStation.objects.all().order_by('Name')})


def edit_policestation(request, id):
    users = PoliceStation.objects.get(id=id)
    context = {'users': users}
    return render(request, 'citizen/policestation_edit.html', context)


def update_policestation(request, id):
    id = PoliceStation.objects.get(id=id)
    form = PoliceStationForms(request.POST or None, instance=id)
    form.save()
    return HttpResponseRedirect(reverse('citizen:policestationcreate'))


def delete_policestation(request, id):
    tl = PoliceStation.objects.get(id=id)
    tl.delete()
    return HttpResponseRedirect(reverse('citizen:policestationcreate'))


def load_Village(request):
    State_id = request.GET.get('State')
    District_id = request.GET.get('District')
    Taluka_id = request.GET.get('Taluka')
    Hobali_id = request.GET.get('Hobali')
    Circle_id = request.GET.get('Circle')
    Districts = District.objects.filter(State_id=State_id).order_by('State')
    Talukas = Taluka.objects.filter(District_id=District_id).order_by('Name')
    Hobalis = Hobali.objects.filter(Taluka_id=Taluka_id).order_by('Name')
    Circles = Circle.objects.filter(Hobali_id=Hobali_id).order_by('Name')
    Villages = VillageCity.objects.filter(Circle_id=Circle_id).order_by('Name')
    context = {'District': Districts, 'Taluka': Talukas, 'Hobali': Hobalis, 'Circle': Circles, 'Village': Villages}
    return render(request, 'citizen/Village_dropdown_list_option.html', context)


def partdetailcreate(request):
    form = PartDetailsForms(request.POST)

    if form.is_valid():
        form.save()
        return redirect('citizen:partdetailcreate')
    return render(request, 'citizen/PartDetails_form.html',
                  {'form': form, 'partdetails': PartDetails.objects.all().order_by('Name')})


def edit_partdetail(request, id):
    users = PartDetails.objects.get(id=id)
    context = {'users': users}
    return render(request, 'citizen/policestation_edit.html', context)


def update_partdetail(request, id):
    id = PartDetails.objects.get(id=id)
    form = PartDetailsForms(request.POST or None, instance=id)
    form.save()
    return HttpResponseRedirect(reverse('citizen:partdetailcreate'))


def delete_partdetail(request, id):
    tl = PartDetails.objects.get(id=id)
    tl.delete()
    return HttpResponseRedirect(reverse('citizen:partdetailcreate'))


def load_Police(request):
    State_id = request.GET.get('State')
    District_id = request.GET.get('District')
    Taluka_id = request.GET.get('Taluka')
    Hobali_id = request.GET.get('Hobali')
    Circle_id = request.GET.get('Circle')
    VillageCity_id = request.GET.get('VillageCity')
    Districts = District.objects.filter(State_id=State_id).order_by('State')
    Talukas = Taluka.objects.filter(District_id=District_id).order_by('Name')
    Hobalis = Hobali.objects.filter(Taluka_id=Taluka_id).order_by('Name')
    Circles = Circle.objects.filter(Hobali_id=Hobali_id).order_by('Name')
    Villages = VillageCity.objects.filter(Circle_id=Circle_id).order_by('Name')
    Polices = PoliceStation.objects.filter(VillageCity_id=VillageCity_id).order_by('Name')
    context = {'District': Districts, 'Taluka': Talukas, 'Hobali': Hobalis, 'Circle': Circles, 'Village': Villages,
               'Police': Polices}
    return render(request, 'citizen/Police_dropdown_list_option.html', context)


def pollingstationcreate(request):
    form = PollingStationForms(request.POST)

    if form.is_valid():
        form.save()
        return redirect('citizen:pollingstationcreate')
    return render(request, 'citizen/PollingStation_form.html',
                  {'form': form, 'pollingstation': PollingStation.objects.all().order_by('Name')})


def edit_pollingstation(request, id):
    users = PollingStation.objects.get(id=id)
    context = {'users': users}
    return render(request, 'citizen/pollingstation_edit.html', context)


def update_pollingstation(request, id):
    id = PollingStation.objects.get(id=id)
    form = PollingStationForms(request.POST or None, instance=id)
    form.save()
    return HttpResponseRedirect(reverse('pollingstationcreate'))


def delete_pollingstation(request, id):
    tl = PollingStation.objects.get(id=id)
    tl.delete()
    return HttpResponseRedirect(reverse('pollingstationcreate'))


def load_PartDetails(request):
    State_id = request.GET.get('State')
    District_id = request.GET.get('District')
    Taluka_id = request.GET.get('Taluka')
    Hobali_id = request.GET.get('Hobali')
    Circle_id = request.GET.get('Circle')
    VillageCity_id = request.GET.get('VillageCity')
    PoliceStation_id = request.GET.get('PoliceStation')
    Districts = District.objects.filter(State_id=State_id).order_by('State')
    Talukas = Taluka.objects.filter(District_id=District_id).order_by('Name')
    Hobalis = Hobali.objects.filter(Taluka_id=Taluka_id).order_by('Name')
    Circles = Circle.objects.filter(Hobali_id=Hobali_id).order_by('Name')
    Villages = VillageCity.objects.filter(Circle_id=Circle_id).order_by('Name')
    Polices = PoliceStation.objects.filter(VillageCity_id=VillageCity_id).order_by('Name')
    Parts = PartDetails.objects.filter(PoliceStation_id=PoliceStation_id).order_by('Name')
    context = {'District': Districts, 'Taluka': Talukas, 'Hobali': Hobalis, 'Circle': Circles,
               'Village': Villages, 'Police': Polices, 'Part': Parts}
    return render(request, 'citizen/Part_dropdown_list_option.html', context)


def create_consttype(request):
    form = ConstituencyTypeForms(request.POST)

    if form.is_valid():
        form.save()
        return redirect('citizen:create_consttype')
    return render(request, 'citizen/ConstituencyType.html',
                  {'form': form, 'Consttype': ConstituencyType.objects.all().order_by('Name')})


def update_consttype(request, id):
    id = ConstituencyType.objects.get(id=id)
    form = ConstituencyTypeForms(request.POST or None, instance=id)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('citizen:create_consttype'))
    return render(request, 'citizen/ConstituencyType.html', {'form': form,
                                                             'Consttype': ConstituencyType.objects.all().order_by(
                                                                 'Name')})


def delete_consttype(request, id):
    user = ConstituencyType.objects.get(id=id)
    user.delete()
    return HttpResponseRedirect(reverse('citizen:create_consttype'))


def constituencycreate(request):
    form = ConstituencyForms(request.POST)

    if form.is_valid():
        form.save()
        return redirect('citizen:constituencycreate')
    return render(request, 'citizen/Constituency.html',
                  {'form': form, 'constituency': Constituency.objects.all().order_by('Name')})


def edit_constituency(request, id):
    users = Constituency.objects.get(id=id)
    context = {'users': users}
    return render(request, 'citizen/constituency_edit.html', context)


def update_constituency(request, id):
    id = Constituency.objects.get(id=id)
    form = ConstituencyForms(request.POST or None, instance=id)
    form.save()
    return HttpResponseRedirect(reverse('citizen:constituencycreate'))


def delete_constituency(request, id):
    tl = Constituency.objects.get(id=id)
    tl.delete()
    return HttpResponseRedirect(reverse('citizen:constituencycreate'))


def load_Const(request):
    State_id = request.GET.get('State')
    District_id = request.GET.get('District')
    Districts = District.objects.filter(State_id=State_id).order_by('State')
    Talukas = Taluka.objects.filter(District_id=District_id).order_by('Name')
    context = {'District': Districts, 'Taluka': Talukas}
    return render(request, 'citizen/Const_dropdown_list_option.html', context)


def create_reporter(request):
    form = PressReportersForms(request.POST)

    if form.is_valid():
        form.save()
        return redirect('create_reporter')
    return render(request, 'citizen/Reporters.html',
                  {'form': form, 'Reporter': PressReporters.objects.all().order_by('Reporter')})


def update_reporter(request, id):
    id = PressReporters.objects.get(id=id)
    form = PressReportersForms(request.POST or None, instance=id)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('citizen:create_reporter'))
    return render(request, 'citizen/Reporters.html', {'form': form,
                                                      'Reporter': PressReporters.objects.all().order_by(
                                                          'Reporter')})


def delete_reporter(request, id):
    user = PressReporters.objects.get(id=id)
    user.delete()
    return HttpResponseRedirect(reverse('citizen:create_reporter'))


def create_reporterconst(request):
    form = PressReportersConstForms(request.POST)

    if form.is_valid():
        form.save()
        return redirect('citizen:create_reporterconst')
    return render(request, 'citizen/ReporterConst.html',
                  {'form': form, 'ReporterConst': PressReporterConstituency123.objects.all()})


def update_reporterconst(request, id):
    id = PressReporterConstituency123.objects.get(id=id)
    form = PressReportersConstForms(request.POST or None, instance=id)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('citizen:create_reporterconst'))
    return render(request, 'citizen/ReporterConst.html', {'form': form,
                                                          'ReporterConst': PressReporterConstituency123.objects.all().order_by(
                                                              'Constituency')})


def delete_reporterconst(request, id):
    user = PressReporterConstituency123.objects.get(id=id)
    user.delete()
    return HttpResponseRedirect(reverse('citizen:create_reporterconst'))


def party(request):
    if request.method == 'POST':
        form = PartyForms(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('citizen:success')
    else:
        form = PartyForms()
    return render(request, 'citizen/Party.html',
                  {'form': form, 'Party': Party123.objects.all()})


def success(request):
    return HttpResponse('successfully uploaded')


def delete_party(request, id):
    user1 = Party123.objects.get(id=id)
    user1.delete()
    return redirect('citizen:party')


def update_party(request, id):
    id = Party123.objects.get(id=id)
    form = PartyForms(request.POST or None, instance=id)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('citizen:party'))
    return render(request, 'citizen/Party.html', {'form': form,
                                                  'Party': Party123.objects.all().order_by('Name')})


def create_memberstype(request):
    form = MembersTypeForms(request.POST)
    names = MembersType.objects.all().count()

    if form.is_valid():
        form.save()
        return redirect('citizen:create_memberstype')
    return render(request, 'citizen/MembersType.html',
                  {'form': form, 'names': names, 'MembersType': MembersType.objects.all().order_by('Title')})


def update_memberstype(request, id):
    id = MembersType.objects.get(id=id)
    form = MembersTypeForms(request.POST or None, instance=id)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('citizen:create_memberstype'))
    return render(request, 'citizen/MembersType.html', {'form': form,
                                                        'MembersType': MembersType.objects.all().order_by(
                                                            'Title')})


def delete_memberstype(request, id):
    user = MembersType.objects.get(id=id)
    user.delete()
    return HttpResponseRedirect(reverse('citizen:create_memberstype'))


def create_members(request):
    form = MembersForms(request.POST)

    if form.is_valid():
        form.save()
        return redirect('citizen:create_members')
    return render(request, 'citizen/Members.html',
                  {'form': form, 'Members': Members.objects.all().order_by('FirstName')})


def update_members(request, id):
    id = Members.objects.get(id=id)
    form = MembersForms(request.POST or None, instance=id)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('citizen:create_members'))
    return render(request, 'citizen/Members.html', {'form': form,
                                                    'Members': Members.objects.all().order_by(
                                                        'FirstName')})


def delete_members(request, id):
    user = Members.objects.get(id=id)
    user.delete()
    return HttpResponseRedirect(reverse('citizen:create_members'))


def load_Constituency(request):
    ConstituencyType_id = request.GET.get('ConstituencyType')
    Constituencys = Constituency.objects.filter(ConstituencyType_id=ConstituencyType_id).order_by('Name')
    return render(request, 'citizen/constituency_dropdown_list_options.html', {'Constituency': Constituencys})


def create_event(request):
    form = EventForms(request.POST)

    if form.is_valid():
        form.save()
        return redirect('create_event')
    return render(request, 'citizen/Event.html',
                  {'form': form, 'Event': Event.objects.all().order_by('Date')})


def update_event(request, id):
    id = Event.objects.get(id=id)
    form = EventForms(request.POST or None, instance=id)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('create_event'))
    return render(request, 'citizen/Event.html', {'form': form,
                                                  'Event': Event.objects.all().order_by('Date')})


def delete_event(request, id):
    user = Event.objects.get(id=id)
    user.delete()
    return HttpResponseRedirect(reverse('create_event'))


def create_project(request):
    form = ProjectsForms(request.POST)

    if form.is_valid():
        form.save()
        return redirect('citizen:create_project')
    return render(request, 'citizen/Projects.html',
                  {'form': form, 'Projects': Projects.objects.all().order_by('Title')})


def update_project(request, id):
    id = Projects.objects.get(id=id)
    form = ProjectsForms(request.POST or None, instance=id)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('citizen:create_project'))
    return render(request, 'citizen/Projects.html', {'form': form,
                                                     'Projects': Projects.objects.all().order_by(
                                                         'Title')})


def delete_project(request, id):
    user = Projects.objects.get(id=id)
    user.delete()
    return HttpResponseRedirect(reverse('citizen:create_project'))


def load_project(request):
    Constituency_id = request.GET.get('Constituency')
    Member = Members.objects.filter(Constituency_id=Constituency_id).order_by('FirstName')
    return render(request, 'citizen/project_dropdown_list_options.html', {'Members': Member})


def create_partyworkers(request):
    form = PartyworkersForms(request.POST)
    if form.is_valid():
        form.save()
        return redirect('citizen:create_partyworkers')
    return render(request, 'citizen/Partyworkers.html',
                  {'form': form, 'partyworkers': PartyWorkers.objects.all().order_by('Name')})


def update_partyworkers(request, id):
    id = PartyWorkers.objects.get(id=id)
    form = PartyworkersForms(request.POST or None, instance=id)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('citizen:create_partyworkers'))
    return render(request, 'citizen/Partyworkers.html', {'form': form,
                                                         'partyworkers': PartyWorkers.objects.all().order_by(
                                                             'Name')})


def delete_partyworkers(request, id):
    user = PartyWorkers.objects.get(id=id)
    user.delete()
    return HttpResponseRedirect(reverse('citizen:create_partyworkers'))


def load_partyworkers(request):
    Constituency_id = request.GET.get('Constituency')
    Member = Members.objects.filter(Constituency_id=Constituency_id).order_by('FirstName')
    return render(request, 'citizen/partyworkers_dropdown_list_options.html', {'Members': Member})


def create_committeestructure(request):
    form = CommitteeStructureForms(request.POST)

    if form.is_valid():
        form.save()
        return redirect('citizen:create_committeestructure')
    return render(request, 'citizen/Committeestructure.html',
                  {'form': form, 'Committestr': CommitteeStructure123.objects.all().order_by('Position')})


def update_committeestructure(request, id):
    id = CommitteeStructure123.objects.get(id=id)
    form = CommitteeStructureForms(request.POST or None, instance=id)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('citizen:create_committeestructure'))
    return render(request, 'citizen/Committeestructure.html', {'form': form,
                                                               'Committestr': CommitteeStructure123.objects.all()})


def delete_committeestructure(request, id):
    user = CommitteeStructure123.objects.get(id=id)
    user.delete()
    return HttpResponseRedirect(reverse('citizen:create_committeestructure'))


def create_committee(request):
    form = CommitteeForms(request.POST)

    if form.is_valid():
        form.save()
        return redirect('citizen:create_committee')
    return render(request, 'citizen/Committee.html',
                  {'form': form, 'Committe': Committee123.objects.all().order_by('Name')})


def update_committee(request, id):
    id = Committee123.objects.get(id=id)
    form = CommitteeForms(request.POST or None, instance=id)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('citizen:create_committee'))
    return render(request, 'citizen/Committee.html', {'form': form,
                                                      'Committe': Committee123.objects.all()})


def delete_committee(request, id):
    user = Committee123.objects.get(id=id)
    user.delete()
    return HttpResponseRedirect(reverse('citizen:create_committee'))


def create_committeemembers(request):
    form = CommitteeMembersForms(request.POST)

    if form.is_valid():
        form.save()
        return redirect('citizen:create_committeemembers')
    return render(request, 'citizen/Committeemembers.html',
                  {'form': form, 'Committemem': CommitteeMembers123.objects.all().order_by('Start_Date')})


def update_committeemembers(request, id):
    id = CommitteeMembers123.objects.get(id=id)
    form = CommitteeMembersForms(request.POST or None, instance=id)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('citizen:create_committeemembers'))
    return render(request, 'citizen/Committeemembers.html', {'form': form,
                                                             'Committemem': CommitteeMembers123.objects.all()})


def delete_committeemembers(request, id):
    user = CommitteeMembers123.objects.get(id=id)
    user.delete()
    return HttpResponseRedirect(reverse('citizen:create_committeemembers'))


def complaints(request):
    data = Quiz.objects.all()
    stu = {
    "quizzes": data
    }
    return render(request,"citizen/complaints_list.html", stu)


def delete_complaints(request, id):
    user = Quiz.objects.get(id=id)
    user.delete()
    return HttpResponseRedirect(reverse('citizen:complaints'))

