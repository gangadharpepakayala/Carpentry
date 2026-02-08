from django.contrib.auth.forms import UserCreationForm
from django import forms
from image_uploader_widget.widgets import ImageUploaderWidget
from . models import User,Order,Sell,Payment

class UsrForm(UserCreationForm):
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Password"}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Password Again"}))
	class Meta:
		model = User
		fields = ["username","mob"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Username",
			}),
		"mob":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Mobile Number",
			}),
		}

class OrForm(forms.ModelForm):
	class Meta:
		model = Order
		fields = ["state","address","provide_wood","wood_type","furniture_name","dimensions","img1","img2"]
		label = {
		       'img1' : ImageUploaderWidget(),
		}
		widgets = {
		"state":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Your State",
			}),
		"address":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Address",
			}),
		"provide_wood":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Provide Wood Or Not",
			}),
		"wood_type":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Wood Name",
			}),
		"furniture_name":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Furniture Name",
			}),
		"dimensions":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Dimensions __x__x__",
			}),
		"img1": forms.FileInput(attrs={
                "class": "form-control my-2",  # Bootstrap styling
            }),
         "img2": forms.FileInput(attrs={
                "class": "form-control my-2",
            }),

		}

class UsupForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ["username","mob","email"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"User Name",
			}),
		"mob":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Mobile Number",
			}),
		"email":forms.EmailInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Mail id",
			}),
		}

class SelForm(forms.ModelForm):
	class Meta:
		model = Sell
		fields = ["prdct_id","wd_type","f_name","dim","c_price","o_price","im1","im2"]
		label = {
		        'im1' : ImageUploaderWidget(),
		        'im2' : ImageUploaderWidget(),
		}
		widgets = {
		"prdct_id":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter id",
			}),
		"wd_type":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Wood Name",
			}),
		"f_name":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Furniture Name",
			}),
		"dim":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Dimensions __x__x__",
			}),
		"c_price":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Current Price",
			}),
		"o_price":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Original Price",
			}),


		}

class PAccptForm(forms.ModelForm):
	class Meta:
		model = Order
		fields = ["wood_price","manfac_price","m_time"]
		widgets = {
        
		"wood_price":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter wood Price",
			}),
		"manfac_price":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter manufacture Price",
			}),
        "m_time":forms.DateInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Completion date",
			}),

		}

class SelUpForm(forms.ModelForm):
	class Meta:
		model = Sell
		fields = ["o_price","c_price"]
		widgets = {
			"o_price":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Original price",
			}),
			"c_price":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Current price",
			}),

		}

class PaymentForm(forms.ModelForm):
     class Meta:
         model=Payment
         fields=['c_name','c_number','c_expdate','c_cvv']
         widgets ={
         "c_name":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter name on card",
			}),
			"c_number":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter card number",
			}),
			"c_expdate":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter expdate",
			}),
			"c_cvv":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter CVV",
			}),
		}
