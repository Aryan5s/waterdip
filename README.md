## Description : 

A server that can keep track of tasks. This Server can do the Following : 
1. Create a new task with a title property and a boolean determining whether the task has been completed. A new unique id would be created for each new task
2. List all tasks created
3. Get a specific task
4. Delete a specified task
5. Edit the title or completion of a specific task
6. Bulk add multiple tasks in one request
7. Bulk delete multiple tasks in one request

this application will accept JSON and/or URL parameters and will return JSON data. It is ready to be integrated into a web system

## List of Endpoints :
Here is a specific list of endpoints that will be required, along with the method and the inputs/outputs:

## Create a New Task  : 
```sh
POST /v1/tasks
```
## Input :
```sh
{title: "Test Task 2"}
```
## Output :
```sh
{id: 2} (returns a 201 code)
```
The id returned is a unique id for the todo that was just created

## List all tasks created : 
```sh
GET /v1/tasks
```
## Input :
```sh
None
```
## Output :
```sh
(return a 200 code)
{
   tasks: [
     {id: 1, title: "Test Task 1", is_completed: true},
     {id: 2, title: "Test Task 2", is_completed: false}
   ]
}
```
This endpoint list all tasks including their id's

## Get a specific task:
```sh
GET /v1/tasks/{id}
```
## Input :
```sh
id (passed through the URL)
```
## Output :
```sh
(return a 200 code)
{id: 3, title: "Test Task 2", is_completed: false}
```
## On Error :
```sh
if id not found:
(return a 404 code)

{
    error: "There is no task at that id"
}
```
This endpoint returns a specific task or returns a 404 not found response

## Delete a specific task : 
```sh
DELETE /v1/tasks/{id}
```
## Input :
```sh
id (passed through the URL)
```
## Output :
```sh
None (return a 204 code)
```
 This endpoint deletes a specific task. If the task doesn’t exist still send the same response

## Edit the title or completion of a specific task : 
```sh
PUT /v1/tasks/{id}
```
## Input :
```sh
{title: "Test Task 2", is_completed: false}
```
## Output :
```sh
None (return a 204 code)
```
## On Error :
```sh
if id not found:
(return a 404 code)

{
    error: "There is no task at that id"
}
```
This endpoint deletes a specific task or returns a 404 not found response

## Bulk add tasks : 
```sh
POST /v1/tasks
```
## Input :
```sh
{
   tasks: [
      {title: "Test Task 1", is_completed: true},
      {title: "Test Task 2", is_completed: false},
      {title: "Test Task 3", is_completed: true}
   ]
}
```
## Output :
```sh
(return a 201 code)
{
   tasks: [
      {id: 1},
      {id: 2},
      {id: 3}
   ]
}
```
This endpoint bulk adds more than one task. Note that this feature uses the same endpoint as the single task creation endpoint

## Bulk Delete Tasks :
```sh
DELETE /v1/tasks
```
## Input :
```sh
{
   tasks: [
     {id: 1},
     {id: 2},
     {id: 3}
  ]
}
```
## Output :
```sh
None (returns a 204 code)
```
This endpoint bulk deletes more than one task.
