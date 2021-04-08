import random

from django.db.models import Count
from django.forms import modelformset_factory
from . import models
from .form import PropertyDetails, CustomerSignUpForm, AgentSignUpForm, PropertyImageForm, Agent_profile
from .models import Afeedback, Ufeedback, Agent, Comments_model,Customer
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect, render
from django.contrib import messages, auth
from django.views.generic import CreateView
from .models import User, Property, PropertyImage
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, \
    PageNotAnInteger


def index(request):
    posts = Property.objects.all()
    agents = Agent.objects.all()
    l1 = list(posts)
    if len(l1) >= 6:
        n = 6
    else:
        n = 3
    obj1 = random.sample(l1, n)
    l2 = list(agents)
    n1 = 3
    obj2 = random.sample(l2, n1)
    return render(request, 'index.html', {'posts': obj1, 'agents': obj2})


@login_required(login_url='/login')
def view_properties(request):
    if request.user.is_agent:
        user = request.user
        info1 = Comments_model.objects.filter(user=user)
        xlist = list(info1)
        print(xlist)
        xcount = len(xlist)
        print(xcount)

    if request.user.is_agent:
        id = request.user.id
        info = Property.objects.filter(agent=id)
    return render(request, 'view_properties.html', {'info': info, 'info1': info1, 'xcount': xcount})


@login_required(login_url='/login')
def a_notification(request):
    if request.user.is_agent:
        user = request.user
        print(user)
        info1 = Comments_model.objects.filter(user=user)
        xlist = list(info1)
        print(xlist)
        xcount = len(xlist)
        id = request.user.id
        print(id)
        info = Comments_model.objects.filter(user=id)
    return render(request, 'a_notification.html', {'info': info, 'info1': info1, 'xcount': xcount})


@login_required(login_url='/login')
def delete1(request, id):
    form3 = Comments_model.objects.get(pk=id)
    form3.delete()
    return redirect('a_notification')


@login_required(login_url='/login')
def customer_dashboard(request):
    return render(request, 'customer_dashboard.html')


def services(request):
    return render(request, 'services.html')


def about(request):
    agents = Agent.objects.all()
    paginator = Paginator(agents, 3)
    # 3 posts	in	each	page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If	page	is	out	of	range	deliver	last	page	of	results
        posts = paginator.page(1)
    except EmptyPage:
        # If	page	is	out	of	range	deliver	last	page	of	results
        posts = paginator.page(paginator.num_pages)
    return render(request, 'about.html', {'page': page, 'posts': posts})


def contact(request):
    return render(request, 'contact.html')


def agent_grid(request):
    agents = Agent.objects.all()
    paginator = Paginator(agents, 3)
    # 3 posts	in	each	page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If	page	is	out	of	range	deliver	last	page	of	results
        posts = paginator.page(1)
    except EmptyPage:
        # If	page	is	out	of	range	deliver	last	page	of	results
        posts = paginator.page(paginator.num_pages)
    return render(request, 'agent_grid.html', {'page': page, 'posts': posts})

#
# def ufeedback(request):
#     if request.method == "POST":
#         print(request)
#         subjects = request.POST.get('subject', '')
#         descriptions = request.POST.get('description', '')
#         print(subjects, descriptions)
#         feedback = Ufeedback(subject=subjects, description=descriptions)
#         feedback.save()
#     return render(request, 'ufeedback.html')


@login_required(login_url='/login')
def view_agent(request):
    if request.user.is_agent:
        user = request.user
        info1 = Comments_model.objects.filter(user=user)
        xlist = list(info1)
        print(xlist)
        xcount = len(xlist)
        print(xcount)

    if request.method == 'POST':
        form = Agent_profile(request.POST, request.FILES)
        if form.is_valid():
            a_mobile = form.cleaned_data['a_mobile']
            a_address = form.cleaned_data['a_address']
            a_company_name = form.cleaned_data['a_company_name']
            a_company_mobile = form.cleaned_data['a_company_mobile']
            a_company_address = form.cleaned_data['a_company_address']
            a_company_email = form.cleaned_data['a_company_email']
            a_dis = form.cleaned_data['a_dis']
            a_image = form.cleaned_data['a_image']
            edituser=Agent(
            user_id= request.user,
            a_mobile=a_mobile,
            a_address=a_address,
            a_company_name=a_company_name,
            a_company_mobile=a_company_mobile,
            a_company_address=a_company_address,
            a_company_email=a_company_email,
            a_dis = a_dis,
            a_image=a_image,
        )

            edituser.save()
            return render(request, 'view_agent.html')
    else:
        form = Agent_profile(instance=request.user)
        return render(request, 'view_agent.html', {'form':form, 'info1': info1, 'xcount': xcount})


@login_required(login_url='/login')
def add_property(request):
    if request.user.is_agent:
        user = request.user
        info1 = Comments_model.objects.filter(user=user)
        xlist = list(info1)
        print(xlist)
        xcount = len(xlist)
        print(xcount)
    ImageFormSet = modelformset_factory(models.PropertyImage, form=PropertyImageForm, extra=3)
    if request.method == 'POST':
        postForm = PropertyDetails(request.POST, request.FILES)
        formset = ImageFormSet(request.POST, request.FILES, queryset=models.PropertyImage.objects.none())

        if postForm.is_valid() and formset.is_valid():
            post_form = postForm.save(commit=False)
            post_form.agent = request.user
            post_form.save()
            for form in formset.cleaned_data:
                if 'images' in form:
                    image = form['images']
                    photo = models.PropertyImage(property=post_form, images=image)
                    photo.save()
            # messages.success(request,"Posted!")
            return redirect("agent_dashboard")
        # else:
        #     print
        #     postForm.errors, formset.errors
    else:
        postForm = PropertyDetails()
        formset = ImageFormSet(queryset=models.PropertyImage.objects.none())
    return render(request, 'add_property.html', {'postForm': postForm, 'formset': formset, 'info1': info1, 'xcount': xcount})


