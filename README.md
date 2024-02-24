
# Open-Foods WebSite Scrapper

Uma api capaz de buscar informações sobre diversos produtos alimentíçios no site br.open-foods.org!

## O que foi utilizado?

- Pyppeteer
- Python 3
- FastApi
- Asyncio

## Regras seguidas:

- Sem usar persistencia de dados
- Usar Puppeteer (Pyppeteer no caso, mas é uma implementação do Puppeteer para poder ser usado com python)
- Usar Swagger 
- Respostas das requisições da api seguem o modelo passado no enunciado

## Como instalar?

- Baixar e instalar o python: https://www.python.org/downloads/
- Instalar virtual env: pip install virtualenv
- Criar um ambiente virtual: python3 -m venv .venv
- Activar: source .venv/bin/actvate

- mkdir open-foods
- git clone open-foods/ https://github.com/ivaldir301/Open-Foods.git
- python3 install -r requirements.txt || pip install -r requirements.txt
- uvicorn main:app --reload

## Organização do projecto

![alt text](media/folderStructure.png?raw=true)

- media: Contem fotos utilizadas no ficheiro readme
- pyppeteer_scripts: Local onde estão armazenados os scrappers, logs de scrapping e pasta com utilidades
  - Scrappers são os scripts Pyppeteer para percorrer o website e apanhar os dados necessários
  - Logs contem mensagens de diferentes estágios do scrapping de acordo com scrappings anteriores
  - Utilidades sendo um conjunto de funções com lógicas repitidas durante o projecto
- Routes: Contem rotas do FastApi e lógica para retorno de cada uma
- main.py: Ficheiro príncipal do FastApi contento referencias para as rotas e rota de teste da api.

## Rotas

- Para retornar produtos baseado em nutriscore e em nova score: http://127.0.0.1:8000/produtos?nutriscore={nutriscore}&nova={nova}

- Para retornar produtos baseado no id do produto: http://127.0.0.1:8000/Product/?id={id}

## Exemplos de requisições:

- http://127.0.0.1:8000/produtos?nutriscore=B&nova=1

### Resposta:
```
[
  {
    "id": "7891000284933",
    "name": "Ninho - Nestle - 380g",
    "nutrition": {
      "score": "score desconhecido",
      "title": null
    },
    "nova": {
      "score": "A",
      "title": "Alimentos não processados ou minimamente processados"
    }
  },
  {
    "id": "7891021006125500",
    "name": "Café Torrado E Moído Tradicional Melitta Caixa 500g",
    "nutrition": {
      "score": "score desconhecido",
      "title": "Nutri-Score desconhecido"
    },
    "nova": {
      "score": "A",
      "title": "Alimentos não processados ou minimamente processados"
    }
  },
  {
    "id": "8011780000922",
    "name": "Nudeln Spaghetti - Riscossa - 500g",
    "nutrition": {
      "score": "A",
      "title": "Qualidade nutricional muito boa"
    },
    "nova": {
      "score": "A",
      "title": "Alimentos não processados ou minimamente processados"
    }
  }
]
```


- http://127.0.0.1:8000/Product/?id=7898024394181

### Resposta:
```
{
  "title": "Nutella - Ferrero - 350g",
  "quantity": "350 g",
  "ingridients": {
    "hasPalmOil": true,
    "isVegan": false,
    "isVegetarian": false,
    "list": [
      "AZÚCAR, GRASA VEGETAL, AVELLANAS, LECHE DESCREMADA EN POLVO, CACAO EN POLVO DESGRASADO, EMULSIFICANTE (LECITINAS), SABORIZANTE. CONTIENE AVELLANA, LECHE Y DERIVADOS DE SOJA."
    ]
  },
  "nutrition": {
    "servingSize": "Tamanho da porção:                    20g",
    "values": [
      [
        "high",
        "Gorduras/lípidos em quantidade elevada (31%)"
      ],
      [
        "high",
        "Gorduras/lípidos/ácidos gordos saturados em quantidade elevada (10.5%)"
      ],
      [
        "low",
        "Sal em quantidade baixa (0.105%)"
      ]
    ],
    "data": {
      "Energia": {
        "per100g": "2.230 kj(535 kcal)",
        "perServing": "2.230 kj(535 kcal)"
      },
      "Gorduras/lípidos": {
        "per100g": "31 g",
        "perServing": "6,2 g"
      },
      "Carboidratos": {
        "per100g": "0 g",
        "perServing": "0 g"
      },
      "Fibra alimentar": {
        "per100g": "0 g",
        "perServing": "0 g"
      },
      "Proteínas": {
        "per100g": "3 g",
        "perServing": "0,6 g"
      },
      "Sal": {
        "per100g": "6,5 g",
        "perServing": "6,5 g"
      }
    }
  },
  "nova": {
    "score": "4",
    "title": "Alimentos ultra-processados"
  }
}
```



## Overview e teste dos endpoints utilizando Swagger

![alt text](media/endpoints.png?raw=true)


- Passo 1: Através do terminal inicie o servidor uvicorn com o comando - uvicorn main:app --reload

- Passo 2: Acesse a página da documentação da api em http://127.0.0.1:8000/docs#

- Passo 3: Passe os parametros e realize o request

## Principais desafios durante o exame

- Puppeteer/Pyppeteer, sendo a primeira vez utilizando a biblioteca.
- Demorei um pouco para descobrir como aumentar o tempo de timeout do Pyppeteer, o que mais me frustrou mas consegui ultrapassar
- Conseguir coletar dados de alguns elementos dentro do site, que se situavam dentro de vários outros componentes como div's, ul's, etc.
- Conseguir organizar o projecto da forma mas modular e organizada, mantendo em mente boas práticas 
- O tempo de entrega sendo relativamente pouco, mas tornou o desafio mais divertido ;)

