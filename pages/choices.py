from users.models import User

Users = User.objects.all()

assignee_choices = {}

for user in Users:
    user_username = user.username
    assignee_choices[user_username] = user_username


priority_choices = {
    'High': 'High',
    'medium': 'Medium',
    'Low': 'Low'
}

progress_choices = {
    'Not Started': 'Not Started',
    'In Progress': 'In Progress',
    'Completed': 'Completed'
}