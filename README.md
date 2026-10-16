# Cloud Task App

A working task management app. Built, tested, and deployed on the internet.

## Live App (Working Now)
**Click here to use it:** https://cloud-task-app.onrender.com/tasks

## What I Built

### Level 1: Simple App
- ✓ Python Flask server
- ✓ SQLite database
- ✓ Can save tasks
- ✓ Can view tasks

### Level 2: Docker Box
- ✓ App inside a Docker container
- ✓ Container works on any computer

### Level 3: Cloud Deployment
- ✓ App is live on the internet
- ✓ Anyone can access it

### Level 4: Production Ready
- ✓ Deployed on Render
- ✓ Live and working NOW

## How to Use the App

### See All Tasks
https://cloud-task-app.onrender.com/tasks

### Create a New Task
```bash
curl -X POST [https://cloud-task-app.onrender.com/tasks](https://cloud-task-app.onrender.com/tasks) -H "Content-Type: application/json" -d '{"title": "Buy milk"}'
