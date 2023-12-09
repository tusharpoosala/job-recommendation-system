from dailyapp.forms import ContactForm, EmployerForm, CandidateForm, NotificationForm, PreferenceForm, ResumeForm
from dailyapp.models import Employer, Candidate, Add_notification, Preferences, Resume
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    return render(request, "index.html", {})


def new_post(request):
    return render(request, "new-post.html", {})



def contact(request):
    return render(request, "contact.html", {})


def job_post(request):
    return render(request, "job-post.html", {})


def send_message(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "contact.html", {})
    return render(request, "contact.html", {})


def employer(request):
    return render(request, "employer_regpage.html", {})


def employer_reg(request):
    if request.method == "POST":
        email = request.POST["email"]
        if Employer.objects.filter(email=email).exists():
            print("email already exist")
            return render(request, "employer_regpage.html", {})
        else:
            emp = EmployerForm(request.POST, request.FILES)
            print(emp.errors)
            if emp.is_valid():
                try:
                    emp.save()
                    return render(request, "employer_login.html", {})
                except Exception as e:
                    print(e)
            return render(request, "employer_regpage.html", {})


def employer_login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = Employer.objects.filter(email=email, password=password)
        if user.exists():
            request.session['email'] = email
            return render(request, "employer_home.html", {"msg": email})
        else:
            return render(request, "employer_login.html", {"msg": "email or password not exist"})
    return render(request, "employer_login.html", {"msg": " "})


def employer_view(request):
    email = request.session["email"]
    employers = Employer.objects.get(email=email)
    return render(request, "view_employer.html", {"employer": employers})


def employer_logout(request):
    request.session["email"] = ""
    del request.session["email"]
    return render(request, "employer_login.html", {})


def employer_is_login(request):
    if request.session.__contains__("email"):
        return True
    else:
        return False


def employer_chpwd(request):
    if employer_is_login(request):
        if request.method == "POST":
            email = request.session["email"]
            password = request.POST["password"]
            newpassword = request.POST["newpassword"]
            confirmpwd = request.POST["confirmpwd"]
            if newpassword == confirmpwd:
                try:
                    user = Employer.objects.get(email=email, password=password)
                    print(user)
                    user.password = newpassword
                    user.save()
                    msg = 'password update successfully'
                    return render(request, "employer_login.html", {"msg": msg})
                except:
                    msg = 'incorrect  password'
                    return render(request, "employer_chpwd.html", {"msg": msg})
            else:
                return render(request, "employer_chpwd.html", {"msg": "password doesn't match"})
        return render(request, "employer_chpwd.html", {})
    else:
        return render(request, "employer_login.html", {})


def employer_edit(request, id):
    employer = Employer.objects.get(id=id)
    return render(request, "employer_update.html", {"employer": employer})


def employer_update(request):
    if request.method == "POST":
        id = request.POST["id"]
        employers = Employer.objects.get(id=id)
        form = EmployerForm(request.POST, request.FILES, instance=employers)
        print(form.errors)
        if form.is_valid():
            form.save()
        return redirect("/employer_view")
    return render(request, "employer_update.html", {})


def employer_delete(request, id):
    employer = Employer.objects.get(id=id)
    employer.delete()
    return render(request, "employer_regpage.html", {})


def candidate(request):
    return render(request, "candidate_regpage.html", {})


def candidate_reg(request):
    if request.method == "POST":
        email = request.POST["email"]
        if Candidate.objects.filter(email=email).exists():
            print("email already exist")
            return render(request, "candidate_regpage.html", {})
        else:
            emp = CandidateForm(request.POST, request.FILES)
            print(emp.errors)
            if emp.is_valid():
                try:
                    emp.save()
                    return render(request, "candidate_login.html", {})
                except Exception as e:
                    print(e)
            return render(request, "candidate_regpage.html", {})


def candidate_login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = Candidate.objects.filter(email=email, password=password)
        if user.exists():
            request.session['email'] = email
            return render(request, "candidate_home.html", {"msg": email})
        else:
            return render(request, "candidate_login.html", {"msg": "email or password not exist"})
    return render(request, "candidate_login.html", {"msg": " "})


def candidate_view(request):
    email = request.session["email"]
    candidates = Candidate.objects.get(email=email)
    print(candidates)
    return render(request, "view_candidate.html", {"candidates": candidates})


def candidate_logout(request):
    request.session["email"] = ""
    del request.session["email"]
    return render(request, "candidate_login.html", {})


def candidate_is_login(request):
    if request.session.__contains__("email"):
        return True
    else:
        return False


def candidate_chpwd(request):
    if candidate_is_login(request):
        if request.method == "POST":
            email = request.session["email"]
            password = request.POST["password"]
            newpassword = request.POST["newpassword"]
            confirmpwd = request.POST["confirmpwd"]
            if newpassword == confirmpwd:
                try:
                    user = Candidate.objects.get(email=email, password=password)
                    print(user)
                    user.password = newpassword
                    user.save()
                    msg = 'password update successfully'
                    return render(request, "candidate_login.html", {"msg": msg})
                except:
                    msg = 'incorrect  password'
                    return render(request, "candidate_chpwd.html", {"msg": msg})
            else:
                return render(request, "candidate_chpwd.html", {"msg": "password doesn't match"})
        return render(request, "candidate_chpwd.html", {})
    else:
        return render(request, "candidate_login.html", {})


def candidate_edit(request, id):
    candidate = Candidate.objects.get(id=id)
    return render(request, "candidate_update.html", {"candidate": candidate})


