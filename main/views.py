from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from  .models import task,updates
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView


class RegisterForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={'type': 'text', 'placeholder': 'Title'}), required=True)
    date =  forms.DateField(widget=forms.DateInput(attrs={'type': "date", 'placeholder': ' '}),required=True)
    discription = forms.CharField(widget=forms.Textarea(
        attrs={'type': 'text', 'placeholder': ' '}), required=True)

    class Meta:
        model = task
        fields = ['title', 'priority', 'date', 'discription']

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['icon_name'] = "fa fa-lock"
        self.fields['date'].widget.attrs['icon_name'] = "fa fa-calender"


class Register(CreateView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = './'

    def form_valid(self, form):
        if not task.objects.filter(title=form['title']).exists():
            form.save()
        else:
            raise forms.ValidationError("task already exists")
        return super(Register, self).form_valid(form)

def home(request):
    data = task.objects.all()
    update=updates.objects.last()
    context={'data':data, 'num':10, 'number':len(data),'up':update.id}
    return render(request, 'home.html', context)


def edit(request):
    id=request.GET.get('id')
    obj = task.objects.get(id=id)
    obj.title = request.GET.get('title')
    if request.GET.get('date') !="":
        obj.date = request.GET.get('date')
    obj.priority = request.GET.get('priority')
    obj.discription = request.GET.get('discription')
    obj.save()
    return HttpResponse("success")

def delete(request):
   id=request.GET.get('id')
   obj = task.objects.get(id=id)
   obj.delete()
   return HttpResponse("success")

def update(request):
    obj=task.objects.all()
    update=updates.objects.all().order_by('-id')
    up_id=int(request.GET.get('up'))
    if (update[0].id>up_id):
        temp=""
        upd=""
        for i in obj:
            temp = temp +'<tr class = "data d'+str(i.id)+'"><td>'+i.title+'</td><td>'+str(i.date)+'</td><td>'+i.priority+'</td><td>'+i.discription+'</td><td><span class = "edit" id ="'+str(i.id)+'"><i class="fa fa-pencil-square-o" aria-hidden="true"></i></span><span class = "delete" id ="'+str(str(i.id))+'"><i class="fa fa-trash" aria-hidden="true"></i></span></td></tr><tr class = "edata e'+str(i.id)+'"> <form id ="f'+str(i.id)+'"><input type="hidden" value="'+str(i.id)+'" name="id"><td><input value="'+i.title+'" name="title" type="text"></td><td><input name="date" type="date"><br>('+str(i.date)+'))</td><td><select value="'+i.priority+'" name="priority" style="border-radius: 50%;"><option>High</option><option>Medium</option><option>Low</option></select></td><td><input value="'+i.discription+'" name="discription" type="text"></td></form><td><span class = "save" id ='+str(i.id)+'><i class="fa fa-floppy-o" aria-hidden="true"></i></span><span class = "cancel" id ='+str(i.id)+'><i class="fa fa-times" aria-hidden="true"></i></span></td></tr>'
        z=update[0]
        upd=upd+'<div class="p'+str(z.id)+'"style="padding:10px;margin:5px;background-color:aqua;border-radius:10%">'+str(z)+'<a id="'+str(z.id)+'"style="padding:3px;" class="p"><i class="fa fa-times" aria-hidden="true"></i></a></div>'
        print(upd)
        return JsonResponse({'data':temp,'number':len(obj),'r_up':update[0].id,'upd':upd})
    
    else :
        return HttpResponse("no update")