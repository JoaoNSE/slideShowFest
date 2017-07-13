# slideShowFest
Aplicação distribuída que envia fotos de um celular android para servidor e mostra em um monitor.

# Como usar
Servidor:
Primeiro deve-se baixar as bibliotecas necessárias do python.

O código mostraImg.py possui uma função para mostrar as imagens na pasta fotos, se ela estiver vazia, mostra a foto da pasta semFoto.
A interface passa as fotos caso uma tecla seja apertada e volta a foto quando a seta esquerda é apertada.

O código clique_auto.py possui uma função que fica clicando tab a cada certo intervalo de tempo.

O código servidorFotos.py chama as duas funções e a executam em threads separadas.

Para rodar o servidor, basta executar o servidorFotos.py.
