let first = document.getElementById('mb3')
let second = document.getElementById('mb2')
// console.log(second)
first.onclick = function () {
    window.location.href = "http://127.0.0.1:5500/first/web/html/register.html"
}

second.onclick = function () {
    var user = document.getElementById('user').value
    var pwd = document.getElementById('pwd').value
    console.log(user)
    console.log(pwd)
    axios.get("http://172.20.10.3:8000/app/login?user=" + user + "&pwd=" + pwd).then(res => {
        console.log(res)
        this.result = res.data
        console.log(res)
        var result = res.data
        if (result == '登录成功') {
            // window.location.href = "http://127.0.0.1:5500/first/web/html/start.html"
            document.getElementById('first').action = "./start.html";
            document.getElementById("first").submit(); 
        }
        else {
            alert('登录失败')
        }
    })
}





