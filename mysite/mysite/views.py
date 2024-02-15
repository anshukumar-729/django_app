from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from rest_framework.decorators import api_view
from rest_framework import status,viewsets
from django.db.models import Q
from back.models import Form
from back.models import Posts
import json 

def homepage(request):
    data = Form.objects.all()
    data_list = [{'name': item.name, 'id_num': item.id_num} for item in data]
    print(data_list)
    return JsonResponse({"data":data_list})


@api_view(['POST'])
def create_post(request):
    title = ''
    desc = ''
    data = json.loads(request.body)
    try:
        # title = data['title_var']
        # desc = data['desc_var']
        # Posts.objects.create(title_var=title,desc_var = desc)

        new_data = Posts()
        new_data.title_var = data['title_var']
        new_data.desc_var = data['desc_var']
        new_data.save()
        return Response("Created",status=status.HTTP_201_CREATED)
    except:
        return Response("Unable to create",status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
def get_or_create_post(request):
    title = ''
    desc = ''
    data = json.loads(request.body)
    try:
        title = data['title_var']
        desc = data['desc_var']
        Posts.objects.get_or_create(title_var=title,desc_var=desc)
        return Response("Created",status=status.HTTP_201_CREATED)
    except:
        return Response("Unable to create",status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def bulk_create_post(request):
    data = json.loads(request.body)
    try:
        new_data = []
        for val in data["data"]:
            new_object = Posts(title_var=val["title_var"],desc_var=val["desc_var"])
            new_data.append(new_object)
        Posts.objects.bulk_create(new_data)
        return Response("Created",status=status.HTTP_201_CREATED)
    except:
        return Response("Unable to create",status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def update_post(request):
    data = json.loads(request.body)
    try:
        new_object = Posts.objects.get(id_var=data["id_var"])
        new_object.title_var = "new_title"
        new_object.save()
        return Response("Updated",status=status.HTTP_200_OK)
    except:
        return Response("Unable to Update",status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def update_or_create_post(request):
    data = json.loads(request.body)
    try:
        Posts.objects.update_or_create(
            title_var=data["title_var"],
            defaults={
                "title_var":data["title_var"],
                "desc_var": data["desc_var"]
            }
        )
        return Response("Updated",status=status.HTTP_200_OK)
    except:
        return Response("Unable to Update",status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def bulk_update_post(request):
    data = json.loads(request.body)
    try:
        queryset = Posts.objects.filter(title_var=data["title_var"])
        for i in queryset:
            i.desc_var = data["desc_var"]
        Posts.objects.bulk_update(queryset,["desc_var"])
        return Response("Updated",status=status.HTTP_200_OK)
    except:
        return Response("Unable to Update",status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_post(request):
    data = json.loads(request.body)
    try:
        # print(request.GET.get("id"))
        # new_data = Posts.objects.all()
        # new_data = Posts.objects.get(id_var = data["id_var"]) #throw error in multiple row
        # new_data = Posts.objects.all().order_by("-id_var").filter(title_var = data["title_var"]).exclude(id_var=data["id_var"])[0:3]
        # new_data = Posts.objects.filter(id_var__in=[1,2,3,4,5,6])
        # new_data = Posts.objects.all().values("title_var","desc_var")
        new_data = Posts.objects.all().values_list("title_var",flat=True)
        # print(new_data)
        # new_data = [{"id":val.id_var,"title_var":val.title_var,"desc_var":val.desc_var} for val in new_data]
        return Response({"data":new_data},status=status.HTTP_200_OK)
    except:
        return Response("Unable to get the data",status=status.HTTP_400_BAD_REQUEST)
    
    return HttpResponse("nothing")


@api_view(['GET'])
def get_Q_filter_post(request):
    data = json.loads(request.body)
    try:
        # new_data = Posts.objects.filter(Q(id_var=data["id_var"])|Q(title_var=data["title_var"]))
        # new_data = Posts.objects.filter(Q(id_var=data["id_var"])&Q(title_var=data["title_var"]))
        # new_data = Posts.objects.filter(~Q(id_var=data["id_var"])&Q(title_var=data["title_var"]))
        new_data = Posts.objects.filter(Q(id_var=data["id_var"])&Q(title_var=data["title_var"])&Q(desc_var=data["desc_var"]))
        new_data = [{"id":val.id_var,"title_var":val.title_var,"desc_var":val.desc_var} for val in new_data]
        return Response({"data":new_data},status=status.HTTP_200_OK)
    except:
        return Response("Unable to get the data",status=status.HTTP_400_BAD_REQUEST)
    
    return HttpResponse("nothing")


@api_view(['GET'])
def get_lookup_post(request):
    data = json.loads(request.body)
    try:
        # new_data = Posts.objects.filter(title_var__exact=data["title_var"])
        # new_data = Posts.objects.filter(title_var__iexact=data["title_var"])
        # new_data = Posts.objects.filter(title_var__startswith=data["title_var"])
        # new_data = Posts.objects.filter(title_var__istartswith=data["title_var"])
        # new_data = Posts.objects.filter(title_var__contains=data["title_var"])
        # new_data = Posts.objects.filter(title_var__icontains=data["title_var"])
        # new_data = Posts.objects.filter(title_var__endswith=data["title_var"])
        # new_data = Posts.objects.filter(title_var__iendswith=data["title_var"])
        # new_data = Posts.objects.filter(id_var__in=[1,2,3])
        # new_data = Posts.objects.filter(id_var__gt=2)
        # new_data = Posts.objects.filter(id_var__gte=2)
        # new_data = Posts.objects.filter(id_var__lt=4)
        # new_data = Posts.objects.filter(id_var__lte=4)
        new_data = [{"id":val.id_var,"title_var":val.title_var,"desc_var":val.desc_var} for val in new_data]
        return Response({"data":new_data},status=status.HTTP_200_OK)
    except:
        return Response("Unable to get the data",status=status.HTTP_400_BAD_REQUEST)
    
    return HttpResponse("nothing")





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
