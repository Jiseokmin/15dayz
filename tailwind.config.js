module.exports = {
  purge: [],
  darkMode: false, // or 'media' or 'class'
  theme: {    
      // minWidth: {
      //  '0': '0',
      //  '1/4': '25%',
      //  '1/2': '50%',
      //  '3/4': '75%',
      //  'full': '100%',
      // },
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
