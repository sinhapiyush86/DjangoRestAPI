from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import Temperature
from .serializers import TemperatureSerializer
from django.http import JsonResponse,HttpResponse
from rest_framework.parsers import JSONParser
from .serializers2 import TemperatureSerializer2

# Create your views here.
@csrf_exempt
def apimethod(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TemperatureSerializer(data=data,many=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201,safe=False)
        return JsonResponse(serializer.errors, status=400)
    elif request.method =='GET':
        tempdata = Temperature.objects.all()
        serialized_data = TemperatureSerializer2(tempdata,many=True)
        return JsonResponse({"key":serialized_data.data})
@csrf_exempt
def edit(request,id):
    obj = Temperature(pk=id)
    if request.method == 'PUT':
        data = JSONParser().parse(request)

        serializer = TemperatureSerializer(obj,data=data)

        if serializer.is_valid():
            serializer.save()
            return HttpResponse("Successfully updated")

    if request.method == 'DELETE':
        obj.delete()
        return HttpResponse("succesfully deleted")


    
	
