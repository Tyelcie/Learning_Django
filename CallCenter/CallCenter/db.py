from django.http import HttpResponse
from cc.models import inbound

def opdb(request):
    response = ''
    response1 = ''

    list = inbound.objects.all()

    # response2 = inbound.objects.filter(id = 1)

    # response3 = inbound.objects.get(id = 1)

    # inbound.objects.order_by('general_source')[0:2]

    # inbound.objects.order_by('id')

    for var in list:
        response1 += var.general_source + '\n'
        response = response1
    return HttpResponse('<p>' + response + '</p>')
