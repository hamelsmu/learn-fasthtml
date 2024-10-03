from fasthtml.common import *

# The below code to the following JavaScript code:
# document.addEventListener('DOMContentLoaded', function() {
#     document.body.addEventListener('htmx:configRequest', (event) => {
#         event.detail.headers['my-token'] = 'my_token_value';
#     });
# });
js = HtmxOn('configRequest', "event.detail.headers['my-token'] = 'my_token_value';")
app, rt = fast_app(hdrs=(js,))

@rt("/")
def get(): return Div("Click me", hx_get="/data")

@rt("/data")
def data(): return "Data from the server"

serve()
