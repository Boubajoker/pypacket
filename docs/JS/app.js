const txtAnim = document.querySelector("h1")

new Typewriter(txtAnim, {
    deleteSpeed: 50,
    loop: true,
})
.typeString("Welcome To pypacket Documentation !")
.pauseFor(3000)
.typeString('Create <strong style="color: red;">youre packet files !</strong>')
.pauseFor(3000)
.deleteChars(32)
.start()