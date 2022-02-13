import { defineNuxtConfig } from "nuxt3"
import confs from "./runtimeConfig"

export default defineNuxtConfig({
  css: [
    "@/assets/scss/variables.scss",
    "@/assets/scss/main.scss",
  ],
  publicRuntimeConfig: confs
})
