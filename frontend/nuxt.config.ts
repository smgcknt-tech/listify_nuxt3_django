import { defineNuxtConfig } from "nuxt3"
import confs from "./runtimeConfig"

export default defineNuxtConfig({
  css: ["@/assets/scss/main.scss"],
  modules: ["nuxtjs-mdi-font"],
  vite: {
    ssr: true,
    css: {
      preprocessorOptions: {
        scss: {
          sourceMap: true,
          additionalData: `@import "@/assets/scss/mixin.scss"; @import "@/assets/scss/variables.scss";`
        }
      }
    }
  },
  publicRuntimeConfig: confs
})
