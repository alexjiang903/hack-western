// vite.config.js (Frontend)
import { fileURLToPath, URL } from 'node:url';
import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';
import vueJsx from '@vitejs/plugin-vue-jsx';
import vueDevTools from 'vite-plugin-vue-devtools';

export default defineConfig({
  plugins: [
    vue(),
    vueJsx(),
    vueDevTools(),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url)),
    },
  },
  server: {
    proxy: {
      // This will proxy API calls to your backend server
      '/api': {
        target: 'http://localhost:5000', // Backend URL
        changeOrigin: true, // Needed for virtual hosted sites
        secure: false, // If using https, set this to true
      },
    },
  },
});
