#-*- coding: utf-8-*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from django.views.generic import ListView, DetailView
from trans.models import TransactsModel
from trans.forms import TransactsForm, SignUpForm
import datetime
import logging

logger = logging.getLogger('views')


def index(request):
    isAuth = auth.get_user(request).username
    context = {'isAuth': isAuth}
    return render(request, 'index.html', context)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            logger.info('signup user: ' + username)
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form, 'level_1': True})


@login_required(login_url='login')
def tr_add(request):
    if request.method == "POST":
        form = TransactsForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.id = TransactsModel.objects.get_id()
            post.created_dt = datetime.datetime.today()
            post.save()
            return redirect('all_trans')
    else:
        form = TransactsForm()
        return render(request, 'trans_add.html', {'form': form, 'isAuth': True, 'level_1': True})


@login_required(login_url='login')
def tr_edit(request, pk):
    tr = get_object_or_404(TransactsModel, pk=pk)
    if request.method == "POST":
        form = TransactsForm(request.POST, instance=tr)
        if form.is_valid():
            tr = form.save(commit=False)
            tr.user = request.user
            tr.save()
            return redirect('one_tr', pk=pk)
    else:
        form = TransactsForm(instance=tr)
    return render(request, 'trans_edit.html', {'form': form, 'isAuth': True, 'level_2': True})


class TransListView(ListView):
    model = TransactsModel
    paginate_by = 1
    context_object_name = 'trs'

    template_name = 'trans.html'

    def get_queryset(self):
        qs = TransactsModel.objects.get_all_trans(self.request.user.id)
        return qs

    def get_context_data(self, **kwargs):
        context = super(TransListView, self).get_context_data(**kwargs)
        context['isAuth'] = auth.get_user(self.request).username
        context['level_1'] = True
        return context


class TransactDetail(DetailView):
    model = TransactsModel

    context_object_name = 'tr'
    template_name = 'transact.html'

    def get_context_data(self, **kwargs):
        context = super(TransactDetail, self).get_context_data(**kwargs)
        context['isAuth'] = auth.get_user(self.request).username
        context['level_2'] = True
        return context

    def get_object(self):
        object = super(TransactDetail, self).get_object()
        return object


def u_logout(request):
    logout(request)
    return redirect('index')


def u_login(request):
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('index')
        else:
            logger.info('failed login user: ' + username)
            return render(request, 'login.html', {'error_login': True, 'level_1': True})
    else:
        return render(request, 'login.html')

