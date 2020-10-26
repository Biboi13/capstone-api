from django.shortcuts import  get_object_or_404, render, redirect

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import VCTSerializer,Prob_occurSerializer,RespondanceSerializer

# Create your views here.
from api.models import VCT,Prob_occur,Respondance


@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'VCT_list':'VCT_list',
        'VCT_add':'VCT_add',
        'VCT_update':'VCT_update',
        'VCT_delete':'VCT_delete',

        'Prob_occur_list':'Prob_occur_list',
        'Prob_occur_add':'Prob_occur_add',
        'Prob_occur_update':'Prob_occur_update',
        'Prob_occur_delete':'Prob_occur_delete',

        'Res_list':'Res_list',
        'Res_add':'Res_add',
        'Res_update':'Res_update',
        'Res_delete':'Res_delete',
 	}
	return Response(api_urls)

#View
@api_view(['GET'])
def VCT_list(request):
    vct = VCT.objects.all()
    serializer = VCTSerializer(vct, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def Prob_occur_list(request):
    prob = Prob_occur.objects.all()
    serializer = Prob_occurSerializer(prob, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def Res_list(request):
    res = Respondance.objects.all()
    serializer = RespondanceSerializer(res, many=True)
    return Response(serializer.data)


#Add
@api_view(['POST'])
def VCT_add(request):
    serializer = VCTSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def Prob_occur_add(request):
    serializer = Prob_occurSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def Res_add(request):
    serializer = RespondanceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


#Update
@api_view(['POST'])
def VCT_update(request, pk):
	vct = VCT.objects.get(id=pk)
	serializer = VCTSerializer(instance=vct, data=request.data)

	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

@api_view(['POST'])
def Prob_occur_update(request, pk):
	prob = Prob_occur.objects.get(id=pk)
	serializer = Prob_occurSerializer(instance=prob, data=request.data)

	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

@api_view(['POST'])
def Res_update(request, pk):
	res = Respondance.objects.get(id=pk)
	serializer = RespondanceSerializer(instance=res, data=request.data)

	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

#delete

@api_view(['DELETE'])
def VCT_delete(request, pk):
	vct = VCT.objects.get(id=pk)
	vct.delete()
	return Response('Item succsesfully delete!')

@api_view(['DELETE'])
def Prob_occur_delete(request, pk):
	prob = Prob_occur.objects.get(id=pk)
	prob.delete()
	return Response('Item succsesfully delete!')

@api_view(['DELETE'])
def Res_delete(request, pk):
	res = Respondance.objects.get(id=pk)
	res.delete()
	return Response('Item succsesfully delete!')
