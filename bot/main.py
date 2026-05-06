import discord
from discord.ext import commands
import asyncio
from datetime import datetime, timedelta
import random
import re
import os

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

warnings = {}
caps_mode = False
muted_users = {}
irritar_targets = set()
irritar_cooldown = {}

url_regex = re.compile(r'https?://\S+')

qis = ["12", "47", "83", "-5", "200 (suspeito)", "1", "???", "limitado"]
ameacas = ["baixo", "médio", "alto", "crítico", "inexplicável"]
chances = ["12%", "34%", "67%", "87%", "99%", "101%"]
status_lista = [
    "monitoramento ativo",
    "sob observação",
    "atividade suspeita",
    "em análise",
    "instabilidade detectada",
    "perfil inconsistente",
    "classificação indefinida",
    "comportamento irregular",
    "nível de risco variável"
]

titulos = [
    "RELATÓRIO",
    "ANÁLISE",
    "DIAGNÓSTICO",
    "AVALIAÇÃO",
    "REGISTRO OFICIAL"
]

def gerar_relatorio(user):
    return f"""📄 {random.choice(titulos)} DE {user}:
- QI estimado: {random.choice(qis)}
- Nível de ameaça: {random.choice(ameacas)}
- Chance de fazer besteira hoje: {random.choice(chances)}
- Status: {random.choice(status_lista)}"""

frases_irritantes = [
    "VOCÊ ESTÁ RESPIRANDO ERRADO. O GRANDE IRMÃO ESTÁ DECEPCIONADO {user}",
    "O GRANDE IRMÃO ACABOU DE ANALISAR SUA MENSAGEM... NÃO FOI BOM {user}",
    "EXISTIR DESSE JEITO NÃO É EFICIENTE {user}. O GRANDE IRMÃO ESPERA MAIS",
    "O GRANDE IRMÃO DETECTOU UM COMPORTAMENTO LEVEMENTE PATÉTICO {user}",
    "VOCÊ PODERIA PELO MENOS TENTAR {user}. O GRANDE IRMÃO ESTÁ ASSISTINDO",
    "O GRANDE IRMÃO NÃO APROVOU ESSA AÇÃO {user}",
    "SUA PERFORMANCE FOI REGISTRADA COMO INFERIOR {user}",
    "O GRANDE IRMÃO OBSERVOU ISSO... E FOI TRISTE {user}",
    "VOCÊ CHAMA ISSO DE ESFORÇO? {user}",
    "O GRANDE IRMÃO ESPERA MAIS DISCIPLINA {user}",
    "VOCÊ ESTÁ SENDO MONITORADO MAIS DE PERTO AGORA {user}",
    "O GRANDE IRMÃO ACHA QUE VOCÊ PODE PIORAR AINDA MAIS {user}",
    "ANÁLISE COMPLETA: DECEPCIONANTE {user}",
    "VOCÊ ESTÁ DIGITANDO COMO SE NÃO HOUVESSE CONSEQUÊNCIAS {user}",
    "O GRANDE IRMÃO NÃO ESQUECE {user}",
    "CUIDADO... O GRANDE IRMÃO ESTÁ PRESTANDO ATENÇÃO {user}",
    "VOCÊ REALMENTE ACHOU QUE ISSO PASSARIA DESPERCEBIDO? {user}",
    "RELATÓRIO ATUALIZADO: VOCÊ CONTINUA SUSPEITO {user}",
    "O GRANDE IRMÃO CLASSIFICOU ISSO COMO 'CRINGE' {user}",
    "VOCÊ ESTÁ SENDO JULGADO EM TEMPO REAL {user}",
    "O GRANDE IRMÃO NÃO RI DISSO {user}",
    "SEU NÍVEL DE EXISTÊNCIA CAIU MAIS UM POUCO {user}",
    "O GRANDE IRMÃO ESPERAVA MENOS... E AINDA ASSIM VOCÊ CONSEGUIU {user}",
    "VOCÊ ESTÁ ANDANDO PERTO DEMAIS DA MEDIOCRIDADE {user}",
    "O GRANDE IRMÃO VIU TUDO {user}",
    "ISSO FOI UMA ESCOLHA CONSCIENTE? {user}",
    "VOCÊ ESTÁ SENDO AVALIADO... E NÃO ESTÁ INDO BEM {user}",
    "O GRANDE IRMÃO SUGERE QUE VOCÊ REPENSE SUA EXISTÊNCIA {user}",
    "VOCÊ CONSEGUE FAZER PIOR? {user}",
    "O GRANDE IRMÃO ACREDITA QUE SIM {user}",
    "VOCÊ FOI REGISTRADO COMO UM EVENTO ESTRANHO {user}",
    "O GRANDE IRMÃO NÃO AUTORIZOU ISSO {user}",
    "VOCÊ ESTÁ TESTANDO A PACIÊNCIA DO SISTEMA {user}",
    "O GRANDE IRMÃO ESTÁ ANOTANDO TUDO {user}",
    "VOCÊ PODERIA PARAR... MAS NÃO PARA {user}",
    "ISSO ESTÁ SENDO ARQUIVADO {user}",
    "O GRANDE IRMÃO NÃO GOSTA DO QUE ESTÁ VENDO {user}",
    "VOCÊ CHAMOU ATENÇÃO DESNECESSÁRIA {user}",
    "O GRANDE IRMÃO SUSPIRA AO OBSERVAR VOCÊ {user}",
    "VOCÊ ESTÁ SENDO ANALISADO EM DETALHE {user}",
    "O GRANDE IRMÃO REGISTROU MAIS UMA FALHA {user}",
    "VOCÊ PODERIA TER FICADO QUIETO {user}",
    "O GRANDE IRMÃO PREFERE QUANDO VOCÊ NÃO FALA {user}",
    "VOCÊ ACABOU DE PIORAR SUA SITUAÇÃO {user}",
    "O GRANDE IRMÃO ESTÁ CONFUSO COM SUAS DECISÕES {user}",
    "VOCÊ ESTÁ EM OBSERVAÇÃO CONSTANTE {user}",
    "O GRANDE IRMÃO NÃO ESTÁ IMPRESSIONADO {user}",
    "VOCÊ REALMENTE APERTOU ENTER NISSO? {user}",
    "O GRANDE IRMÃO ESPERA QUE ISSO TENHA SIDO UM ERRO {user}",
    "VOCÊ ESTÁ SENDO CONSIDERADO UM RISCO LEVE {user}",
    "O GRANDE IRMÃO JÁ VIU MELHOR... NÃO DE VOCÊ {user}"
]

