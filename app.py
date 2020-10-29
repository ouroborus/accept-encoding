import json

def app(environ, start_response):
  #data = b"Hello, World!\n"
  #data = '\n'.join([
  #  '%s: %s' % (key, value) for key, value in sorted(environ.items())
  #]).encode('utf-8')
  #data = json.dumps({ 'accept-encoding': environ.get('HTTP_ACCEPT_ENCODING', None) }).encode('utf-8')
  data = json.dumps({str(k):str(v) for k, v in environ.items()}).encode('utf-8')
  start_response("200 OK", [
    ("Content-Type", "application/json"),
    ("Content-Length", str(len(data)))
  ])
  return [data]
