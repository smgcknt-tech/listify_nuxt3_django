import { defineNuxtConfig } from "nuxt3"
import confs from "./runtimeConfig"

export default defineNuxtConfig({
  css: ["@/assets/css/main.scss"],
  build: {
    transpile: ["vuetify"]
  },
  vite: {
    define: {
      "process.env.DEBUG": "false"
    }
  },
  publicRuntimeConfig: confs
})
