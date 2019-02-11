from django.shortcuts import render
import os

UPLOAD_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'upload')

# Create your views here.
def home(request):
	if request.method == 'POST':
		if 'file' in request.FILES:
			print(UPLOAD_DIR)
			print('123121231231')
			file = request.FILES['file']
			filename = file._name

			fp = open('%s/%s' % (UPLOAD_DIR, filename) , 'wb')
			for chunk in file.chunks():
				fp.write(chunk)
			fp.close()
		else:
			print('!@#!@#!@#@!@#!#')
	return render(request, 'home.html', {'data': {'test1': 123, 'test2': 456}})

def upload(req):
    if req.method == 'POST':
        if 'file' in req.FILES:
            print('123121231231')
            file = req.FILES['file']
            filename = file._name

            fp = open('%s/%s' % (UPLOAD_DIR, filename) , 'wb')
            for chunk in file.chunks():
                fp.write(chunk)
            fp.close()
            return HttpResponse('File Uploaded')
        else:
            print('!@#!@#!@#@!@#!#')
    return HttpResponse('Failed to Upload File')