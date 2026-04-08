// Carga un archivo HTML y lo inserta en el contenedor
async function loadPartial(containerId, filePath) {
  try {
    const response = await fetch(filePath);
    const html = await response.text();
    document.getElementById(containerId).innerHTML = html;
  } catch (error) {
    console.error(`Error cargando ${filePath}:`, error);
  }
}

// Cargar todos los componentes
document.addEventListener('DOMContentLoaded', () => {
  loadPartial('header-container', 'partials/header.html');
  loadPartial('fusion-badge-container', 'partials/fusion-badge.html');
  loadPartial('hero-container', 'partials/hero.html');
  loadPartial('progress-container', 'partials/progress-bar.html');
  loadPartial('eras-container', 'partials/eras.html');
  loadPartial('how-container', 'partials/how-it-works.html');
  loadPartial('cta-container', 'partials/cta.html');
  loadPartial('footer-container', 'partials/footer.html');
});