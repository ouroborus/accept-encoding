import json

origins = set([
  'https://nearest.ouroborus.org',
])

def app(environ, start_response):
  origin = environ.get('HTTP_ORIGIN', None)
  if origin is None or origin not in origins:
    start_response("403 Forbidden", [
      ("Vary", "Origin"),
    ])
    return []
  
  accept_encoding = environ.get('HTTP_ACCEPT_ENCODING', None)
  if accept_encoding is None:
    accept_encoding = 'null'
  else:
    accept_encoding = '"' + accept_encoding + '"'
  
  #data = ('{"Accept-Encoding":' + accept_encoding + '}').encode('utf-8')
  data = json.dumps({str(k):str(v) for k, v in environ.items()}).encode('utf-8')
  
  start_response("200 OK", [
    ("Content-Type", "application/json"),
    ("Access-Control-Allow-Origin", origin),
  ])
  return [data]