def property_grid(request):
    selected_type = None
    property = Property.objects.all()
    if request.method == "POST":
        selected_type = request.POST.get("type")
        property = Property.objects.filter(type=selected_type)
    type1 = Property.objects.values_list('type', flat=True).annotate(c=Count('type'))

    paginator = Paginator(property, 3)
    # 3 posts	in	each	page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If	page	is	out	of	range	deliver	last	page	of	results
        posts = paginator.page(1)
    except EmptyPage:
        # If	page	is	out	of	range	deliver	last	page	of	results
        posts = paginator.page(paginator.num_pages)
    return render(request, 'property_grid.html', {'posts': posts, 'type1': type1, 'selected_type': selected_type})


@login_required(login_url='/loginuser')
def agent_dashboard(request):
    if request.user.is_agent:
        user = request.user
        info1 = Comments_model.objects.filter(user=user)
        xlist= list(info1)
        print(xlist)
        xcount= len(xlist)
        print(xcount)
    return render(request, 'agent_dashboard.html', {'info1': info1, 'xcount': xcount})


@login_required(login_url='/login')
def update_property(request, id=0):
    if request.user.is_agent:
        user = request.user
        info1 = Comments_model.objects.filter(user=user)
        xlist = list(info1)
        print(xlist)
        xcount = len(xlist)
        print(xcount)

    form2 = Property.objects.get(pk=id)
    if id == 0:
        form = PropertyDetails(request.POST)
    else:
        form2 = Property.objects.get(pk=id)
        form = PropertyDetails(request.POST, request.FILES, instance=form2)
    if form.is_valid():
        form.save()
        return redirect('agent_dashboard')
    return render(request, "update_property.html", {'form2': form2, 'info1': info1, 'xcount': xcount})


@login_required(login_url='/login')
def delete(request, id):
    form3 = Property.objects.get(pk=id)
    form3.delete()
    return redirect('view_properties')


@login_required(login_url='/login')
def afeedback(request):
    if request.user.is_agent:
        user = request.user
        info1 = Comments_model.objects.filter(user=user)
        xlist = list(info1)
        print(xlist)
        xcount = len(xlist)
        print(xcount)

    if request.method == "POST":
        subject = request.POST.get('subject', '')
        description = request.POST.get('description', '')
        feedback = Afeedback(subject=subject, description=description)
        feedback.save()
    return render(request, 'afeedback.html', {'info1': info1, 'xcount': xcount})


@login_required(login_url='/login')
def ufeedback(request):
    if request.method == "POST":
        print(request)
        subjects = request.POST.get('subject', '')
        descriptions = request.POST.get('description', '')
        print(subjects, descriptions)
        feedback = Ufeedback(subject=subjects, description=descriptions)
        feedback.save()
    return render(request, 'ufeedback.html')


class customer_register(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = 'customer_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/login')


class agent_register(CreateView):
    model = User
    form_class = AgentSignUpForm
    template_name = 'agent_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/login')


def login_request(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        user = authenticate(username=username, password=password)
        # auth.login(request, user)
        if user is not None:
            auth.login(request, user)

            if request.user.is_customer:
                return redirect('customer_dashboard')
            elif request.user.is_agent:
                return redirect('agent_dashboard')
        else:
            messages.info(request, 'Invalid Credentials')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('/')


def property_single(request, id):
    post = get_object_or_404(Property, id=id, )
    post1 = Property.objects.filter(id=id)
    post2 = Property.objects.get(id=id)

    photos = PropertyImage.objects.filter(property=post)
    for p in post1:
        x = p.agent
    y = Agent.objects.filter(user=x)
    for p1 in y:
        img = p1.a_image.url
    if request.method == "POST":
        user = post2.agent
        name = request.POST.get('name', '')
        u_email = request.POST.get('u_email', '')
        comments = request.POST.get('comments', '')

        c = Comments_model(name=name, u_email=u_email, comments=comments,user=user)
        c.save()
    return render(request, 'property_single.html',
                  {'post': post, 'post1': post1, 'photos': photos, 'img': img})


@login_required(login_url='/login')
def u_properties(request):
    selected_status = None
    selected_type = None

    property = Property.objects.all()

    if request.method == "POST":
        selected_status = request.POST.get("status")
        selected_type = request.POST.get("type")
        property = Property.objects.filter(status=selected_status, type=selected_type)
    status1 = Property.objects.values_list('status', flat=True).annotate(c=Count('status'))
    status2 = Property.objects.values_list('type', flat=True).annotate(c=Count('type'))

    paginator = Paginator(property, 3)
    # 3 posts	in	each	page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If	page	is	out	of	range	deliver	last	page	of	results
        posts = paginator.page(1)
    except EmptyPage:
        # If	page	is	out	of	range	deliver	last	page	of	results
        posts = paginator.page(paginator.num_pages)
    return render(request, 'u_properties.html', {'posts': posts, 'property': property, 'selected_status': selected_status, 'status1': status1, 'status2': status2, 'selected_type': selected_type,})


def view_user(request):
    if request.user.is_customer:
        user = request.user
    customer = Customer.objects.filter(user=user)
    return render(request, 'view_user.html',{'customer': customer})

