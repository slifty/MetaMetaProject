import json
class meta_audio:
	def GET(self, miid='', tasks='', results=''):
		tasks = json.loads(tasks)
		results = json.loads(results)
		return json.dumps('')
		
	def POST(self):	
		return json.dumps('')