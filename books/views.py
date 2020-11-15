from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView, FormView, CreateView
from .models import Book
from django.utils import timezone
from django.urls import reverse_lazy
from .forms import BookForm

# Create your views here.
class BookListView(ListView):
    model = Book
    template_name = 'books/index.html'
    context_object_name = "books"
    paginate_by = 2

class BookByGenreView(ListView):
    model = Book
    template_name = 'books/index.html'
    context_object_name = "books"
    paginate_by = 2

    def get_queryset(self, **kwargs):
        queryset = Book.objects.filter(category__name__icontains=self.kwargs.get('genre'))
        return queryset

class BookIndexView(TemplateView):
    template_name = "books/index.html"

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.all()
        return context

class BookDetailView(DetailView):
    model = Book
    context_object_name = "book"
    template_name = 'books/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        books = Book.objects.get(slug=self.kwargs.get('slug'))
        books.visits = books.visits + 1
        books.save()
        context['visitas'] = books.visits
        context['current_time'] = timezone.now()
        return context

# cuando se quiere usar un formulario para enviar una data
# no para guardar los datos.
class BookAddView(FormView):
    template_name = 'books/create.html'
    form_class = BookForm
    success_url = '/books/list'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

# esta es usada para crear un objeto en la base de datos
class BookStoreView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'books/create.html'
    success_url = reverse_lazy("books:books_list")

    # initial data in form
    def get_initial(self, *args, **kwargs):
        initial = super().get_initial(*args, **kwargs)
        initial['title'] = 'Enter title'
        return initial

