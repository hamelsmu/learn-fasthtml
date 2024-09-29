Write the server-side code (in Python using Flask) to trigger a 'userUpdated' event on the client side when a user is updated:

```python
@app.route('/update-user', methods=['POST'])
def update_user():
    # Update user logic here
    response = make_response("User updated")
    # Add your code here to trigger the 'userUpdated' event
    return response
```