Write the server-side code (in Python using Flask) to redirect the user to "/dashboard" after a successful login, using HTMX:

```python
@app.route('/login', methods=['POST'])
def login():
    # Login logic here
    if login_successful:
        response = make_response("Login successful")
        # Add your code here to redirect using HTMX
        return response
    else:
        return "Login failed", 401
```