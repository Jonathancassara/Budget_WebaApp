// tailwind.config.js
module.exports = {
  content: [
    './frontend/templates/**/*.html', // Inclure vos templates Django
    './frontend/templates/**/*.html',
    './static/js/**/*.js',            // Inclure vos scripts JS si nécessaire
  ],
  theme: {
    extend: {},
  },
  plugins: [],
};
