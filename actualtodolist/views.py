from django.shortcuts import render,redirect

todoList=[]
# Create your views here.
def index(request):
    
    if request.POST:
        new_task=request.POST["task"]
        todoList.append(new_task.strip())
        return redirect("index")
    
    return render(request,"actualtodolist/index.html",context={"tasks":todoList})



