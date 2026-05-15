// ── Tabs ──────────────────────────────────────────
const tabs = document.querySelectorAll('.form-tab');
const bodies = document.querySelectorAll('.form-body');

tabs.forEach((tab, i) => {
  tab.addEventListener('click', () => {
    tabs.forEach(t => t.classList.remove('active'));
    bodies.forEach(b => b.classList.remove('active'));
    tab.classList.add('active');
    bodies[i].classList.add('active');
  });
});

// Mostrar error de URL si viene redirigido con ?error=
const params = new URLSearchParams(window.location.search);
const error = params.get('error');
if (error) {
  const msg = error === 'correo_existe'
    ? 'Este correo ya está registrado. Inicia sesión.'
    : 'Correo o contraseña incorrectos.';
  const errorEl = document.createElement('p');
  errorEl.textContent = msg;
  errorEl.style.cssText = 'color:#B84F2C;font-size:13px;margin-top:8px;font-style:italic;';
  // Mostrar debajo del botón activo
  const activeForm = document.querySelector('.form-body.active');
  if (activeForm) {
    const submitBtn = activeForm.querySelector('.btn-submit');
    if (submitBtn) submitBtn.parentElement.insertBefore(errorEl, submitBtn.nextSibling);
  }
  // Activar tab correcto según error
  if (error === 'credenciales') {
    tabs[1].click();
  }
}

// ── Submit Registro ───────────────────────────────
const btnRegistro = document.querySelector('#registro-form .btn-submit');
if (btnRegistro) {
  btnRegistro.addEventListener('click', async (e) => {
    e.preventDefault();
    const formEl = document.getElementById('registro-form');
    const body = new FormData();
    formEl.querySelectorAll('input[name], select[name]').forEach(el => {
      body.append(el.name, el.value);
    });

    try {
      const res = await fetch('/registro', { 
        method: 'POST', 
        body,
        redirect: 'follow'
      });
      if (res.redirected) {
        window.location.href = res.url;
      }
    } catch (err) {
      console.error('Error en registro:', err);
    }
  });
}

// ── Submit Login ──────────────────────────────────
const btnLogin = document.querySelector('#login-form .btn-submit');
if (btnLogin) {
  btnLogin.addEventListener('click', async (e) => {
    e.preventDefault();
    const formEl = document.getElementById('login-form');
    const body = new FormData();
    formEl.querySelectorAll('input[name]').forEach(el => {
      body.append(el.name, el.value);
    });

    try {
      const res = await fetch('/login', { 
        method: 'POST', 
        body,
        redirect: 'follow'
      });
      if (res.redirected) {
        window.location.href = res.url;
      }
    } catch (err) {
      console.error('Error en login:', err);
    }
  });
}

// ── Link "Inicia sesión aquí" en el footer del form ──
const footerLink = document.querySelector('.form-footer-link');
if (footerLink) {
  footerLink.addEventListener('click', () => tabs[1].click());
}
