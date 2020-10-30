## `Accept-Encoding` request header reflector

This is designed for hosting on Heroku for use with https://nearest.ouroborus.org

`http` requests return a JSON response containing the request headers. Meant for testing.

`https` requests return a JSON response containing just the `Accept-Encoding` request header. Allowed `Origin` domains are whitelisted. Rejected domains receive 403 response.
