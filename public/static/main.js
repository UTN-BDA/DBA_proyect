const url = "http://127.0.0.1:5000/api/categorias/listar_categorias";
const urlEgresos = "http://127.0.0.1:5000/api/egresos/listar_egresos";
const urlIngresos = "http://127.0.0.1:5000/api/ingresos/listar_ingresos";

fetch(url)
  .then(res => res.json())
  .then(data => {
    const categorias = data.map(e => e.nombre); // Listado de nombres para las etiquetas
    const idsCategorias = data.map(e => e.id_categoria); // Lista los id de las categorias

    // Obtener egresos
    fetch(urlEgresos)
      .then(res => res.json())
      .then(egresos => {
        const egresosPorCategoria = new Array(idsCategorias.length).fill(0); //Crea un array 
        egresos.forEach(egreso => { // Recorre cada objeto del array 
          const categoriaId = egreso.categoria_id;
          const index = idsCategorias.indexOf(categoriaId);// Busca en la lista de ids de categorias
                                                           // si encuntra una coincidencia guarda la posicion en index, si no existe el index sera -1 
          if (index !== -1) {
            egresosPorCategoria[index] += egreso.monto;
          }
        });
        // Obtener ingresos
        fetch(urlIngresos)
          .then(res => res.json())
          .then(ingresos => {
            const ingresosPorCategoria = new Array(idsCategorias.length).fill(0);
            ingresos.forEach(ingreso => {
              const categoriaId = ingreso.categoria_id; 
              const index = idsCategorias.indexOf(categoriaId);
              if (index !== -1) {
                ingresosPorCategoria[index] += ingreso.monto;
              }
            });
            // Crear el grafico
            const ctx = document.getElementById('myChart');

            new Chart(ctx, {
              type: 'bar',
              data: {
                labels: categorias,
                datasets: [
                  {
                    label: 'Egresos',
                    data: egresosPorCategoria,
                    borderWidth: 1,
                    backgroundColor: 'rgba(255, 99, 132, 0.8)',
                    hoverBackgroundColor: 'rgba(255, 99, 132, 1)',
                    borderColor: 'rgba(255, 99, 132, 1)',
                    borderRadius: 4,
                    barThickness: 30,
                    barPercentage: 0.6,
                  },
                  {
                    label: 'Ingresos',
                    data: ingresosPorCategoria,
                    borderWidth: 1,
                    backgroundColor: 'rgba(54, 162, 235, 0.8)',
                    hoverBackgroundColor: 'rgba(54, 162, 235, 1)',
                    borderColor: 'rgba(54, 162, 235, 1)',
                    borderRadius: 4,
                    barThickness: 30,
                    barPercentage: 0.6,
                  }
                ]
              },
              options: {
                responsive: true,
                plugins: {
                  title: {
                    display: true,
                    text: 'Resumen de Ingresos y Egresos por Categoría',
                    font: {
                      size: 18,
                      weight: 'bold'
                    }
                  },
                  legend: {
                    position: 'top',
                    labels: {
                      font: {
                        size: 14
                      }
                    }
                  },
                  tooltip: {
                    mode: 'index',
                    intersect: false,
                    backgroundColor: 'rgba(0, 0, 0, 0.8)',
                    titleFont: { size: 14, weight: 'bold' },
                    bodyFont: { size: 14 },
                  }
                },
                scales: {
                  y: {
                    beginAtZero: true,
                    grid: {
                      display: true,
                      color: 'rgba(0, 0, 0, 0.05)',
                    },
                    title: {
                      display: true,
                      text: 'Monto',
                      font: { size: 14, weight: 'bold' }
                    }
                  },
                  x: {
                    grid: { display: false },
                    title: {
                      display: true,
                      text: 'Categorías',
                      font: { size: 14, weight: 'bold' }
                    }
                  }
                }
              }
            });
          });
      });
  });