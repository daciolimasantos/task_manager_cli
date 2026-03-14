import argparse
from task_manager import TaskManager

def main():
    parser = argparse.ArgumentParser(description="TaskManager CLI")
    subparsers = parser.add_subparsers(dest="command")
    
    # add a task
    parser_add = subparsers.add_parser("add", help="Add a new task")
    parser_add.add_argument("title", help="Title of the task")
    parser_add.add_argument("-d", "--description", default="", help="Description of the task")
    
    # remove a task
    parser_remove = subparsers.add_parser("remove", help="Remove a task by ID")
    parser_remove.add_argument("id", type=int, help="ID of the task to complete")
    
    # complete a task
    parser_complete = subparsers.add_parser("complete", help="Mark task as completed")
    parser_complete.add_argument("id", type=int, help="ID of the task to complete")
    
    # list the tasks
    subparsers.add_parser("list", help="List all tasks")
    
    # save the tasks
    subparsers.add_parser("save", help="Save tasks to file")
    
    # load the tasks
    subparsers.add_parser("load", help="Load tasks from file")
    
    args = parser.parse_args()
    
    manager = TaskManager()
    manager.load_tasks() # carrega uma vez no inicio
    
    if args.command == "add":
        manager.add_task(args.title, args.description)
        manager.save_tasks()
    elif args.command == "remove":
        manager.remove_task(args.id)
        manager.save_tasks()
    elif args.command == "complete":
        manager.complete_task(args.id)
        manager.save_tasks()
    elif args.command == "list":
        manager.list_tasks()
    elif args.command == "save":
        manager.save_tasks()
    elif args.command == "load":
        manager.load_tasks()
        manager.list_tasks()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()