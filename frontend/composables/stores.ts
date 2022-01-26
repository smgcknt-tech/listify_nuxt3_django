import { useState } from "#app"

export const useSomething = () => {
  return useState("NameOfState", () => 0)
}