def candidate_update(request):
    if request.method == "POST":
        id = request.POST["id"]
        candidates = Candidate.objects.get(id=id)
        form = CandidateForm(request.POST, request.FILES, instance=candidates)
        print(form.errors)
        if form.is_valid():
            form.save()
        return redirect("/candidate_view")
    return render(request, "candidate_update.html", {})


def candidate_delete(request, id):
    candidate = Candidate.objects.get(id=id)
    candidate.delete()
    return render(request, "candidate_regpage.html", {})


def add_notification(request):
    email = request.session["email"]
    employer = Employer.objects.get(email=email)
    if request.method == "POST":
        form = NotificationForm(request.POST)
        print("hai", form.errors)
        if form.is_valid():
            form.save()
            return render(request, "add_notification.html", {"employer": employer.id})
    return render(request, "add_notification.html", {"employer": employer.id})


def notification_view(request):
    email = request.session["email"]
    employer = Employer.objects.get(email=email)
    notifications = Add_notification.objects.filter(employer_id=employer.id)
    return render(request, "view_notification.html", {"notifications": notifications})


def notification_edit(request, id):
    notifications = Add_notification.objects.get(id=id)
    return render(request, "notification_update.html", {"notifications": notifications})


def notification_update(request):
    global id
    email = request.session["email"]
    employer = Employer.objects.get(email=email)
    if request.method == "POST":
        id = request.POST["id"]
        notification = Add_notification.objects.get(id=id)
        notification = NotificationForm(request.POST, instance=notification)
        print(notification.errors)
        if notification.is_valid():
            notification.save()
            notification = Add_notification.objects.filter(employer_id=employer.id)
        return render(request, "notification_update.html", {"notifications": notification})
    return render(request, "notification_update.html", {"id": id})


def notification_delete(request, id):
    notification = Add_notification.objects.get(id=id)
    notification.delete()
    return render(request, "add_notification.html", {})


def set_preferences(request):
    email = request.session["email"]
    candidate = Candidate.objects.get(email=email)
    if request.method == "POST":
        form = PreferenceForm(request.POST)
        print("hai", form.errors)
        if form.is_valid():
            form.save()
            return redirect("/view_preference")
    return render(request, "set_preference.html", {"id": candidate.id})


def view_preference(request):
    email = request.session['email']
    candidate = Candidate.objects.get(email=email)
    preferences = Preferences.objects.filter(candidate_id=candidate.id)
    print("hai")
    return render(request, "view_preference.html", {"preferences": preferences})


def preference_edit(request, id):
    preferences = Preferences.objects.get(id=id)
    return render(request, "preference_update.html", {"preferences": preferences})


def preference_update(request):
    global id
    email = request.session["email"]
    candidate = Candidate.objects.get(email=email)
    if request.method == "POST":
        id = request.POST["id"]
        preference = Preferences.objects.get(id=id)
        form = PreferenceForm(request.POST, instance=preference)
        print(form.errors)
        if form.is_valid():
            form.save()
            preferences = Preferences.objects.filter(candidate_id=candidate.id)
            return render(request, "view_preference.html", {"preferences": preferences})
    return render(request, "preference_update.html", {"id": id})


def preference_delete(request, id):
    preference = Preferences.objects.get(id=id)
    preference.delete()
    return redirect("/view_preference")


def view_notifications(request):
    notifications = Add_notification.objects.all()
    return render(request, "notifications.html", {"notifications": notifications})

def recomend(request):
    email=request.session["email"]
    canid=Candidate.objects.get(email=email)
    pref = Preferences.objects.filter(candidate=canid)
    skills=[]
    for p in pref:
        skills.append(p.technologies)
    recomend=Add_notification.objects.filter(skills_required__in=skills)
    return render(request, "recomend.html", {"recomend": recomend})


def resume_upload(request):
    email = request.session["email"]
    candidate = Candidate.objects.get(email=email)
    if request.method == "POST":
        form = ResumeForm(request.POST, request.FILES)
        print("hai", form.errors)
        if form.is_valid():
            form.save()
            return render(request, "resume.html", {"candidate": candidate.id})
    return render(request, "resume.html", {"candidate": candidate.id})


def applyjob(request, id):
    email = request.session["email"]
    customer = Candidate.objects.get(email=email)
    notifications = Add_notification.objects.get(id=id)
    print("hii")
    if request.method == 'POST':
        resume = ResumeForm(request.POST,request.FILES)
        if resume.is_valid:
            print("errors", resume.errors)
            resume.save()
            return render(request, "apply_job.html", {"msg": "job is posted", "id": notifications.id, "customer": customer.id})
    return render(request, "apply_job.html", {"id": notifications.id, "customer": customer.id})


def apply_display(request):
    email = request.session['email']
    person = Candidate.objects.get(email=email)
    resumes = Resume.objects.filter(person_id=person.id)
    return render(request, "application_applied.html", {"apply": resumes})


def job_applied(request, id):
    candatelist = Resume.objects.filter(notification_id=id)
    return render(request, "job_applied.html", {"applied": candatelist})


def job_approve(request, applied_id):
    approve = Resume.objects.get(id=applied_id)
    approve.job_status = 1
    approve.save()
    return redirect('/notification_view')


def job_reject(request, applied_id):
    reject = Resume.objects.get(id=applied_id)
    reject.job_status = 2
    reject.save()
    return redirect('/notification_view')

def unknown(request):
    return render(request,"candidate_home.html",{})


def empunknown(request):
    return render(request,"employer_home.html",{})