// @ts-check
import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';

// https://astro.build/config
export default defineConfig({
  // Configure base path for GitHub Pages
  // Set to '/' if using custom domain, otherwise '/repo-name'
  base: '/',

  // Output configuration
  outDir: 'dist',

  vite: {
    plugins: [tailwindcss()]
  }
});
