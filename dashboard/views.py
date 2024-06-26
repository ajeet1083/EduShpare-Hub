from django.shortcuts import render, redirect, HttpResponse
from .models import Notes, Homework
from .forms import *
from django.contrib import messages
from django.views import generic
from youtubesearchpython import VideosSearch
import requests
import wikipedia
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, 'dashboard/home.html')
@login_required(login_url = 'login')
def notes(request):
    if request.method == 'POST':
        form = NotesForm(request.POST)
        if form.is_valid():
            notes = Notes(user = request.user, title = request.POST['title'], description = request.POST['description'])
            notes.save()
        messages.success(request, f"Notes Added Successfully By {request.user.username}")
        return redirect('notes')
        
    else:
        form = NotesForm()
    notes = Notes.objects.filter(user = request.user)
   
    context = {'notes' : notes, 'form':form}

    return render(request, 'dashboard/notes.html', context)


def notes_delete(request, pk = None):
    Notes.objects.get(id = pk).delete()
    return redirect('notes')

class NotesDetailView(generic.DetailView):
    model = Notes
    
@login_required(login_url = 'login')    
def homework(request):
    if request.method == 'POST':
        form = HomeworkForm(request.POST) 
        if form.is_valid():
            try:
                finished = request.POST['is_finished']
                if finished == 'on':
                    finished = True
                else:
                    finished = False
            except:
                finished = False
                
            homework = Homework(
                user = request.user,
                subject = request.POST['subject'],
                title = request.POST['title'],
                description = request.POST['description'],
                due = request.POST['due'],
                is_finished = finished
            )
            homework.save()
            messages.success(request, f'Homework added form {request.user.username}!!')
        return redirect('homework')
            
    else:
        form = HomeworkForm()
    homeworks =  Homework.objects.filter()
    if len(homeworks) == 0:
        homework_done = True
    else:
        homework_done = False
    context = {'homework' : homeworks, 'homework_done' : homework_done, "form": form}
    return render(request, 'dashboard/homework.html', context)
    
    
def update_homework(request, pk):
    homework = Homework.objects.get(id = pk)
    if homework.is_finished == True:
        homework.is_finished = False
    else:
        homework.is_finished = True
    homework.save()
    return redirect('homework')

def delete_homework(request, id):
    homework = Homework.objects.get(id = id).delete()
    return redirect('homework')


def youtube(request):
    if request.method == 'POST':
        form = DashboardForm(request.POST)
        text = request.POST['text']
        video = VideosSearch(text, limit = 10)
        result_list = []
        
        for i in video.result()['result']:
            
            result_dict = {
                'id' : i['id'],
                'input' : text,
                'title' : i['title'],
                'duration' : i['duration'],
                'thumbnail' : i['thumbnails'][0]['url'],
                'channel' : i['channel']['name'],
                'link' : i['link'],
                'views' : i['viewCount']['short'],
                'published' : i['publishedTime'],
            }
            desc = ''
            if i['descriptionSnippet']:
                for j in i['descriptionSnippet']:
                    desc += j['text']
            result_dict['description'] = desc
            result_list.append(result_dict)
        context = {
            'form': form,
            'results' : result_list
        }
        return render(request, 'dashboard/youtube.html', context)
    
    else:
        form = DashboardForm()
    context = {'form' : form}
    return render(request, 'dashboard/youtube.html', context)

@login_required
def todo(request):
    todo = Todo.objects.filter(user = request.user)
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            try:
                finished = request.POST['is_finished']
                if finished == 'on':
                    finished = True
                else:
                    finished = False
            except:
                finished = False
                
            todo = Todo(
                user = request.user,
                title = request.POST['title'],
                is_finished = finished
            )
            todo.save()
            messages.success(request, f'To do added successfully from {request.user}')
        return redirect('todo')
    else:
        form = TodoForm()
    context = {'todos' : todo, 'form' : form}
    return render(request, 'dashboard/todo.html', context)

