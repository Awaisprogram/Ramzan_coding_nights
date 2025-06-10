import click
import json 
import os

TODO_FILE = "todo.json"

def load_tasks():
  if not os.path.exists(TODO_FILE):
    return []
  with open(TODO_FILE, "r") as file:
    return json.load(file)
  
def save_task(tasks):
  with open(TODO_FILE, "w") as file:
    json.dump(tasks, file , indent=4)  

@click.group()    
def cli():
  """Simple todo list manager"""
  pass

@click.command()
@click.argument("task")
def add(task):
  """Add a new task to the list"""
  tasks = load_tasks()
  tasks.append({"task":task,"done": False})
  save_task(tasks)
  click.echo(click.style(f"Task added {task}", fg="green", bold=True))

@click.command
def list():
    """list all the task"""
    tasks = load_tasks()
    if not tasks:
      click.echo("No task found")
      return
    for index, task in enumerate(tasks, 1):
      status = "✅" if task["done"] else "❌"
      click.echo(click.style(f"{index}. {task["task"]} : [{status}]", fg="green", bold=True))  

@click.command()
@click.argument("task_number", type=int)
def complete(task_number):
    """Mark a task as complete"""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["done"] = True
        save_task(tasks)
         click.echo(click.style(f"Task {task_number} marked as completed.", fg="green", bold=True))
    else:
        click.echo(click.style(f"Invalid task number: {task_number}", fg="red", bold=True))
        
@click.command()
@click.argument("task_number", type=int)
def remove(task_number):
    """Remove a task from the list"""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        save_task(tasks)
        click.echo(click.style(f"Removed task {removed_task['task']}", fg="red", bold=True))
    else:
        click.echo(click.style(f"Invalid task number: {task_number}", fg="red", bold=True))

cli.add_command(add)
cli.add_command(list)
cli.add_command(complete)
cli.add_command(remove)



if __name__ == "__main__":
  cli()


