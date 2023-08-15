from users.models import User

Users = User.objects.all()
"""Imports Users"""

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

due_date_choices = {
    '1': '1 Month',
    '2': '2 Months',
    '3': '3 Months',
    '6': '6 Months',
    '12': '12 Months',
}