def update_todo(request, id):
    todo = Todo.objects.get(id = id)
    if todo.is_finished:
        todo.is_finished = False
    else:
         todo.is_finished = True
    todo.save()
    return redirect('todo')

def delete_todo(request, id):
    Todo.objects.get(id = id).delete()
    return redirect('todo')

def books(request):
    if request.method == 'POST':
        form = DashboardForm(request.POST)
        text = request.POST['text']
        url = "https://www.googleapis.com/books/v1/volumes?q=" + text
        r = requests.get(url)
        r.raise_for_status()
        answer = r.json()
        
        result_list = []

        
        answer_len = len(answer['items'])
        for i in range(answer_len):  
            result_dict = {
                'title' : answer['items'][i]['volumeInfo'].get('title', ""),
                'subtitle' : answer['items'][i]['volumeInfo'].get('subtitle', ""),
                'description' : answer['items'][i]['volumeInfo'].get('description', ""),
                'count' : answer['items'][i]['volumeInfo'].get('pageCount', ""),
                'categories' : answer['items'][i]['volumeInfo'].get('categories', ""),
                'rating' : answer['items'][i]['volumeInfo'].get('averageRating', ""),
                'thumbnail' : answer['items'][i]['volumeInfo']['imageLinks'].get('thumbnail', ""),
                'preview' : answer['items'][i]['volumeInfo'].get('previewLink', ""),
                
                
            }
            result_list.append(result_dict)
        
        context = {
            'form': form,
            'results' : result_list
        }
        return render(request, 'dashboard/books.html', context)
    
    else:
        form = DashboardForm()
    context = {'form' : form}
    return render(request, 'dashboard/books.html', context)


def dictionary(request):
    if request.method == 'POST':
        form = DashboardForm(request.POST)
        text = request.POST['text']
        url = "https://api.dictionaryapi.dev/api/v2/entries/en_US/" + text
        r = requests.get(url)
        r.raise_for_status()
        answer = r.json()
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>0")
        for key, value in answer[0].items():
            print(key+"-----------",value)
            
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>1")
        
        # for key, value in answer[1].items():
        #     print(key+"-----------",value)
        # print("++++++++++++++++++++++++------->meanings")
        # for key, value in answer[0]['meanings'].items():
        #     print(key+"-------------------meaning----------", value)    
       
        try:
            print("try-----------------------------------------------------=========")
            
            phonetics = None
            audio = None
            for i in answer[0]['phonetics']:
                if i['text'] != None and i['audio'] !=None:
                    phonetics = i['text']
                    audio = i['audio']
                    break
            print(phonetics)
            
            print(audio)
            partOfspeech = answer[0]['meanings'][0]['partOfSpeech']
            print(partOfspeech)
            difinition = answer[0]['meanings'][0]['definitions'][0]['definition']
            print(difinition)
            example = None 
            for i in answer[0]['meanings'][0]['definitions']:
                if i.get('example', None) != None:
                    example = i['example']
                    break
                    
            print(example, "example")
            syno = list()
            for i in answer[0]['meanings'][0]['definitions']:
                if len(i.get('synonyms'))>0:
                    syno.extend(i.get('synonyms'))
            for i in answer[1]['meanings'][0]['definitions']:
                if len(i.get('synonyms'))>0:
                    syno.extend(i.get('synonyms'))
            
            print(syno , "synomyms")
            antonyms =  answer[0]['meanings'][0]['definitions'][0]['antonyms'] 
            print(antonyms)          
            context = {
                'form': form,
                'phonetics' : phonetics,
                'audio' : audio,
                'definition' : difinition,
                'example' : example,
                'synosyms' : syno,
                'antonyms' : antonyms,
                'partOfSpeech' : partOfspeech,
                'input' : text,
            }
            print("try-----------------------------------------------------=========")
        except Exception as e:
            print(type(e))
            context = {
                'form' : form,
                'input' : text,
            }
        return render(request, 'dashboard/dictionary.html', context)
    else:
        form = DashboardForm()
    context = {'form' : form}
    return render(request, 'dashboard/dictionary.html', context)


