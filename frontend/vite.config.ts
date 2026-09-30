import { defineConfig } from 'vite'
import { resolve } from 'node:path'

export default defineConfig({
  base: '/static/react-report/',
  build: {
    outDir: resolve(__dirname, '../static/react-report'),
    // Preserve the many unrelated bundles already served from this directory.
    emptyOutDir: false,
    rollupOptions: {
      input: {
        app: resolve(__dirname, 'src/main.tsx'),
        home: resolve(__dirname, 'src/home.tsx'),
        copilot: resolve(__dirname, 'src/copilot/panel-entry.tsx'),
        'copilot-admin': resolve(__dirname, 'src/copilot/admin-entry.tsx')
      },
      output: { entryFileNames: '[name].js', assetFileNames: '[name].[ext]' }
    }
  }
})
