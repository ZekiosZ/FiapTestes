let idade = 17;
if(idade>=18){
    console.log("Você e maio de idade");
}

let nota= 6;
if (nota>=7){ 
   console.log("Aluno aprovado!!!");
}else{
    console.log("Vc ta fudido");
}

let hora = 21;
if(hora<12){
    console.log("Bom dia");
}else if(hora<18){
    console.log('Se mata, Boa tarde');
}else{
    console.log("Boa noite fdp");
}

let idadeUsuario = 15;
if(idadeUsuario>=0 && idadeUsuario<=12){
    console.log("Vocé e uma criança macaquinho");
}else if(idadeUsuario>=13 && idadeUsuario<=17){
    console.log("Voce e um adolescente"); 
}else{
    console.log("Voce e um adulto");
} 
const readline = require ("readline").createInterface({
     input: process.stdin,
     output: process.stdout
})

readline.question("Por favor, digite sua idade: ",(idade) => {
    const idadeNumero = parseInt(idade);

    if(!isNaN(idadeNumero)){
        if(idadeNumero>=18){
            console.log('Voce e maior de idade');
        }
    }else{
        console.log("Por favor digite umj numero valido");
    }
    readline.close;
})
