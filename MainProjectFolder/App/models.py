from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
#from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils import timezone
from django.conf import settings
from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver
# Create your models here.

class MyUserManager(BaseUserManager):
    def create_user(self, email, username,phone, password=None):
        if not email:
            raise ValueError("email is required")
        if not username:
            raise ValueError("Your user name is required")


        
        

        user=self.model(
            email=self.normalize_email(email),
            username=username,
            phone=phone,
            
            
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, phone, username, password=None):
        user=self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            phone=phone,

        )
        user.is_admin=True
        user.is_staff=True
        user.is_customer=False
        
        user.is_superuser=True
        user.save(using=self._db)
        return user

    

  
class MyUser(AbstractBaseUser):
    email=models.EmailField(verbose_name="email", max_length=100, unique=True)
    first_name=models.CharField(verbose_name="first name", max_length=100, unique=False)
    username=models.CharField(verbose_name="user name", max_length=100, unique=True)
    middle_name=models.CharField(verbose_name="middle name", max_length=100, unique=False)
    last_name=models.CharField(verbose_name="last name", max_length=100, unique=False)
    company_name=models.CharField(verbose_name="company name", max_length=100, unique=False)
    phone=models.CharField(verbose_name="phone", max_length=15)
    profile_image = models.ImageField(upload_to='media/', blank=True, null=True)
    date_joined=models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    # Role_Choices = (
    #         ('MULTI TEACHER', 'MULTI TEACHER'),
    #         ('PHYSICS TEACHER', 'PHYSICS TEACHER'),
    #         ('CHEMISTRY TEACHER', 'CHEMISTRY TEACHER'),
    #         ('BIOLOGY TEACHER', 'BIOLOGY TEACHER'),
    #         ('ENGLISH TEACHER', 'ENGLISH TEACHER'),
    #         ('CIVICS TEACHER', 'CIVICS TEACHER'),
    #         ('MATHEMATICS TEACHER', 'MATHEMATICS TEACHER'),
    #         ('HISTORY TEACHER', 'HISTORY TEACHER'),
    #         ('GEOGRAPHY TEACHER', 'GEOGRAPHY TEACHER'),
    #         ('KISWAHILI TEACHER', 'KISWAHILI TEACHER'),
    #     )

    # role=models.CharField(verbose_name="role", choices=Role_Choices, max_length=50)
    last_login=models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=False)
    is_customer=models.BooleanField(default=True)

    hide_email = models.BooleanField(default=True)

    


    USERNAME_FIELD="username"
    REQUIRED_FIELDS=['email','phone']
    
    objects=MyUserManager()

    def __str__(self):
        return self.username


    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True





class Huduma(models.Model):
    
    JinaLaHuduma = models.CharField(verbose_name="Jina La Huduma",max_length=100, blank=False,null=False)
    PichaYaHuduma = models.ImageField(verbose_name="Picha Ya Huduma", upload_to='media/PichaZaHuduma/',blank=True,null=True)
    
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.JinaLaHuduma}"
    
    class Meta:
        verbose_name_plural = "Huduma"

class MgawanjoWaHuduma(models.Model):
    Category = models.ForeignKey(Huduma, verbose_name="Category",on_delete=models.CASCADE, blank=True,null=True)
    
    JinaLaHuduma = models.CharField(verbose_name="Jina La Huduma",max_length=100, blank=False,null=False)
    PichaYaHuduma = models.ImageField(verbose_name="Picha Ya Huduma", upload_to='media/PichaZaHuduma/',blank=True,null=True)
    
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.JinaLaHuduma}"
    
    class Meta:
        verbose_name_plural = "Mgawanjo Wa Huduma"



class UmriWaKuku(models.Model):
    
    UmriKwaWiki = models.IntegerField(verbose_name="Wiki ?", blank=False,null=False)
    UmriKwaSiku = models.IntegerField(verbose_name="Siku ? (Usijaze)", blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Wiki {self.UmriKwaWiki}, Siku {self.UmriKwaSiku}"
    
    class Meta:
        verbose_name_plural = "Umri Wa Kuku"

@receiver(pre_save, sender=UmriWaKuku)
def set_UmriKwaSiku(sender, instance, **kwargs):
    # Check if the instance is new (i.e., it doesn't have a primary key yet)
    if instance._state.adding:
        instance.UmriKwaSiku = instance.UmriKwaWiki * 7



class AinaZaKuku(models.Model):
    
    AinaYaKuku = models.CharField(verbose_name="Aina Ya Kuku",max_length=100, blank=False,null=False)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.AinaYaKuku}"
    
    class Meta:
        verbose_name_plural = "Aina Za Kuku"




class UnitZaVyakula(models.Model):
    
    Unit = models.CharField(verbose_name="Unit", max_length=500,blank=False,null=False)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.Unit
    
    class Meta:
        verbose_name_plural = "Unit Za Vyakula"

