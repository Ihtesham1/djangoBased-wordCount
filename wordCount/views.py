import operator

from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def count(request):
    fulltext = request.GET['fulltext']
    wordcount = fulltext.split()

    worddict = {}
    for word in wordcount:
        #it will add in the existing word
        if word in worddict:
            worddict[word] += 1
        else:
            #it will start counting when new word is found
            worddict[word] = 1


    sorteddict = sorted(worddict.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext': fulltext, 'wordcount': len(wordcount), 'SortedDict': sorteddict})