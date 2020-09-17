import time

from django.db.models import Q
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, CreateView, UpdateView, DeleteView
from .forms import PixaForm, UsersSignupForm, Authentication
from .models import UploadFile
import requests
from .api import get_api


class AjaxableResponseMixin:
    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.is_ajax():
            data = {
                'pk': self.object.pk,
            }
            return JsonResponse(data)
        else:
            return response


class BaseHome(TemplateView):
    template_name = 'admin/index.html'
    queryset = UploadFile.objects.all().order_by("id")[:4]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ImageList(ListView):
    template_name = 'admin/file_list.html'
    queryset = UploadFile.objects.all().order_by("id")[:4]


class FileUpload(AjaxableResponseMixin, CreateView):
    template_name = 'admin/file.html'
    form_class = PixaForm
    success_url = reverse_lazy("pixabay:image-panel")


# class PixabaySearch(AjaxableResponseMixin, TemplateView):
#     template_name = 'admin/baysearch.html'

    # def get_context_data(self, *args, **kwargs):
    #     context = {
    #         'req': get_api()
    #     }
    #     return context


def index(request):
    return render(request, 'admin/baysearch.html')


def result(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        url = f'https://pixabay.com/api/?key=18254741-ce7f3e60a43d460c4e262ec4f&q={query}&image_type=photo'
        pixabay = requests.get(url).json()
        image_info = {
            'webformat': pixabay['hits'][0]['webformatURL'],
            'width': pixabay['hits'][0]['imageWidth'],
            'height': pixabay['hits'][0]['imageHeight'],
            'views': pixabay['hits'][0]['views']
        }
        return render(request, 'admin/result.html', {'im': image_info})


class UpdateFile(AjaxableResponseMixin, UpdateView):
    model = UploadFile
    success_url = reverse_lazy('pixabay:image-panel')
    template_name = 'admin/file.html'
    form_class = PixaForm


class FileDelete(DeleteView):
    model = UploadFile
    success_url = reverse_lazy("pixabay:image-panel")
    template_name = 'admin/file_list.html'

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'GET':
            return super().post(self, *args, **kwargs)
        return super().dispatch()


def searchImage(request):
    search_keyword = request.GET['query']
    search_result = UploadFile.objects.filter(
        Q(file_name__icontains=search_keyword) | Q(file_format__icontains=search_keyword)).values('file_name',
                                                                                                  'file_format')
    search_result = list(search_result)
    return JsonResponse(search_result, safe=False)
