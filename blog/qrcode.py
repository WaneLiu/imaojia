from django.shortcuts import render_to_response
from django import forms
from django.http import HttpResponse
import qrcode
class UserForm(forms.Form):
    input_content = forms.CharField()


def get_qrcode(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            print(uf.cleaned_data['input_content'])
            img = qrcode.make(uf.cleaned_data['input_content'])
            with open(r'/upload/101.jpg', 'wb') as f:
               # s = img
               # f.write(s)
               img.save('/upload/101.jpg')
            return HttpResponse('二维码已生成')
    else:
        uf = UserForm()
    return render_to_response('get_qrcode.html',{'uf':uf})