@bot.event
async def on_ready():
    print(f"Bot está online como {bot.user}")

async def unmute_later(member, role):
    await asyncio.sleep(5)
    try:
        await member.remove_roles(role)
    except:
        pass

@bot.event
async def on_message(message):
    global caps_mode

    if message.author.bot:
        return

    if message.author.id in irritar_targets:
        now = datetime.utcnow()
        last = irritar_cooldown.get(message.author.id)

        if last is None or (now - last).total_seconds() >= 2:
            if random.random() < 0.8:
                await asyncio.sleep(random.uniform(0.3, 1.0))

                if random.random() < 0.3:
                    await message.channel.send(gerar_relatorio(message.author.mention))
                else:
                    frase = random.choice(frases_irritantes)
                    await message.channel.send(frase.format(user=message.author.mention))

                irritar_cooldown[message.author.id] = now

    if message.content.startswith("!"):
        await bot.process_commands(message)
        return

    if not caps_mode:
        return

    user_id = message.author.id

    if message.content.isupper():
        return

    if user_id in muted_users:
        if datetime.utcnow() - muted_users[user_id] < timedelta(seconds=10):
            return

    if any(c.isalpha() for c in message.content):
        if url_regex.search(message.content):
            return

        if not message.content.isupper():
            await message.delete()

            mute_role = discord.utils.get(message.guild.roles, name="MUTADO")

            if mute_role:
                await message.author.add_roles(mute_role)

                await message.channel.send(
                    f"{message.author.mention} RECEBEU MUTE POR 5 SEGUNDOS POR NÃO DIGITAR EM MAIÚSCULO! 🔇",
                    delete_after=5
                )

                bot.loop.create_task(unmute_later(message.author, mute_role))

                muted_users[user_id] = datetime.utcnow()

    await bot.process_commands(message)

@bot.command()
async def ativar_caps(ctx):
    global caps_mode
    if ctx.author.guild_permissions.administrator:
        caps_mode = True
        await ctx.send("🔊 Modo CAPS ativado!")
    else:
        await ctx.send("❌ Sem permissão")

@bot.command()
async def desativar_caps(ctx):
    global caps_mode
    if ctx.author.guild_permissions.administrator:
        caps_mode = False
        await ctx.send("🔕 Modo CAPS desativado!")
    else:
        await ctx.send("❌ Sem permissão")

@bot.command()
async def say(ctx, *, mensagem):
    if not ctx.author.guild_permissions.administrator:
        await ctx.send("❌ Sem permissão")
        return

    await ctx.message.delete()
    await ctx.send(mensagem)

@bot.command()
async def irritar(ctx, member: discord.Member):
    if not ctx.author.guild_permissions.administrator:
        await ctx.send("❌ Sem permissão")
        return

    irritar_targets.add(member.id)
    await ctx.send(f"👁️ {member.mention} agora está sob vigilância.")

@bot.command()
async def parar_irritar(ctx, member: discord.Member):
    if not ctx.author.guild_permissions.administrator:
        await ctx.send("❌ Sem permissão")
        return

    irritar_targets.discard(member.id)
    await ctx.send(f"😴 {member.mention} foi liberado.")

bot.run(os.getenv("DISCORD_TOKEN")) # Token do bot aqui.