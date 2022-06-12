var data = decodeURI(location.search.substr('1',).split('=')[1])
function change(datas, data) {
    console.log(datas.book)
    var books = document.getElementById('second')
    var middle = document.getElementById('middle')

    books.onclick = function () {
        middle.innerHTML = "";
        var tables = document.createElement('table')
        axios.get('http://172.20.10.3:8000/app/getimg?n=' + data).then(res => {
            // console.log(res.data.img)
            var result = res.data.img
            console.log(result)
            for (var i = 0; i < datas.book.length; i++) {
                if (datas.book[i] != 'NULL') {
                    var img = document.createElement('img');
                    var td1 = document.createElement('td');
                    var td2 = document.createElement('td')
                    var tr = document.createElement('tr');
                    var p = document.createElement('p');
                    tables.style.marginLeft = '350px'
                    tables.style.animation = "example1 3s ease-out 1s backwards"
                    middle.appendChild(tables)
                    tables.style.border = "1"
                    tables.appendChild(tr)
                    tr.appendChild(td1)
                    tr.appendChild(td2)
                    img.src = "http://172.20.10.3:8000/static/img/" + result[i]
                    img.style.width = "200px";
                    img.style.height = "200px"
                    td1.appendChild(img)
                    td2.appendChild(p)
                    var text = document.createTextNode(datas.book[i])
                    p.appendChild(text)
                    p.style.marginLeft = "400px"
                    p.style.fontSize = "25px"
                }
            }
        })
    }
}
if (data == '计算机科学与技术') {
    axios.get("http://172.20.10.3:8000/app/computer").then(res => {
        console.log(res)
        var data = decodeURI(location.search.substr('1',).split('=')[1])
        // console.log(data)
        change(res.data, data)
        lesson(res.data.Class, data, res.data.classurl)
        intro(res.data.intro[0], data)
    })
    analysis()
}

if (data == '管理') {
    axios.get("http://172.20.10.3:8000/app/manage").then(res => {
        var data = decodeURI(location.search.substr('1',).split('=')[1])
        console.log(res)
        change(res.data, data)
        lesson(res.data.Class, data, res.data.classurl)
        intro(res.data.intro[0], data)
    })
    analysis()
}

if (data == '英语') {
    //url is django address
    axios.get('http://172.20.10.3:8000/app/english').then(res => {
        var data = decodeURI(location.search.substr('1',).split('=')[1])
        console.log(res.data)
        change(res.data, data)
        lesson(res.data.Class, data, res.data.classurl)
        intro(res.data.intro[0], data)
    })
    analysis()
}

if (data == '经济学') {
    axios.get('http://127.0.0.1:8000/app/economys').then(res => {
        var data = decodeURI(location.search.substr('1',).split('=')[1])
        // console.log(res.data.Class)
        change(res.data, data)
        lesson(res.data.Class, data, res.data.classurl)
        intro(res.data.intro[0], data)
    })
    analysis()
}



function lesson(classcourse, data, classurl) {
    var course = document.getElementById('fifth')
    console.log(classcourse)
    var middless = document.getElementById('middle')
    course.onclick = function () {
        middless.innerHTML = "";
        var tables = document.createElement('table')
        for (var i = 0; i < classcourse.length; i++) {
            var finallys = classurl[i].split('course')[1]
            if (classcourse[i] != 'NULL') {
                var td1 = document.createElement('td');
                var td2 = document.createElement('td')
                var tr = document.createElement('tr');
                var p1 = document.createElement('p');
                var a = document.createElement('a')
                tables.style.marginLeft = '210px'
                tables.style.marginTop = '15px'
                tables.style.animation = "example1 4s ease-out 1s backwards";
                middless.appendChild(tables)
                tables.style.border = "1"
                tables.appendChild(tr)
                tr.appendChild(td1)
                tr.appendChild(td2)
                td1.appendChild(p1)
                td2.appendChild(a)
                var text1 = document.createTextNode(classcourse[i])
                var text2 = document.createTextNode(classurl[i])
                p1.appendChild(text1)
                a.appendChild(text2)
                a.href = "https://ke.qq.com/course" + finallys
                a.style.marginLeft = "100px"
                a.style.fontSize = "15px"
                p1.style.textAlign = "center"
                p1.style.marginTop = '10px'
                p1.style.fontSize = "20px"
            }
        }
    }
}

function intro(introsss, data) {
    var intros = document.getElementById('first')

    var middlesss = document.getElementById('middle')
    intros.onclick = function () {
        console.log(intros)
        middlesss.innerHTML = ""
        var tables = document.createElement('table')
        var img = document.createElement('img');
        var td1 = document.createElement('td');
        var td2 = document.createElement('td')
        var tr = document.createElement('tr');
        var p = document.createElement('p');
        tables.style.marginTop = '80px'
        middle.appendChild(tables)
        tables.style.animation = "example1 4s ease-out 1s backwards";
        tables.style.border = "1"
        tables.appendChild(tr)
        tr.appendChild(td1)
        tr.appendChild(td2)
        img.src = "http://172.20.10.3:8000/static/img/" + data + '.jpg'
        img.style.width = "300px";
        img.style.height = "300px"
        img.style.marginLeft = '20px'
        td1.appendChild(img)
        td2.appendChild(p)
        var text = document.createTextNode(introsss)
        p.appendChild(text)
        p.style.marginLeft = "20px"
        // p.style.textAlign = "center"
        p.style.fontSize = "20px"
    }
}


function analysis(){
    thirds = document.getElementById('third')
    middless = document.getElementById('middle')
    thirds.onclick=function(){
        console.log(thirds)
        form = document.createElement('form')
        input_1 = document.createElement('input')
        input_2 = document.createElement('input')
        input_3 = document.createElement('input')
        button = document.createElement('button')
        button.setAttribute('id','button1');
        form.setAttribute('method','get');
        button.setAttribute('type','button')
        middless.appendChild(form)
        form.appendChild(input_1)
        form.appendChild(input_2)
        form.appendChild(input_3)
        form.appendChild(button)
        let texts = document.createTextNode('分析')
        button.appendChild(texts)
        form.appendChild(button)
        button1.onclick=function(){
            value_1 = input_1.value
            value_2 = input_2.value
            value_3 = input_3.value
            axios.get('http://127.0.0.1:8000/app/usemain?num='+value_1+'&work='+value_2+'&page='+value_3).then(res => {
                console.log(res)
                
                if(res!='NULL'){
                    middless.innerHTML = ""
                    img1 = document.createElement('img')
                    img2 = document.createElement('img')
                    img3 = document.createElement('img')
                    img4 = document.createElement('img')
                    img1.src="http://127.0.0.1:8000/static/img/"+value_2 + "上班地点.png"
                    img2.src="http://127.0.0.1:8000/static/img/"+value_2 + "学历要求.png"
                    img3.src="http://127.0.0.1:8000/static/img/"+value_2 + "职责.png"
                    img4.src="http://127.0.0.1:8000/static/img/"+value_2 + "要求.png"
                    img1.style.width="350px"
                    img1.style.height="350px"
                    img1.style.marginLeft="70px"
                    img1.style.marginTop="50px"
                    img2.style.width="350px"
                    img2.style.height="350px"
                    img2.style.marginLeft="10px"
                    img3.style.width="350px"
                    img3.style.height="350px"
                    img3.style.marginLeft="10px"
                    img4.style.width="350px"
                    img4.style.height="350px"
                    img4.style.marginLeft="10px"
                    middless.appendChild(img1)
                    middless.appendChild(img2)
                    middless.appendChild(img3)
                    middless.appendChild(img4)
                }
            })

        }
    }
}
