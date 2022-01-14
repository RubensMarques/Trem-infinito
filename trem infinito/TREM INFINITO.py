#importações
from random import shuffle
from time import sleep
from os import system
from sys import exit

#listas e dicionarios
v=int(3)
vidas=[v]
ficha={'jogador':'', 'vidas':vidas}
futebol=[
['Qual jogador é conhecido como "Bruxo"?'], ['Ronaldinho Gaucho', 'Cristiano Ronaldo', 'Messi', 'Pelé', 'A'],
['Quem ganhou a Bola de Ouro de 2001?'], ['Ronaldo', 'Beckham', 'Romário', 'Owen', 'D'],
['qual a nacionalidade de Erling Haaland?'],['finlandês', 'polonês', 'norueguês', 'escocês', 'C'],
['Quem ganhou a primeira edição da champions league?'], ['Steua bucarest', 'liverpool', 'malmo', 'real madrid','D'],
['qual desses jogadores ganhou uma copa do mundo?'], ['neymar', 'messi', 'cristiano ronaldo', 'mbappé', 'D'],
['quem é o jogador em atividade mais velho do mundo?'],['buffon', 'fernando prass', 'iniesta', 'kazu', 'D'],
['qual a nacionalidade de Richarlison?'],['brasileiro', 'argentino', 'boliviano', 'português', 'A'],
['quem é o ex-presidente da FIFA?'],['thierry henry', 'michel platini', 'joão havelange', 'carlos alberto torres', 'C'],
['qual desses nunca ganhou uma bola de ouro?'],['neymar', 'cristiano ronaldo', 'lewandowski', 'kaká', 'A'],
['qual seleção foi a vice campeã da copa de 1990?'],['brasil', 'thecoslováquia', 'frança', 'argentina', 'D'],
['quantos gols o Gabigol fez no Brasileirão 2019?'], ['23', '22', '25', '24', 'C'],
['qual a nacionalidade de Luka Modric?'],['islandês', 'croata', 'holandês', 'espanhol', 'B'],
['quantas bolas de ouro ganhou Ronaldo fenômeno?'], ['2', '4', '5', '3', 'D'],
['na final da copa do mundo de 2014, quem fez o gol do titulo alemão?'], ['Kroos', 'Götze', 'Muller', 'Klose', 'B'],
['pelé fez quantos gols na carreira(oficiais e não oficiais)?'],['1000', '1283', '1181', '1303', 'B'],
['qual a nacionalidade de Kevin DeBruyne?'],['belga', 'alemão', 'suéco', 'inglês', 'A']]

anime=[
['em Death Note qual o alter ego do protagonista?'], ['L', 'Kira', 'shinigami', 'death', 'B'],
['em YU-GI-OH qual combinação de cartas o Yugi derrota Seito Kaiba?'],['caribou+multiplicação', 'as 5 partes de exodia', 'feiticeira negra+cilindro magico', 'mago negro + mirror force', 'B'],
['no anime Hunter x Hunter a família de killua era composta totalmente por:'],['contrabandistas', 'assassinos', 'vendedores', 'comediantes', 'B'],
['em Dragon Ball z quem derrotou o vilão Cell?'],['mister satan', 'trunks', 'goku', 'gohan', 'D'],
['por que Ash tem Pikachu como seu pokemon inicial?'],['porque a mãe o obrigou', 'porque ele dormiu demais', 'porque foi sua escolha', 'porque ele pegou a pokebola errada', 'B'],
['quem mata Shisui Uchiha?'], ['seu irmão', 'ele comete suicidio', 'seu melhor amigo', 'sua namorada', 'B'],
['qual o tipo de jutsu é especialidade do clã Uzumaki?'], ['doujutsu', 'bukijutsu', 'fuuinjutsu', 'senjutsu', 'C'],
['qual o titã de Eren Yeager? (Attack on titan)'],['titã de ataque', 'titã encouraçado', 'titã bestial', 'titã colossal', 'A'],
['qual desses animes se passa dentro de um jogo?'],['Re:zero', 'SAO', 'danmashi', "Knight's & Magic", 'B'],
['em Nanatsu NO TaiZai quem é o pecado da luxúria?'],['Gowther', 'ban', 'diane', 'meliodas', 'A'],
['qual o nome da tropa do Toppa em Dragon ball Super?'],['tropa dos poderosos', 'tropa dos onze universos', 'tropa do orgulho', 'tropa dos deuses', 'C'],
['quem venceu o torneio do poder?(Dragon ball super)?'],['android 17', 'vegeta', 'jirem', 'goku', 'A'],
['qual clã é especialista em jutsu de selamento(Naruto)?'],['uchiha', 'uzumaki', 'haruno', 'senju', 'B'],
['qual desses clãs não existem(Naruto)?'],['yuki', 'fuuma', 'kanati', 'inuzuka', 'C'],
['Ban é do qual clã(Nanatsu NO TaiZai)?'],['das fadas', 'dos imortais', 'dos demônios', 'dos humanos', 'D'],
['qual desses clãs não existem(Nanatsu NO TaiZai)?'], ['druidas', 'feras', 'mutantes', 'vampiros', 'C']]

