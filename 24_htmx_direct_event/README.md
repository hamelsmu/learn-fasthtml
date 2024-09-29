Complete the `hx-trigger` attribute to only trigger the request when the click event occurs directly on the button, not on any child elements:

```html
<button hx-post="/action" hx-trigger="click [...]">
  <span>Perform Action</span>
</button>
```