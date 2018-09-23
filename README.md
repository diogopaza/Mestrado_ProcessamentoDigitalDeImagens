<h1>Processamento Digital de Imagens</h1>
<h3>Disciplina Mestrado Ciências da Computação UEM</h3>

<p> Processamento de imagens: é um processo onde a entrada do sistema é uma imagem e a saída é um conjunto de valores númericos.
<br>
Visão Computacional: possui como entrada uma imagem porém a saída é uma interpretação da imagem como um todo ou parcialmente.

</p>
<h4>OpenCV(Open Source Computer Vision): é uma biblioteca de programação de código aberta. </h4>
<p>OpenCV foi desenvolvida pela Intel e possui mais de 500 funções.</p>

<h4>Instalação do módulo OpenCV do Python 3  no Windows</h4>
	<ul>
		<li>Baixar e instalar o Python. Link de download: <a href='https://www.python.org/downloads/'>download Python</a></li>
		<li>Baixar e instalar o <a href='https://support.microsoft.com/en-us/help/2977003/the-latest-supported-visual-c-downloads'>Microsoft Visual C++ 2017</a></li>
		<li>Instalar o Matplotlib que é uma biblioteca dedicada ao traçado gráfico.<br>
			comando no console: pip install matplotlib</li>
		<li>Instalar o módulo numpy que fornece centenas de funções matemáticas úteis além de constantes como base de logaritmos naturais.<br>
		Para instalar o módulo numpy executar o comando no console: pip install numpy </li>
		<li><a href='https://www.lfd.uci.edu/~gohlke/pythonlibs/#opencv'>Baixar OpenCV</a></li>
		<li>Copiar o arquivo do OpenCV que foi baixado para a subpasta script dentro do diretório onde seu Python esta instalado</li>
		<li>Dentro da subpasta scripts do seu Python executar o comando: pip install <strong>nomeDoArquivo Baixado</strong></li>
		<li>Para testar, executar o dentro do IDLE do Python o comando import cv2, se nenhum erro for retornado o módulo OpenCV está funcionando.</li>
	</ul>

<h4>Comando básicos<h4>
	<p>No prompot do DOS(ou qualquer outro console) digitar o comando python com isso ele mostrara na tela a versão do Python e com isto já é testado se o P`ython está funcionando.</p>

<h6>Iniciando com OpenCV</h6>
<p>Para carregar uma imagem, primeiro parametro o nome da imagem e o segundo caso vaor seja 0 a imagem será carregada em tons de cinza, caso o parametro seja omitido a imagem é carregada com cores normalmente   </p>

imagem_carregada = cv2.imread("nome_da_imagem", )
<p>Exibir a imagem em uma janela, primeiro parametro o nome da janela e o segundo o nome da iamgem que foi carregada</p>
cv2.imshow("ImagemCarregada", imagemCarregada)

<h3>Detalhes de Python e OpenCV</h3>
<p></p>
<br>
<br>
<br>
<p>link tutorial Pyton + OpenCV: https://www.youtube.com/watch?v=wmC5U9Vv7Ck&list=PL-t7zzWJWPtx3enns2ZAV6si2p9zGhZJX</p>