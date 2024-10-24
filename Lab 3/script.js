//script utilizado para importar las librerias necesarias para implementar MD5 desde la consola del navegador

var script = document.createElement('script');
script.src = 'https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.1.1/crypto-js.min.js';
script.onload = function() {
    console.log('CryptoJS cargado');
};
document.head.appendChild(script);