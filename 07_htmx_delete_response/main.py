from fasthtml.common import *

app, rt = fast_app()

@rt("/")
def get():
    return Div(
        "Delete Item",
        hx_delete="/delete-item/1",
        hx_target="#item-list",
        hx_swap="outerHTML"
    ), Div(id="item-list")

@app.route('/delete-item/<int:id>', methods=['DELETE'])
def delete_item(id):
    # Delete item logic here
    response = make_response("", 204)
    return response

serve()