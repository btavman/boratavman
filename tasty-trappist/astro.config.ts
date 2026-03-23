import tailwindcss from "@tailwindcss/vite";
import { defineConfig } from "astro/config";
import type { PluginOption } from "vite";

// https://astro.build/config
export default defineConfig({
  vite: {
    plugins: [tailwindcss() as PluginOption],
  },
});
