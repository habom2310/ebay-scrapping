from django.http import HttpResponse
from django.shortcuts import render
import ebay.scraper as scraper
from django.template import loader

def index(request):
    data = scraper.get_data()
    print(data[0])

    # template = loader.get_template('ebay/index.html')
    # context = {
    #     'data': data,
    # }
    # return HttpResponse(template.render(context, request))
    return render(request, 'ebay/index.html', {'data': data})