desenho=[
['no desenho "os jovens titãs em ação" qual herói da liga da justiça é sempre motivo de piada?'],['Batman', 'aquaman', 'mulher maravilha', 'superman', 'B'],
['no final de "apenas um show" que personagem não teve filhos?'],['benson', 'musculoso', 'mordecai', 'rigby', 'A'],
['qual o nome verdadeiro de Kick Buttowisk?'],['Billy Buttowisk', 'Klarence Buttowisk', 'Greg Buttowisk','wate Buttowisk', 'B'],
['quantas vezes Gumball beijou Darwin?'],['1', '2', '6', '8', 'C'],
['como Rick identificava os parasitas em sua casa?(Rick and Morty)'],['parasitas não riam', 'não se tem memorias ruins com parasitas', 'não se ama parasitas', 'parasitas não choram', 'B'],
['que personagem maltrata o Lula molusco para usar sua tinta para fazer limonada?'],['patrick', 'plankton', 'Seu Sirigueijo', 'sandy', 'A'],
['qual a primeira musica cantada no desenho urso sem curso?'], ['garota dourada', 'juntos de novo', 'just my tipe', 'te iogurte', 'A'],
['quantos coelhos a monica ja teve?'], ['1', '2', '3', '4', 'C'],
['qual o nome do cavalo de pica-pau?'], ['pepe legal','pé-de-pano', 'uni', 'ventania', 'B'],
['o que Beth pede a Meeseks?(Rick and Morty)'],['pede um encontro', 'pede para se divorciar do Jerry', 'pede mais tempo com seu pai', 'pede para ser uma mulher mais plena', 'D'],
['qual o nome das irmãs da personagem Marge Simpson?'],['brenda e nelma', 'renata e jessica', 'diane e nelma', 'patty e selma', 'D'],
['em "jovens titãs em ação" quem é o irmão de Trigon?'],['slide', 'irmao sangue', 'ravena', 'a morte', 'D'],
['em que tipo de alimento Rick se transforma?(Rick and Morty)'], ['picles', 'cenoura', 'milho', 'batata', 'A'],
['qual o nome da namorada do pica-pau?'],['meany', 'chelly', 'leany', 'winnie', 'D'],
['qual o artefato de Eric? (caverna do dragão)'],['arco e flecha', 'escudo', 'massa', 'chapeu mágico','B'],
['qual a cor da máscara da tartaruga ninja Rafael?'],['vermelha', 'azul', 'laranja', 'roxa', 'A']]

dccomic=[
['qual o verdadeiro nome do superman?'],['kent klarson', 'kal-el', 'clark kent', 'bruce wayne', 'B'],
['quem é o lider da liga da justiça?'],['batman', 'flash', 'ciborgue', 'superman', 'D'],
['quem foi o primeiro vilão da liga da justiça?'],['starro', 'darkseid', 'coringa', 'brainiac', 'A'],
['qual é o nome do ciborgue?'],['arthur curry', 'bruce wayne', 'victor stone', 'slide wilson', 'C'],
['onde nasceu a mulher maravilha?'], ['tamânia', 'tanaghar', 'grecia', 'themyscira', 'D'],
['qual o nome da mãe da mulher maravilha?'], ['atena', 'hipolita', 'artemis', 'diana', 'B'],
['onde a nave do superman aterrisou?'], ['metropoles', 'smallville', 'texas', 'cost city', 'B'],
['qual a tropa dos lanternas se alimenta da esperança?'],['azul', 'verde', 'vermelho', 'amarelo', 'A'],
['qual parentesco de Bart Allen com Barry Allen nos quadrinhos?'],['filho', 'pai', 'neto', 'sobrinho', 'C'],
['quem faz parte da trindade?'],['batman, superman e mulher maravilha', 'batman, superman e flash', 'batman, superman e aquaman', 'batman, superman e laterna verde', 'A'],
['quem é Arthur Curry?'],['aquaman', 'lanterna verde', 'caçador de marte', 'gavião negro','A'],
['qual a fraqueza do caçador de marte?'],['sol', 'kriptonita', 'fogo', 'bomba nuclear', 'C'],
['qual o primeiro lanterna verde humano?'], ['alan scott', 'hal jordan', 'john stewart', 'jessica cruz', 'A'],
['quem é o capuz vermelho?'], ['coringa', 'jason todd', 'tim drake', 'damian wayne', 'B'],
['qual o nome da prima do superman?'], ['tina-el', 'kaila-el', 'kira la-el', 'kara zor-el', 'D'],
['qual o nome do filho do batman?'],['damian wayne', 'robin wayne', 'jason wayne', 'martin wayne', 'A']]
trem=[desenho, anime, futebol, dccomic]
tre=['desenho', 'anime', 'futebol', 'dc comic']
abc=['A)', 'B)', 'C)', 'D)', 'RESP)']
fase=[]
sorteiofase=[0,1,2,3]
sorteioperg=[0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30]
cs=0
condperg=0
ps=0

