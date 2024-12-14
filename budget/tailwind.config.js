module.exports = {
  content: [
    './templates/**/*.html',       // Tous les fichiers HTML/Django dans le dossier templates
    './frontend/templates/**/*.html', // Chemin spécifique si vous avez plusieurs apps
    './static/js/**/*.js',         // Fichiers JS dans static/js
  ],
  theme: {
    extend: {},
  },
  plugins: [],
};
