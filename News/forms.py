#coding:utf-8

from django import forms

class Register(forms.Form):
    user = forms.CharField(max_length=32,label='用户名',required=True)
    password = forms.CharField(max_length=32,label='密码',required=True)
    phone = forms.CharField(max_length=15,label='手机号',required=False)

    def clean_password(self): #命名必须是clean_字段名称
        password = self.cleaned_data['password']
        if password[0].isdigit(): #判断首字是否是数字
            raise forms.ValidationError("First can't be number")
        return password