# **Java Spring Open Feign Plugin**

Plugin Java Spring Open Feign é um conjunto de técnologias e metodologia de desenvolvimento que juntos auxiliam na construção de Clients HTTP em Aplicações Java Spring Boot.

Este Plugin possui suporte para projetos criados junto a Stack Java Spring Boot REST API. E Dado a isso também suporta projetos Java Spring Boot que utilizem **Maven** como gerenciador de dependencias e tenham suas configurações de properties no padrão **YAML**.


Nas proximas sessões você encontrará em detalhes informações sobre como utilizar Plugin Java Spring Open Feign para habilitar a capacidade de construir clients HTTP em seus projetos. 

Abaixo esta de forma sumariazada cada sessão desta documentação.

1. [Técnologias base da Plugin](#tecnologias-base-da-plugin)
2. [Capacidades Habilitadas ao uso da Plugin](#quais-são-as-capacidades-habilitadas)
3. [Beneficio de utilizar a Plugin](#quais-os-beneficios-de-utilizar-java-spring-open-feign-plugin)
4. [Aplicando Java Spring Open Feign Plugin](#aplicando-java-spring-open-feign-plugin)


## **Tecnologias base da Plugin**

Objetivo desta sessão é informar quais são as técnologias que fazem parte do Java Spring Open Feign Plugin.

Ao aplicar este plugin em um projeto Java Spring Boot, sua aplicação poderá se beneficiar de toda infraestrutura da ferramenta Spring Cloud Open Feign, que lhe permitirá criar Clients HTTP de maneira declarativa utilizando a API  de mapeamento do Spring Web.


### **Composição Técnologica**

A definição deste Plugin foi pensada visando as maiores dores no uso de Clients HTTP em aplicativos Java Spring Boot.

Entendemos que a qualidade é inegociavel, e olhamos para as técnologias e metodologias como meio para obter a tão desejada qualidade no software. Essa premissa foi o guia para escolha de cada técnologia detalhada abaixo.


- Ambiente de produção
    - Spring Cloud Open Feign
    - Spring Web
- Ambiente de testes
    - Spring Cloud Contract WireMock
    - JUnit



## **Quais são as capacidades Habilitadas**

Ao aplicar em seu projeto Java Spring Boot, o Java Spring Open Feign Plugin, seu projeto será capaz:

1. Criar Clients HTTP de maneira declarativa
2. Configurar padrões de resiliência de forma explicita
3. Criar MocksServers utilizando WireMock
4. Criar uma suite de testes de integração automatizada junto a WireMock


## **Quais os Beneficios de Utilizar Java Spring Open Feign Plugin**

1. Facilidade na configuração do Spring Cloud Open Feign em seu projeto através da StackSpot CLI.
2. Criar Clients HTTP de forma declarativa
3. Configuração padrão personalizada para Clients Feign
4. Configuração personalizada para Clients 
5. Codigos de exemplo de Criação de Clients HTTP Feign  baseado em boas praticas.
6. Codigos de exemplo de Criação MocksServers com WireMock baseado em boas praticas.
5. Codigos de exemplo de Criação de Consumidores Kafka baseado em boas praticas.
6. Codigos de exemplo de Testes de integração para Clients Feign baseado em boas praticas.

[Assita este video para ver os beneficios de utilizar Java Spring Open Feign Plugin em seu projeto](https://youtu.be/JhG3LjNhggA)


## **Aplicando Java Spring Open Feign Plugin**

Para Aplicar o Java Spring Open Feign Plugin em  seus projetos e desfrutar de seus beneficios é necessário que você tenha a CLI da StackSpot instalada em sua maquina. [Caso você não tenha siga este tutorial para fazer a instalação](https://docs.stackspot.com/docs/stk-cli/installation/).

### 1. Importe a Stack em sua maquina

```sh
stk import stack https://github.com/zup-academy/java-springboot-restapi-stack
```

### 2. Agora verifique se a Stack foi importada com sucesso

```sh
stk list stack | grep java-springboot
```

### 3. Aplique o Plugin, no diretorio do seu projeto, execute

```sh
stk apply plugin java-springboot-restapi-stack/java-spring-open-feign-plugin
```   

### 4. Verifque as modificações em seu projeto

```sh
git status
```   



## Suporte

Caso precise de ajuda, por favor abra uma [issue no repositorio do Github da Stack](https://github.com/zup-academy/java-spring-open-feign-plugin/issues).