from django.test import TestCase
from django.contrib.auth.models import User
from .models import NeighborHood


class NeighborTestClass(TestCase):
    def setUp(self):
        user = User.objects.create_user(username="john",email="john@gmail.com",password="pass123")
        self.neighbor = NeighborHood(name = 'Embakasi',location = 'Nairobi',admin = user,about='This has been the best neighborhood',administrator='John doe',doctor_no='0937293',police_num='0292002')
        self.neighbor.save_hood()

    def test_get_neighborhood(self):
        my_hood = NeighborHood.my_neighbor(name)
        self.assertTrue(len(my_hood)==0)

    def test_save_hood(self):
        self.neighbor.save_hood()
        my_hood =NeighborHood.objects.all()
        self.assertTrue(len(my_hood) > 0)