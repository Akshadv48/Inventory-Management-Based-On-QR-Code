import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','inventory.settings')

import django
django.setup()


import random

from store.models import Owner,Installation,Maintainance

from faker import Faker

fake = Faker()
items_list =['Coffee maker', 'Blender', 'Mixer', 'Toaster', 'Microwave',
 'Crock pot', 'Rice cooker', 'Pressure cooker', 'Bachelor griller (U.K)', 
 'Stove', 'Lamp', 'Light bulb', 'Lantern', 'Torch', 'Clothes iron', 'Electric drill', 
 'Kettle', 'Water cooker (U.K)/ Electric kettle/ Hot pot (U.S)', 'Water purifier', 
 'Kitchen hood', 'Electric guitar', 'Vacuum cleaner', 'Electric fan', 'Evaporative cooler', 
 'Air conditioner', 'Oven', 'Dishwasher', 'Television', 'Speaker', 'Clothes dryer', 'Washing machine', 
 'Refrigerator']


def addOwner():
	owner_id  = int(random.randrange(1111111111,20000000000,1))
	owner_Fname = fake.first_name()
	owner_Lname = fake.last_name()
	registered_date = fake.date_time()

	ownr = Owner.objects.get_or_create(owner_id=owner_id,owner_Fname=owner_Fname,owner_Lname=owner_Lname,registered_date=registered_date)[0]
	
	return ownr

def populate(n=20):

	for I in range(n):
		ownr = addOwner()

		

		for i in range(15):

			installed_item = random.choice(items_list)
			item_id = random.randrange(516846,100051560,15)
			install_date = fake.date_time_between(start_date='-3y', end_date='now', tzinfo=None)
			inst = Installation.objects.get_or_create(owner=ownr,installed_item=installed_item,item_id=item_id,install_date=install_date)[0]

			for j in range(5):
				maintain_date = fake.date_time_between(start_date='-2y', end_date='now', tzinfo=None)
				Remarks = fake.sentence(nb_words=10, variable_nb_words=False)
				maint = Maintainance.objects.get_or_create(owner=ownr,maintain_item=installed_item,item_id=item_id,maintain_date=maintain_date,Remarks=Remarks)[0]

print("populating")
populate()
print('Done')