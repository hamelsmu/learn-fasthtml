Modify the HTML to show a loading spinner (with class 'spinner') during an HTMX request:

```html
<button hx-get="/slow-data">Load Slow Data</button>
<div class="spinner" style="display:none;">Loading...</div>
```