import self
from django.db.models import DateField
from django.forms import DateInput

from django_school import settings
from .models import State, District, Taluka, Hobali, Circle, VillageCity, PoliceStation, PartDetails, PollingStation, \
    ConstituencyType, Constituency, PressReporters, PressReporterConstituency, PressReporterConstituency123, Party, \
    Party123, MembersType, Members, Events123, Event, Projects, PartyWorkers, CommitteeStructure, CommitteeStructure123, \
    Committee123, CommitteeMembers123

from django import forms


class ContactForm(forms.Form):
    Name = forms.CharField(required=False, max_length=100)
    Email = forms.EmailField(required=True)
    Comment = forms.CharField(widget=forms.Textarea, required=True)


class EmailForm(forms.Form):
    subject = forms.CharField(required=True)
    Name = forms.CharField(required=True)
    Email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)


class StateForms(forms.ModelForm):
    class Meta:
        model = State
        fields = ['Code', 'State']


class DistrictForms(forms.ModelForm):
    class Meta:
        model = District
        fields = ['Code', 'Name', 'State']


class TalukaForms(forms.ModelForm):
    class Meta:
        model = Taluka
        fields = ('Code', 'Name', 'State', 'District')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['District'].queryset = District.objects.none()

        if 'State' in self.data:
            try:
                State_id = int(self.data.get('State'))
                self.fields['District'].queryset = District.objects.filter(State_id=State_id).order_by('Name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            State_id = self.data.get('State')
            self.fields['District'].queryset = District.objects.filter(State_id=State_id).order_by('Name')


class HobaliForms(forms.ModelForm):
    class Meta:
        model = Hobali
        fields = ('Name', 'State', 'District', 'Taluka')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['District'].queryset = District.objects.none()

        if 'State' in self.data:
            try:
                State_id = int(self.data.get('State'))
                self.fields['District'].queryset = District.objects.filter(State_id=State_id).order_by('Name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            State_id = self.data.get('State')
            self.fields['District'].queryset = District.objects.filter(State_id=State_id).order_by('Name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Taluka'].queryset = Taluka.objects.none()

        if 'District' in self.data:
            try:
                District_id = int(self.data.get('District'))
                self.fields['Taluka'].queryset = Taluka.objects.filter(District_id=District_id).order_by('Name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            District_id = self.data.get('District')
            self.fields['Taluka'].queryset = Taluka.objects.filter(District_id=District_id).order_by('Name')


class CircleForms(forms.ModelForm):
    class Meta:
        model = Circle
        fields = ('Name', 'State', 'District', 'Taluka', 'Hobali')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['District'].queryset = District.objects.none()

        if 'State' in self.data:
            try:
                State_id = int(self.data.get('State'))
                self.fields['District'].queryset = District.objects.filter(State_id=State_id).order_by('Name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['District'].queryset = self.instance.State.District_set.order_by('Name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Taluka'].queryset = Taluka.objects.none()

        if 'District' in self.data:
            try:
                District_id = int(self.data.get('District'))
                self.fields['Taluka'].queryset = Taluka.objects.filter(District_id=District_id).order_by('Name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['Taluka'].queryset = self.instance.District.Taluka_set.order_by('Name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Hobali'].queryset = Hobali.objects.none()

        if 'Taluka' in self.data:
            try:
                Taluka_id = int(self.data.get('Taluka'))
                self.fields['Hobali'].queryset = Hobali.objects.filter(Taluka_id=Taluka_id).order_by('Name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['Hobali'].queryset = self.instance.Taluka.Hobali_set.order_by('Name')


class VillageCityForms(forms.ModelForm):
    class Meta:
        model = VillageCity
        fields = ('Name', 'Pincode', 'State', 'District', 'Taluka', 'Hobali', 'Circle')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['District'].queryset = District.objects.none()

        if 'State' in self.data:
            try:
                State_id = int(self.data.get('State'))
                self.fields['District'].queryset = District.objects.filter(State_id=State_id).order_by('Name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['District'].queryset = self.instance.State.District_set.order_by('Name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Taluka'].queryset = Taluka.objects.none()

        if 'District' in self.data:
            try:
                District_id = int(self.data.get('District'))
                self.fields['Taluka'].queryset = Taluka.objects.filter(District_id=District_id).order_by('Name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['Taluka'].queryset = self.instance.District.Taluka_set.order_by('Name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Hobali'].queryset = Hobali.objects.none()

        if 'Taluka' in self.data:
            try:
                Taluka_id = int(self.data.get('Taluka'))
                self.fields['Hobali'].queryset = Hobali.objects.filter(Taluka_id=Taluka_id).order_by('Name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['Hobali'].queryset = self.instance.Taluka.Hobali_set.order_by('Name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Circle'].queryset = Circle.objects.none()

        if 'Hobali' in self.data:
            try:
                Hobali_id = int(self.data.get('Hobali'))
                self.fields['Circle'].queryset = Circle.objects.filter(Hobali_id=Hobali_id).order_by('Name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['Circle'].queryset = self.instance.Hobali.Circle_set.order_by('Name')


class PoliceStationForms(forms.ModelForm):
    class Meta:
        model = PoliceStation
        fields = ('Name', 'State', 'District', 'Taluka', 'Hobali', 'Circle', 'VillageCity')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['District'].queryset = District.objects.none()

        if 'State' in self.data:
            try:
                State_id = int(self.data.get('State'))
                self.fields['District'].queryset = District.objects.filter(State_id=State_id).order_by('Name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['District'].queryset = self.instance.State.District_set.order_by('Name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Taluka'].queryset = Taluka.objects.none()

        if 'District' in self.data:
            try:
                District_id = int(self.data.get('District'))
                self.fields['Taluka'].queryset = Taluka.objects.filter(District_id=District_id).order_by('Name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['Taluka'].queryset = self.instance.District.Taluka_set.order_by('Name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Hobali'].queryset = Hobali.objects.none()

        if 'Taluka' in self.data:
            try:
                Taluka_id = int(self.data.get('Taluka'))
                self.fields['Hobali'].queryset = Hobali.objects.filter(Taluka_id=Taluka_id).order_by('Name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['Hobali'].queryset = self.instance.Taluka.Hobali_set.order_by('Name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Circle'].queryset = Circle.objects.none()

        if 'Hobali' in self.data:
            try:
                Hobali_id = int(self.data.get('Hobali'))
                self.fields['Circle'].queryset = Circle.objects.filter(Hobali_id=Hobali_id).order_by('Name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['Circle'].queryset = self.instance.Hobali.Circle_set.order_by('Name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['VillageCity'].queryset = VillageCity.objects.none()

        if 'Circle' in self.data:
            try:
                Circle_id = int(self.data.get('Circle'))
                self.fields['VillageCity'].queryset = VillageCity.objects.filter(Circle_id=Circle_id).order_by('Name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['VillageCity'].queryset = self.instance.Circle.Village_set.order_by('Name')


class PartDetailsForms(forms.ModelForm):
    class Meta:
        model = PartDetails
        fields = ('Name', 'Number', 'State', 'District', 'Taluka', 'Hobali', 'Circle', 'VillageCity', 'PoliceStation')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['District'].queryset = District.objects.none()

        if 'State' in self.data:
            try:
                State_id = int(self.data.get('State'))
                self.fields['District'].queryset = District.objects.filter(State_id=State_id).order_by('Name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['District'].queryset = self.instance.State.District_set.order_by('Name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Taluka'].queryset = Taluka.objects.none()

        if 'District' in self.data:
            try:
                District_id = int(self.data.get('District'))
                self.fields['Taluka'].queryset = Taluka.objects.filter(District_id=District_id).order_by('Name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['Taluka'].queryset = self.instance.District.Taluka_set.order_by('Name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Hobali'].queryset = Hobali.objects.none()

        if 'Taluka' in self.data:
            try:
                Taluka_id = int(self.data.get('Taluka'))
                self.fields['Hobali'].queryset = Hobali.objects.filter(Taluka_id=Taluka_id).order_by('Name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['Hobali'].queryset = self.instance.Taluka.Hobali_set.order_by('Name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Circle'].queryset = Circle.objects.none()

        if 'Hobali' in self.data:
            try:
                Hobali_id = int(self.data.get('Hobali'))
                self.fields['Circle'].queryset = Circle.objects.filter(Hobali_id=Hobali_id).order_by('Name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['Circle'].queryset = self.instance.Hobali.Circle_set.order_by('Name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['VillageCity'].queryset = VillageCity.objects.none()

        if 'Circle' in self.data:
            try:
                Circle_id = int(self.data.get('Circle'))
                self.fields['VillageCity'].queryset = VillageCity.objects.filter(Circle_id=Circle_id).order_by('Name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['VillageCity'].queryset = self.instance.Circle.Village_set.order_by('Name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['PoliceStation'].queryset = PoliceStation.objects.none()

        if 'VillageCity' in self.data:
            try:
                VillageCity_id = int(self.data.get('VillageCity'))
                self.fields['PoliceStation'].queryset = PoliceStation.objects.filter(
                    VillageCity_id=VillageCity_id).order_by('Name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['PoliceStation'].queryset = self.instance.VillageCity.PoliceStation_set.order_by('Name')


class PollingStationForms(forms.ModelForm):
    class Meta:
        model = PollingStation
        fields = (
            'Name', 'State', 'District', 'Taluka', 'Hobali', 'Circle', 'VillageCity', 'PoliceStation', 'PartDetails')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['District'].queryset = District.objects.none()

        if 'State' in self.data:
            try:
                State_id = int(self.data.get('State'))
                self.fields['District'].queryset = District.objects.filter(State_id=State_id).order_by('Name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['District'].queryset = self.instance.State.District_set.order_by('Name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Taluka'].queryset = Taluka.objects.none()

        if 'District' in self.data:
            try:
                District_id = int(self.data.get('District'))
                self.fields['Taluka'].queryset = Taluka.objects.filter(District_id=District_id).order_by('Name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['Taluka'].queryset = self.instance.District.Taluka_set.order_by('Name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Hobali'].queryset = Hobali.objects.none()

        if 'Taluka' in self.data:
            try:
                Taluka_id = int(self.data.get('Taluka'))
                self.fields['Hobali'].queryset = Hobali.objects.filter(Taluka_id=Taluka_id).order_by('Name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['Hobali'].queryset = self.instance.Taluka.Hobali_set.order_by('Name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Circle'].queryset = Circle.objects.none()

        if 'Hobali' in self.data:
            try:
                Hobali_id = int(self.data.get('Hobali'))
                self.fields['Circle'].queryset = Circle.objects.filter(Hobali_id=Hobali_id).order_by('Name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['Circle'].queryset = self.instance.Hobali.Circle_set.order_by('Name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['VillageCity'].queryset = VillageCity.objects.none()

        if 'Circle' in self.data:
            try:
                Circle_id = int(self.data.get('Circle'))
                self.fields['VillageCity'].queryset = VillageCity.objects.filter(Circle_id=Circle_id).order_by('Name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['VillageCity'].queryset = self.instance.Circle.Village_set.order_by('Name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['PoliceStation'].queryset = PoliceStation.objects.none()

        if 'VillageCity' in self.data:
            try:
                VillageCity_id = int(self.data.get('VillageCity'))
                self.fields['PoliceStation'].queryset = PoliceStation.objects.filter(
                    VillageCity_id=VillageCity_id).order_by('Name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['PoliceStation'].queryset = self.instance.VillageCity.PoliceStation_set.order_by('Name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['PartDetails'].queryset = PartDetails.objects.none()

        if 'PoliceStation' in self.data:
            try:
                PoliceStation_id = int(self.data.get('PoliceStation'))
                self.fields['PartDetails'].queryset = PartDetails.objects.filter(
                    PoliceStation_id=PoliceStation_id).order_by('Name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['PartDetails'].queryset = self.instance.PoliceStation.PartDetails_set.order_by('Name')


class ConstituencyTypeForms(forms.ModelForm):
    class Meta:
        model = ConstituencyType
        fields = ['Code', 'Name', 'Description']


class ConstituencyForms(forms.ModelForm):
    class Meta:
        model = Constituency
        fields = ('Name', 'Number', 'State', 'District', 'Taluka', 'ConstituencyType')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['District'].queryset = District.objects.none()

        if 'State' in self.data:
            try:
                State_id = int(self.data.get('State'))
                self.fields['District'].queryset = District.objects.filter(State_id=State_id).order_by('Name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['District'].queryset = self.instance.State.District_set.order_by('Name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Taluka'].queryset = Taluka.objects.none()

        if 'District' in self.data:
            try:
                District_id = int(self.data.get('District'))
                self.fields['Taluka'].queryset = Taluka.objects.filter(District_id=District_id).order_by('Name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['Taluka'].queryset = self.instance.District.Taluka_set.order_by('Name')


class PressReportersForms(forms.ModelForm):
    class Meta:
        model = PressReporters
        fields = ['Reporter', 'City', 'MediaName', 'MediaType', 'Mobile', 'Email', 'Website']


class PressReportersConstForms(forms.ModelForm):
    class Meta:
        model = PressReporterConstituency123
        fields = ['PressReporters', 'Constituency', 'Status']


class PartyForms(forms.ModelForm):
    class Meta:
        model = Party123
        fields = ['Name', 'Description', 'Img', 'ShortName', 'SignName']


class PartyworkersForms(forms.ModelForm):
    class Meta:
        model = PartyWorkers
        fields = ('Name', 'City', 'Address', 'Status', 'Mobile', 'Email', 'Members', 'PollingStation')


class MembersTypeForms(forms.ModelForm):
    class Meta:
        model = MembersType
        fields = ['Code', 'Title']


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.DateInput):
    input_type = 'time'


class MembersForms(forms.ModelForm):
    class Meta:
        model = Members
        widgets = {
            'Dob': DateInput()
        }

        fields = ('FirstName', 'MiddleName', 'LastName', 'Dob', 'Mobile', 'SpouseName'
                  , 'Telephone', 'Website', 'Photo', 'MembersType', 'ConstituencyType', 'Constituency')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Constituency'].queryset = Constituency.objects.none()

        if 'ConstituencyType' in self.data:
            try:
                ConstituencyType_id = int(self.data.get('ConstituencyType'))
                self.fields['Constituency'].queryset = Constituency.objects.filter(
                    ConstituencyType_id=ConstituencyType_id).order_by('Name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            ConstituencyType_id = self.data.get('ConstituencyType')
            self.fields['Constituency'].queryset = Constituency.objects.filter(
                ConstituencyType_id=ConstituencyType_id).order_by('Name')


class EventForms(forms.ModelForm):
    class Meta:
        widgets = {
            'Date': DateInput(),
            'Time': TimeInput()
        }
        model = Event
        fields = ['Title', 'Description', 'Place', 'Date', 'Time', 'Documents']


class ProjectsForms(forms.ModelForm):
    class Meta:
        model = Projects
        widgets = {
            'Year': DateInput()
        }

        fields = ('Title', 'Amount', 'Description', 'status', 'Year', 'Constituency', 'Members')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Members'].queryset = Members.objects.none()

        if 'Constituency' in self.data:
            try:
                Constituency_id = int(self.data.get('Constituency'))
                self.fields['Members'].queryset = Members.objects.filter(
                    Constituency_id=Constituency_id).order_by('Name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            Constituency_id = self.data.get('Constituency')
            self.fields['Members'].queryset = Members.objects.filter(
                Constituency_id=Constituency_id).order_by('Name')


class CommitteeStructureForms(forms.ModelForm):
    class Meta:
        model = CommitteeStructure123
        fields = ['Position', 'Numbers']


class CommitteeForms(forms.ModelForm):
    class Meta:
        model = Committee123
        fields = ['Name', 'ShortName', 'level']


class CommitteeMembersForms(forms.ModelForm):
    class Meta:
        widgets = {
            'Start_Date': DateInput(),
            'End_Date': DateInput()
        }
        model = CommitteeMembers123
        fields = ['Name', 'CommitteeStructure', 'Committee', 'Start_Date', 'End_Date', 'Status']
