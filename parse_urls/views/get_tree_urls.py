from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View
from bs4 import BeautifulSoup
import json


def parse(url_to_parse, list_all_url, result, main_url):
    soup = BeautifulSoup(url_to_parse)
    return soup.prettify()


class GetUrlToParse(View):

    def get(self, request):
        return render(request, 'InputForm.html')

    def post(self, request):
        result = parse(url_to_parse=request.POST.get('search'), list_all_url=[], result={},
                       main_url=request.POST.get('search'),)
        print(result)
        data = json.dumps(result)
        return HttpResponse(data, content_type='application/json')


