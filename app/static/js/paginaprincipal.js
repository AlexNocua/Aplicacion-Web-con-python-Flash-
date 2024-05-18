
const contenedorConfig = document.querySelector('#ContendorConfiguraciones')
const MostrarConfig = document.querySelector('#Mostrarconfiguraciones')
const OcultarBoton = document.querySelector('.button_ocultar')
console.log(MostrarConfig);

OcultarBoton.addEventListener('click', () => {
    contenedorConfig.style.opacity = '0'
    contenedorConfig.style.zIndex = '0'
})
MostrarConfig.addEventListener('click', () => {


    contenedorConfig.style.opacity = '1'
    contenedorConfig.style.zIndex = '111'


})



// ocultar el contenedor de lista de personas
const btnPersonas = document.querySelector('.btnpersonas')
const button_ocultarPersonas = document.querySelector('.button_ocultarPersonas')
const listaSolicitudes = document.querySelector('.listaSolicitudes')
button_ocultarPersonas.addEventListener('click', () => {
    listaSolicitudes.style.opacity = '0'
    listaSolicitudes.style.zIndex = '0'
})
btnPersonas.addEventListener('click', () => {
    listaSolicitudes.style.opacity = '1'
    listaSolicitudes.style.zIndex = '111'


})

// ocultar el contenedor de lista de solicitudes
const btnsolicitudes = document.querySelector('.btnsolicitudes')
const button_ocultarsolicitudes = document.querySelector('.button_ocultarsolicitudes')
const AceptarSolicitudes = document.querySelector('.AceptarSolicitudes')
button_ocultarsolicitudes.addEventListener('click', () => {
    AceptarSolicitudes.style.opacity = '0'
    AceptarSolicitudes.style.zIndex = '0'
})
btnsolicitudes.addEventListener('click', () => {
    AceptarSolicitudes.style.opacity = '1'
    AceptarSolicitudes.style.zIndex = '111'


})