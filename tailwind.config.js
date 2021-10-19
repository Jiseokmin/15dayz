module.exports = {
  purge: [],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
    
    },
  },
  variants: {
    extend: {       ringColor: ['hover', 'active'],},
  },
  plugins: [],
}

const colors = require('tailwindcss/colors')

module.exports = {
  theme: {
    ringColor: {
      white: colors.white,
      pink: colors.fuchsia,
    }
  }
}
