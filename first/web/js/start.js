let data = decodeURI(location.search.substr('1', ).split('&')[0].split('=')[1])
let commits = document.getElementById('last')
let firsts = document.getElementById('first')
firsts.innerHTML='欢迎您 , '+  data
