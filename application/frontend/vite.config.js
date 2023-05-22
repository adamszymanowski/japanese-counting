import { defineConfig } from 'vite'
import { svelte } from '@sveltejs/vite-plugin-svelte'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [svelte()],
  server: {
    host: '0.0.0.0',
    port: 5000,
    watch: {
        // use polling to detect file changes in Docker
        usePolling: true,
        interval: 500
    },
  },
})