class Vyakula(models.Model):
    
    
    product_name = models.CharField(verbose_name="Jina La Chakula", max_length=100,blank=False,null=False)
    ProductDescription = models.TextField(verbose_name="Maelezo", max_length=10000,blank=True,null=True)
    InitialPrice = models.IntegerField(verbose_name="Bei Ya Mwanzo Ya Chakula", blank=True,null=True)
    price = models.IntegerField(verbose_name="Bei Ya sasa Ya Chakula (Usijaze)", blank=True,null=True)   
    #ProductUnit = models.CharField(verbose_name="Product Unit", max_length=100,blank=True,null=True)
    ProductQuantity = models.IntegerField(verbose_name="Kiasi - KG (Usijaze)",default=1, blank=True,null=True)
    #InitialProductQuantity = models.IntegerField(verbose_name="Kiasi Cha Mwanzo Store-KG (Usijaze)",blank=True,null=True)    
    Unit = models.ForeignKey(UnitZaVyakula, verbose_name="Unit Ya Chakula",on_delete=models.CASCADE, blank=True,null=True)
    ProductImage = models.ImageField(verbose_name="Picha Ya Chakula", upload_to='media/PichaZaVyakula/',blank=True,null=True)

    

    #Hutakiwi kujaza Hizi
    # Protini_In_1Kg = models.IntegerField(verbose_name="Kiwango Cha Protini - % Kwenye 1Kg Ya Chakula", blank=True,null=True)

    
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)

    
    
    class Meta:
        verbose_name_plural = "Vyakula"
        
    
    def __str__(self):
        return f" {self.product_name} "


# @receiver(pre_save, sender=ProductsStores)
# def Products__initial_quantity(sender, **kwargs):
#     Initial_qty = kwargs['instance']
#     Initial_qty.InitialProductQuantity = Initial_qty.ProductQuantity
#     # total_cart_items = CartItems.objects.filter(user = cart_items.user )
#     # cart = Cart.objects.get(id = cart_items.cart.id)
#     # cart.total_price = cart_items.price
#     # cart.save()

#@receiver(pre_save, sender=Vyakula)
# def set_initial_quantity(sender, instance, **kwargs):
#     # Check if the instance is new (i.e., it doesn't have a primary key yet)
#     if instance._state.adding:
#         instance.InitialProductQuantity = instance.ProductQuantity

@receiver(pre_save, sender=Vyakula)
def set_price_from_initial_price(sender, instance, **kwargs):
    # Check if the instance is new (i.e., it doesn't have a primary key yet)
    if instance._state.adding:
        instance.price = instance.InitialPrice








class Virutubisho(models.Model):
    JinaLaChakula = models.ForeignKey(Vyakula, verbose_name="Jina La Chakula",on_delete=models.CASCADE, blank=True,null=True)  
    Protini = models.IntegerField(verbose_name="Kiwango Cha Protini- %", blank=False,null=False)
    Cabohydrate = models.IntegerField(verbose_name="Kiwango Cha Cabohydrate- %", blank=False,null=False)
    Wanga = models.IntegerField(verbose_name="Kiwango Cha Wanga- %", blank=False,null=False)
    Fati = models.IntegerField(verbose_name="Kiwango Cha Fati- %", blank=False,null=False)
    Vitamini = models.IntegerField(verbose_name="Kiwango Cha Vitamini- %", blank=False,null=False)
    
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Wiki {self.JinaLaChakula.product_name}"
    
    class Meta:
        verbose_name_plural = "Umri Wa Kuku"





