Complete the `hx-trigger` attribute to debounce keyup events by 500ms and only trigger if the input has changed:

```html
<input type="text" name="search" hx-get="/search" hx-trigger="keyup [...]">
```