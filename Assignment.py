import requests
import json

#Assignment Object
#Properties: TOKEN, id, name, description, created_at, updated_at, due_at
#Functions: 	
class Assignment:
	def __init__(self, TOKEN, assignment_id, assignment_name, assignment_description, assignment_created_at, assignment_updated_at, assignment_due_at):
		self.TOKEN = TOKEN
		self.id = assignment_id
		self.name = assignment_name
		self.description = assignment_description
		self.created_at = assignment_created_at
		self.updated_at = assignment_updated_at
		self.due_at = assignment_due_at
	