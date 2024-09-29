from fasthtml.common import *

app, rt = fast_app()

@rt("/")
def get():
    return Div(
        "Click me",
        id="interactive-div",
        onclick="monitorEvents(this, 'click')"
    )

@app.route("/static/js/main.js")
def js():
    return """
        document.getElementById('interactive-div')
            .addEventListener('click', () => {
                console.log('Clicked!');
            });
    """

serve()