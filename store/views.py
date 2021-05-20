#python Libs
import json
import copy

from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.utils import timezone

#
from .models import *

#
# Create your views here.
def getOwnerInfo(o_id):
	owner_info = list(Owner.objects.filter(owner_id=str(o_id)).values())
	if len(owner_info) == 0:
		return "notfound"
	return owner_info

def get_installation_Info(o_id):
	#try:
	Installation_info = list(Installation.objects.filter(owner_id=str(o_id)).values_list('installed_item','item_id','install_date'))
		
	return Installation_info if len(Installation_info) > 0 else "No Installations Done Yet"

	#except IndexError:
		#return "No Installations Done Yet"

def get_mainatainance_date(o_id):
	try:
		Maintainance_info = list(Maintainance.objects.filter(owner_id=str(o_id)).values_list('maintain_date').order_by('-maintain_date')[:1])
		return (str(Maintainance_info[0][0])[:10] if type(Maintainance_info) == list else Maintainance_info)
	except IndexError:
		return "No Maintainace Done Yet"



def get_maintainance_info_item(request,o_id,i_id):
	try:

		Main_hist = list(Maintainance.objects.filter(owner_id=str(o_id)).filter(item_id=str(i_id)).values_list('owner_id','maintain_item','item_id','maintain_date','Remarks').order_by('-maintain_date'))

		owner_info = getOwnerInfo(o_id)

		details_dict ={}

		for i in owner_info[0]:
			details_dict[i] = owner_info[0][i]

		details_dict['maint_his'] = Main_hist
		#return JsonResponse(details_dict,safe=False)


		return render(request,"maininfo.html",details_dict);
	except IndexError:
		return HttpResponse('No Maintainance Records for \'user-id\' : \'%d\''%(o_id))




def GetDetails(request,o_id):
	try : 
		details_dict = {}
		owner_info = list(Owner.objects.filter(owner_id=str(o_id)).values())
		Installation_info = get_installation_Info(o_id)
		Maintainance_info = get_mainatainance_date(o_id)

		#print(Installation_info,Maintainance_info)
		#print(Installation_info)
		for i in owner_info[0]:
			details_dict[i] = owner_info[0][i]

		details_dict['installed_item'] = Installation_info
		details_dict['last_maintainance_on'] = Maintainance_info

		#print(details_dict)
		return JsonResponse(details_dict,safe=False)
	except IndexError:
		return JsonResponse({"error":"notfound"},safe=False)
		#return HttpResponse("<center><H1> The User with \'user-id\' : \' %d \' Is Not Registered!</H1><br>SomeThing Fishy is Going On!...</center>"%(o_id))
	
def GetDetails2(request,o_id):
	try : 
		details_dict = {}
		owner_info = list(Owner.objects.filter(owner_id=str(o_id)).values())
		Installation_info = get_installation_Info(o_id)
		Maintainance_info = get_mainatainance_date(o_id)

		#print(Installation_info,Maintainance_info)
		#print(Installation_info)
		for i in owner_info[0]:
			details_dict[i] = owner_info[0][i]


		details_dict['installed_item'] = Installation_info
		details_dict['last_maintainance_on'] = Maintainance_info
		details_dict['title'] = "Owner Details"

		#print(details_dict)
		#return JsonResponse(details_dict,safe=False)
		return render(request,"info.html",details_dict);
	except IndexError:
		#return JsonResponse({"error":"notfound"},safe=False)
		return HttpResponse("<center><H1> The User with \'user-id\' : \' %d \' Is Not Registered!</H1><br>SomeThing Fishy is Going On!...</center>"%(o_id))

def getOwnerInfo(o_id):
	owner_info = list(Owner.objects.filter(owner_id=str(o_id)).values())
	if len(owner_info) == 0:
		return "notfound"
	return owner_info



def index(request):
	if request.method == 'POST':
		x= request.POST['owner_id']
		if len(x)<=0:
			return render(request,"sc.html",{"title":"Home","error":"ID Must Not be Empty"});
			
		else:
			ans = getOwnerInfo(x)
			if ans  == "notfound":
				return render(request,"sc.html",{"title":"Home","error":"invalid ID Try again"});
			else:
				#print(ans)
				return GetDetails2(request,x);
				#return render(request,"sc.html",{"title":"Home","owner_id":ans[0][1]});

	return render(request,"sc.html",{"title":"Home"});


def Maintainance_rec(request,o_id):
	try:
		details_dict={}
		owner_info = list(Owner.objects.filter(owner_id=str(o_id)).values())
		Main_hist = list(Maintainance.objects.filter(owner_id=str(o_id)).values_list('owner_id','maintain_item','item_id','maintain_date','Remarks').order_by('maintain_date'))

		for i in owner_info[0]:
			details_dict[i] = owner_info[0][i]

		details_dict['maint_his'] = Main_hist

		if len(Main_hist) == 0:
			raise IndexError
		return render(request,"maininfo.html",details_dict);
		#return JsonResponse(Main_hist,safe=False)

	except IndexError:
		return HttpResponse('No Maintainance Records for \'user-id\' : \'%d\''%(o_id))



def Add_owner(request,o_id,o_namef,o_namel):

	ll = list(Owner.objects.filter(owner_id=str(o_id)).values())
	if len(ll) == 0:
		o_info = Owner(owner_id=int(o_id),
					owner_Fname=str(o_namef),
					owner_Lname=str(o_namel),
					registered_date=timezone.now())
		o_info.save()
	#q = QueryDict(di_ct)
	return HttpResponse(list(Owner.objects.filter(owner_id=str(o_id)).values()))


def Add_owner_installation(request,o_id,install_item,item_id1):

	Installation.objects.create(owner_id=o_id,installed_item=install_item,item_id=item_id1,install_date=timezone.now())

	return HttpResponse(list(Installation.objects.filter(owner_id=str(o_id)).values_list('installed_item','item_id','install_date')))


def Add_owner_maintainance(request,o_id,installed_item,item_id1,remarks):

	Maintainance.objects.create(owner_id=o_id,maintain_item=installed_item,item_id=item_id1,maintain_date=timezone.now(),Remarks=remarks)

	return HttpResponse(list(Maintainance.objects.filter(owner_id=str(o_id)).values()))