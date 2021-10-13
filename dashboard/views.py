from django.shortcuts import render
from .models import *

# Create your views here.
def homePage(request):
    agent = Agentname.objects.all()
    context={'agent':agent}
    return render(request, 'index.html', context)

def puPage(request):
    pu = AnnouncedPuResults.objects.all()
    context={'pu':pu}
    return render(request, 'pu_result.html', context)

def pollingPage(request):
    pg = PollingUnit.objects.all()
    context={'pg':pg}
    return render(request, 'polling_unit.html', context)


def resultPage(request):
    x=[]
    puid=[]
    pa=[]
    score=[]
    if request.method == 'POST':
        res = request.POST['lga']
        res = int(res)
        print(res)
        loc = PollingUnit.objects.filter(lga_id=res)
        for i in loc:
            y = i.uniqueid
            x.append(y)
        for r in x:
            polls = AnnouncedPuResults.objects.filter(polling_unit_uniqueid=r)
            for i in polls:
                puid.append(i.polling_unit_uniqueid)
                pa.append(i.party_abbreviation)
                score.append(i.party_score)
            print(sum(score))
        total = sum(score)
        context={'res':res, 'puid':puid, 'pa':pa, 'score':score, 'total':total}
        print(x)
        return render(request, 'result.html',context)
        
    return render(request, 'result.html')

from .forms import PollForm
def newpollPage(request):
    form = PollForm()
    if request.method=='POST':
        form=PollForm(request.POST)
        if form.is_valid():
            form.save()
    result = newPollingUnit.objects.all()
    return render(request, 'new_polls.html', {'form':form})
    
    