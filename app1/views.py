from django.shortcuts import render

# Create your views here.
def home(request):
    if request.method == 'GET':
        return render(request,'home.html') 
    else:
        str=request.POST['text1']
        str2=[]
        result=[]
        for i in str:
            if str.count(i)>1:
                if i not in str2:
                    str2.append(i)
        for i in range(0,len(str2)):
            result.append({"letter":str2[i],"count":str.count(str2[i])})
        h=max(result,key=lambda x:x['count'])
        return render(request,'home.html',{'str':str,'abc':result,'cd':h})
       


       