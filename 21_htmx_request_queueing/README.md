Complete the `hx-trigger` attribute to queue up to 3 requests if they occur while a request is in flight:

```html
<button hx-post="/increment" hx-trigger="click [...]">Increment</button>
```