#cores
cyan = '\033[1;36m'
white='\033[1;97m'
yellow= '\033[1;33m'
fim='\033[0m'
green='\033[92m'
red='\033[91m'
neg='\033[;1m'

# definição de funções
def clear():
	system('cls')

#função de introdução
def intro():
	traço='='*70
	tam=len(traço)
	print(traço)
	intro=f"""{neg}
{f'  OI, SOU O MAQUINISTA, PARECE QUE VOCÊ NÃO ESTÁ TÃO BEM ASSIM NÉ? ':^{tam}}
{f'      ENTÃO, VOCÊ ESTÁ PRESO NO {cyan}{"TREM INFINITO"}{fim},{neg} E PARA CONSEGUIR ':^{tam}}
{f'SAIR VÔCE PRECISA ACERTAR ALGUMAS PERGUNTAS. VOCÊ TERÁ ':^{tam}}
{f'3 VIDAS DURANTE O JOGO, SE CONSEGUIR CHEGAR ATÉ O FINAL TERÁ ':^{tam}}
{f'SUA RECOMPENSA, SERÁ LIBERTADO, ENCONTRANDO O CAMINHO DE CASA.':^{tam}}
{f'BOA SORTE!!!':^{tam}}"""
	for c in intro:
		print(c, end='', flush=True)
		sleep(0.03)
	print()
	print(traço)
	print()
	print(f'{neg}{"[TECLE ENTER PARA CONTINUAR]":^{tam}}{fim}')
	input()
	system('cls')

#função do cabeçalho
def cab():
	traço='='*41
	tam=len(traço)
	print(traço)
	print(f'{yellow}{"JOGADOR":^{tam}}{fim}')
	print(traço)

#função de maiusculo
def up(m):
	return f'{m}'.upper()

#função de game over
def gameover():
	lin='='*62
	tam=len(lin)
	if vidas[0]==0:
		clear()
		p='='*60
		print(f"{red}{p}")
		print(f'{neg}{red}{"  GAME OVER!!":^60}')
		print(f'{up(ficha["jogador"]):^60}')
		print(f'{neg}{red}{up("agora ficará para sempre no meu trem infinito."):^60}{fim}')
		print(f"{red}{p}")
		input(f'{neg}{"[TECLE ENTER PARA CONTINUAR]":^{tam}}')
		clear()
		print(f"{lin}")
		print(f"{yellow}{'AGRADECIMENTOS':^{tam}}{fim}")
		print(f"""{neg}{lin}

DEV: RUBENS MARQUES
		
AJUDA TÉCNICA: LISANDRA(NAMORADA)
		
STAFF: GUILHERME(SOBRINHO)""")
		
		print(f"{lin}")
		input(f'{neg}{"[TECLE ENTER PARA FINALIZAR]":^{tam}}')
		exit()

#função de volta pra casa
def home():
	global cs
	global j
	if cs==4:
		clear()
		print(neg)
		lin='='*62
		tam=len(lin)
		print(f"{red}{lin}")
		print(f"{neg}{red}{'CAMPEÃO':^{tam}}")
		print(f"{red}{lin}")
		print(f"{neg}{cyan}{up('parabÉns')} {up(ficha['jogador'])}, {up('achei que nunca fosse conseguir,'):^30}")
		print(f"""{up('porém tenho palavra, irei te libertar, espero te ver de novo.'):^30}""")
		print(f"{up('faça uma boa viagem de volta para casa!!'):^30}")
		print(f"{cyan}{lin}")
		sleep(3)
		input(f'{neg}{"[TECLE ENTER PARA CONTINUAR]":^{tam}}')
		clear()
		print(f"{lin}")
		print(f"{yellow}{'AGRADECIMENTOS':^{tam}}{fim}")
		print(f"""{neg}{lin}

DEV: RUBENS MARQUES
		
AJUDA TÉCNICA: LISANDRA(NAMORADA)
		
STAFF: GUILHERME(SOBRINHO)""")
		
		print(f"{lin}")
		input(f'{neg}{"[TECLE ENTER PARA FINALIZAR]":^{tam}}')
		exit()