class TaarifaZaKuku(models.Model):

    # Hapa utajaza kila aina ya kuku na kwa kila Chakula na kwa kila wiki
    # Eg: AinaYaKuku: Stata
    #     UmriKwaWiki: Wiki 1
    #     JinaLaChakula: Mahindi
    #     KiwangoChaProtini_In_1Kg: 80%
    #     KiwangoChaWanga_In_1Kg: 80%, etc


    AinaYaKuku = models.ForeignKey(AinaZaKuku, verbose_name="Aina Ya Kuku",on_delete=models.CASCADE, blank=True,null=True)
    UmriKwaWiki = models.ForeignKey(UmriWaKuku, verbose_name="Umri Wa Kuku - Wiki ?",on_delete=models.CASCADE, blank=True,null=True)
    JinaLaChakula = models.ForeignKey(Vyakula, verbose_name="Jina La Chakula",on_delete=models.CASCADE, blank=True,null=True)

    #-------------------KWA WIKI YA KWANZA-----------------
    KiasiChaChakulaKwaWiki_1 = models.IntegerField(verbose_name="Kiasi Cha Chakula Kwa Wiki 1 - KG ", default=0, blank=True,null=True)

    Protini = models.IntegerField(verbose_name="Kiwango Cha Protini - % Kwenye 1Kg Ya Chakula", default=0, blank=True,null=True)
    Cabohydrate = models.IntegerField(verbose_name="Kiwango Cha Cabohydrate- %", default=0, blank=True,null=True)
    Wanga = models.IntegerField(verbose_name="Kiwango Cha Wanga- %", default=0, blank=True,null=True)
    Fati = models.IntegerField(verbose_name="Kiwango Cha Fati- %", default=0, blank=True,null=True)
    Vitamini = models.IntegerField(verbose_name="Kiwango Cha Vitamini- %", default=0, blank=True,null=True)

    #HIZI HATAKIWI KUJAZA KWA WIKI YA 1
    KiasiChaProtiniKilichopokwenye_KiasiChaChakulaKwaWiki_1 = models.IntegerField(verbose_name="Kiasi Cha Protini Kwa Wiki 1 - KG (Usijaze)",default=0,  blank=True,null=True)
    KiasiChaWangaKilichopokwenye_KiasiChaChakulaKwaWiki_1 = models.IntegerField(verbose_name="Kiasi Cha Wanga Kwa Wiki 1 - KG (Usijaze)",default=0,  blank=True,null=True)
    KiasiChaCabohydrateKilichopokwenye_KiasiChaChakulaKwaWiki_1 = models.IntegerField(verbose_name="Kiasi Cha Cabohydrate Kwa Wiki 1 - KG (Usijaze)",default=0,  blank=True,null=True)
    KiasiChaVitaminiKilichopokwenye_KiasiChaChakulaKwaWiki_1 = models.IntegerField(verbose_name="Kiasi Cha Vitamini Kwa Wiki 1 - KG (Usijaze)",default=0,  blank=True,null=True)
    KiasiChaFatiKilichopokwenye_KiasiChaChakulaKwaWiki_1 = models.IntegerField(verbose_name="Kiasi Cha Fati Kwa Wiki 1 - KG (Usijaze)", default=0, blank=True,null=True)  

    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Wiki {self.AinaYaKuku.AinaYaKuku}"
    
    class Meta:
        verbose_name_plural = "Taarifa Za Kuku"



#----------------------KWA WIKI YA 1------------------------------
@receiver(pre_save, sender=TaarifaZaKuku)
def set_KiasiChaProtiniKilichopokwenye_KiasiChaChakulaKwaWiki_1(sender, instance, **kwargs):
    # Check if the instance is new (i.e., it doesn't have a primary key yet)
    if instance._state.adding:
        instance.KiasiChaProtiniKilichopokwenye_KiasiChaChakulaKwaWiki_1 = instance.KiasiChaChakulaKwaWiki_1 * instance.Protini

@receiver(pre_save, sender=TaarifaZaKuku)
def set_KiasiChaWangaKilichopokwenye_KiasiChaChakulaKwaWiki_1(sender, instance, **kwargs):
    # Check if the instance is new (i.e., it doesn't have a primary key yet)
    if instance._state.adding:
        instance.KiasiChaWangaKilichopokwenye_KiasiChaChakulaKwaWiki_1 = instance.KiasiChaChakulaKwaWiki_1 * instance.Wanga
@receiver(pre_save, sender=TaarifaZaKuku)

def set_KiasiChaCabohydrateKilichopokwenye_KiasiChaChakulaKwaWiki_1(sender, instance, **kwargs):
    # Check if the instance is new (i.e., it doesn't have a primary key yet)
    if instance._state.adding:
        instance.KiasiChaCabohydrateKilichopokwenye_KiasiChaChakulaKwaWiki_1 = instance.KiasiChaChakulaKwaWiki_1 * instance.Cabohydrate

@receiver(pre_save, sender=TaarifaZaKuku)
def set_KiasiChaFatiKilichopokwenye_KiasiChaChakulaKwaWiki_1(sender, instance, **kwargs):
    # Check if the instance is new (i.e., it doesn't have a primary key yet)
    if instance._state.adding:
        instance.KiasiChaFatiKilichopokwenye_KiasiChaChakulaKwaWiki_1 = instance.KiasiChaChakulaKwaWiki_1 * instance.Fati

@receiver(pre_save, sender=TaarifaZaKuku)
def set_KiasiChaVitaminiKilichopokwenye_KiasiChaChakulaKwaWiki_1(sender, instance, **kwargs):
    # Check if the instance is new (i.e., it doesn't have a primary key yet)
    if instance._state.adding:
        instance.KiasiChaVitaminiKilichopokwenye_KiasiChaChakulaKwaWiki_1 = instance.KiasiChaChakulaKwaWiki_1 * instance.Vitamini





#-------------------MWISHO WA MFUGAJI APP--------------------


