Modify the following HTML to update the browser's address bar to "/new-page" when the button is clicked, without triggering a full page reload:

```html
<button hx-get="/new-page-content" hx-target="body">Go to New Page</button>
```