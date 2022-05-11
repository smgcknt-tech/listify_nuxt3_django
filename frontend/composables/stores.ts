import { useState } from "#app"

export const useHeaderOpen = () => {
  return useState("headerMenuBtn", () => false)
}
