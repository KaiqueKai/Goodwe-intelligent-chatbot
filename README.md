# GoodWe Intelligent Chatbot

## Objetivo

Chatbot desenvolvido para auxiliar operadores de infraestrutura de carregamento de veículos elétricos, fornecendo informações sobre eficiência energética, monitoramento, manutenção preventiva e operação de estações de carregamento.

## Tecnologias Utilizadas

* Python 3
* Ollama Cloud API
* Modelo Gemma 3 (4B)
* python-dotenv
* Biblioteca Ollama

## Estrutura do Projeto

```text
Sprint 2 Jorge/
│
├── .env
├── .gitignore
├── requirements.txt
├── README.md
│
├── prompts/
│   └── system_prompt.md
│
├── src/
│   └── chatbot.py
│
└── tests/
    └── casos_teste.md
```

## Instalação

Instale as dependências:

```bash
pip install -r requirements.txt
```

## Configuração

Crie um arquivo `.env` na raiz do projeto:

```env
OLLAMA_API_KEY=sua_api_key
```

## Modelo Utilizado

O chatbot utiliza o modelo:

```
gemma3:4b
```

Disponível na biblioteca da Ollama:

https://ollama.com/library/gemma3

## Execução

Execute o chatbot com:

```bash
python src/chatbot.py
```

## Casos de Teste

Os casos de teste estão documentados em:

```
docs/casos_teste.md
```

## Exemplo de Uso

Usuário:

Como reduzir o consumo energético de uma estação de carregamento?

Chatbot:

Para reduzir o consumo energético de uma estação de carregamento, é possível implementar estratégias como carga inteligente, monitoramento contínuo dos indicadores de consumo, manutenção preventiva dos equipamentos e otimização dos horários de carregamento.

## Equipe

- André Debiazzi — RM 569062
- Kaique da Silva — RM 572718
- Vinicius Cristal — RM 572049
- Lucas Barros - RM 571528
- Renan Eskildssen RM 571097
