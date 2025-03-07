var data = decodeURI(location.search.substring('1',).split('=')[1])
console.log(data)
function change(datas, data) {
    console.log(datas.book);
    var books = document.getElementById('second');
    var middle = document.getElementById('middle');

    books.onclick = function () {
        middle.innerHTML = "";
        var tables = document.createElement('table');
        tables.style.marginLeft = '350px';
        tables.style.animation = "example1 3s ease-out 1s backwards";
        tables.style.border = "1";
        middle.appendChild(tables);

        axios.get('http://127.0.0.1:8000/app/getimg?n=' + data).then(res => {
            var result = res.data.img;
            console.log(result);
            for (var i = 0; i < datas.book.length; i++) {
                if (datas.book[i] !== 'NULL') {
                    var img = document.createElement('img');
                    var td1 = document.createElement('td');
                    var td2 = document.createElement('td');
                    var tr = document.createElement('tr');
                    var p = document.createElement('p');

                    img.src = "http://127.0.0.1:8000/static/img/" + result[i];
                    img.style.width = "200px";
                    img.style.height = "200px";

                    p.textContent = datas.book[i];
                    p.style.marginLeft = "400px";
                    p.style.fontSize = "25px";

                    td1.appendChild(img);
                    td2.appendChild(p);
                    tr.appendChild(td1);
                    tr.appendChild(td2);
                    tables.appendChild(tr);
                }
            }
        });
    }
}
// 定义一个函数用于处理请求和分析数据
function fetchData(url) {
    axios.get(url)
      .then(res => {
        if (res.status === 200) { // 或者 res.ok === true
          console.log(res);
          var data = decodeURI(location.search.substring(1).split('=')[1]);
          change(res.data, data);
          lesson(res.data.Class, data, res.data.classurl);
          intro(res.data.intro[0], data);
          analysis(); // 这里调用分析函数
        } else {
          console.error("Failed to fetch data:", res.statusText);
        }
      })
      .catch(error => {
        console.error("Error fetching data:", error);
      });
  }
  
  // 根据不同的数据类型调用不同的请求函数
  if (data == '计算机科学与技术') {
    fetchData("http://127.0.0.1:8000/app/computer");
  }
  
  if (data == '管理') {
    fetchData("http://127.0.0.1:8000/app/manage");
  }
  
  if (data == '英语') {
    fetchData("http://127.0.0.1:8000/app/english");
  }
  
  if (data == '经济学') {
    fetchData("http://127.0.0.1:8000/app/economys");
  }
  


  function lesson(classcourse, data, classurl) {
    var course = document.getElementById('fifth');
    console.log(classcourse);
    var middless = document.getElementById('middle');
    course.onclick = function () {
        middless.innerHTML = "";
        var tables = document.createElement('table');
        tables.style.marginLeft = '210px';
        tables.style.marginTop = '15px';
        tables.style.animation = "example1 4s ease-out 1s backwards";
        tables.style.border = "1";
        middless.appendChild(tables);

        for (var i = 0; i < classcourse.length; i++) {
            if (classcourse[i] !== 'NULL') {
                var tr = document.createElement('tr');
                var td1 = document.createElement('td');
                var td2 = document.createElement('td');
                var p1 = document.createElement('p');
                var a = document.createElement('a');

                var finallys = classurl[i].split('course')[1];
                var text1 = document.createTextNode(classcourse[i]);
                var text2 = document.createTextNode(classurl[i]);

                a.href = "https://ke.qq.com/course" + finallys;
                a.style.marginLeft = "100px";
                a.style.fontSize = "15px";

                p1.style.textAlign = "center";
                p1.style.marginTop = '10px';
                p1.style.fontSize = "20px";

                p1.appendChild(text1);
                a.appendChild(text2);
                td1.appendChild(p1);
                td2.appendChild(a);
                tr.appendChild(td1);
                tr.appendChild(td2);
                tables.appendChild(tr);
            }
        }
    };
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
        img.src = "http://127.0.0.1:8000/static/img/" + data + '.jpg'
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
    var thirds = document.getElementById('third');
    var middless = document.getElementById('middle');
    thirds.onclick = function(){
        // console.log(thirds);
        middless.innerHTML = "";
        var img1 = document.createElement('img');
        var img2 = document.createElement('img');
        var img3 = document.createElement('img');
        var img4 = document.createElement('img');
        img1.src = "http://127.0.0.1:8000/static/img/python上班地点.png";
        img2.src = "http://127.0.0.1:8000/static/img/python学历要求.png";
        img3.src = "http://127.0.0.1:8000/static/img/python职责.png";
        img4.src = "http://127.0.0.1:8000/static/img/python要求.png";
        img1.style.width = "350px";
        img1.style.height = "350px";
        img1.style.marginLeft = "70px";
        img1.style.marginTop = "50px";
        img2.style.width = "350px";
        img2.style.height = "350px";
        img2.style.marginLeft = "10px";
        img3.style.width = "350px";
        img3.style.height = "350px";
        img3.style.marginLeft = "10px";
        img4.style.width = "350px";
        img4.style.height = "350px";
        img4.style.marginLeft = "10px";
        middless.appendChild(img1);
        middless.appendChild(img2);
        middless.appendChild(img3);
        middless.appendChild(img4);
    }
}
    //     var form = document.createElement('form');
    //     var label = document.createTextNode('请选择：');
    //     var select = document.createElement('select');
    //     var optionEmpty = document.createElement('option');
    //     var option1 = document.createElement('option');
    //     var option2 = document.createElement('option');
    //     var input_2 = document.createElement('input');
    //     var input_3 = document.createElement('input');
    //     var button = document.createElement('button');
    //     button.setAttribute('id','button1');
    //     form.setAttribute('method','get');
    //     button.setAttribute('type','button');
    //     middless.appendChild(form);
    //     form.appendChild(label);
    //     form.appendChild(select);
    //     select.appendChild(optionEmpty);
    //     select.appendChild(option1);
    //     select.appendChild(option2);
    //     form.appendChild(button);
    //     var texts = document.createTextNode('分析');
    //     button.appendChild(texts);

    //     optionEmpty.value = '';
    //     optionEmpty.textContent = '请选择';
    //     option1.value = '重新爬取';
    //     option1.textContent = '重新爬取';
    //     option2.value = '不重新爬取';
    //     option2.textContent = '不重新爬取';

    //     input_2.placeholder = '工作岗位';
    //     input_3.placeholder = '多少页';

    //     button.style.display = 'none'; // 默认隐藏分析按钮

    //     select.onchange = function() {
    //         if (form.contains(input_2) && form.contains(input_3)) {
    //             form.removeChild(input_2);
    //             form.removeChild(input_3);
    //         }
    //         if (select.value === '重新爬取') {
    //             form.appendChild(input_2);
    //             form.appendChild(input_3);
    //             button.style.display = 'block'; // 显示分析按钮
    //         }
    //     };

    //     button.onclick = function(){
    //         var value_1 = select.value;
    //         var value_2 = input_2.value;
    //         var value_3 = input_3.value;
    //         axios.get('http://127.0.0.1:8000/app/usemain?num='+value_1+'&work='+value_2+'&page='+value_3).then(res => {
    //             console.log(res);

    //             if(res !== 'NULL'){
    //                 middless.innerHTML = "";
    //                 var img1 = document.createElement('img');
    //                 var img2 = document.createElement('img');
    //                 var img3 = document.createElement('img');
    //                 var img4 = document.createElement('img');
    //                 img1.src = "http://127.0.0.1:8000/static/img/" + value_2 + "上班地点.png";
    //                 img2.src = "http://127.0.0.1:8000/static/img/" + value_2 + "学历要求.png";
    //                 img3.src = "http://127.0.0.1:8000/static/img/" + value_2 + "职责.png";
    //                 img4.src = "http://127.0.0.1:8000/static/img/" + value_2 + "要求.png";
    //                 img1.style.width = "350px";
    //                 img1.style.height = "350px";
    //                 img1.style.marginLeft = "70px";
    //                 img1.style.marginTop = "50px";
    //                 img2.style.width = "350px";
    //                 img2.style.height = "350px";
    //                 img2.style.marginLeft = "10px";
    //                 img3.style.width = "350px";
    //                 img3.style.height = "350px";
    //                 img3.style.marginLeft = "10px";
    //                 img4.style.width = "350px";
    //                 img4.style.height = "350px";
    //                 img4.style.marginLeft = "10px";
    //                 middless.appendChild(img1);
    //                 middless.appendChild(img2);
    //                 middless.appendChild(img3);
    //                 middless.appendChild(img4);
    //             }
    //         });
    //     };

    //     form.style.textAlign = 'center'; // 居中显示表单
    // };
// }
