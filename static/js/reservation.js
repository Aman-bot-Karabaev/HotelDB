let phoneInput = document.querySelector('#phone')
console.log(phoneInput)
const im = new Inputmask("+\\9\\96(999)99-99-99");
im.mask(phoneInput);