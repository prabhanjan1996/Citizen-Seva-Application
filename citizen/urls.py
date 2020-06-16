from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path

from django_school import settings
from citizen import views
from .models import Taluka, Hobali

app_name = 'citizen'
urlpatterns = [

    # path('email/', emailView, name='email'),
    path('index_contact/', views.index_contact, name='index_contact'),
    path('', views.admin_index, name='admin_index'),
    path('about/', views.about, name='about'),
    path('seen/', views.seen, name='seen'),

    path('HomePage/', views.HomePage, name='HomePage'),
    path('send_mail_plain_with_file', views.send_mail_plain_with_file, name='plain_email'),

    path('create_state', views.create_state, name='create_state'),
    url(r'^edit_state/(?P<id>\d+)$', views.edit_state, name='edit_state'),

    path('delete/<int:id>', views.delete_state),

    path('create_district', views.create_district, name='create_district'),
    path('update_district/<int:id>', views.update_district, name='update_district'),
    path('delete_district/<int:id>', views.delete_district, name='delete_district'),

    path('talukacreate/', views.talukacreate, name='talukacreate'),
    path('<int:pk>/', views.TalukaUpdateView.as_view(), name='TalukaUpdateView'),
    path('ajax/load_District/', views.load_District, name='ajax_load_District'),
    path('delete_taluka/<int:id>', views.delete_taluka, name='delete_taluka'),

    path('hobalicreate/', views.hobalicreate, name='hobalicreate'),
    path('<int:pk>/', views.HobaliUpdateView.as_view(), name='HobaliUpdateView'),
    path('ajax/load_Taluka/', views.load_Taluka, name='ajax_load_Taluka'),
    path('delete_hobali/<int:id>', views.delete_hobali, name='delete_hobali'),

    path('circlecreate/', views.circlecreate, name='circlecreate'),
    path('update_circle/<int:id>', views.update_circle, name='update_circle'),
    path('ajax/load_Hobali/', views.load_Hobali, name='ajax_load_Hobali'),
    path('delete_circle/<int:id>', views.delete_circle, name='delete_circle'),

    path('villagecreate/', views.villagecreate, name='villagecreate'),
    url(r'^edit_village/(?P<id>\d+)$', views.edit_village, name='edit_village'),
    url(r'^edit_village/update_village/(?P<id>\d+)$', views.update_village, name='update_village'),
    path('ajax/load_Circle/', views.load_Circle, name='ajax_load_Circle'),
    path('delete_village/<int:id>', views.delete_village, name='delete_village'),

    path('policestationcreate/', views.policestationcreate, name='policestationcreate'),
    url(r'^edit_policestation/(?P<id>\d+)$', views.edit_policestation, name='edit_policestation'),
    url(r'^edit_policestation/update_policestation/(?P<id>\d+)$', views.update_policestation,
        name='update_policestation'),
    path('ajax/load_Village/', views.load_Village, name='ajax_load_Village'),
    path('delete_policestation/<int:id>', views.delete_policestation, name='delete_policestation'),

    path('partdetailcreate/', views.partdetailcreate, name='partdetailcreate'),
    url(r'^edit_partdetail/(?P<id>\d+)$', views.edit_partdetail, name='edit_partdetail'),
    url(r'^edit_partdetail/update_partdetail/(?P<id>\d+)$', views.update_partdetail,
        name='update_partdetail'),
    path('ajax/load_Police/', views.load_Police, name='ajax_load_Police'),
    path('delete_partdetail/<int:id>', views.delete_partdetail, name='delete_partdetail'),

    path('pollingstationcreate/', views.pollingstationcreate, name='pollingstationcreate'),
    url(r'^edit_pollingstation/(?P<id>\d+)$', views.edit_pollingstation, name='edit_pollingstation'),
    url(r'^edit_pollingstation/update_pollingstation/(?P<id>\d+)$', views.update_pollingstation,
        name='update_pollingstation'),
    path('ajax/load_PartDetails/', views.load_PartDetails, name='ajax_load_PartDetails'),
    path('delete_pollingstation/<int:id>', views.delete_pollingstation, name='delete_pollingstation'),

    path('create_consttype', views.create_consttype, name='create_consttype'),
    path('update_consttype/<int:id>', views.update_consttype, name='update_consttype'),
    path('delete_consttype/<int:id>', views.delete_consttype, name='delete_consttype'),

    path('constituencycreate/', views.constituencycreate, name='constituencycreate'),
    url(r'^edit_constituency/(?P<id>\d+)$', views.edit_constituency, name='edit_constituency'),
    url(r'^edit_constituency/update_constituency/(?P<id>\d+)$', views.update_constituency, name='update_constituency'),
    path('ajax/load_Const/', views.load_Const, name='ajax_load_Const'),
    path('delete_constituency/<int:id>', views.delete_constituency, name='delete_constituency'),

    path('create_reporter', views.create_reporter, name='create_reporter'),
    path('update_reporter/<int:id>', views.update_reporter, name='update_reporter'),
    path('delete_reporter/<int:id>', views.delete_reporter, name='delete_reporter'),

    path('create_reporterconst', views.create_reporterconst, name='create_reporterconst'),
    path('update_reporterconst/<int:id>', views.update_reporterconst, name='update_reporterconst'),
    path('delete_reporterconst/<int:id>', views.delete_reporterconst, name='delete_reporterconst'),

    path('party', views.party, name='party'),
    path('success', views.success, name='success'),
    path('delete_party/<int:id>', views.delete_party, name='delete_party'),
    path('update_party/<int:id>', views.update_party, name='update_party'),

    path('create_memberstype', views.create_memberstype, name='create_memberstype'),
    path('update_memberstype/<int:id>', views.update_memberstype, name='update_memberstype'),
    path('delete_memberstype/<int:id>', views.delete_memberstype, name='delete_memberstype'),

    path('create_members', views.create_members, name='create_members'),
    path('update_members/<int:id>', views.update_members, name='update_members'),
    path('ajax/load_Constituency/', views.load_Constituency, name='ajax_load_Constituency'),
    path('delete_members/<int:id>', views.delete_members, name='delete_members'),

    path('create_event', views.create_event, name='create_event'),
    path('update_event/<int:id>', views.update_event, name='update_event'),
    path('delete_event/<int:id>', views.delete_event, name='delete_event'),

    path('create_project', views.create_project, name='create_project'),
    path('update_project/<int:id>', views.update_project, name='update_project'),
    path('ajax/load_project/', views.load_project, name='ajax_load_project'),
    path('delete_project/<int:id>', views.delete_project, name='delete_project'),

    path('create_partyworkers', views.create_partyworkers, name='create_partyworkers'),
    path('update_partyworkers/<int:id>', views.update_partyworkers, name='update_partyworkers'),
    path('ajax/load_partyworkers/', views.load_partyworkers, name='ajax_load_partyworkers'),
    path('delete_partyworkers/<int:id>', views.delete_partyworkers, name='delete_partyworkers'),

    path('create_committeestructure', views.create_committeestructure, name='create_committeestructure'),
    path('update_committeestructure/<int:id>', views.update_committeestructure, name='update_committeestructure'),
    path('delete_committeestructure/<int:id>', views.delete_committeestructure, name='delete_committeestructure'),

    path('create_committee', views.create_committee, name='create_committee'),
    path('update_committee/<int:id>', views.update_committee, name='update_committee'),
    path('delete_committee/<int:id>', views.delete_committee, name='delete_committee'),

    path('create_committeemembers', views.create_committeemembers, name='create_committeemembers'),
    path('update_committeemembers/<int:id>', views.update_committeemembers, name='update_committeemembers'),
    path('delete_committeemembers/<int:id>', views.delete_committeemembers, name='delete_committeemembers'),

    path('complaints/', views.complaints, name='complaints'),
    path('delete_complaints/<int:id>', views.delete_complaints, name='delete_complaints'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
