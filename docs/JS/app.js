const txtAnim = document.querySelector("h1");
const btnCopy = document.querySelector(".btn-copy");
const txtCopy = document.querySelector("#install_command");

btnCopy.addEventListener('click', () => {
    navigator.clipboard.writeText(txtCopy.innerText);
})

new Typewriter(txtAnim, {
    deleteSpeed: 50,
    loop: true,
})
.typeString("Welcome To pypacket Documentation !")
.pauseFor(3000)
.typeString('Code <strong style="color: aliceblue;">packet, it will apears !</strong>')
.pauseFor(300)
.deleteChars(32)
.start()