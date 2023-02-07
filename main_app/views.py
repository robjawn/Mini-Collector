from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from .models import Mini, Stock, Paint
from .forms import StockForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Define the home view
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def mini_index(request):
    minis = Mini.objects.all()
    return render(request, 'minis/index.html', { 'minis': minis })

@login_required
def mini_detail(request, mini_id):
    mini = Mini.objects.get(id=mini_id)
    latest_inventory = Stock.objects.order_by('-id').latest('date')
    paints_mini_doesnt_have = Paint.objects.exclude(id__in = mini.paints.all().values_list('id'))
    stock_form = StockForm()
    return render(request, 'minis/detail.html', { 'mini': mini, 'stock_form': stock_form, 'latest_inventory': latest_inventory, 'paints': paints_mini_doesnt_have })

@login_required
def add_stock(request, mini_id):
  form = StockForm(request.POST)
  if form.is_valid():
    new_stock = form.save(commit=False)
    new_stock.mini_id = mini_id
    new_stock.save()
  return redirect('detail', mini_id=mini_id)

@login_required
def assoc_paint(request, mini_id, paint_id):
  # Note that you can pass a toy's id instead of the whole object
  Mini.objects.get(id=mini_id).paints.add(paint_id)
  return redirect('detail', mini_id=mini_id)


def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

class MiniCreate(LoginRequiredMixin, CreateView):
    model = Mini
    fields = '__all__'
    success_url = '/minis/'

    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super().form_valid(form)

class MiniUpdate(LoginRequiredMixin, UpdateView):
    model = Mini
    fields ='__all__'

class MiniDelete(LoginRequiredMixin, DeleteView):
    model = Mini
    success_url = '/minis/'

class PaintIndex(LoginRequiredMixin, ListView):
    model = Paint

class PaintCreate(LoginRequiredMixin, CreateView):
    model = Paint
    fields = '__all__'

class PaintDetail(LoginRequiredMixin, DetailView):
    model = Paint

class PaintDelete(LoginRequiredMixin, DeleteView):
    model = Paint
    fields = '__all__'

class PaintUpdate(LoginRequiredMixin, UpdateView):
    model = Paint
    fields = '__all__'