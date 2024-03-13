from django.shortcuts import render

from .models import Pupil



# Create your views here.
def pupils_list(request):
    if 'pupil' not in request.GET:
        pupils = Pupil.objects.all() # SELECT * FROM pupils;
        return render(request, 'pupils/pupils_list.html', {'pupils': pupils})
    else:
        pupils = Pupil.objects.filter(name__icontains=request.GET['pupil'])
        # SELECT * FROM pupils WHERE name LIKE '%str%';
        return render(request, 'pupils/pupils_list.html', {'pupils': pupils})


def pupils_detail(request, pk):
    pupil = Pupil.objects.get(id=pk)
    return render(request, 'pupils/pupil_info.html', {'pupil': pupil})
