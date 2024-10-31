from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import TodoItem
import json

# Create your views here.

#Todo 목록 추가하기.
@csrf_exempt
def add_view(request):
    data = json.loads(request.body)  
    todo = TodoItem(title=data['title'], description=data.get('description', ''))
    todo.save()
    return JsonResponse({'message': '투두 항목이 성공적으로 추가되었습니다.'}, status=200)

@csrf_exempt
def show_view(request):
    todo = TodoItem.objects.all().values()
    return JsonResponse({"message" : list(todo)},safe=False)
#전체 Todo 삭제하기.
@csrf_exempt
def all_delete_view(request):
    TodoItem.objects.all().delete()
    return JsonResponse({"message":"모든 TodoList를 삭제했습니다."})



#특정 Todo 삭제하기.
@csrf_exempt        
def delete_view(request):
    data = json.loads(request.body)
    todo_title = data.get('title')
    todo = TodoItem.objects.get(title=todo_title)
    todo.delete()
    
    return JsonResponse({"message":"계획이 삭제 되었습니다."})

#description 수정할때.
@csrf_exempt
def modify_view(request):
    data = json.loads(request.body)
    todo_title = data.get('title')
    description = data.get('description')
    
    todo = TodoItem.objects.get(title=todo_title)
    todo.description = description
    todo.save()
    return JsonResponse({"title": todo.title, "description" : todo.description,"completed": todo.completed}, safe=False)

#Todo를 진행함.
@csrf_exempt
def todo_view(request):
    data = json.loads(request.body)
    todo_title = data.get('title')
    todo = TodoItem.objects.get(title=todo_title)
    todo.completed = True
    todo.save()
    
    return JsonResponse({"title": todo.title, "completed": todo.completed}, safe=False)

#Todo를 진행하지 않음.
@csrf_exempt
def not_todo_view(request):
    data = json.loads(request.body)
    todo_title = data.get('title')
    nottodo = TodoItem.objects.get(title=todo_title)
    nottodo.completed = False
    nottodo.save()

    return JsonResponse({"title": nottodo.title, "completed": nottodo.completed}, safe=False)