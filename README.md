# Discord Moderation & Interaction Bot (Python)

## Visão Geral

Este projeto demonstra a construção de um sistema automatizado para moderação e interação em tempo real em servidores Discord, utilizando programação assíncrona em Python.

O bot combina regras de moderação, respostas automatizadas e comportamento dinâmico baseado em probabilidade, simulando um sistema reativo com múltiplos estados e controle de usuários.

---

## Funcionalidades

### Sistema de moderação automática
- Detecção de mensagens fora do padrão (ex: CAPS obrigatório)
- Aplicação de punições temporárias (mute automático)
- Controle de permissões por cargo (admin)

### Sistema de comportamento dinâmico
- Monitoramento de usuários específicos
- Respostas automáticas com base em probabilidade
- Geração de mensagens aleatórias

### Arquitetura baseada em eventos
- Uso de async/await para execução concorrente
- Processamento em tempo real de mensagens (`on_message`)

### Controle de estado
- Rastreamento de usuários mutados
- Cooldowns para evitar spam
- Gerenciamento de sessões de monitoramento

### Validação de conteúdo
- Uso de expressões regulares (regex) para detectar links
- Filtros para evitar punições indevidas

---

## Tecnologias utilizadas

- Python
- discord.py
- Asyncio
- Regex

---

## Como rodar

### 1. Instalar dependências

- pip install -r requirements.txt

### 2. Configurar variável de ambiente

- DISCORD_TOKEN=seu_token_aqui

### 3. Executar o bot

- python bot/main.py

---

## Exemplos de comandos


!ativar_caps

!desativar_caps

!irritar @usuario

!parar_irritar @usuario

!say mensagem


---

## Objetivo do projeto

Explorar conceitos de:
- Programação assíncrona
- Sistemas orientados a eventos
- Automação de moderação
- Controle de estado em aplicações em tempo real

---

## Autor

Projeto desenvolvido por Gilsemberg como prática de programação e automação utilizando Python.
