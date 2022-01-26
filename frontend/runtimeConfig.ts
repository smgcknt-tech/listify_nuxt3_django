// local
const confs = {
  ENV: process.env.ENV,
  ApiUrl: "http://127.0.0.1:8000",
  NuxtApi: "http://localhost:3000"
}

// Use different name from .env file or you get error
if (process.env.ENV === "develop") {
  confs.ApiUrl = process.env.API_URL
  confs.NuxtApi = process.env.NUXT_API_URL
}

export default confs
