import { defineNuxtConfig } from "nuxt3"
import confs from "./runtimeConfig"

export default defineNuxtConfig({
  css: ["vuetify/lib/styles/main.sass", "@/assets/css/main.scss"],
  publicRuntimeConfig: confs,
  build: {
    parallel: true,
    cache: true,
    hardSource: true,
    transpile: ["vuetify"]
  }
})
