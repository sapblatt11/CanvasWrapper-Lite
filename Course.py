import requests
import json

from Assignment import Assignment
#Course Object
#Properties: token, id, name, course_code
#Functions: getAssignments

class Course:
	def __init__(self, token, id, name, course_code):
		self.token = token
		self.id = id
		self.name = name
		self.course_code = course_code
	
	#return a list of Assignment objects for a Course
	def getAssignments(self):
		assignments = []
		r = requests.get("https://stjohnsprep.instructure.com/api/v1/courses/%s/assignments?access_token=%s" % (self.id, self.token)).json()
		for assignment in r:
			assignment_id = assignment["id"]
			assignment_name = assignment["name"]
			assignment_description = assignment["description"]
			assignment_created_at = assignment["created_at"]
			assignment_updated_at = assignment["updated_at"]
			assignment_due_at = assignment["due_at"]
			
			assignments.append(Assignment(self.token, assignment_id, assignment_name, assignment_description, assignment_created_at, 
				assignment_updated_at, assignment_due_at))
		
		return assignments
	