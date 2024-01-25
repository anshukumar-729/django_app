from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from back.models import Form
import json 

def homepage(request):
    data = Form.objects.all()
    data_list = [{'name': item.name, 'id_num': item.id_num} for item in data]
    print(data_list)
    return JsonResponse({"data":data_list})


@csrf_exempt
@require_POST
def save(request):
    try:
        if(request.method=="POST"):
            data = json.loads(request.body)
            # print(data)
            temp = Form.objects.filter(id_num=int(data['id_num'])).exists()
            if(not temp):
                newData = Form(name=data['name'],id_num=int(data['id_num']))
                newData.save()

    except:
        print("passing")
        pass
    data = Form.objects.all()
    data_list = [{'name': item.name, 'id_num': item.id_num} for item in data]
    print(data_list)
    return JsonResponse({"data":data_list})


@csrf_exempt
@require_POST
def delete(request):
    try:
        if(request.method=="POST"):
            data = json.loads(request.body)
            print(data)
            temp = Form.objects.filter(id_num=int(data['id_num'])).exists()
            if(temp):
                newData = Form.objects.get(id_num=int(data['id_num']))
                newData.delete()

    except:
        print("passing")
        pass
    data = Form.objects.all()
    data_list = [{'name': item.name, 'id_num': item.id_num} for item in data]
    print(data_list)
    return JsonResponse({"data":data_list})


@csrf_exempt
@require_POST
def update(request):
    try:
        if(request.method=="POST"):
            data = json.loads(request.body)
            print(data)
            temp = Form.objects.filter(id_num=int(data['id_num'])).exists()
            if(temp):
                newData = Form.objects.get(id_num=int(data['id_num']))
                newData.name = data['name']
                newData.id_num = int(data['id_num'])
                newData.save()

    except:
        print("passing")
        pass
    data = Form.objects.all()
    data_list = [{'name': item.name, 'id_num': item.id_num} for item in data]
    print(data_list)
    return JsonResponse({"data":data_list})
