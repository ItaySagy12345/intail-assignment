import tsconfigPaths from "vite-tsconfig-paths";
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react(), tsconfigPaths()],
  resolve: {
    alias: [{ find: "@", replacement: "/src" }]
  },
  build: {
    outDir: "../app/build"
  }
});
