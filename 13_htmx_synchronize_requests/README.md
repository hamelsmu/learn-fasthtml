Complete the HTML to synchronize requests between two buttons so that only one request can be in flight at a time:

```html
<div>
  <button hx-get="/data1">Load Data 1</button>
  <button hx-get="/data2">Load Data 2</button>
</div>
```