def wiki(request):
    if request.method == 'POST':
        text = request.POST['text']
        print(text)
        form = DashboardForm(request.POST)
        wiki_list = []
        def add_wiki_list(text):
            search = wikipedia.page(text)
            wiki_list.append(
                    {
                        'title':search.title,
                        'link' : search.url,
                        'summary' : search.summary
                    }
            ) 
        
        try:
            add_wiki_list(text)
        except wikipedia.exceptions.DisambiguationError as e:
            options = e.options
            count = 0
            for option in options:
                try:
                    add_wiki_list(option)
                    count += 1
                    if count == 5:
                        break
                except wikipedia.exceptions.PageError as e:
                    print("Page Error------------------------------------------------------------->")
        except wikipedia.exceptions.PageError as e:
            print("Page Error------------------------------------------------------------->")
        context = {
            'form' : form,
            'items' : wiki_list,
        }
        return render(request, 'dashboard/wiki.html', context)
    form = DashboardForm()
    context = {
        'form' : form,
    }
    return render(request, 'dashboard/wiki.html', context)


def conversion(request):
    if request.method == 'POST':
        form = ConversionForm(request.POST)
        if request.POST.get('measurement') == 'length':
            measurment_form = LenghtConversionForm()
            context ={
                'form' : form,
                'm_form': measurment_form,
                'input' : True,
            }
            
            if 'input' in request.POST:
                first = request.POST['measure1']
                second = request.POST['measure2']
                input_value = request.POST['input']
                answer = ''
                
                if input_value and int(input_value) >= 0:
                    if first == 'yard' and second == 'foot':
                        answer = f'{input_value} yard = {int(input_value)*3} foot'
                    if first == 'foot' and second == 'yard':
                        answer = f'{input_value} foot = {int(input_value)/3} yard'
                context = {
                    'form': form,
                    'm_form': measurment_form,
                    'input': True,
                    'answer': answer
                }
            return render(request, 'dashboard/conversion.html', context)
        if request.POST.get('measurement') == 'mass':
            measurment_form = MassConversionForm(request.POST)
            if 'input' in request.POST:
                first = request.POST['measure1']
                second = request.POST['measure2']
                input_value = request.POST['input']
                answer = ''
                if input_value and int(input_value) >= 0:
                    if first == 'pound' and second == 'kilogram':
                        answer = f'{input_value} pound = {int(input_value) * 0.453592} kilogram'
                    if first == 'kilogram' and second == 'pound':
                        answer = f'{input_value} kilogram = {int(input_value) * 2.20462} pound'
                context = {
                    'form': form,
                    'm_form': measurment_form,
                    'input': True,
                    'answer': answer
                }
                
                return render(request, 'dashboard/conversion.html', context)

    else:
        form = ConversionForm()

    context = {
        'form': form,
        'input': False,
    }
    return render(request, 'dashboard/conversion.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account is created for {username} !!')
            return redirect('login')

    else:       
        form = UserRegistrationForm()
    contex = {
        'form' : form
    }
    return render(request, 'dashboard/register.html', contex)

@login_required(login_url = 'login')
def profile(request):
    homework = Homework.objects.filter(is_finished = False, user = request.user)
    todo = Todo.objects.filter(is_finished = False, user = request.user)
    print(len(homework), len(todo))
    if len(homework) == 0:
        homework_done = True
    else:
        homework_done = False
    if len(todo) == 0 :
        todo_done = True
    else:
        todo_done = False
        
    context = {
        'homeworks' : homework,
        'todos' : todo,
        'homework_done' : homework_done,
        'todo_done' : todo_done,
    }
    for i in list(homework):
        print(i.id)
    print(homework_done, todo_done)
    return render(request, 'dashboard/profile.html', context)

def compile(request):
    return render(request, 'dashboard/compiler1.html')

def resume(request):
    return render(request, 'dashboard/resume_maker.html')

def image_download(request):
    return render(request, 'dashboard/image_download.html')