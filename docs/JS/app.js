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
console.warn("%c!!STOP!! This is a tool only for devellopers GET OUT of here! Or see GitHub Repo https://github.com/Boubajoker/pypacket/", "color: red; font-size:30px");
console.log("     _              ");
console.log("    | |             ");
console.log(" ___| |_ ___  _ __  ");
console.log("/ __| __/ _ \| '_ \ ");
console.log("\__ \ || (_) | |_) |");
console.log("|___/\__\___/| .__/ ");
console.log("             | |    ");
console.log("             |_|    ");