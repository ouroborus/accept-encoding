def app(environ, start_response):
  #data = b"Hello, World!\n"
  data = '\n'.join([
    '%s: %s' % (key, value) for key, value in sorted(environ.items())
  ])
  start_response("200 OK", [
    ("Content-Type", "text/plain"),
    ("Content-Length", str(len(data)))
  ])
  return iter([data])
