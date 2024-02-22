// alert('Funcionando')

//Mostar el Registro el registro
const app_description = document.getElementById('app_description')
const contenidoLogin = document.getElementById('contenido_login')
const formRegistro = document.getElementById('register')
const mostrar_Form = document.getElementById('mostrar_Form').addEventListener('click', function () {
    console.log('ffadsa')
    // formRegistro.classList.toggle('mostrar_Form');
    if (formRegistro.style.display === 'none') {
        formRegistro.style.display = 'flex';
        contenidoLogin.style.display = 'none';
        app_description.style.display = 'none';
    } else {
        formRegistro.style.display = 'none';
    }
})
//ocultar el registro

const btn_volverLogin = document.getElementById('btn_volverLogin').addEventListener('click', function () {

    if (formRegistro.style.display === 'flex') {
        formRegistro.style.display = 'none';
        contenidoLogin.style.display = 'flex';
        app_description.style.display = 'flex';
    } else {
        formRegistro.style.display = 'flex';
    }
})
