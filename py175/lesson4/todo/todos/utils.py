def delete_todo_by_id(todo_id, lst):
    lst['todos'] = [todo for todo in lst['todos'] if todo['id'] != todo_id]

def error_for_list_title(title, lists, current=None):
    if title == current:
        return 'You entered the same title'
    if any(lst['title'] == title for lst in lists):
        return 'The title must be unique.'
    elif not 1 <= len(title) <= 100:
        return 'The title must be between 1 and 100 characters.'
    
def error_for_todo(todo):
    if not 1 <= len(todo) <= 100:
        return 'The title must be between 1 and 100 characters.'

def find_list_by_id(list_id, lists):
    return next((lst for lst in lists if lst['id'] == list_id), None)

def find_todo_by_id(todo_id, lst):
    return next((todo for todo in lst if todo['id'] == todo_id), None)

def is_list_completed(lst):
    return len(lst['todos']) > 0 and todos_remaining(lst) == 0

def is_todo_completed(todo):
    return todo['completed']

def mark_all_done(lst):
    for todo in lst['todos']:
        todo['completed'] = True

def sort_items(items, select_completed):
    return sorted(items, key=lambda item: (select_completed(item), item['title'].lower()))

def todos_remaining(lst):
    return sum(1 for todo in lst['todos'] if not todo['completed']) 