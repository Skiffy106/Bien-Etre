/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./app/**/*.{js,jsx,ts,tsx}", "components/**/*.{js,jsx,ts,tsx}"],
  presets: [require("nativewind/preset")],
  theme: {
    extend: {
      colors: {
        primary: {
          primary: "#606C38",
          accent: "#DDA15E",
          "accent-2": "#BC6C25",
          "accent-3": "#A8DADC",
          "accent-4": "#457B9D",
          "accent-5": "#1D3557",
          "accent-6": "#E63946",
          background: "#FEFAE0",
          "background-dark": "#03071E",
        }
      }
    },
  },
  plugins: [],
}

