from .models import *
from main.models import *

def extras (request): # add to templates in settings
   
    # query = ""
    # if request.GET:
    #     query = request.GET['q']
    #     context['query'] = str(query)
    genre = Genre.objects.all()

    context= {
        'genre': genre,
    }
   
    return context