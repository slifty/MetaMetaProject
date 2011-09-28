import web
from meta_video import meta_video
from meta_audio import meta_audio
from meta_text import meta_text
from meta_image import meta_image
import json

urls = (
	'/(.*)', 'front_controller'
)

class front_controller:
	CONTROLLERS = {
		'audio' : meta_audio,
		'video': meta_video,
		'image': meta_image,
		'text': meta_text
	}

	def GET(self, path):
		if not path in front_controller.CONTROLLERS:
			raise web.notfound('HTTP 404 - Unknown Request')
		controller = front_controller.CONTROLLERS[path]
		handler = controller()
		query = dict(web.input())
		try:
			res = handler.GET(**query)
			if isinstance(res, dict):
				web.header('Content-Type', 'application/json')
				res = json.dumps(res)
				if('callback' in query):
					return query['callback'] + '(' + res + ')'
				else:
					return res
			else:
				if('callback' in query):
					return query['callback'] + '({})'
				else:
					return "{}"
		except TypeError:
			msg = 'HTTP 400 - Bad Request'
			if getattr(controller, '__doc__', False):
				msg += '\n' + controller.__doc__
				raise self.badrequest(msg)
				def badrequest(self, message):
					return web.HTTPError('400 Bad Request', {'Content-Type': 'text/plain'}, message)

app = web.application(urls, globals())

if __name__ == "__main__": app.run()