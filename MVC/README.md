# MVC

Objetivo é entender MVC

## O que é MVC?

MVC é uma sigla que representa o padrão de arquitetura de software "Model-View-Controller" (Modelo-Visão-Controlador). É um padrão amplamente utilizado no desenvolvimento de aplicativos e sistemas de software, especialmente em desenvolvimento web, para separar a lógica de negócios, a lógica de apresentação e a lógica de controle em componentes distintos. Essa separação ajuda a melhorar a manutenção, escalabilidade e flexibilidade do software. Aqui está uma explicação das três principais partes do padrão MVC:

1. Modelo (Model):
   - O "Modelo" representa a camada de dados e a lógica de negócios do aplicativo. Ele é responsável por gerenciar os dados, realizar cálculos, aplicar regras de negócios e responder a consultas do Controlador. O Modelo não está diretamente ligado à interface do usuário; em vez disso, fornece uma representação abstrata dos dados subjacentes.

2. Visão (View):
   - A "Visão" é a camada de apresentação do aplicativo. Ela é responsável por exibir os dados ao usuário de uma forma compreensível. A Visão não contém lógica de negócios; seu principal objetivo é apresentar os dados do Modelo de uma maneira que seja fácil de entender e interagir. Em muitas aplicações web, as Visões são frequentemente criadas com HTML, CSS e, em alguns casos, JavaScript.

3. Controlador (Controller):
   - O "Controlador" é a camada de controle do aplicativo. Ele atua como intermediário entre o Modelo e a Visão. O Controlador recebe as entradas do usuário, decide como responder a elas e faz chamadas para o Modelo para realizar operações. Ele também atualiza a Visão para refletir as mudanças nos dados. Em essência, o Controlador orquestra as interações entre o Modelo e a Visão.

A principal vantagem do padrão MVC é a separação clara de responsabilidades. Isso facilita a manutenção do código, pois as mudanças em uma parte do aplicativo geralmente não afetam diretamente as outras partes. Além disso, facilita o desenvolvimento colaborativo, pois diferentes equipes ou desenvolvedores podem trabalhar em camadas diferentes do aplicativo sem interferir no trabalho uns dos outros.

MVC é amplamente adotado em muitos frameworks de desenvolvimento web, como Ruby on Rails, Django (para Python), Angular (para JavaScript/TypeScript), e outros, para facilitar o desenvolvimento de aplicativos web escaláveis e organizados.


**OBS:** Texto gerado pelo ChatGPT

## Como rodar?

~~~
python3 view.py
~~~

As instruções aparecem no terminal.