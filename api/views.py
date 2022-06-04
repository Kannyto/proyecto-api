from operator import le
from django.http import JsonResponse
from django.utils.decorators import method_decorator
# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.views import View
import json, urllib
import requests

from .models import Company

# Create your views here.

class CompanyView(APIView):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def generate_request(url, params={}):
        response = requests.get(url, params=params)

        if response.status_code == 200:
            return response.json()

    def get_username(params={}):
        response = generate_request('https://randomuser.me/api', params)
        if response:
            user = response.get('results')[0]
            return user.get('name').get('first')

        return ''"

#     def get(self,request,id=0):
#         if (id>0):
#             companies=list(Company.objects.filter(id=id).values())
#             if len(companies)> 0:
#                 company=companies[0]
#                 datos={'mensaje':'Correcto','companies':company}
#             else:
#                 datos={'mensaje':'Companias no encontradas'}
#             return JsonResponse(datos)
#         else:
#             companies=list(Company.objects.values())
#             if len(companies)>0:
#                 datos={'mensaje':'Correcto','companies':companies}
#             else:
#                 datos={'mensaje':'Companies no encontradas'}
#             return JsonResponse(datos)
    
#     def post(self,request):
#         # print(request.body)
#         jd=json.loads(request.body)
#         # print(jd)
#         Company.objects.create(name=jd['name'],website=jd['website'],fundacion=jd['fundacion'])
#         datos={'mensaje':'Correcto'}
#         return JsonResponse(datos)

#     def put(self,request,id=0):
#         jd=json.loads(request.body)
#         companies=list(Company.objects.filter(id=id).values())
#         if len(companies)> 0:
#             company=Company.objects.get(id=id)
#             company.name=jd['name']
#             company.website=jd['website']
#             company.fundacion=jd['fundacion']
#             company.save()
#             datos={'mensaje':'Correcto'}
#         else:
#             datos={'mensaje':'Companias no encontradas'}
#         return JsonResponse(datos)

#     def delete(self,request,id=0):
#         companies=list(Company.objects.filter(id=id).values())
#         if len(companies)> 0:
#             Company.objects.filter(id=id).delete()
#             datos={'mensaje':'Correcto'}
#         else:
#             datos={'mensaje':'Companies no encontradas'}
#         return JsonResponse(datos)
