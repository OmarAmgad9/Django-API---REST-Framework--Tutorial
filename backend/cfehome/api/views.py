from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.


def api_home(request):


    body = request.body

    print(body)
    return JsonResponse({'message': 'This message from api'})