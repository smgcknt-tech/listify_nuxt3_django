import { defineNuxtConfig } from "nuxt3"
import confs from "./runtimeConfig"

export default defineNuxtConfig({
  css: ["vuetify/lib/styles/main.sass", "@mdi/font/css/materialdesignicons.min.css"],
  publicRuntimeConfig: confs,
  build: {
    transpile: ["vuetify"]
  }
})
