from fasthtml.common import *

app, rt = fast_app()

@rt("/")
def get():
    return Div(
        Button("Load Data 1", hx_get="/data1", hx_sync="exclusive"),
        Button("Load Data 2", hx_get="/data2", hx_sync="exclusive")
    )

@rt("/data1")
def data1():
    import time
    time.sleep(2)  # Simulating a slow request
    return "Data 1 from the server"

@rt("/data2")
def data2():
    import time
    time.sleep(2)  # Simulating a slow request
    return "Data 2 from the server"

serve()