#função de fase
def level():
	shuffle(sorteiofase)
	while True:
		global cs
		global condperg
		global ps
		fase.insert(0, sorteiofase[cs])
		cs+=1
		cima='='*55
		bv=len(cima)
		mundo=(tre[fase[0]])
		
		print(f"""
			(((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((
								     =========   _(((_
								    |    __   |  |   |
====     {cima}    |   |__|  |__|   |_____
    |   |{f'VOCÊ ESTÁ NO MUNDO {mundo}!':^{bv}}|   |   |  |     |   |     |____
    |   |{'ACERTE DUAS PERGUNTAS E PASSE':^{bv}}|   |___|__|_______________|    |
    |   |{f'PARA O PRÓXIMO MUNDO.':^{bv}}|   |    TREM INFINITO     |____|
==== --- {cima} --- ======================
(x)_______(x)__(x)__(x)__(x)__(x)__(x)__(x)__(x)__(x)__(x)__(x)_______(x)__(x)__(x)__(x)________________________

			""".upper())
		i=0
		respinp=''
		perg=[]
		shuffle(sorteioperg)
		while True:
			perg.insert(0, sorteioperg[ps])
			ps+=1
			resp=perg[0]+1

			print(up(trem[fase[0]][perg[0]][0]))
			for k, va in enumerate((trem[fase[0]][resp])):
				if i<4:
					print(abc[i], end='')
					print(up(va), end='')
					print()
					i+=1
			i=0
			while True:
				print()
				respinp=str(input(f'{neg}{yellow}{"DIGITE A LETRA CORRETA: "}{fim}')).upper().strip()[0]
				if respinp not in 'ABCD':
					print(f'{neg}{red} ERRO! {fim}{neg}DIGITE APENAS UMA DAS LETRAS CORRESPONDENTES')
				elif respinp in 'ABCD':
					break
			if respinp!=trem[fase[0]][resp][4]:
				del vidas[0]
				global v
				v-=1
				vidas.append(v)
				gameover()
				print()
				print(f'{red}{"VOCE ERROU, TENTE NOVAMENTE"}{fim}')
				print()
				if vidas[0] <2:
					print(f'AGORA VOCÊ SO TEM {red}{vidas[0]} vida{fim}')
				else:
					print(f'AGORA VOCÊ SO TEM {red}{vidas[0]} vidas{fim}')
			else:
				print()
				print(f'{green}{"PARABÉNS VOCÊ ACERTOU"}{fim}')
				print()
				condperg+=1
				if condperg==2:
					break
		if cs==4:
			home()		
		print('VÁ PARA O PRÓXIMO VAGÃO')
		sleep(2)
		clear()
		print()
		condperg=0
		home()

#capa
clear()
traço='='*41
tam=len(traço)
print(traço)
print(f'{yellow}{"TREM INFINITO!":^{tam}}{fim}')
print(traço)
sleep(1)
print(f'{neg}{"[TECLE ENTER PARA CONTINUAR]":^41}{fim}') 
input()

#introdução
clear()
intro()

#cabeçalho
cab()

#nome do player
j=(str(input(up('digite o seu nome: ')))).upper()
ficha['jogador']=j
clear()

#inicio
cima='='*55
bv=len(cima)
print(f"""
	                                                                         )())
	                                                             =========   _)))_
	                                                            |    __   |  |   |
====     {cima}    |   |__|  |__|   |_____
    |   |{f'      BEM VINDO{red} {j} {fim}!':^{bv}}         |   |   |  |     |   |     |____
    |   |{'VOCÊ CHEGOU AO PRIMEIRO VAGÃO!':^{bv}}|   |___|__|_______________|    |
    |   |{'COMPLETE OS MUNDOS PARA CONSEGUIR VOLTAR PARA CASA.':^{bv}}|   |    TREM INFINITO     |____|
==== --- {cima} --- ======================
(x)_______(x)__(x)__(x)__(x)__(x)__(x)__(x)__(x)__(x)__(x)__(x)_______(x)__(x)__(x)__(x)____________________________

	""")
print(f'{neg}{"[TECLE ENTER PARA CONTINUAR]":^60}{fim}') 
input()
clear()

#fases
level()