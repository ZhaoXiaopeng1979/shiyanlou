#!/usr/bin/env python3

import json

courses = {1:'Linux', 2:'Vim', 3:'Git'}

with open('courses.json', 'w') as file:
    file.write(json.dumps(courses))

with open('courses.json', 'r') as file:
    new_courses = json.loads(file.read())

print('courses:', courses)
print('new_courses', new_courses)
print('The type of new_courses is:',type(new_courses))
