from django.shortcuts import render
from django.http import HttpResponse
from django.conf.global_settings import STATICFILES_DIRS


# Create your views here.


def test(request):
    print(STATICFILES_DIRS)
    context = {'hello': 'Hello World!'}
    return render(request, 'insight/test.html', context)
    #return HttpResponse('<html><body>Hello my Django</body></html>')
