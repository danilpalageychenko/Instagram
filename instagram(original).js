if (location.href.indexOf("instagram.com")==-1)
{
console.log("Скрипт необходимо запускать в чьём-то профиле Instagram.\nНапример, https://www.instagram.com/timatiofficial/")
}
else if (parseInt(document.getElementsByClassName("_bkw5z")[1].firstChild.parentElement.attributes[1].value.split(" ").join(""))<3000000)
{
console.log("На аккаунте " + document.getElementsByClassName("_i572c")[0].innerHTML + " недостаточно подписчиков для работы скрипта.")
console.log("Выбери кого-то, у кого больше 3 миллионов подписчиков. \nНапример, https://www.instagram.com/timatiofficial/");
}
else
{
time=prompt("Введите количество секунд между действиями","30");
a=document.getElementsByClassName("_ah57t");
var i = 1;
function nakr() {a[0].click();setTimeout(function(){a[0].click()}, 2000);console.log("---------------------------------------------" + i++);}
setInterval(nakr,time*1000);
console.log("Скрипт запущен.");
console.log("Интервал между действиями равен " + time + " сек.");
console.log("При закрытии данной вкладки работа скрипта будет завершена.");
}
