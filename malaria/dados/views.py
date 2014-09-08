#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.template.loader import get_template
from django.template import Context
from malaria.dados.models import CIDADE, PACIENTE
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.encoding import smart_str, smart_unicode
from django.core.context_processors import csrf
from django.shortcuts import render_to_response

def index(request):    
    vTemplate = get_template('index.html')
    vSaida = vTemplate.render(Context({}))
    return HttpResponse(vSaida)

def mapa(request):
    vArquivo = open('malaria/staticfiles/js/pontos.json', 'w')
    vArquivo.write('[\n')

    vSaida = ''
    vPost = False;
    if ((request.method == "POST") and
         ((request.POST.get("edCidade") != '') or
           (request.POST.get("cbUF") != ''))):
        vCidades = CIDADE.objects.all().filter(CID_NOME__icontains=request.POST.get("edCidade"), CID_UF__icontains=request.POST.get("cbUF"));
        vPost = True;
    else:
        vCidades = CIDADE.objects.all().filter();

    vPrimeiro = True; 
    for vCidade in vCidades:        
        vPaciente = PACIENTE.objects.all().filter(CID_CODIGO_NOT=vCidade.CID_CODIGO)

        if ((vPaciente.count() > 0) or
            (vPost)):

            if (vPrimeiro == False):
                vArquivo.write(',')
                vArquivo.write('\n')

            vPrimeiro = False;
            vArquivo.write('{"Id": ')
            vArquivo.write(str(vCidade.CID_CODIGO))
            vArquivo.write(',"Latitude": ')
            vArquivo.write(str(vCidade.CID_LATITUDE))
            vArquivo.write(',"Longitude": ')
            vArquivo.write(str(vCidade.CID_LONGITUDE))
            vArquivo.write(',"Descricao": "')
            vArquivo.write(smart_str(vCidade.CID_NOME))
            vArquivo.write('/' + str(vCidade.CID_UF))
            vArquivo.write(smart_str('<br>Total de Notificações: '))
            vArquivo.write(str(vPaciente.count()) + '"')
            vArquivo.write('}')        
        
    vArquivo.write(']')
    vArquivo.close();

    vContext = {'vSaida': vSaida}
    vContext.update(csrf(request))
    return render_to_response("mapa.html", vContext)    

def informativo(request):    
    vTemplate = get_template('informativo.html')
    vSaida = vTemplate.render(Context({}))
    return HttpResponse(vSaida)

def estatisticas(request):    
    vTemplate = get_template('estatisticas.html')
    vSaida = vTemplate.render(Context({}))
    return HttpResponse(vSaida)

def sobre(request):    
    vTemplate = get_template('sobre.html')
    vSaida = vTemplate.render(Context({}))
    return HttpResponse(vSaida)