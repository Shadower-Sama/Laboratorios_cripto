//script utilizado para generar el hash de la contraseña por consola
var hash = CryptoJS.MD5('weakpass').toString();
console.log(hash);