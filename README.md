# AirInsight

Pipeline de dados para coleta e acompanhamento histórico de preços de passagens aéreas.

> **Status:** MVP em desenvolvimento. O repositório ainda não representa um produto concluído.

## Problema

Preços de passagens variam conforme rota, data da busca, data do voo e outros fatores. O AirInsight pretende registrar observações ao longo do tempo para permitir comparações, identificação de tendências e construção de análises reproduzíveis.

## Escopo do MVP

- Rotas iniciais: MCZ-GRU, MCZ-GIG e MCZ-BSB
- Coleta com Playwright e Python
- Validação e padronização dos dados
- Persistência histórica em PostgreSQL
- Controle de duplicidades e rastreabilidade das execuções
- Camada analítica em SQL e modelo dimensional
- Dashboard no Power BI

## Arquitetura planejada

Google Flights → Playwright/Python → validação e tratamento → PostgreSQL → camada analytics em SQL → Power BI

## Status do desenvolvimento

- [x] Estrutura inicial do repositório
- [x] Protótipo de coleta no Google Flights
- [ ] Configuração e persistência no PostgreSQL
- [ ] Histórico e carga idempotente
- [ ] Tratamento de duplicidades
- [ ] Logging e tabela de execução
- [ ] Testes automatizados e testes de qualidade dos dados
- [ ] Camada analítica e modelo dimensional
- [ ] Dashboard no Power BI
- [ ] Execução agendada
- [ ] Release v1.0

## Princípios do projeto

- Não armazenar credenciais no repositório
- Respeitar os termos e limites da fonte consultada
- Não contornar CAPTCHA ou mecanismos de proteção
- Manter dados de exemplo para demonstração reproduzível
- Separar coleta, transformação e carga
- Documentar decisões, limitações e falhas conhecidas

## Tecnologias previstas para o MVP

- Python
- Playwright
- PostgreSQL
- SQL
- Power BI
- Git e GitHub

Cloud e Machine Learning não fazem parte do primeiro MVP.

## Objetivo profissional

O AirInsight é um projeto de portfólio para demonstrar integração de dados, automação, SQL, modelagem dimensional, qualidade, rastreabilidade e Business Intelligence em um problema ligado a aviação e turismo.
