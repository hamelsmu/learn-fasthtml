# [Tricks Of The HTMX Masters](https://hypermedia.systems/tricks-of-the-htmx-masters/) Quiz

This repository contains a comprehensive quiz to test and reinforce your understanding of the Hypermedia Systems Chapter "Tricks of the HTMX Masters". The quiz covers various advanced topics and techniques for building dynamic web applications using HTMX.

## Topics Covered

The repo includes questions on the following key areas:

1. HTMX Attributes
   - hx-swap and its modifiers (swap, settle, show, scroll, focus-scroll)
   - hx-trigger and its modifiers (filters, synthetic events)
   - hx-target
   - hx-get, hx-post, and other HTTP method attributes
   - hx-sync
   - hx-push-url
   - hx-disable
   - hx-indicator
   - hx-preserve

2. Events in HTMX
   - HTMX-generated events (htmx:load, htmx:configRequest, htmx:beforeRequest, htmx:afterRequest, etc.)
   - Server-generated events (using HX-Trigger response header)
   - Using htmx:configRequest for custom headers
   - Canceling requests with htmx:abort

3. HTTP Requests & Responses
   - Custom headers in HTMX (HX-Request, HX-Trigger, HX-Target, etc.)
   - HTTP response codes and HTMX behavior (204 No Content, 286 for stopping polling)
   - HX-Refresh and HX-Redirect response headers

4. Updating Other Content
   - Expanding selection
   - Out of Band swaps (hx-swap-oob)
   - Event-driven updates

5. Debugging HTMX
   - Using htmx.logAll() for logging all events
   - Monitoring events in Chrome using monitorEvents()

6. Security Considerations
   - Content Security Policies and their impact on HTMX
   - Using hx-disable to prevent HTMX processing on user-generated content

7. Configuring HTMX
   - Setting config options via meta tags (defaultSwapStyle, defaultSwapDelay, etc.)

8. Advanced HTMX Techniques
   - Synchronizing requests with hx-sync
   - Using event filters in hx-trigger
   - Working with synthetic events (like 'intersect' for lazy loading)
   - Handling form submissions (including file uploads)
   - Implementing polling and SSE (Server-Sent Events)

9. Integration with other technologies
   - Using HTMX with server-side frameworks (e.g., Flask)
   - Combining HTMX with client-side scripting (hyperscript, JavaScript)




