from django import forms
def check_for_a(value):
    if value[0].lower()=='a':
        raise forms.ValidationError('name should starts with a')

def check_for_length(value):
    if len(value)<8:
        raise forms.ValidationError('length should atleat 8')

class StudentForm(forms.Form):
    username=forms.CharField(max_length=100,validators=[check_for_a,check_for_length])
    password=forms.CharField(max_length=100,widget=forms.PasswordInput)
    confirm_password=forms.CharField(max_length=100,widget=forms.PasswordInput)
    botcatcher=forms.CharField(max_length=100,widget=forms.HiddenInput,required=False)



    def clean(self):
        pa=self.cleaned_data['password']
        cpa=self.cleaned_data['confirm_password']
        if pa!=cpa:
            raise forms.ValidationError('password not match')


    def clean_botcatcher(self):
        bot=self.cleaned_data['botcatcher']
        if len(bot)>0:
            raise forms.ValidationError('bot is inserting ther data')



