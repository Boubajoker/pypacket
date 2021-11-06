const btn_ctrl_1 = document.querySelector("#btn_control_1");
const btn_ctrl_2 = document.querySelector("#btn_control_2")

btn_ctrl_1.addEventListener('click', () => {
    window.alert("To shutdown the server close your terminal.")
})
btn_ctrl_2.addEventListener('click', () => {
    window.open("server/pypacket_server.zip")
})