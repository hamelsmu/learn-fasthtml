Modify the HTML to listen for a 'userUpdated' event on the body element and trigger a refresh of the user info div:

```html
<div id="user-info" hx-get="/user-info">
  <!-- User info here -->
</div>
```