from django.db.models import Q
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Books
# Create your views here.

@csrf_exempt
def book_list(request):
    books = ''
    q = request.GET.get('q')
    
    if q:
        books = Books.objects.filter(name = q)
    else:
        books = Books.objects.all()
    data = {'books': []}
    for book in books:
        data['books'].append({
            'name': book.name,
            'author': book.author,
        })
    return JsonResponse(data)