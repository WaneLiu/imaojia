from django.shortcuts import render_to_response
from django import forms
from django.http import HttpResponse

class UserForm(forms.Form):
    username = forms.CharField()
    uploadImg = forms.FileField()
def regist(request):
    if request.method == 'POST':
        uf = UserForm(request.POST, request.FILES)
        if uf.is_valid():
            print(uf.cleaned_data['username'])
            print(uf.cleaned_data['uploadImg'])
            with open(r'/upload/' + uf.cleaned_data['uploadImg'].name,'wb') as fp:
                s = uf.cleaned_data['uploadImg'].read()
                fp.write(s)
            return HttpResponse('ok')
    else:
        uf = UserForm()
    return render_to_response('regist.html',{'uf':uf})

def show_video(request):
    return render_to_response('show_video.html')
