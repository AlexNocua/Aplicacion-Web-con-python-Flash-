// alert('Funcionando')

//Mostar el Registro el registro
const contenidoLogin = document.getElementById('contenido_login')
const formRegistro = document.getElementById('register')
const mostrar_Form = document.getElementById('mostrar_Form').addEventListener('click', function () {
    console.log('ffadsa')
    // formRegistro.classList.toggle('mostrar_Form');
    if (formRegistro.style.display === 'none') {
        formRegistro.style.display = 'block';
        contenidoLogin.style.display = 'none';
    } else {
        formRegistro.style.display = 'none';
    }
})
//ocultar el registro

const btn_volverLogin = document.getElementById('btn_volverLogin').addEventListener('click', function () {

    if (formRegistro.style.display === 'block') {
        formRegistro.style.display = 'none';
        contenidoLogin.style.display = 'block';
    } else {
        formRegistro.style.display = 'block';
    }
})
