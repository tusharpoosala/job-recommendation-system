from dailyapp.models import Contact, Employer, Candidate, Add_notification, Preferences, Resume
from django import forms


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"


class EmployerForm(forms.ModelForm):
    class Meta:
        model = Employer
        fields = "__all__"


class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = "__all__"


class NotificationForm(forms.ModelForm):
    class Meta:
        model = Add_notification
        fields = ('interview_date', 'city', 'employer', 'responsibility', 'skills_required', 'experience', 'salary',
                  'description', 'title')


class PreferenceForm(forms.ModelForm):
    class Meta:
        model = Preferences
        fields = "__all__"


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ('notification_id', 'person', 'resume', 'datetime')
