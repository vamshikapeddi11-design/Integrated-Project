async function loadStatus(){

let res = await fetch("http://127.0.0.1:5000/status")
let data = await res.json()

document.getElementById("level").innerText = data.level
document.getElementById("status").innerText = data.status

}

setInterval(loadStatus,2000)
