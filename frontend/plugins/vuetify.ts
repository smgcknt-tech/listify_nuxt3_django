import { defineNuxtPlugin } from "#app"
import { createVuetify } from "vuetify"
import * as components from "vuetify/components"
import * as directives from "vuetify/directives"

export default defineNuxtPlugin((nuxtApp) => {
  const vuetify = createVuetify({
    theme: {
      defaultTheme: "myCustomTheme",
      themes: {
        myCustomTheme: {
          dark: false,
          colors: {
            background: "#6200EE",
            surface: "#6200EE",
            primary: "#6200EE",
            secondary: "#03DAC6",
            error: "#B00020",
            info: "#2196F3",
            success: "#4CAF50",
            warning: "#FB8C00"
          },
          variables: {}
        }
      }
    },
    components,
    directives
  })
  nuxtApp.vueApp.use(vuetify)
})
