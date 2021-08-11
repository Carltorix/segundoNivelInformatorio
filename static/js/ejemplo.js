

//tomas el select
const miSelect=document.getElementById("miSelect");
//creas el objeto option
var miOption=document.createElement("option");
//cargar el primer valor
miOption.setAttribute("value",1.05);
miOption.appendchiled("0 a 100");
miSelect.appendChild(miOption);

var puntaje=1.20;
const incr=0.20;
extremoInf=100;
extremoSup=200;
for ( var i=3,i< 7,i++){
    miOption.setAttribute("value",puntaje);
    miOption.appendChild(str(extremoInf+ "a" +extremoSup);
    miSelect.appendChild(miOption);
    puntaje=puntaje+incr;
    extremoInf= extremoInf +100;
    extremoSup= extremoSup +100;     
}
