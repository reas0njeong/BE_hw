from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def word_count(request):
    return render(request, 'word_count.html')

def hello(request):
    entered_name = request.GET['fulltext']
    return render(request, 'hello.html', {'entered_name': entered_name})


def result(request):
    entered_text = request.GET['fulltext']
    word_list = entered_text.split()

    word_dictionary = {}

    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1

    word_max_value = max(word_dictionary.values())
    
    word_max_key =[]
    for key, value in word_dictionary.items():
        if value == word_max_value:
            word_max_key.append(key)

    all_word_count = len(entered_text)
    space_count = entered_text.count(' ')
    nospace_word_count = all_word_count - space_count

    return render(request, 'result.html', {'alltext' : entered_text, 'word_max_key': word_max_key, 'word_max_value': word_max_value, 'all_word_count': all_word_count, 'nospace_word_count': nospace_word_count, 'dictionary' : word_dictionary.items()})

