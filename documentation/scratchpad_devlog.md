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