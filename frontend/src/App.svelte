<script>
  import { onMount } from 'svelte';

  // Lógica de validación y envío
  let nombre = '';
  let correo = '';
  let telefono = '';
  let mensaje = '';
  let estado = '';

  // Lógica del menú desplegable personalizado
  let servicio = '';
  let menuAbierto = false;
  const opcionesServicio = [
    "Fabricación en Hule",
    "Mecanizado de Metales",
    "Soldadura",
    "Mantenimiento Pesado"
  ];

  function seleccionarServicio(opcion) {
    servicio = opcion;
    menuAbierto = false;
  }

  async function enviarCorreo() {
    // Validar que haya seleccionado un servicio
    if (servicio === '') {
      estado = 'Por favor, selecciona un tipo de servicio.';
      return;
    }

    estado = 'Enviando...';
    
    try {
      // Conectamos con el backend de FastAPI
      const respuesta = await fetch('https://morsol-api.onrender.com/api/contacto', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          nombre: nombre,
          correo: correo,
          telefono: telefono,
          servicio: servicio,
          mensaje: mensaje
        })
      });

      if (respuesta.ok) {
        const datos = await respuesta.json();
        estado = '¡Cotización enviada con éxito!';
        
        // Limpiamos los campos del formulario
        nombre = '';
        correo = '';
        telefono = '';
        servicio = '';
        mensaje = '';
      } else {
        estado = 'Hubo un error al enviar. Inténtalo de nuevo.';
      }
    } catch (error) {
      console.error(error);
      estado = 'Error de conexión con el servidor.';
    }
  }

  // Lógica de Animaciones al hacer Scroll
  onMount(() => {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          // Cuando entra en pantalla, quita la transparencia y el desplazamiento
          entry.target.classList.remove('opacity-0', 'translate-y-12');
          entry.target.classList.add('opacity-100', 'translate-y-0');
          // Deja de observar para que la animación solo ocurra una vez
          observer.unobserve(entry.target);
        }
      });
    }, {
      threshold: 0.15 // Se activa cuando el 15% de la sección es visible
    });

    // Aplica el observador a todos los elementos con esta clase
    document.querySelectorAll('.animar-scroll').forEach((el) => {
      observer.observe(el);
    });
  });
</script>

