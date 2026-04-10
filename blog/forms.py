from .models import user_blog
from django import forms



"""in this part we are going to  make a form using django forms  and modelforms """

class userblogfrom(forms.ModelForm):
    class Meta:
        model = user_blog
        fields = "__all__"


