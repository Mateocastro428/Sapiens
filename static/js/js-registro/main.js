/* Tabs registro / login */
document.querySelectorAll('.form-tab').forEach(tab => {
  tab.addEventListener('click', () => {
    document.querySelectorAll('.form-tab').forEach(t => t.classList.remove('active'));
    tab.classList.add('active');
    
    // Alternar formularios
    if (tab.textContent === 'Crear cuenta') {
      document.getElementById('registro-form').classList.add('active');
      document.getElementById('login-form').classList.remove('active');
    } else if (tab.textContent === 'Iniciar sesión') {
      document.getElementById('login-form').classList.add('active');
      document.getElementById('registro-form').classList.remove('active');
    }
  });
});
