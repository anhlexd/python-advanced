from django.shortcuts import render
from datetime import datetime
# Create your views here.

def show_info(request, name):
    print('HELLO')
    info = {
        'countries': [
            'Viet Nam',
            'England',
            'United States',
            'Germany',
        ],
            'now': datetime.now()
    }

    return render(request, name + '.html', info)