<main class="font-sans selection:bg-orange-500 selection:text-white pb-20">
  
  <!-- NAVEGACIÓN -->
  <nav class="fixed top-0 w-full z-50 bg-slate-900/95 backdrop-blur-md border-b border-slate-800">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between h-20">
        <div class="flex-shrink-0 flex items-center gap-3">
          <img src="/logo.png" alt="MORSOL Logo" class="h-22 object-contain">
        </div>
        <div class="hidden md:flex items-center space-x-8">
          <a href="#inicio" class="text-gray-300 hover:text-white text-sm font-semibold transition-colors">INICIO</a>
          <a href="#servicios" class="text-gray-300 hover:text-white text-sm font-semibold transition-colors">SERVICIOS</a>
          <a href="#nosotros" class="text-gray-300 hover:text-white text-sm font-semibold transition-colors">NOSOTROS</a>
          <a href="#proyectos" class="text-gray-300 hover:text-white text-sm font-semibold transition-colors">PROYECTOS</a>
          <a href="#contacto" class="bg-orange-600 hover:bg-orange-500 text-white px-5 py-2.5 rounded-md text-sm font-bold tracking-wide transition-colors shadow-lg">
             COTIZA AHORA
          </a>
        </div>
      </div>
    </div>
  </nav>

  <!-- HERO SECTION -->
  <section id="inicio" class="relative pt-40 pb-32 lg:pt-56 lg:pb-40 bg-slate-900 bg-[url('https://images.unsplash.com/photo-1504917595217-d4dc5ebe6122?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80')] bg-cover bg-center">
    <div class="absolute inset-0 bg-slate-900/80"></div> 
    <!-- Agregamos las clases base de animación al contenedor del texto -->
    <div class="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-left animar-scroll opacity-0 translate-y-12 transition-all duration-1000 ease-out">
      <h1 class="text-5xl md:text-6xl lg:text-7xl font-extrabold text-white tracking-tight mb-4 max-w-4xl leading-tight">
        SOLUCIONES INDUSTRIALES <br>
        <span class="text-orange-500">EN HULES Y METALES</span>
      </h1>
      <p class="mt-6 text-xl text-gray-300 font-light max-w-2xl mb-12">
        Brindamos servicios de mecanizado de precisión, fabricación en hule y mantenimiento de equipo pesado con estándares de calidad excepcionales.
      </p>
      <div class="flex gap-4">
        <a href="#servicios" class="bg-orange-600 hover:bg-orange-500 text-white font-bold py-4 px-10 rounded-md transition-colors text-sm uppercase tracking-wide">
          Nuestros Servicios
        </a>
        <a href="#proyectos" class="border-2 border-white hover:border-orange-500 hover:text-orange-500 text-white font-bold py-4 px-10 rounded-md transition-colors text-sm uppercase tracking-wide">
          Ver Proyectos &rarr;
        </a>
      </div>
    </div>
  </section>

  <!-- SERVICIOS -->
  <section id="servicios" class="py-28 bg-gray-50 border-b border-gray-200">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center animar-scroll opacity-0 translate-y-12 transition-all duration-1000 ease-out delay-100">
      <p class="text-orange-600 font-bold tracking-widest text-sm mb-2 uppercase">— Servicios</p>
      <h2 class="text-3xl md:text-4xl font-extrabold text-slate-900 uppercase tracking-wider mb-16">
        Lo que hacemos
      </h2>
      
      <div class="grid grid-cols-1 md:grid-cols-4 gap-8">
        <div class="p-8 bg-white rounded-lg shadow-sm border border-gray-100 hover:border-orange-500 hover:shadow-lg transition-all duration-300 text-left group">
          <div class="text-orange-500 text-4xl mb-6 font-black transform group-hover:scale-110 transition-transform">⚙️</div>
          <h3 class="text-lg font-bold text-slate-900 mb-3 uppercase">Mecanizado de Precisión</h3>
          <p class="text-gray-600 text-sm leading-relaxed">Torneado, fresado y rectificado de piezas metálicas con alta exactitud.</p>
        </div>
        <div class="p-8 bg-white rounded-lg shadow-sm border border-gray-100 hover:border-orange-500 hover:shadow-lg transition-all duration-300 text-left group">
          <div class="text-orange-500 text-4xl mb-6 font-black transform group-hover:scale-110 transition-transform">⬛</div>
          <h3 class="text-lg font-bold text-slate-900 mb-3 uppercase">Fabricación en Hule</h3>
          <p class="text-gray-600 text-sm leading-relaxed">Moldeado de alta resistencia, empaques y componentes industriales a medida.</p>
        </div>
        <div class="p-8 bg-white rounded-lg shadow-sm border border-gray-100 hover:border-orange-500 hover:shadow-lg transition-all duration-300 text-left group">
          <div class="text-orange-500 text-4xl mb-6 font-black transform group-hover:scale-110 transition-transform">🔥</div>
          <h3 class="text-lg font-bold text-slate-900 mb-3 uppercase">Soldadura Estructural</h3>
          <p class="text-gray-600 text-sm leading-relaxed">Uniones robustas y fabricación de soportes pesados garantizando durabilidad.</p>
        </div>
        <div class="p-8 bg-white rounded-lg shadow-sm border border-gray-100 hover:border-orange-500 hover:shadow-lg transition-all duration-300 text-left group">
          <div class="text-orange-500 text-4xl mb-6 font-black transform group-hover:scale-110 transition-transform">🔧</div>
          <h3 class="text-lg font-bold text-slate-900 mb-3 uppercase">Mantenimiento Pesado</h3>
          <p class="text-gray-600 text-sm leading-relaxed">Mecánica correctiva e intervención estructural para maquinaria industrial.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- NOSOTROS -->
  <section id="nosotros" class="bg-slate-900 py-32 border-t border-slate-800 overflow-hidden">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 grid grid-cols-1 md:grid-cols-2 gap-16 items-center">
      <div class="rounded-lg overflow-hidden border-l-4 border-orange-500 shadow-2xl relative h-[500px] animar-scroll opacity-0 translate-y-12 transition-all duration-1000 ease-out">
        <img src="/manuel chambeando.png" alt="Trabajo en taller" class="w-full h-full object-cover">
      </div>
      <div class="animar-scroll opacity-0 translate-y-12 transition-all duration-1000 ease-out delay-200">
        <p class="text-orange-500 font-bold tracking-widest text-sm mb-3 uppercase">— Nosotros</p>
        <h2 class="text-3xl md:text-5xl font-extrabold text-white uppercase tracking-wider mb-8 leading-tight">
          Experiencia que <br> <span class="text-orange-500">garantiza resultados</span>
        </h2>
        <p class="text-gray-400 mb-10 text-lg leading-relaxed">
          Somos un taller industrial enfocado en brindar soluciones robustas. Rechazamos lo frágil; nos especializamos en la mecánica pesada, el mecanizado y la formulación de hules para sectores productivos exigentes.
        </p>
        
        <div class="space-y-6">
          <div class="flex items-start gap-5">
            <div class="text-orange-500 text-3xl font-bold mt-1">✓</div>
            <div>
              <h4 class="text-white font-bold uppercase text-lg">Calidad Estructural</h4>
              <p class="text-gray-400 text-base mt-1">Trabajamos con materiales de primera y altos estándares de torneado.</p>
            </div>
          </div>
          <div class="flex items-start gap-5">
            <div class="text-orange-500 text-3xl font-bold mt-1">✓</div>
            <div>
              <h4 class="text-white font-bold uppercase text-lg">Compromiso Total</h4>
              <p class="text-gray-400 text-base mt-1">Entregas puntuales para que la industria no se detenga.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- PROYECTOS -->
  <section id="proyectos" class="py-32 bg-white">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center animar-scroll opacity-0 translate-y-12 transition-all duration-1000 ease-out">
      <p class="text-orange-600 font-bold tracking-widest text-sm mb-2 uppercase">— Proyectos</p>
      <h2 class="text-3xl md:text-5xl font-extrabold text-slate-900 uppercase tracking-wider mb-16">
        Algunos de nuestros trabajos
      </h2>
      
      <!-- Cuadrícula de fotos -->
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8 text-left">
        
        <!-- Proyecto 1: Mecanizado -->
        <div class="group cursor-pointer">
          <div class="overflow-hidden rounded-md shadow-md bg-slate-800 aspect-[4/3] mb-5 relative">
            <img src="https://placehold.co/600x450/1e293b/f97316?text=Foto+Eje+CNC" alt="Eje industrial" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110">
          </div>
          <h3 class="text-slate-900 font-bold uppercase text-base mb-1">Eje Industrial</h3>
          <p class="text-gray-500 text-sm">Mecanizado de precisión</p>
        </div>

        <!-- Proyecto 2: Hule -->
        <div class="group cursor-pointer">
          <div class="overflow-hidden rounded-md shadow-md bg-slate-800 aspect-[4/3] mb-5 relative">
            <img src="https://placehold.co/600x450/1e293b/f97316?text=Foto+Hule+Moldeado" alt="Piezas de hule" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110">
          </div>
          <h3 class="text-slate-900 font-bold uppercase text-base mb-1">Empaques a Medida</h3>
          <p class="text-gray-500 text-sm">Fabricación de hule moldeado</p>
        </div>

        <!-- Proyecto 3: Soldadura -->
        <div class="group cursor-pointer">
          <div class="overflow-hidden rounded-md shadow-md bg-slate-800 aspect-[4/3] mb-5 relative">
            <img src="https://images.unsplash.com/photo-1504328345606-18bbc8c9d7d1?q=80&w=600&auto=format&fit=crop" alt="Estructura metálica" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110">
          </div>
          <h3 class="text-slate-900 font-bold uppercase text-base mb-1">Estructura Metálica</h3>
          <p class="text-gray-500 text-sm">Fabricación y soldadura pesada</p>
        </div>

        <!-- Proyecto 4: Mantenimiento -->
        <div class="group cursor-pointer">
          <div class="overflow-hidden rounded-md shadow-md bg-slate-800 aspect-[4/3] mb-5 relative">
            <img src="https://images.unsplash.com/photo-1619642751034-765dfdf7c58e?q=80&w=600&auto=format&fit=crop" alt="Mantenimiento de flota" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110">
          </div>
          <h3 class="text-slate-900 font-bold uppercase text-base mb-1">Mantenimiento Flota</h3>
          <p class="text-gray-500 text-sm">Mecánica y reparación estructural</p>
        </div>
        
      </div>
    </div>
  </section>

  <!-- CONTACTO -->
  <section id="contacto" class="bg-gray-50 pb-32 pt-10">
    <div class="max-w-7xl mx-auto grid grid-cols-1 lg:grid-cols-2 shadow-2xl overflow-hidden rounded-xl animar-scroll opacity-0 translate-y-12 transition-all duration-1000 ease-out">
      
      <div class="bg-slate-900 p-12 lg:p-20 flex flex-col justify-center">
        <p class="text-orange-500 font-bold tracking-widest text-sm mb-3 uppercase">— Contáctanos</p>
        <h2 class="text-3xl md:text-5xl font-extrabold text-white uppercase tracking-wider mb-10 leading-tight">
          Cotiza tu proyecto <br> <span class="text-orange-500">Con Nosotros</span>
        </h2>
        
        <div class="space-y-8 text-gray-300">
          <div class="flex items-center gap-5">
            <span class="text-orange-500 font-bold text-2xl">📞</span>
            <p class="text-lg">+505 82441616</p>
          </div>
          <div class="flex items-center gap-5">
            <span class="text-orange-500 font-bold text-2xl">✉️</span>
            <p class="text-lg">administracion@industriasmorsol.com</p>
          </div>
          <div class="flex items-center gap-5">
            <span class="text-orange-500 font-bold text-2xl">📍</span>
            <p class="text-lg leading-relaxed">Puente la granja 35 metros al sur,<br>León - Nic</p>
          </div>
        </div>
      </div>

      <div class="bg-white p-12 lg:p-20">
        <form on:submit|preventDefault={enviarCorreo} class="space-y-8">
          <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
            <input type="text" bind:value={nombre} placeholder="Nombre completo" required
              class="w-full bg-gray-50 border border-gray-200 rounded-md px-5 py-4 focus:outline-none focus:border-orange-500 focus:ring-1 focus:ring-orange-500 text-slate-900 transition-colors">
            
            <input type="email" bind:value={correo} placeholder="Correo electrónico" required
              class="w-full bg-gray-50 border border-gray-200 rounded-md px-5 py-4 focus:outline-none focus:border-orange-500 focus:ring-1 focus:ring-orange-500 text-slate-900 transition-colors">
          </div>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-8 relative">
            <input type="tel" bind:value={telefono} placeholder="Teléfono" required
              class="w-full bg-gray-50 border border-gray-200 rounded-md px-5 py-4 focus:outline-none focus:border-orange-500 focus:ring-1 focus:ring-orange-500 text-slate-900 transition-colors">
            
            <div class="relative w-full">
              <button 
                type="button" 
                on:click={() => menuAbierto = !menuAbierto}
                class="w-full h-full min-h-[56px] bg-gray-50 border border-gray-200 rounded-md px-5 flex justify-between items-center focus:outline-none focus:border-orange-500 focus:ring-1 focus:ring-orange-500 text-left transition-colors"
              >
                <span class={servicio === '' ? 'text-gray-400' : 'text-slate-900 font-medium'}>
                  {servicio === '' ? 'Tipo de servicio' : servicio}
                </span>
                <svg class={`w-5 h-5 text-gray-500 transition-transform duration-200 ${menuAbierto ? 'rotate-180' : ''}`} fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
                </svg>
              </button>

              {#if menuAbierto}
                <button type="button" class="fixed inset-0 w-full h-full cursor-default z-10" on:click={() => menuAbierto = false} aria-label="Cerrar menú"></button>
                <ul class="absolute z-20 top-[105%] left-0 w-full bg-white border border-gray-200 shadow-2xl rounded-md overflow-hidden origin-top">
                  {#each opcionesServicio as opcion}
                    <li>
                      <button 
                        type="button"
                        on:click={() => seleccionarServicio(opcion)}
                        class="w-full text-left px-5 py-4 text-slate-700 hover:bg-orange-50 hover:text-orange-600 hover:font-bold transition-all border-l-4 border-transparent hover:border-orange-500"
                      >
                        {opcion}
                      </button>
                    </li>
                  {/each}
                </ul>
              {/if}
            </div>
          </div>

          <textarea bind:value={mensaje} rows="5" placeholder="Cuéntanos sobre tu proyecto o necesidad (Medidas, materiales, etc.)" required
            class="w-full bg-gray-50 border border-gray-200 rounded-md px-5 py-4 focus:outline-none focus:border-orange-500 focus:ring-1 focus:ring-orange-500 text-slate-900 transition-colors"></textarea>

          <button type="submit"
            class="w-full bg-orange-500 hover:bg-orange-600 text-white font-bold py-5 rounded-md transition duration-300 uppercase tracking-widest text-base flex justify-center items-center gap-2 shadow-lg hover:shadow-xl transform hover:-translate-y-1">
            Enviar Mensaje
          </button>
          {#if estado}
            <p class="text-center text-sm font-semibold text-slate-800 mt-4 p-3 bg-orange-100 border border-orange-200 rounded-md shadow-sm">{estado}</p>
          {/if}
        </form>
      </div>
    </div>
  </section>

  <!-- FOOTER -->
  <footer class="bg-slate-950 py-12 border-t border-slate-900 text-center">
    <div class="max-w-7xl mx-auto px-4 flex flex-col items-center justify-center gap-6">
      <img src="/logo.png" alt="MORSOL Logo" class="h-30 grayscale opacity-40 hover:grayscale-0 hover:opacity-100 transition-all cursor-pointer">
      <p class="text-gray-500 text-sm">© 2026 MORSOL Soluciones Industriales. León, Nicaragua. Todos los derechos reservados.</p>
    </div>
  </footer>

  <!-- BOTÓN FLOTANTE WHATSAPP -->
  <a href="https://wa.me/50582441616" target="_blank" rel="noopener noreferrer" 
     class="fixed bottom-8 right-8 bg-[#25D366] hover:bg-green-500 text-white p-4 rounded-full shadow-2xl transition-all duration-300 hover:scale-110 z-50">
    <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="currentColor" viewBox="0 0 16 16">
      <path d="M13.601 2.326A7.854 7.854 0 0 0 7.994 0C3.627 0 .068 3.558.064 7.926c0 1.399.366 2.76 1.057 3.965L0 16l4.204-1.102a7.933 7.933 0 0 0 3.79.965h.004c4.368 0 7.926-3.558 7.93-7.93A7.898 7.898 0 0 0 13.6 2.326zM7.994 14.521a6.573 6.573 0 0 1-3.356-.92l-.24-.144-2.494.654.666-2.433-.156-.251a6.56 6.56 0 0 1-1.007-3.505c0-3.626 2.957-6.584 6.591-6.584a6.56 6.56 0 0 1 4.66 1.931 6.557 6.557 0 0 1 1.928 4.66c-.004 3.639-2.961 6.592-6.592 6.592zm3.615-4.934c-.197-.099-1.17-.578-1.353-.646-.182-.065-.315-.099-.445.099-.133.197-.513.646-.627.775-.114.133-.232.148-.43.05-.197-.1-.836-.308-1.592-.985-.59-.525-.985-1.175-1.103-1.372-.114-.198-.011-.304.088-.403.087-.088.197-.232.296-.346.1-.114.133-.198.198-.33.065-.134.034-.248-.015-.347-.05-.099-.445-1.076-.612-1.47-.16-.389-.323-.335-.445-.34-.114-.007-.247-.007-.38-.007a.729.729 0 0 0-.529.247c-.182.198-.691.677-.691 1.654 0 .977.71 1.916.81 2.049.098.133 1.394 2.132 3.383 2.992.47.205.84.326 1.129.418.475.152.904.129 1.246.08.38-.058 1.171-.48 1.338-.943.164-.464.164-.86.114-.943-.049-.084-.182-.133-.38-.232z"/>
    </svg>
  </a>
</main>