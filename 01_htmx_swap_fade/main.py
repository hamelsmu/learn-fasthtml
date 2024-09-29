from fasthtml.common import *

# Define custom CSS for fade-out animation
css = Style("""
.fade-me-out.htmx-swapping {
  opacity: 0;
  transition: opacity 1s ease-out;
}
""")

# Create a FastHTML app with custom CSS header
app, rt = fast_app(hdrs=(css,))

@rt("/")
def get():
    # Return a Div containing a paragraph with HTMX attributes
    return Div(P("Click Me to Change",
        hx_get="/data",  # HTMX will make a GET request to /data when clicked
        hx_swap="outerHTML swap:1s",  # Replace the entire element, with a 1s swap duration
        cls="fade-me-out"  # Apply the fade-out class for animation
    ))

@rt("/data")
def data(): return "New Data"  # Simple endpoint returning new content

# Start the FastHTML server
serve()