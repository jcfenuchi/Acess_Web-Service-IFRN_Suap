
<h1>Proposta da atividade</h1>
<p>esse projeto foi feito para ser uma atividade final da materia programação para redes, onde foi nós dada a missão de encontrar uma api(end point, web services) e consumir os dados fazendo uma aplicação que exiba os dados de forma elegante, facil entendimento e utilização.</p>


<h2>Instruções para registro de token, e execução.<br></h2>
<p>para realizar seu acesso é necessario obter um token de acesso.<br><p>
<li>1º faça login na sua conta suap atraves do link<a href='https://suap.ifrn.edu.br/'> https://suap.ifrn.edu.br/</a></li>


<li>2º acesse <a href='https://suap.ifrn.edu.br/api/'>https://suap.ifrn.edu.br/api/ </a> <-- nesta parte deverar ter seu nome e matricula no canto superior direito.</li>

![exemplo_da_pagina](/image/suap_api.png)


<li>3º clique em Minhas Aplicações ou acesse <a href='https://suap.ifrn.edu.br/api/applications/'>https://suap.ifrn.edu.br/api/applications/ </a><br> faça uma aplicação "padrão" que pode ser encontrado no readme.md do cliente suap django em referencias.<br>
<p> - Client type: confidential<br> -Authorization Grand Type: Authorization Code<br>-Reducert URIs: http://localhost:8888/complete/suap/</p>

![suap_cadastro](/image/suap_applications.png)

<p>logo após voce vai obter</p>
um json contendo client_id e client_secret essas duas informações deve ser colocado em ambos codigos localizados <br>
<strong> -> cliente_suap_django/cliente_suap_django/local_settings_sample.py</strong><br>
<strong> -> cliente_suap_django/cliente_suap_django/local_settings.py</strong><br>
SOCIAL_AUTH_SUAP_KEY = "codigo client_id"<br>
SOCIAL_AUTH_SUAP_SECRET = "codigo cliente_secret"<br>

![suap_aplicação](/image/passo%203.png)
![suap_aplicação](/image/cod_aut_01.png)
![suap_aplicação](/image/cod_aut_02.png)

<li> 4º instalar o django e suas dependencias encontradas em requerements.txt dentro da pasta cliente_suap_django.<br>
- pip install <br>
Django==3.2.4<br>
social-auth-app-django==4.0.0<br>
social-auth-core==4.1.0<br>
<li> 5º entrar na pasta cliente_suap_django e digita o seguinte comando<br> 
<strong>python3 ./manage.py runserver 0.0.0.0:8888</strong><br>

![codigo_executando](/image/manager_client_django.png)

logo após abra e acesse no seu navegador<br>
<strong>https://localhost:8888</strong><br>

![locahost](/image/localhost%3A8888%20.png)
<p>apos feito o login deverar aparecer os seguintes campos, para nossa aplicação o campo importante é o <strong>Access_Token</strong> que deve ser colocado dentro do codigo main.py</p>

![locahost](/image/Django_logado.png)
<br>basta colocar no codigo main.py em uma variavel chamada Token.<br>

![codigo_main](/image/codigo%20_no_main.png)
<br>obs: apos essa etapa o token temporario sera de quem logou, então se deslogar e outra pessoa fizer login vai ser gerado um outro token temporario da pessoa que realizou o acesso.
<li> 6º execute o codigo main.py<br>
<strong>python3 main.py</strong></li>
<br>

![menu_main](/image/menu_main.png)
<p> atualmente o menu conta com essas funcionalidades de consultas da imagem <p>

<h2>Referencias</h2>
<p>nesse codigo foi ultilizado o cliente_suap_django para obtenção do token para realizar a consulta no qual pode ser encontrado atraves do link <a href='https://github.com/ifrn-oficial/cliente_suap_django'>cliente_suap_django</a> <-- codigo cliente suap django<br><a href='https://suap.ifrn.edu.br/api/docs/'>endpoints/Docs da api</a> <-- onde pode ser encontrado links e info sobre Get,Post... <br></p>

<h3>Finalização</h3>
<p>deixo o codigo aberto para quem quiser desfrutar ou aprimorar, espero que esse codigo ajude futuro usuarios da api ou de como ultilizar.<p>

