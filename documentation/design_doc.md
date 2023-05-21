# Design Document

Rough outline:

I have this idea for japanese counting practice app (or actually japanese counting spelling) - where the interface would emulate flick input on mobile devices. I want to practice docker, so I was thinking using python as a web-server, redis for storing values, for example - 100: hyaku - I know it's simple enough to do it with just python, but like I said I want to practice. When it comes to frontend I was thinking Svelte, where there is container for building a frontend, and the compiled result is somehow copied to python web app. I'm not sure how to handle test/build and production environments. 

Second thoughts:

Now that I see how it might work.
Maybe not necessarily replicate flick keyboard 100%, but take most of the concepts from it and have very similar interface. Flick keyboard makes sense on mobile, but I do not think it will work all that well just in browser on a PC. It will also be easier to implement and not got bogged down with tiny little details - I have got also a backend to do, so spending too much time on interface does not make sense.
