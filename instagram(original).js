if (location.href.indexOf("instagram.com")==-1)
{
console.log("Скрипт необходимо запускать в чьём-то профиле Instagram.\nНапример, https://www.instagram.com/timatiofficial/")
}
else
{
time=prompt("Введите количество секунд между действиями","30");
a=document.getElementsByClassName("vBF20 _1OSdk")[0].firstChild
var i = 1;
function nakr() {
a.click();
if (b=document.getElementsByClassName("aOOlW -Cab_")[0])
{
setTimeout(function(){b.click()}, 2000);
setTimeout(function(){a.click()}, 3000);
}}
setInterval(nakr,time*1000);
}
