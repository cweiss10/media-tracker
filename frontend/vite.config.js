import { defineConfig } from 'vite'
import { svelte } from '@sveltejs/vite-plugin-svelte'

console.log('Vite configuration loaded');

// https://vite.dev/config/
export default defineConfig({
  plugins: [svelte()],
  server: {
    port: 5173, // Default port for Vite
  },
})
