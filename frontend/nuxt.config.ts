import { defineNuxtConfig } from "nuxt3"
import confs from "./runtimeConfig"

export default defineNuxtConfig({
  css: ["@/assets/css/main.scss"],
  publicRuntimeConfig: confs,
  build: {
    parallel: true,
    cache: true,
    hardSource: true
  }
})
