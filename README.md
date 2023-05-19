# Japanese Counting Spelling Practice App

Rough outline:

I have this idea for japanese counting practice app (or actually japanese counting spelling) - where the interface would emulate flick input on mobile devices. I want to practice docker, so I was thinking using python as a web-server, redis for storing values, for example - 100: hyaku - I know it's simple enough to do it with just python, but like I said I want to practice. When it comes to frontend I was thinking Svelte, where there is container for building a frontend, and the compiled result is somehow copied to python web app. I'm not sure how to handle test/build and production environments. 


# Devlog
frontend setup:
- `docker run -v ${PWD}:/app -w /app node:14.18 yarn create vite frontend --template svelte`

- **OBSOLETE**:
- `pushd frontend`
- `docker run -v ${PWD}:/app -w /app node:14 npx degit sveltejs/template svelte-app`


After some fixes, it works but `rollup` does not seem to watch for changes properly.
(used `docker exec -it japanese-counting-frontend-1 sh` to debug the container)

Tried using `nodeamon`, but it did not work.
Tried using `supervisor`, does not work in first few tries, but this does:
- `CMD supervisor -w . -x sh -- -c "npm run dev"`
(BTW: these do NOT work `CMD ["supervisor", "-w", ".", "-x", "npm", "run", "dev"]`, `CMD ["supervisor", "-w", ".", "-x", "sh", "-c", "npm run dev"]`, `CMD ["supervisor", "-w", ".", "-x", "sh", "-c", "'npm run dev'"]`)

