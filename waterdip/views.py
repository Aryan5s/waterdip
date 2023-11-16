from django.shortcuts import render
from .models import Task_collection
from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize
import uuid

# Create your views here.
def index(request):
    return HttpResponse('<h1>Welcome To WaterDip AI assignment</h1>')

def multipleTaskMethods(request):
       # Create a specific task or bulk adds taks
    if request.method == 'POST':
        try:
            singleTaskTitle = request.GET['title']
            tasks_data = request.data.get('tasks' , [])
            
            if singleTaskTitle : 
                taskTitle = singleTaskTitle
                taskStatus = False
                taskId = uuid.uuidv1()
                
                newTask = {
                    'id' : taskId,
                    'title' : taskTitle,
                    'is_completed' : taskStatus
                }    
                
                Task_collection.insert_one(newTask) 
                return HttpResponse({
                'id' : taskId
            } , content_type = 'application/json' , status = 201)
            else :
                tasks_id = []
            
                for tasks in tasks_data:
                    taskTitle = tasks.title
                    taskStatus = tasks.is_completed
                    taskId : uuid.uuid1()
                    tasks_id.append(taskId)
                
                    new_task = {
                        'id' : taskId,
                        'title' : taskTitle,
                        'is_completed' : taskStatus
                }
             
                Task_collection.insert_one(new_task)   
                
            return HttpResponse({
                'tasks' : tasks_id
            } , content_type = 'application/json' , status = 201) 
        except Exception as e:
            response = {
                'message' : str(e)
            }
            return HttpResponse(response , content_type = 'application/json' , status = 500)      
    
    # bulk delete
    if request.method == 'DELETE':
        try:
            task_ids_data = request.data.get('tasks' , [])
        
            if len(task_ids_data) == 0:
                return HttpResponse({
                'error' : 'No tasks can be deleted'
            } , content_type = 'application/json' , status = 201)
        
            for taskIds in task_ids_data:
                Task_collection.find_one_and_delete(taskIds.id)
            
            return HttpResponse({
                'message' : 'Successfully deleted all tasks'
            } , content_type = 'application/json' , status = 201)
        except Exception as e:
            reponse  = {
                'error' : str(e)
            }
            
            return HttpResponse(response , content_type = 'application/json' , status = 500)
              
    # List all the tasks 
    if request.method == 'GET': 
        try:
            tasks = Task_collection.find()
            return HttpResponse(tasks , content_type = 'application/json' , status = 200)
        except Exception as e:
            response = {
                'error' : str(e)
            }
            return HttpResponse(response , content_type = 'application/json' , status = 404)
    

def specifcTaskMethod(request, id):
    
    if request.method == 'PUT':
        try:
            taskTitle = request.GET['title']
            taskStatus = request.GET['is_completed']
            
            task = Task_collection.find_one(id)
            if not task : 
                return HttpResponse({
                    'error' : 'There is No task at the id : ${id}'
                }, content_type = 'application/json' , status = 404)
                
            update_operation = {
                '$set':{
                    'title' : taskTitle,
                    'is_completed' : taskStatus
                }
            }
            Task_collection.find_one_and_update({'id' : id},  update_operation)    
            return HttpResponse({
                'message' : 'successfully updated the record with id : ${id}'
            }, contengt_type = 'application/json' , status = 204)
        except Exception as e:
            print('except')
    
    if request.method == 'DELETE':
        try:
            task = Task_collection.find_one(id)
            if not task :
                return HttpResponse({
                    'message' : 'no Task found with id, might have already been deleted'
                } , content_type = 'application/json' , status = 204)
                
            Task_collection.find_one_and_delete(id)
            
            return HttpResponse({
                'message' : 'successfully deleted'
            } , content_type = 'application/json' , status = 204)
        except Exception as e:
            response = {
               'error' : str(e)
           }   
            return HttpResponse(response, content_type = 'application/json' , status = 500)   
            
    
    # Get a specific task
    if request.method == 'GET':
       try:    
        requestedTask = Task_collection.find_one(id)
        
        if not requestedTask :
            response = {
               'error': "There is no task at that id"
            }
            return HttpResponse(response ,  content_type = 'application/json' , status = 404)
        
        return HttpResponse(requestedTask ,  content_type = 'application/json' , status = 200)
           
       except Exception as e:
           response = {
               'error' : str(e)
           }   
           return HttpResponse(response, content_type = 'application/json' , status = 500)
        
        
