import requests
import json
 
from Course import Course
from Assignment import Assignment
token = "12128~Ow2Ej413oHxrtHqV81El97ai0eEHcBrV3yLQGwJfaaBHhnK9JoY4jGBANgxnTTJY"

# py:function:: getCourses()
#
#   Return a list that contains a users courses.
def getCourses():
	courses = []
	r = requests.get("https://stjohnsprep.instructure.com/api/v1/courses?access_token=%s" % (token)).json()
	for course in r:
		id = course["id"]
		name = course["name"]
		course_code = course["course_code"]
	
		courses.append(Course(token, id, name, course_code))
	return courses