from django.shortcuts import render_to_response
from django.core.files import File
from django.template import RequestContext
from django.shortcuts import render
import re
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from .models import Document, VCF
from .forms import DocumentForm

from django.utils.encoding import smart_str


# Create your views here.


def index(request):
    context = {}

    if request.method == 'GET':
        form = DocumentForm()

     #   return render_to_response('polls/index.html',
     #                             {'form': form}, \
     #                             context_instance=RequestContext(request))

        context['form'] = form

        return render(request, 'polls/index.html', context)

    if request.method == 'POST':
        
        context['sucess'] = False
        form = DocumentForm(request.POST, request.FILES)

        if form.is_valid():
            #newdoc = Document(docfile=request.FILES['docfile'])
            #newdoc.save()
            f = request.FILES['docfile']

            doc = Document(docfile=File(analyse(f), name="result.vcf"))
            doc.save()

            if doc is not None:
                context['sucess'] = True
                context['id'] = doc.pk


                docs = Document.objects.all()

                historic = []
                docs = docs.reverse()
                for d in docs:
                    elem = {}
                    elem['name'] = d.docfile.name
                    elem['id'] = d.pk
                    historic.append(elem)

                context['historic'] = historic

                return render(request, 'polls/result.html', context)

        else:
            return render(request, 'polls/result.html', context)


def download(request):
    id = request.GET.get("id", '')
    if request.method == 'GET':

        d = Document.objects.filter(id = id)[0]
        print d

       # f = open('polls/result.vcf', 'r')
        text = d.docfile.read()

        response = HttpResponse(content=text)
        response['mimetype'] = 'application/force-download'
        response['Content-Disposition'] = 'attachment; filename=%s' % d.docfile.name

        return response


def analyse(f):

  #  f = file('polls/example1_input.vcf', 'r')
    fresult = open('polls/result.vcf', 'w+')

    s = re.compile('GI=')

    # variants = []

    for line in f:
     #   print line
    #   fresult.write(line)
        gene = ''
        line = line.strip()
        if line.startswith('#CHROM'):
            fresult.write(line + '\tOMIN' + '\n')
        elif s.search(line) != None:
            sp = line.split('GI=')
            q = sp[1].split(';')
            gene = q[0]
        #   variants.append(gene)
            fresult.write(line + '\t' + searchGene(gene) + '\n')
        else:
            fresult.write(line + '\n')

    f.close()
    # fresult.close()

    return fresult


def searchGene(gene):
    f = file('polls/genemap2.txt', 'r')

    s = re.compile(gene + '')

    resp = ''

    for line in f:
        col = line.split('|')
        if(len(col) > 9):
        #    print line
        #    print col[5]
            if s.search(col[5]) != None:
        #       print col[8]
                resp = resp + '#' + col[8] + ';'
    if len(resp) > 1:
        return resp
    else:
        return 'NOK'
