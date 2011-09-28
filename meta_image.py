import json
class meta_image:
	def GET(self, miid='', tasks='{}', results='{}', **kwargs):
		try:
			tasks = json.loads(tasks)
		except:
			return {"error": "Invalid input parameters."}
		
		try:
			results = json.loads(results)
		except:
			results = {}
		
		return results
		
	def POST(self):
		return json.dumps('', **kwargs)