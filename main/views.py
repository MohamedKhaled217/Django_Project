from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from main.forms import CategoryForm, TaskForm
from .models import Task, Category

def logout_view(request):
	if request.method == 'POST':
		logout(request)
		return redirect('login')
	return render(request, 'main/logout.html')

def login_view(request):
	if request.method == "POST":
		username = request.POST["username"]
		password = request.POST["password"]
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect("home")
		else:
			return render(request, "main/login.html", {"error": "Invalid username or password"})
	return render(request, "main/login.html")

def index(request):
	tasks = Task.objects.all().order_by("due_date")
	categories = Category.objects.all()
	context = {"tasks": tasks, "categories": categories}
	return render(request, "main/index.html", context)

def detailed_task(request, id):
	task = get_object_or_404(Task, id=id)
	context = {"task": task}
	return render(request, "main/detailed.html", context)

def todo_by_status(request, st):
	todos = Task.objects.filter(status=st)
	context = {"todos": todos, "status": st}
	return render(request, "main/todosstatus.html", context)

def category_tasks(request, category_id):
	category = get_object_or_404(Category, id=category_id)
	tasks = Task.objects.filter(category=category)
	context = {"category": category, "tasks": tasks}
	return render(request, "main/category_tasks.html", context)

def create_task(request):
	if request.method == "POST":
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("home")
	else:
		form = TaskForm()
	return render(request, "main/createTask.html", {"form": form})

def create_category(request):
	if request.method == "POST":
		form = CategoryForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("home")
	else:
		form = CategoryForm()
	return render(request, "main/createCategory.html", {"form": form})

def update_task(request, id):
	task = get_object_or_404(Task, id=id)
	if request.method == "POST":
		form = TaskForm(request.POST, instance=task)
		if form.is_valid():
			form.save()
			return redirect("home")
	else:
		form = TaskForm(instance=task)
	return render(request, "main/updateTask.html", {"form": form})

def delete_task(request, id):
	task = get_object_or_404(Task, id=id)
	if request.method == "POST":
		task.delete()
		return redirect("home")
	return render(request, "main/deleteTask.html", {"task": task})