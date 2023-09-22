from django.shortcuts import render
import os

# Create your views here.
def homepage(req):
    img_src = os.listdir('assets/images')
    hypos = [list(filter(lambda x: f'theory_{i}' in x, img_src)) for i in range(len(img_src))]
    variables = {f'hypo{i}':hypos[i] for i in range(len(hypos))}
    for i in variables:
        variables[i] = sorted(variables[i])
    return render(req, 'home.html', variables)
