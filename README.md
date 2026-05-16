# AirInsight — Prompt de Contexto do Projeto

O AirInsight é um projeto pessoal de engenharia e análise de dados voltado para o setor de aviação e viagens. O objetivo é construir uma plataforma de inteligência de passagens aéreas capaz de coletar, armazenar, analisar e visualizar dados de voos para gerar insights sobre preços, tendências e comportamento do mercado aéreo.

## Objetivos do projeto

- Monitorar preços de passagens ao longo do tempo
- Criar histórico de preços de voos
- Identificar tendências e padrões de variação
- Comparar companhias aéreas, rotas e períodos
- Gerar dashboards analíticos
- Automatizar pipelines de coleta e processamento de dados
- Explorar engenharia de dados, BI e cloud computing

## Tecnologias utilizadas

- Backend e dados: Python, Pandas, Requests, SQLAlchemy
- Banco de dados: PostgreSQL
- Visualização: Microsoft Power BI
- APIs: Skyscanner for Business (exemplo)
- Cloud (futuro): Microsoft Azure

## Estrutura inicial do MVP

Fluxo inicial:

Python → API de Voos → Tratamento de Dados → PostgreSQL → Power BI

### Funcionalidades do MVP

- Consulta de preços de voos via API
- Coleta automatizada de dados (pipeline simples)
- Armazenamento histórico de preços
- Tratamento e padronização de dados
- Dashboard com evolução de preços, comparação entre destinos e companhias, tendências temporais e insights sobre melhores períodos de compra

## Possíveis evoluções futuras

- Integração com Azure e automação em cloud
- Machine Learning para previsão de preços
- Sistema de alertas (preços/variações)
- API própria e front-end web
- Ranking de aeroportos e análise de experiência de viagem
- Análise de atrasos de voos

## Objetivo profissional

Além do aprendizado técnico, o projeto servirá como portfólio para oportunidades em BI, Data Analytics, Engenharia de Dados e tecnologia para aviação e turismo. O foco é construir uma aplicação que simule um produto real, com arquitetura organizada, pipeline automatizada, documentação técnica e dashboards analíticos.

---

Se quiser, posso também:

- adicionar um `requirements.txt` com dependências básicas;
- criar um esqueleto de pipeline em Python (`collector.py`, `transform.py`, `loader.py`);
- gerar um exemplo de esquema de banco (DDL) para PostgreSQL.

Diga qual opção prefere que eu implemente a seguir.

## Exemplo de uso rápido do pipeline

1. Crie e ative um ambiente virtual (Windows PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

2. Copie as variáveis de ambiente exemplo:

```powershell
copy .env.example .env
# Edite .env e preencha FLIGHTS_API_KEY e DATABASE_URL
```

3. Executar os módulos do pipeline (exemplos simples):

```powershell
python collector.py
python transform.py
python loader.py
```

Observação: os módulos presentes são esqueleto — adapte parâmetros de API e `DATABASE_URL` antes de executar em produção.