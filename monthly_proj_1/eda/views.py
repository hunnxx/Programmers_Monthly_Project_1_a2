from django.shortcuts import render
import os

# Create your views here.
def homepage(req):
    img_src = os.listdir('assets/images')
    hypos = [list(filter(lambda x: f'theory_{i+1}' in x, img_src)) for i in range(len(img_src))]
    variables = {f'hypo{i+1}':hypos[i] for i in range(len(hypos))}
    return render(req, 'home.html', variables)