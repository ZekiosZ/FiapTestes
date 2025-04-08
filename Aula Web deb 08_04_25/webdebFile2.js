console.log("Script Externo rodando para o DOM");

const tituloElemento = document.getElementById("tituloDinámico");//seleciona o elemento <h2> pelo seu ID
tituloElemento.textContent = "Texto alterado pelo JavaScript";//alterna o texto do <h2>
tituloElemento.style.color = 'purple';//altera a cor do texto para roxo

const botaoElemento = document.getElementById('umBotao');//selecionando o botão por ID
botaoElemento.addEventListener('click',function(){
    alert('Botão foi cliclado!!!');//quando o botão for clickado, uma caixa de alerta aparecera
})    