# Discord Moderation & Interaction Bot (Python)

Bot desenvolvido em Python utilizando a biblioteca discord.py, com foco em automação de moderação e interações dinâmicas em tempo real.

# Funcionalidades
Sistema de moderação automática:
-Detecção de mensagens fora do padrão (ex: CAPS obrigatório)
-Aplicação de punições temporárias (mute automático)
-Controle de permissões por cargo (admin)
Sistema de comportamento dinâmico:
-Monitoramento de usuários específicos
-Respostas automáticas com base em probabilidade
-Geração de mensagens aleatórias (simulação de “IA cômica”)
Arquitetura baseada em eventos:
-Uso de async/await para lidar com múltiplas ações simultâneas
-Processamento em tempo real de mensagens (on_message)
Controle de estado:
-Rastreamento de usuários mutados
-Cooldowns para evitar spam
-Gerenciamento de sessões de “monitoramento”
Validação de conteúdo:
-Uso de expressões regulares para detectar links
-Filtros para evitar punições indevidas
# Tecnologias utilizadas

Python
discord.py
Asyncio
Regex

# Como rodar
Instalar dependências:

pip install -r requirements.txt

Criar variável de ambiente:

DISCORD_TOKEN=seu_token_aqui

Rodar:
python bot/main.py
