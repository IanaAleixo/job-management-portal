from django.views import generic
from django.shortcuts import render, redirect, HttpResponse

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required

from django.contrib import messages

from app.jobs.models import Job, Application
from .forms import CreateCompanyUserForm, CreateCandidateUserForm, LoginForm, CreateJobForm, UpdateJobForm


# - Homepage 

def home(request):
    #return HttpResponse("Hello World")
    return render(request, 'jobs/index.html')

# - Register a user

def register_company(request):

    form = CreateCompanyUserForm()

    if request.method == "POST":

        form = CreateCompanyUserForm(request.POST)

        if form.is_valid():
            
            form.save()

            messages.success(request, "Account created successfully!")

            return redirect("dashboard")

    context = {'form':form}

    return render(request, 'jobs/register-company.html', context=context)

def register_candidate(request):

    form = CreateCandidateUserForm()

    if request.method == "POST":

        form = CreateCandidateUserForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request, "Account created successfully!")

            return redirect("dashboard")

    context = {'form':form}

    return render(request, 'jobs/register-candidate.html', context=context)



# - Login a user

def my_login(request):

    form = LoginForm()

    if request.method == "POST":

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:

                auth.login(request, user)

                return redirect("dashboard")

    context = {'form':form}

    return render(request, 'jobs/my-login.html', context=context)


# - Dashboard
def dashboard(request):

    jobs = Job.objects.all()

    context = {'jobs': jobs}

    return render(request, 'jobs/dashboard.html', context=context)

# - Create a job 

@login_required(login_url='my-login')
def create_job(request):

    form = CreateJobForm()

    if request.method == "POST":

        form = CreateJobForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request, "Your job opportinity was created!")

            return redirect("dashboard")

    context = {'form': form}

    return render(request, 'jobs/create-record.html', context=context)


# - Update a job 

@login_required(login_url='my-login')
def update_job(request, pk):

    record = Job.objects.get(id=pk)

    form = UpdateJobForm(instance=record)

    if request.method == 'POST':

        form = UpdateJobForm(request.POST, instance=record)

        if form.is_valid():

            form.save()

            messages.success(request, "Informations updated!")

            return redirect("dashboard")
        
    context = {'form':form}

    return render(request, 'jobs/update-record.html', context=context)


# - Read / View a singular job

@login_required(login_url='my-login')
def singular_job(request, pk):

    all_records = Job.objects.get(id=pk)

    context = {'job':all_records}

    return render(request, 'jobs/view-record.html', context=context)


# - Delete a job

@login_required(login_url='my-login')
def delete_job(request, pk):

    job = Job.objects.get(id=pk)

    job.delete()

    messages.success(request, "Job opportunity deleted!")

    return redirect("dashboard")


# - User logout

def user_logout(request):

    auth.logout(request)

    messages.success(request, "Logout success!")

    return redirect("my-login")

# - Apply to a job

@login_required(login_url='my-login')
def aplly_job(request, pk):

    job = Job.objects.get(id=pk)
    user = request.user
    Application.objects.create(job=job, user=user)

    messages.success(request, "Application succeed!")

    return redirect("dashboard")

# - List candidates

@login_required(login_url='my-login')
def candidates(request, pk):

    job = Job.objects.get(id=pk)

    context = {
        'job': job
    }

    return render(request, 'jobs/view-candidates.html', context=context)
