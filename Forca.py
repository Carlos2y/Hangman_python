# coding: UTF-8

import random
from tkinter import *
from tkinter import messagebox
import playsound
from PIL import ImageTk, Image


class Forca:
    def __init__(self, vida=5, palavra="", morte=0):  # INICIA O JOGO
        self.num = 0
        self.secret = False  # EASTER EGG
        self.side = (1380, 720)  # PADRAO DA RESOLÇÃO DAS TELAS DO JOGO
        self.acerto = []  # INICIA A LISTA DE ACERTOS
        self.erros = []  # INICIA A LISTA DE ERROS
        self.sensitiveCase = 'OFF'  # SENSITIVE CASE MODE / PADRAO OFF
        self.vida = vida  # ViDA DO JOGADOR / PADRAO = 5
        self.morte = morte  # CONTADOR DE TENTATIVAS ERRADAS DO JOGADOR
        self.hw = []  # ESCONDE A PALAVRA E MOSTRA OS ACERTOS NAS CASAS DA PALAVRA
        self.palavra = palavra  # INICIA O TRANSPORTADOR DE PALAVRA
        self.alf = []  # ALFABETO
        self.alfabeto()  # CONSTRUTOR DO ALFABETO
        self.Tela_1()  # INICIA O MENU PRINCIPAL DO JOGO

    def alfabeto(self):  # CONSTRUTOR DO ALFABETO
        for i in range(65, 91):  # LETRAS MAISCULAS
            self.alf.append(chr(i))  # SALVA AS LETRAS MAISCULAS
        for i in range(97, 123):  # LETRAS MINUSCULAS
            self.alf.append(chr(i))  # SALVA AS LETRAS MINUSCULAS

    def Music(self):  # MUSICA DO JOGO
        try:  # TENTA INICIAR A MUSICA DO JOGO
            playsound.playsound(r"Data\Music\Music_BackGround.mp3", 0)  # BACKGROUND MUSIC DO JOGO
        except:  # CASO NAO ENCONTRE O ARQUIVO LEVANTA A MENSAGEM DE ERROR
            messagebox.showinfo("Erro", "ARQUIVO \n\n / Music_BackGround.mp3 / \n\nNAO ENCONTRADO.")  # MESSAGEM ERRO

    def reset(self):  # RESETA ALGUNS DOS STATUS DE JOGO AO SEU VALOR PADRAO
        self.acerto.clear()  # LIMPA A LISTA DE ACERTOS
        self.erros.clear()  # LIMPA A LISTA DE ERROS DO JOGADOR
        self.hw.clear()  # LIMPA A PALAVRA ESCONDIGA
        self.secret = False  # RESETA O FIM
        self.morte = 0  # LIMPA O NUMERO DE ERROS DO JOGADOR

    def Tela_1(self):
        tela_1 = Tk()  # INICIO TELA 1
        tela_1.title('JOGO DA FORCA')  # TITULO DA TELA 1
        tela_1.iconbitmap(r'Data\Imgs\Forca.ico')  # ICONE DA TELA 1
        tela_BG = ImageTk.PhotoImage(Image.open(r'Data\Imgs\Forca.png').resize(self.side))  # IMAGEM DE FUNDO DA TELA_1
        tela_1_Label = Label(tela_1, image=tela_BG, padx=30, pady=30, anchor=CENTER)  # TAMANHO DA TELA 1
        tela_1_Label.grid(row=0, column=0, columnspan=10, rowspan=10)  # MONTA O BG DA TELA 1
        self.Music()  # INICIA A MUSICA DO JOGO

        Button(tela_1, text='JOGAR', padx=17, pady=17,
               bg='black', fg='LightBlue', font=("courier ", "11"),
               command=lambda: (tela_1.destroy(), self.Tela_2())).grid(row=4, column=3)
        # BUTAO 1 DA TELA 1, FINALIZA A TELA 1 E PASSA PARA A TELA 2

        Button(tela_1, text=' SAIR ', padx=17, pady=17,
               bg='black', fg='LightBlue', font=("courier ", "10"),
               command=lambda: (tela_1.destroy(), quit())).grid(row=4, column=6)
        # BUTAO 2 DA TELA 1 PARA SAIDA COMPLETA

        Button(tela_1, text="OPÇÕES", padx=15, pady=15,
               bg='black', fg='LightBlue', font=("courier ", "10"),
               command=lambda: (tela_1.destroy(), self.Opt())).grid(row=0, column=9)
        # BOTAO DE OPÇÕES DO JOGO / DESTROI A TELA 1

        tela_1.mainloop()  # FIM DA TELA 1

    def Tela_2(self):
        tela_2 = Tk()  # INICIO DA TELA 2
        tela_2.title('JOGO DA FORCA')  # TITULO DA TELA
        tela_2.iconbitmap(r'Data\Imgs\Forca.ico')  # ICONE DA TELA
        tela_BG = ImageTk.PhotoImage(Image.open(r'Data\Imgs\Forca.png').resize(self.side))  # IMAGEM DE FUNDO DA TELA
        Label(tela_2, image=tela_BG, anchor=CENTER).grid(row=0, column=0, columnspan=50, rowspan=50)  # TELA MONTADA 2

        Label(tela_2, text="ESCOLHA O MODO DE JOGO", bg='black',
              fg='LightBlue', font=("courier ", "10")).grid(row=21, column=25)  # TEXTO

        Button(tela_2, text=" FACIL ", padx=15, pady=15,
               bg='black', fg='LightBlue', font=("courier ", "10"),
               command=lambda: (tela_2.destroy(), self.Facil())).grid(row=25, column=24)
        # BOTAO PARA JOGAR NO FACIL / DESTROI A TELA 2

        Button(tela_2, text=" MEDIO ", padx=15, pady=15,
               bg='black', fg='LightBlue', font=("courier ", "10"),
               command=lambda: (tela_2.destroy(), self.Medio())).grid(row=25, column=25)
        # BOTAO PARA JOGAR NO MEDIO / DESTROI A TELA 2

        Button(tela_2, text="DIFICIL", padx=15, pady=15,
               bg='black', fg='LightBlue', font=("courier ", "10"),
               command=lambda: (tela_2.destroy(), self.Dificil())).grid(row=25, column=26)
        # BOTAO PARA JOGAR NO IMPOSSIVEL / DESTROI A TELA 2

        Button(tela_2, text="VOLTAR", padx=15, pady=15,
               bg='black', fg='PINK', font=("courier ", "10"),
               command=lambda: (tela_2.destroy(), self.Tela_1())).grid(row=30, column=25)
        # BOTAO PARA VOLTAR A TELA 1 / DESTROI A TELA 2

        tela_2.mainloop()  # FIM DA TELA 2

    def Facil(self):
        tela_Facil = Tk()  # INICIO DA TELA FACIL
        tela_Facil.title('JOGO DA FORCA')  # TITULO DA TELA
        tela_Facil.iconbitmap(r'Data\Imgs\Forca.ico')  # ICONE DA TELA
        Tela_BG = ImageTk.PhotoImage(Image.open(r'Data\Imgs\Forca.png').resize(self.side))  # IMAGEM DE FUNDO DA TELA

        Label(tela_Facil, image=Tela_BG, anchor=CENTER).grid(
            row=0, column=0, columnspan=50, rowspan=50)  # TELA MONTADA FACIL / BG

        Label(tela_Facil, text="DIGITE A PALAVRA QUE DESEJA USAR PARA JOGAR",
              bg="black", fg="Pink", font=("courier ", "10")).grid(row=21, column=25)  # TEXTO INFORMATIVO

        entry = Entry(tela_Facil, width=25, borderwidth=5, justify=CENTER)
        entry.grid(row=23, column=25)  # INPUT DE TEXTO

        def click():  # FUNCAO PARA SALVAR O INPUT DO USUÁRIO NO BACK-END
            x = list(entry.get())  # TRANSFORMA O TEXTO DO USUÁRIO EM LISTA
            for i in range(len(x)):  # VERIFICA SE O TEXTO CONDIZ COM O ALFABETO
                if x[i] not in self.alf:  # TESTA LETRA POR LETRA
                    messagebox.showinfo("ERRO", "SOMENTE LETRAS, SEM ACENTUACAO E ESPAÇO, SAO ACEITAS")
                    # TEXTO DE ERROR

                    return False  # CANCELA O INICIO DO JOGO
            return True  # INICIA O JOGO

        def check(test):  # CHECK PARA INICIAR O JOGO
            if test:  # SE TRUE INICIA O JOGO
                self.palavra = str(entry.get())  # SALVA A PALAVRA DIGITA PELO JOGADOR NO BACK-END

                test = messagebox.askyesno("SALVAR", "DESEJA SALVAR A PALAVRA\n\n / " + str(entry.get()) + " / ?")
                # PERGUNTA SE O JOGADOR NAO DESEJA SALVAR A PALAVRA NO ARQUIVO Palavras_Lista.txt

                if test:  # CASO SIM
                    self.Arquivo(self.palavra)  # SALVA A PALAVRA NO ARQUIVO Palavras_Lista.txt

                tela_Facil.destroy()  # FINALIZA A TELA FACIL
                self.Jogo()  # INICIA O JOGO

        Button(tela_Facil, text="JOGAR", padx=12, pady=11,
               bg='black', fg='PINK', font=("courier ", "10"),
               command=lambda: (check(click()))).grid(row=25, column=25)  # TESTE PARA INICIAR O JOGO

        Button(tela_Facil, text="VOLTAR", padx=10, pady=8,
               bg='black', fg='lightblue', font=("courier ", "8"),
               command=lambda: (tela_Facil.destroy(), self.Tela_2())).grid(row=26, column=25)  # VOLTA A TELA_2 DE JOGO

        tela_Facil.mainloop()  # FIM DA TELA FACIL

    def Medio(self):
        tela_medio = Tk()  # INICIO DA TELA MEDIO
        tela_medio.title('JOGO DA FORCA')  # TITULO DA TELA
        tela_medio.iconbitmap(r'Data\Imgs\Forca.ico')  # ICONE DA TELA
        tela_BG = ImageTk.PhotoImage(Image.open(r'Data\Imgs\Forca.png').resize(self.side))  # IMAGEM DE FUNDO DA TELA
        Label(tela_medio, image=tela_BG, anchor=CENTER).grid(row=0, column=0,
                                                             columnspan=50, rowspan=50)  # TELA MONTADA

        def Roleta():
            try:  # CASO O JOGADOR TENHA A LISTA DE PALAVRAS INICIA A BUSCA DA PALAVRA NO ARQUIVO
                with open(r"Data\Palavras_Lista.txt", encoding="UTF-8") as file:  # ABRE O ARQUIVO
                    arquivo = file.readlines()  # LE O ARQUIVO
                    arquivo = list(map(str.strip, arquivo))  # REMOVE TODAS AS \N
                    cont = 0  # INICIA O CONTADOR
                    for item in range(len(arquivo)):  # INICIA A ITERACAO PELOS ITEMS DO ARQUIVO
                        palavra = random.choice(arquivo)  # ESCOLHE UMA PALAVRA ALEATORIA
                        cont += 1  # INICIA O CONTADOR
                        if palavra == "":  # CASO A PALAVRA ESTEJA VAZIA
                            pass  # PASSA PARA A PROXIMA PALAVRA
                        else:  # SE NAO
                            palavra = list(palavra)  # TRANFORMA A PALAVRA EM UMA LISTA
                            resultado = all(elem in self.alf for elem in palavra)
                            # RESULTADO = COMPARA TODOS OS INDEX DA PALAVRA ESCOLHIDA COM O ALFABETO
                            if resultado:  # SE TUDO ESTIVER DE ACORDA COM O ALFABETO SEM ACENTUACAO E LETRAS VALIDAS
                                palavra = "".join(palavra)  # TRANFORMA A LISTA PALAVRA EM STRING
                                atualizar = str.maketrans("áàéèâêçãõíìóòúùûô",
                                                          "aaeeaecaoiioouuuo")  # TRADUTOR DE ACENTOS
                                palavra = palavra.translate(atualizar)  # REMOVE QUALQUER ACENTO DA PALAVRA
                                self.palavra = palavra  # SALVA A PALAVRA ROLETADA
                                break  # FINALIZA A BUSCA
                        if cont == len(arquivo):  # CASO NENHUMA PALAVRA NO ARQUIVO SEJA VALIDA INICA A ATUALIZACAO
                            messagebox.showinfo("ERRO", "CASO VOCE ESTEJA VENDO ESTA MENSAGEM "
                                                        "INDICA QUE NENHUM DAS PALAVRAS ENCONTRADAS"
                                                        " NO ARQUIVO SAO VALIDAS PARA O JOGO.")  # MENSAGEM DE ERRO
                            raise FileNotFoundError  # GARANTE A CRIACAO E ATUALIZACAO DO ARQUIVO

            except UnicodeDecodeError:  # NAO FACO A MININA IDEA DE COMO ISSO PODE ACONTECER MAIS NO CASO DE SIM
                messagebox.showinfo("ERRO", "CASO VOCE ESTEJA VENDO ESSA MENSAGEM SAIBA QUE UM DOS CARACTERES"
                                            " DITIGOS POSSUI CARACTERES INLEGIVEIS PELO JOGO, PARA MAIORES DUVIDAS,"
                                            " REFERENCIASE PELO ARQUIVO  / Leia_Me.txt / OU PELOS CREDITOS")
                # MEMSAGEM DE ERRO
                lista = ["Voce", "nao", "devia", "estar", "aqui", "entao", "reinicie", "seu", "jogo", "atualize",
                         "lista",
                         "palavras"]  # LISTA EASTER EGG
                palavra = random.choice(lista)  # SELECIONA UMA PALAVRA DA LISTA EASTER EGG
                self.palavra = palavra  # INICIA O JOGO

            except FileNotFoundError:  # CASO O JOGADOR NAO TENHO A LISTA DE PALAVRAS ELE BUSCA NA LISTA INTERNA DE JOGO
                messagebox.showinfo("ERRO", "ARQUIVO \n\n / Palavras_Lista.txt / "
                                            "\n\n NAO ENCONTRADO OU ATUALIZADO COM SUCESSO.\n")  # MENSAGEM DE ERRO
                self.lista_palavras()  # EVOCA A LISTA DE PALAVRAS / INICIA O JOGO

        Button(tela_medio, text="ROLETAR PALAVRA", padx=15, pady=15,
               bg='black', fg='white', font=("courier ", "10"),
               command=lambda: (Roleta(), tela_medio.destroy(), self.Jogo())).grid(row=23, column=24)  # BUTAO DE ROLETA
        # BOTAO PARA INICIAR O JOGO

        Button(tela_medio, text="VOLTAR", padx=10, pady=8,
               bg='black', fg='lightblue', font=("courier ", "8"),
               command=lambda: (tela_medio.destroy(), self.Tela_2())).grid(row=25, column=24)  # VOLTA A TELA_2 DE JOGO

        tela_medio.mainloop()  # FIM DA TELA MEDIO

    def Dificil(self):
        tela_imp = Tk()  # INICIO DA TELA
        tela_imp.title('JOGO DA FORCA')  # TITULO DA TELA
        tela_imp.iconbitmap(r'Data\Imgs\Forca.ico')  # ICONE DA TELA

        Tela_BG = ImageTk.PhotoImage(Image.open(r'Data\Imgs\Dark.png').resize(self.side))
        # IMAGEM DE FUNDO DA TELA / TAMANHO

        Label(tela_imp, image=Tela_BG).grid(
            row=0, column=0, columnspan=55, rowspan=55)  # MONTA A TELA DE FUNDO

        Label(tela_imp, text="   BEM VINDO AO MODO INFERNAL\n ESCOLHA ABAIXO O NUMERO DE SEU SOFRIMENTO !! ",
              bg="black", fg="red", font=("courier ", "10"), anchor=CENTER).grid(column=26, row=22)  # TEXTO DA TELA

        entry = Entry(tela_imp, borderwidth=5, width=17, bg="red", fg="white")  # MONTA O INPUT DO JOGADOR
        entry.grid(column=26, row=23)  # MOSTRA O INPUT PARA O JOGADOR

        def Sorte():
            messagebox.showinfo("SECRETO", "VERDADEIRAMENTE UM HEROI DE ROLANDO"
                                           ", BOA SORTE BRAVO REVOLUCONARIO !!!")  # TEXTO
            x = random.randint(7, 15)  # RECEBE UM NUMERO ALEATORIO
            num = [True, x]  # INVOCA UM NUMERO ALEATORIO LIMITADO ENTRE 7 E 15
            return num

        def click():
            try:  # TENTANDO COM NUMERO INTEIRO
                if int(entry.get()) == 0 or int(entry.get()) < 0:  # TEST 1 / PARA NUMERO < 0 OU NEGATIVO
                    messagebox.showinfo("ERROR", "NUMERO " + str(entry.get()) +
                                        " E INVALIDO TENTE NOVAMENTE!!!!")  # MESSAGEM DE ERRO
                    return [False, 0]  # RETORNA FALSO E 0 PARA CANCELAR O INICIO DO JOGO

                elif 0 < int(entry.get()) <= 5:  # TESTE 2 / EASTER EGG
                    test = messagebox.askyesno("COVARDE", "DESEJA REALMENTE CONTINUAR O JOGO COM SOMENTE " +
                                               str(entry.get()) + " LETRAS ?? ")  # MESSAGEM  DE COVARDE AO JOGADOR

                    if test == 1:  # CASO SIM A MESSAGEM
                        messagebox.showinfo("COVARDE", "A PARTI DE AGORA VOCE ESTA EXPULSO DOS"
                                                       " REVOLUCIONARIOS, NAO ESPERE POR AJUDA NO FIM !!!")  # TEXTO
                        self.secret = True  # FINAL SECRETO
                        return [True, int(entry.get())]  # INICIA O JOGO

                    else:  # CASO NÃO A MESSAGEM
                        messagebox.showinfo("HEROI", "UM VERDADEIRO REVOLUCIONARIO NAO SE AMEDRONTRA PERANTE "
                                                     "A COROA DE ROLAND, A LUTA COMPANHEIRO(A) !!!!")  # MESSAGEM
                        return [False, 0]  # RETORNA FALSO E 0 PARA CANCELAR O INICIO DO JOGO

                elif 0 < int(entry.get()) <= 14:  # TESTE PARA NUME MENOR DO QUE / OU IGUAL A 5 E MAIOR QUE 0
                    messagebox.showinfo("BEM VINDO !", "A FORCA LHE ESPERA, BOA SORTE !!!")  # MESSAGEM AO JOGADOR
                    return [True, int(entry.get())]  # INICIA O JOGO

                elif int(entry.get()) >= 15:  # TESTA SE O NUME NÃO E MAIOR DO QUE 15 / E AVISA INUTILIDADE DO MODO

                    test = messagebox.askyesno("SERIO?", "USAR " + str(entry.get()) +
                                               " LETRAS REMOVER QUALQUER DIFICULDADE DO JOGO")  # MESSAGEM DE DUVIDA

                    if test == 1:  # SE SIM A MESSAGEM
                        return [True, int(entry.get())]  # INICIA O JOGO
                    else:  # SE NAO A MESSAGEM
                        return [False, 0]  # RETORNA FALSO E 0 PARA CANCELAR O INICIO DO JOGO

            except:  # ERROR COM STRING
                messagebox.showinfo("ERROR", "SOMEMTE NUMEROS INTEIROS POSITIVOS SAO VALIDOS \n\n"
                                             "" + str(entry.get()) + " \n\n NAO E VALIDO, TENTE NOVAMENTE !!")
                # MESSAGEM DE ERROR

                return [False, 0]  # RETORNA FALSO E 0 PARA CANCELAR O INICIO DO JOGO

        def rng_Palavra(lst):
            list1 = []  # LISTA PARA SALVAR AS LETRAS ESCOLHIDAS
            if lst[0] and lst[1] > 0:  # CONDICIONAL PARA CANCELAR DO JOGADOR
                for i in range(lst[1]):  # LOOP PARA GERAR A PALAVRA
                    x = random.randint(0, 51)  # RNG DAS LETRAS COM BASE NO ALFABETO
                    list1.append(self.alf[x])  # SALVA A ESCOLHA
                self.palavra = "".join(list1)  # TRANSPORTADOR
                tela_imp.destroy()  # DESTROY A TELA DIFICIL / IMPOSSIVEL
                self.Jogo()  # INICIA O JOGO

        Button(tela_imp, text="JOGAR", bg="black", fg="red", padx=15, pady=11,
               font=("courier ", "10"), command=lambda: (rng_Palavra(click()))).grid(column=26, row=25)
        # BUTAO PARA INICIA O JOGO NO MODO DIFICIL CASO CLICK RETURN TRUE

        Button(tela_imp, text="SORTE", bg="black", fg="red", padx=7, pady=7,
               font=("courier ", "10"), command=lambda: (rng_Palavra(Sorte()))).grid(column=26, row=28)
        # BUTAO PARA RNG UM NUMERO ENTRE 7 A 19 E INICIAR O JOGO

        Button(tela_imp, text="VOLTAR", padx=10, pady=10,
               bg='black', fg='lightblue', font=("courier ", "8"),
               command=lambda: (tela_imp.destroy(), self.Tela_2())).grid(row=30, column=26)  # VOLTA A TELA_2 DE JOGO

        tela_imp.mainloop()  # FIM DA TELA DIFICIL / IMPOSSIVEL

    def Jogo(self):
    #    print(self.palavra)  # DEV HACK - MOSTRA A PALAVRA SENDO JGOADA
        for i in range(len(self.palavra)):  # MONTA A PALAVRA ESCONDIDA
            self.hw.append(" - ")  # MONTA A LISTA

        tela_Jogo = Tk()  # INICIO DA TELA DE JOGO
        tela_Jogo.title('JOGO DA FORCA')  # TITULO DA TELA
        tela_Jogo.iconbitmap(r'Data\Imgs\Forca.ico')  # ICONE DA TELA
        Tela_BG = ImageTk.PhotoImage(Image.open(r'Data\Imgs\Forca_2.png').resize(self.side))  # IMAGEM DE FUNDO DA TELA

        Label(tela_Jogo, image=Tela_BG, anchor=CENTER).grid(
            row=0, column=0, columnspan=55, rowspan=55)  # TELA MONTADA COM BACKGROUND

        messagebox.showinfo("HISTORIA", "POR DECRETO DO REI DE ROLANDO VOCE FOI ACUSADO INJUSTAMENTE DE "
                                        "MORTE E AGORA LUTA PARA PROVAR SUA INOCENCIA, "
                                        "BOA SORTE COMPANHEIRO(A)")  # HISTORIA DO JOGO

        a = Entry(tela_Jogo, width=10, borderwidth=5, justify=CENTER, relief=SUNKEN)  # ENTRY DAS TENTATIVAS(LETRAS)
        a.grid(row=24, column=24)  # AMOSTRA DA TELA

        def word_h():  # PALAVRA ESCONDIDA
            if len(self.palavra) < 5:  # CASO MENOS DE 5 LETRAS
                largura = 15  # PAD X CASO MENOS DE 5 LETRAS
                larg = 35  # PAD Y CASO MENOS DE 5 LETRAS
            else:  # CASO MAIS QUE 5 LETRAS
                largura = len(self.palavra) * 19  # PAD X
                larg = abs(largura / 18)  # PAD Y

            hw = " / ".join(self.hw)  # ESCONDE A PALAVRA ESCOLHIDA

            try:
                hidden1 = LabelFrame(tela_Jogo, text="  Palavra : \n" + hw,
                                     relief=FLAT, width=largura, height=27)  # MONTA A PALAVRA ESCONDIDA
                hidden1.grid(row=20, column=24, sticky="NSEW", ipadx=larg, padx=larg)
                # INVOCA NA TELA DO JOGADOR A PALAVRA ESCONDIDA

            except:
                pass  # IMPEDE O ERRO NA DESTRUICAO DA TELA E DO FRAME

        def stats():  # STATUS DO JOGADOR
            y, c = sorted(self.acerto), sorted(self.erros)  # RECEBE A LISTA DE ACERTOS /Y/ E ERROS /C/
            x, d = set(y), set(c)  # REMOVE DUPLICATAS DAS LISTA /Y/ E /D/
            acerto, erro = " ".join(x), " ".join(d)  # TRANFORMA O SET /x/ e /d/ EM STRING

            sta = "Vidas: " + str(self.vida - self.morte) + "\n" + ("=" * (len(self.acerto) + 7)) + \
                  "\nAcertos: " + acerto + "\n" + ("=" * (len(self.acerto) + 7)) + "\nErros: " + str(erro)
            # TEXTO DO STATUS

            status = Label(tela_Jogo, text=sta, bg="pink", relief=FLAT)  # TELA DO STATUS
            status.grid(row=34, column=24)  # MONTA A TELA DO STATUS

            Label(tela_Jogo, text="SENSITIVECASE: " + self.sensitiveCase, relief=RAISED
                  ).grid(row=0, column=0)  # MOSTRA AO USUÁRIO O SENSITIVECASE

            if self.morte == self.vida:  # SE A MORTE FOR IGUAL A VIDA
                tela_Jogo.destroy()  # DESTROI A TELA ATUAL
                self.Derrota()  # INVOCA A TELA DE DERROTA

            if set(self.acerto) == set(self.palavra):  # TESTA SE O JOGADOR NAO VENCEU O JOGO
                tela_Jogo.destroy()  # DESTROI A TELA ATUAL
                self.Vitoria()  # INVOCA A TELA DE VITORIA

        Button(tela_Jogo, text="TENTAR", padx=7, pady=7,
               bg='red', fg='black', font=("courier ", "10"),
               command=lambda: (a.delete(1, END), self.Tentativa(str(a.get())), stats(), word_h())
               ).grid(row=29, column=24)  # BUTAO PARA TESTAR A LETRA E ATUALIZAR O STATUS E A PAALVRA ESCONDIDA

        stats()  # MONTA A TELA DE STATUS DO JOGADOR
        word_h()  # MONTA A PALAVRA ESCONDIDA PARA O JOGADOR

        # Label(tela_Jogo,text="Palavra: " + self.palavra).grid(row=0, column=50)  # HACK PARA VER A PALAVRA

        tela_Jogo.mainloop()  # FIM DA TELA JOGO

    def Tentativa(self, letra):
        escolha = list(self.palavra)  # RECEBE A PALAVRA ESCOLHIDA EM FORMA DE LISTA

        if letra in self.alf:  # TESTA PARA VER SE O INPUT DO USUARIO E LETRA VALIDA

            if self.sensitiveCase == "ON":  # SENSTIVECASE ONi

                if letra in self.acerto:  # TESTA PARA REPETICAO DE ACERTO
                    messagebox.showinfo("REPETICAO",
                                        "A PROVA \n\n / " + str(letra) + " / \n\nJA FOI USADA!")  # TEXTO DE REPETIÇÃO
                    self.morte += 1  # PUNICAO POR REPETICAO

                elif letra in self.erros:  # TESTA PARA REPETICAO DE ERRO
                    messagebox.showinfo("REPETICAO", "DESISTA A PROVA\n\n / " + str(letra) +
                                        " / \n\n JA FOI INVALIDADA VOCE SO TEM MAIS /  " + str(self.vida - self.morte)
                                        + " /   TENTATIVAS!!!!")  # TEXTO DE REPETICAO
                    self.morte += 1  # PUNICAO POR REPETICAO

                elif letra in escolha:  # VERIFICA SE A PALAVRA POSSUI A LETRA
                    for L in range(len(escolha)):  # TESTA LETRA POR LETRA
                        if letra == escolha[L]:  # SE TRUE SALVA A LETRA DO USUÁRIO
                            self.acerto.append(escolha[L])  # SALVA A LETRA DO USUÁRIO NA LISTA DE ACERTOS
                            self.hw.pop(L)  # REMOVE UM INDEX DA LISTA DE PALAVRA ESCONDIGA
                            self.hw.insert(L, letra)  # MOSTRA A LETRA E A POSICAO DAS MESMAS AO JOGADOR

                else:  # NO CASO DE A LETRA INFORMADA NAO EXISTER NA PALAVRA
                    messagebox.showinfo("BOA TENTATIVA", "A PROVA\n\n /  " + letra + "  / \n\nCLARAMENTE E FALSA !!!")
                    # TEXTO DE ERRO

                    self.erros.append(letra)  # SALVA A LETRA DO JOGADOR NA LISTA DE ERROS
                    self.morte += 1  # ADICIONA UM PONTO AO CONTADOR DE DERROTA  / A PALAVRA NAO TEM A LETRA

            elif self.sensitiveCase == 'OFF':  # SENSITIVECASE OFF

                if letra.lower() in self.acerto or letra.upper() in self.acerto:  # TESTA PARA REPETICAO DE ACERTO
                    # POR ALGUM MOTIVO QUE DESCONHEÇO O .CASEFOLD() E IGNORADO NESSA CASO.
                    messagebox.showinfo("REPETICAO",
                                        "A PROVA\n\n / " + str(letra) + " / \n\nJA FOI USADA!")  # TEXTO DE REPETIÇÃO
                    self.morte += 1  # PUNICAO POR REPETICAO

                elif letra.casefold() in self.erros:  # TESTA PARA REPETICAO DE ERRO
                    messagebox.showinfo("REPETICAO", "DESISTA A PROVA\n\n / " + str(letra) +
                                        " / \n\nJA FOI INVALIDADA VOCE SO TEM MAIS /  " + str(self.vida - self.morte)
                                        + " /  TENTATIVAS!!!!")  # TEXTO DE REPETIÇÃO
                    self.morte += 1  # PUNICAO POR REPETICAO

                elif letra.casefold() in str(escolha).casefold():  # VERIFICA SE A PALAVRA POSSI A LETRA
                    for L in range(len(escolha)):  # TESTA LETRA POR LETRA COM O CASEFOLD()
                        if letra.casefold() == escolha[L].casefold():  # SE TRUE SALVA A LETRA DO JOGADOR
                            self.acerto.append(escolha[L])  # SALVA A LETRA DO JOGADOR NA LISTA DE ACERTOS
                            self.hw.pop(L)  # REMOVE UM INDEX DA LISTA DE PALAVRA ESCONDIDA
                            self.hw.insert(L, letra)  # MOSTRA A LETRA E A POSICAO DAS MESMAS AO JOGADOR

                else:
                    messagebox.showinfo("BOA TENTATIVA", "A PROVA\n\n / " + letra + " / \n\nCLARAMENTE E FALSA !!!")
                    # TEXTO DE ERRO

                    self.erros.append(letra)  # SALVA A LETRA DO JOGADOR NA LISTA DE ERROS
                    self.morte += 1  # ADICIONA UM PONTO AO CONTADOR DE DERROTA / A PALAVRA NAO TEM A LETRA

        else:  # CASO NAO LETRA
            messagebox.showinfo("BOA TENTATIVA", "A PROVA\n\n / " + letra + " / \n\nNAO E VALIDA NESSE JUGAMENTO !!!!")
            # TEXTO DE ERRO

            self.morte += 1  # ADICIONA UM PONTO AO CONTADOR DE DERROTA / NAO LETRA

    def Vitoria(self):
        tela_Vitoria = Tk()  # INICIO DA TELA VITORIA
        tela_Vitoria.title('JOGO DA FORCA')  # TITULO DA TELA
        tela_Vitoria.iconbitmap(r'Data\Imgs\Forca.ico')  # ICONE DA TELA

        if self.secret:  # SECRET
            i = r'Data\Imgs\Derrota.png'  # ON
        else:  # SECRET
            i = r'Data\Imgs\Vitoria.png'  # OFF

        Tela_BG = ImageTk.PhotoImage(Image.open(i).resize((1380, 720)))  # IMAGEM DE FUNDO DA TELA

        Label(tela_Vitoria, image=Tela_BG, anchor=CENTER).grid(
            row=0, column=0, columnspan=9, rowspan=55)  # TELA MONTADA COM BACKGROUND

        if self.secret:  # SECRET ON
            Label(tela_Vitoria, text="UM COVARDER NAO MERECE RESPEITO !!!!"
                  , bg="black", fg="red", font=("courier ", "10")).grid(column=4, row=23)  # TEXTO 1 DA TELA / SECRET

            Label(tela_Vitoria, text="APOS ESCAPAR DA FOICE DE ROLANDO VOCE FOI MORTO PELOS REVOLUCIONARIS,"
                  , bg="black", fg="red", font=("courier ", "10")).grid(column=4, row=24)  # TEXTO 2 DA TELA / SECRET

            Label(tela_Vitoria, text="SEU CORPO DESCARTADO NOS ESGOTOS, E SEU NOME MANCHADO."
                  , bg="black", fg="red", font=("courier ", "10")).grid(column=4, row=25)  # TEXTO 3 DA TELA / SECRET

        else:  # SECRET OFF
            Label(tela_Vitoria, text="MEUS PARABENS, SUAS ACUSACOES FORAM RETIRADAS E AGORA VOCE ESTA LIVRE"
                  , bg="red", fg="white", font=("courier ", "10")).grid(column=4, row=22)  # TEXTP 1 DA TELA

            Label(tela_Vitoria, text="MAS O QUE ACHA DE APOSTAR SUA VIDA MAIS UMA VEZ?"
                                     " A REVOLUCAO SO ACABA QUANDO ROLAND CAIR !!!",
                  bg="red", fg="white", font=("courier ", "10")).grid(column=4, row=23)  # TEXTO 2 DA TELA

        Label(tela_Vitoria, text="PALAVRA : " + self.palavra, font=("courier ", "10"), fg="white", bg="red"
              ).grid(row=26, column=4)  # MOSTRA A PALAVRA JOGADA

        Button(tela_Vitoria, text="APOSTAR", padx=12, pady=11, fg="red", bg="black",
               font=("courier", "10"), command=lambda: (
                tela_Vitoria.destroy(), self.reset(), self.Tela_1())).grid(column=4, row=27)
        # BUTAO DE REINICIAR O JOGO DA TELA 1 / RESETA OS STATUS CONDICIONAIS

        tela_Vitoria.mainloop()  # FIM DA TELA DE VITORIA

    def Derrota(self):
        tela_Derrota = Tk()  # INICIO DA TELA DE DERROTA
        tela_Derrota.title('JOGO DA FORCA')  # TITULO DA TELA
        tela_Derrota.iconbitmap(r'Data\Imgs\Forca.ico')  # ICONE DA TELA
        Tela_BG = ImageTk.PhotoImage(
            Image.open(r'Data\Imgs\Derrota.png').resize((1380, 720)))  # IMAGEM DE FUNDO DA TELA

        Label(tela_Derrota, image=Tela_BG, anchor=CENTER).grid(
            row=0, column=0, columnspan=9, rowspan=55)  # TELA MONTADA COM BACKGROUND

        if self.secret:
            Label(tela_Derrota, text="UM COVARDER NAO MERECE RESPEITO !!!!"
                  , bg="black", fg="red", font=("courier ", "10")).grid(column=4, row=23)  # TEXTO 1 DA TELA / SECRET

            Label(tela_Derrota, text="MESMO APOS SER MORTO PELA FOICE DE ROLANDO,"
                  , bg="black", fg="red", font=("courier ", "10")).grid(column=4, row=24)  # TEXTO 2 DA TELA / SECRET

            Label(tela_Derrota, text="SEU CORPO FOI DESCARTADO NOS ESGOTOS, E SEU NOME MANCHADO."
                  , bg="black", fg="red", font=("courier ", "10")).grid(column=4, row=25)  # TEXTO 3 DA TELA / SECRET

        else:
            Label(tela_Derrota, text="VOCE NAO CONSEGUIU PROVAR SUA INOCENCIA E FOI EXECUTADO"
                  , bg="black", fg="red", font=("courier ", "10")).grid(column=4, row=23)  # TEXTO 1 DA TELA / NORMAL

            Label(tela_Derrota, text="MAS A LUTA PELA REVOLUCAO NAO ACABOU, DESEJA TENTAR NOVAMENTE?"
                  , bg="black", fg="red", font=("courier ", "10")).grid(column=4, row=24)  # TEXTO 2 DA TELA / NORMAL

        Label(tela_Derrota, text="PALAVRA : " + self.palavra, font=("courier ", "10"), bg="black", fg="red"
              ).grid(column=4, row=25)  # MOSTRA A PALAVRA DE JOGO

        Button(tela_Derrota, text="JOGAR NOVAMENTE", padx=12, pady=11, fg="black", bg="red", relief=FLAT,
               font=("arial", "10"), justify=CENTER, command=lambda: (
                tela_Derrota.destroy(), self.reset(), self.Tela_1())).grid(column=4, row=27)
        # BUTAO DE REINICIAR O JOGO DA TELA 1 / RESETA OS STATUS CONDICIONAIS

        tela_Derrota.mainloop()  # FIM DA TELA DE DERROTA

    def Opt(self):  # TELA DE OPÇÕES
        tela_Options = Tk()  # INICIO DA TELA DE DERROTA
        tela_Options.title('JOGO DA FORCA')  # TITULO DA TELA
        tela_Options.iconbitmap(r'Data\Imgs\Forca.ico')  # ICONE DA TELA
        Tela_BG = ImageTk.PhotoImage(Image.open(r'Data\Imgs\Dark.png').resize(self.side))  # IMAGEM DE FUNDO DA TELA

        Label(tela_Options, image=Tela_BG, anchor=CENTER).grid(
            row=0, column=0, columnspan=9, rowspan=55)  # MONTA A TELA DE FUNDO

        a = Label(tela_Options, text=str(self.sensitiveCase),
                  fg="white", bg="black", font=("courier ", "10"))  # MONTA O Sens.Case NA TELA
        a.grid(column=0, row=25)  # MOSTRA NA TELA O Sens.C.

        b = Label(tela_Options, text=str(self.vida),
                  fg="white", bg="black", font=("courier ", "10"))  # MONTA A TELA DA VIDA
        b.grid(column=1, row=25)  # MOSTRA NA TELA A VIDA ATUAL DO JOGADOR

        def vidas():  # LABEL PARA MOSTRAR O ATUAL NUMERO DE VIDAS
            Label(tela_Options, text=str(self.vida),
                  fg="white", bg="black", font=("courier ", "10")).grid(column=1, row=25)
            # MONTA O NUMERO DE VIDAS NA TELA

        def mudar_vidas(num):  # TESTADOR DE CARACTERES PARA A MUDANCA DA VIDA
            try:  # TENTATIVA 1 PARA NAO NUMEROS
                if int(num) > 0:  # TENTATIVA 2 PARA NUMEROS INTERIROS NÃO POSITIVOS E NÃO DECIMAIS.
                    num = int(num)
                    self.vida = num
                else:  # EXCESSÃO 2 PARA NAO INTEIROS POSITIVOS E DECIMAIS.
                    messagebox.showinfo("ERROR", "O CARACTERER INFORMADO NÃO E "
                                                 "NUMERO INTERIOR E POSITIVO.\nTENTE NOVAMENTE !")  # MENSAGEM DE ERRO
            except:  # EXCESSÃO PARA NAO NUMEROS
                messagebox.showinfo("ERROR", "O CARACTERER INFORMADO NÃO E "
                                             "NUMERO INTERIOR E POSITIVO.\nTENTE NOVAMENTE !")  # MENSAGEM DE ERRO

        def clicked():  # FUNCAO PARA MUDAR O SENSITIVE CASE

            # MENSAGEM DE MUDANCA DO SENSITIVE CASE
            test_1 = messagebox.askyesno("Sensitive Case ?", "DESEJA ATIVAR O SENSITIVE CASE ?"
                                                             "\n\n SIM : \n Ex¹.: A != a ( A E DIFERENTE DE a)"
                                                             " \n\n NÃO : \n Ex².: A = a ( A EO MESMO QUE a)")

            if test_1 == 1:  # CASO USUARIO ACEITE / ON
                self.sensitiveCase = 'ON'  # SENSITIVE CASE ON
            else:  # CASO USUARIO RECUSE / OFF
                self.sensitiveCase = 'OFF'  # SENSITIVE CASE OFF / PADRAO

            Label(tela_Options, text=str(self.sensitiveCase),
                  fg="white", bg="black", font=("courier ", "10")
                  ).grid(column=0, row=25)  # MONTA E MOSTRA O S.C NA TELA

        def click():  # MUDA O NUMERO PADRÃO DE VIDAS DO USUÁRIO

            test_2 = messagebox.askyesno("HACK", "NÃO RECOMENDASSE MUDAR O NUMERO PADRAO DE VIDAS!! \n"
                                                 "DESEJA REALMENTE CONTINUAR ?")
            # PERGUNTA AO JOGADOR SE O MESMO DESEJA CONTINUAR COM A MUDANCA DE VIDA

            if test_2 == 1:  # CONSTRUTOR DA ENTRY DE MUDANÇA
                z = Entry(tela_Options, bg="white", fg="black", justify=CENTER)  # INPUT PARA MUDAR O NUMERO DE VIDAS
                z.grid(column=1, row=25)  # MOSTA O INPUT NA TELA
                r = Button(tela_Options, text="MODIFICAR", bg='black', fg='LightBlue', font=("courier ", "10"),
                           padx=9, pady=7, command=lambda: (mudar_vidas(z.get()), z.destroy(), r.destroy(),
                                                            vidas(), x.destroy()))
                r.grid(column=1, row=26)
                # BUTAO R = MUDA A VIDA DO USARIO E DELETA A TELA DA ENTRY Z E OS BUTOES R X DA OPCAO MUDAR VIDA
                x = Button(tela_Options, text="CANCELAR", bg='black', fg='LightBlue', font=("courier ", "9"),
                           padx=9, pady=7, command=lambda: (x.destroy(), z.destroy(), r.destroy(), vidas()))
                x.grid(column=1, row=27)
                # BUTAO X = DELETA OS BUTOES Z R X DA OPCAO MUDAR VIDA

        def atu_palavra(palavra):  # ATUALIZA O ARQUIVO COM UMA PALAVRA DO JOGADOR
            palavra = list(palavra)  # TRANSFORAM A PALAVRA STRING PARA LISTA
            resultado = all(elem in self.alf for elem in palavra)  # VERIFICAR SE TODOS OS INDEX SAO ALFABETICOS
            if resultado:  # SE SIM
                palavra = "".join(palavra)  # TRANSFORMA A PALAVRA DE LISTA PARA STRING
                self.Arquivo(palavra)  # ENVIA A PALAVRA PARA SER SALVA NO ARQUIVO
                messagebox.showinfo("ADCIONADA", "A PALAVRA \n\n  /  " + palavra +
                                    "  / \n\n FOI ADICIONADA COM SUCESSO")  # MEMSAGEM DE SUCESSO
                atualizar()  # RESETA A TELA DE ADICAO PARA PALAVRA
            else:  # SE NAO
                messagebox.showinfo("ERRO", "SOMENTE LETRAS, SEM ACENTUACAO E ESPACO, SAO ACEITAS, TENTE"
                                            " NOVAMETEN")  # MENSAGEM DE ERRO
                atualizar()  # RESETA A TELA DE ADICAO PARA PALAVRA

        def atualizar():  # ATUALIZAR / CRIAR / ACIONAR UMA NOVA PALAVRA (A)O ARQUIVO Palavras_Lista.txt
            test_3 = messagebox.askyesno("SALVAR", "DESEJA ADICIONAR MAIS ALGUMA PALAVRA AO ARQUIVO?")  # MENSAGEM
            self.lista_palavras()  # CRIA O ARQUIVO COM A LISTA DE PALAVRAS PRE-CONFIGURADA
            if test_3 == 1:  # CASO O JOGADOR DESEJE ADICIONAR MAIS ALGUMA PALAVRA
                x = Entry(tela_Options, bg="white", fg="black", justify=CENTER)  # ENTRY ( INPUT ) DO JOGADOR
                x.grid(column=2, row=25)  # MONTA A ENTRY X NA TELA

                y = Button(tela_Options, text="ADICIONAR", bg='black', fg='LightBlue', font=("courier ", "10"),
                           padx=9, pady=7,
                           command=lambda: (atu_palavra(str(x.get())), x.destroy(), y.destroy(), z.destroy()))
                y.grid(column=2, row=26)  # MONTA O Y NA TELA
                # Y = BUTAO PARA ADICIONAR UMA PALAVRA AO ARQUIVO E DELETAR A ENTRY X JUNTO AOS BUTOES Y Z

                z = Button(tela_Options, text="CANCELAR", bg='black', fg='LightBlue', font=("courier ", "9"), padx=9,
                           pady=7, command=lambda: (z.destroy(), x.destroy(), y.destroy(), self.lista_palavras()))
                z.grid(column=2, row=27)  # MONTA Z NA TELA
                # Z = BOTAO PARA CANCELAR A ADICAO DE UMA NOVA PALAVRA / ATUALIZAR A LISTA E DELETAR OS BUTOES X Y Z

                messagebox.showinfo("UPDATE", " ARQUIVO ATUALIZADO.\nCRIADO COM SUCESSO.")  # MENSAGEM INFORMATIVA
            else:
                messagebox.showinfo("UPDATE", " ARQUIVO ATUALIZADO.\nCRIADO COM SUCESSO.")  # MENSAGEM DE FINALIZACAO

        def show():  # MOSTRA A ATUAL LEITURA DO ARQUIVO Palavras_Lista.txt PELO JOGO
            root = Tk()  # INICIA DA TELA
            root.title('LISTA DE PALAVRAS')  # TITULO DA TELA
            root.iconbitmap(r'Data\Imgs\Forca.ico')  # ICONE DA TELA

            myLabel = Label(root, bg="black")  # LABEL DA LISTA DE PALAVRAS OK
            myLabel.pack(side=LEFT)  # MOSTRA A LABEL PARA O JOGADOR

            myLabel_2 = Label(root, bg="black")  # INICIA DA LISTA DE PALAVRAS ERRADAS
            myLabel_2.pack(side=RIGHT)  # MOSTRA A LABEL PARA O JOGADOR

            scrolling = Scrollbar(myLabel, bg="black", bd=10, relief=SUNKEN)
            # SCROLLBAR PARA O JOGADOR SE MOVER PELA LISTA 1
            scrolling.pack(side=RIGHT, fill=Y)  # MOSTRA O SCROLLBAR PARA O JGOADOR

            scrolling_2 = Scrollbar(myLabel_2, bg="black", bd=10, relief=SUNKEN)
            # SCROLLBAR PARA O JOGADOR SE MOVER PELA LISTA 2
            scrolling_2.pack(side=RIGHT, fill=Y)  # MOSTRA O SCROLLBAR PARA O JGOADOR

            myList = Listbox(myLabel, yscrollcommand=scrolling.set, height=50, bg="green", fg="white"
                             , font=("arial", "10", "bold"), bd=10, relief=SUNKEN)  # INICIA A LISTA 1 DE PALAVRAS OK
            myList.insert(END, " PALAVRAS VALIDAS")  # MONTA NO INDEX 1 DA LISTA O MOTIVO DA LISTA
            myList.insert(END, "\n")  # DA UM ESPAÇO

            myList_2 = Listbox(myLabel_2, yscrollcommand=scrolling_2.set, height=50, bg="red", fg="white"
                               , font=("arial", "10", "bold"), bd=10, relief=SUNKEN)  # INICIA A LISTA 2 DE PAL. ERRADAS
            myList_2.insert(END, " PALAVRAS INVALIDAS")  # MONTA NO INDEX 1 DA LISTA O MOTIVO DA LISTA
            myList_2.insert(END, "\n")  # DA UM ESPAÇO

            try:  # TENTA LER O ARQUIVO SE EXISTENTE
                with open(r"Data\Palavras_Lista.txt", encoding="UTF-8") as file:  # ABRE COM UTF-8
                    file = file.readlines()  # LE TODAS AS LINHAS DO ARQUIVO
                    file = list(map(str.strip, file))  # REMOVE TODAS AS \N
                    for i in range(len(file)):  # INICIA O LOOP PARA VALIDAR TODAS AS PALAVRAS DO ARQUIVO
                        if file[i] == '':  # CASO SEJA SO UMA LINHA VAZIA
                            myList.insert(END, str(i) + ".  " + "/ NADA /")  # INFORMA AO JOGADOR QUE NAO A NADA ALI
                            pass  # PASSA PARA A PROXIMA LINHA
                        else:  # SE HOUVER ALGO
                            palavra = str(file[i])  # PALAVRA = DO FILE A PALAVRA EM STRING, PARA GARANTIR.
                            traducao = str.maketrans("áàéèâêçãõíìóòúùûô", "aaeeaecaoiioouuuo")  # TRADUTOR DE ACENTOS
                            palavra = palavra.translate(traducao)  # REMOVE QUALQUER ACENTO DA PALAVRA
                            palavra = list(palavra)  # TRANFORMA A PALAVRA DE STRING EM LISTA
                            resultado = all(elem in self.alf for elem in palavra)  # VERIFICA SE A PALAVRA E VALIDA
                            palavra = "".join(palavra)  # TRANFORMA A PALAVRA DE LISTA PARA STRING

                            if resultado:  # SE A PALAVRA FOR VALIDA
                                myList.insert(END, str(i) + ". " + palavra)  # SALVA A PALAVRA NA LISTA 1
                            else:  # SE A PALAVRA FOR INVALIDA
                                myList_2.insert(END, str(i) + ". " + palavra)  # SALVA A PALAVRA NA LISTA 2

                myList.pack(side=BOTTOM, fill=Y)  # MOSTRA A LISTA 1 PARA O JOGADOR
                scrolling.config(command=myList.yview)  # MOSTRA A BARRA DE ROLAMENTO 1 AO JOGADOR

                myList_2.pack(side=BOTTOM, fill=Y)  # MOSTRA A LISTA 2 PARA O JOGADOR
                scrolling_2.config(command=myList_2.yview)  # MOSTRA A BARRA DE ROLAMENTO 2 AO JOGADOR

                Button(root, text="SAIR", padx=14, pady=9,
                       bg='black', fg='LightBlue', font=("courier ", "10"), command=root.destroy
                       ).pack(side=BOTTOM, anchor=CENTER)  # BOTAO PARA DESTROY / SAIR DA TELA SHOW

                messagebox.showinfo("AVISO", "QUALQUER ACENTUACAO SERA REMOVIDO E TIDA COMO VALIDA,"
                                             " SE TODOS OS CARACTERES FORAM ALFABETICOS.")  # MENSAGEM INFORMATIVA

            except:  # CASO O ARQUIVO NAO EXISTA OU INLEGIVEL
                messagebox.showinfo("ERRO", "ARQUIVO NAO ENCONTRADO, TENTE ATUALIZAR OU CRIAR O ARQUIVO.")  # ERRO
                root.destroy()  # CANCELA O INICIO DA TELA

            root.mainloop()  # FIM DA TELA SHOW()

        Button(tela_Options, text="SENSITVE \nCASE", padx=17, pady=17,
               bg='black', fg='LightBlue', font=("courier ", "10"),
               command=lambda: (clicked(), a.destroy())).grid(column=0, row=24)
        # ATUALIZA O Sens.Case E DESTROI O ANTERIOR

        Button(tela_Options, text="HACK \n MUDAR VIDA", padx=17, pady=17,
               bg='black', fg='LightBlue', font=("courier ", "10"),
               command=lambda: (click())).grid(column=1, row=24)
        # BOTAO DE QUESTAO PARA SABER SE O USUARIO DESEJAR MUDAR O NUMERO PADRÃO DE VIDAS

        Button(tela_Options, text="ATUALIZAR A \nLISTA DE PALAVRAS", padx=17, pady=17,
               bg='black', fg='LightBlue', font=("courier ", "10"),
               command=lambda: (atualizar())).grid(column=2, row=24)
        # BOTAO PARA ATUALIZAR/CRIAR A LISTA DE PALAVRAS OU ADICIONAR NOVAS PALAVRAS A LISTA

        Button(tela_Options, text="MOSTRAR A \nLISTA DE PALAVRAS ATUAL", padx=17, pady=17,
               bg='black', fg='LightBlue', font=("courier ", "10"),
               command=lambda: (show())).grid(column=3, row=24)
        # BUTAO QUE TENTA INICIAR A TELA QUE MOSTRA COMO AS PALAVRAS ESTAO SENDO LIDAS PELO PROGRAMA

        Button(tela_Options, text="VOLTAR", padx=17, pady=17,
               bg='black', fg='LightBlue', font=("courier ", "10"), command=lambda: (
                tela_Options.destroy(), self.Tela_1())).grid(column=8, row=24)
        # BOTAO PARA VOLTAR A TELA INICIAL / DESTROI A TELA DE OPÇÕES.

        Button(tela_Options, text="CREDITOS", padx=15, pady=15,
               bg='black', fg='LightBlue', font=("courier ", "10"),
               command=lambda: (tela_Options.destroy(), self.Creditos())).grid(column=8, row=41)  # CREDITOS DO JOGO

        tela_Options.mainloop()  # FIM DA TELA DE OPÇÕES ( OPTIONS )

    def Arquivo(self, palavra):  # MANIPULACAO DO ARQUIVO TXT
        try:  # TENTA ABRIR OU CRIAR O ARQUIVO, Palavras_Lista.txt.
            with open(r"Data\Palavras_Lista.txt", "a+", encoding="UTF-8") as arquivo:
                # SE ELE EXISTER ABRE COMO READ / UTF8
                if isinstance(palavra, list):  # CASO A PALAVRA RECEBA A LISTA DA lista_palavras
                    arquivo.write("\n")
                    for i in range(len(palavra)):  # SALVA A LISTA DE PALAVRAS NO ARQUIVO COMO WRITER
                        x = str(palavra[i])  # GARANTE QUE A PALAVRA RECEBIDA SEJA UMA STRING
                        x.encode(encoding="UTF-8")  # ENCODE A PALAVRA EM UTF8
                        arquivo.write(x + "\n")  # SALVA A PALAVRA NO ARQUIVO .TXT OU ATUALIZA O ARQUIVO EXISTENTE
                else:  # CASO SEJA SOMENTE UMA PALAVRA
                    arquivo.write("\n")
                    x = str(palavra)  # GARANTE QUE A PALAVRA RECEBIDA SEJA UMA STRING
                    x.encode(encoding="UTF-8" + "\n")  # ENCODE A PALAVRA EM UTF8
                    arquivo.write(palavra)  # DA APPEND NA NOVA PALAVRA NO FINAL DO ARQUIVO.

        except:  # CASO O ARQUIVO NAO POSSA SER CRIADO LEVANTA A MENSAGEM DE ERRO.
            messagebox.showinfo("UPDATE", "POR ALGUM MOTIVO SEU ARQUIVO \n\n / Palavras_Lista.txt / "
                                          "\n\n NÃO FOI CRIADO COM SUCESSO.")
            # CASO O ARQUIVO NAO TENHA SIDO CRIADO COM SUCESSO

    def lista_palavras(self):
        # EXISTE PARA FACILITAR A MODIFICAO DA LISTA NO BACK END SEM PRECISAR MODIFICAR QUALQUER CODIGO

        lista_Palavras = ["Amor", "Bolo", "Cachorro", "Lata", "Ornitorrinco", "otorrinolaringologia",
                          "Mulher", "Lei", "Homem", "Celular", "Vida", "Morte", "Pneumologia", "Beethoven",
                          "Symphony", "Nigthcore", "Americano", "Brasil", "Patriota", "Luta",
                          "Flanelografo", "Gato", "Gata", "Torresmo", "Frango", "Peixe", "Monstrão",
                          "Leo", "Stronda", "Doutor", "Noturno", "Diario", "Diariamente",
                          "Lista"]  # LISTA DE PALAVRAS CASO O ARQUIVO NAO SEJA ENCONTRADO OU INVALIDO

        self.Arquivo(lista_Palavras)  # ATUALIZA/CRIA O ARQUIVO DE PALAVRAS
        while True:  # LOOP PARA GARANTIR QUE A PALAVRA ESCOLHIDA NO FINAL SEJA VALIDA
            palavra = random.choice(lista_Palavras)  # SELECIONA UMA PALAVRA DA LISTA
            atualizar = str.maketrans("áàéèâêçãõíìóòúùûô", "aaeeaecaoiioouuuo")  # TRADUTOR DE ACENTOS
            palavra = palavra.translate(atualizar)  # REMOVE QUALQUER ACENTO DA PALAVRA
            palavra = list(palavra)  # TRANSFORMA A PALAVRA EM LISTA
            resultado = all(elem in self.alf for elem in palavra)  # VERIFICAR SE TODOS OS INDEX SAO ALFABETICOS
            if resultado:  # SE SIM
                palavra = "".join(palavra)  # TRANSFORAM A LISTA EM STRING NOVAMENTE
                self.palavra = palavra  # SALVA A PALAVRA ROLETADA E INICIA O JOGO
                break  # CANCELA A BUSCA / INICIA O JOGO

    def Creditos(self):
        tela_Creditos = Tk()  # INICIA DA TELA DE CREDITOS
        tela_Creditos.title('SOBRE O CRIADOR.')  # TITULO DA TELA
        tela_Creditos.geometry("1400x743")  # TAMANHO TOTAL DA TELA
        tela_Creditos.iconbitmap(r'Data\Extra\ISSTH_Lord_Fifth.ico')  # ICONE DA TELA
        Tela_BG = ImageTk.PhotoImage(Image.open(r'Data\Extra\Sun.png').resize(self.side))  # IMAGEM DE FUNDO DA TELA
        Image_1 = ImageTk.PhotoImage(Image.open(r'Data\Extra\ISSTH_Lord_Fifth.png'))  # IMAGEM 1 LORD FIFTH
        Image_2 = ImageTk.PhotoImage(Image.open(r'Data\Extra\Foto.png'))  # IMAGEM 2  EU

        myFrame = LabelFrame(tela_Creditos, relief=GROOVE, bd=10, bg="black")  # FRAME
        myFrame.pack(fill=NONE, expand=NO, anchor=CENTER)  # MONTA O FRAME NA TELA

        Label(myFrame, image=Tela_BG, bg="black").grid(rowspan=30, columnspan=30)  # LABEL DA IMAGE DE BG
        Label(myFrame, image=Image_2, width=160, height=186, bg="black", relief=RIDGE).grid(row=1, column=15)  # EU

        myLabel = Label(myFrame, width=50, height=20)  # LABEL DO TEXTO
        myLabel.grid(row=14, column=15)  # MONTA A LABEL DO TEXTO

        def image():  # SWITCH DAS IMAGENS
            if self.num == 0:  # LORD FIFTH
                Label(myFrame, image=Image_1, width=160, height=186, bg="black", relief=RIDGE).grid(row=1, column=15)
                self.num = 1  # SWITCH = 1
            elif self.num == 1:  # EU
                Label(myFrame, image=Image_2, width=160, height=186, bg="black", relief=RIDGE).grid(row=1, column=15)
                self.num = 0  # SWITCH = 0

        Button(myFrame, text="< < <", font=("Arial", "10"),
               bg="black", fg="white", padx=9, pady=9, justify=CENTER, relief=GROOVE, command=image).grid(row=1,
                                                                                                          column=13)
        # BUTAO PARA AVANCAR OU VOLTAR A IMAGEM

        Button(myFrame, text="> > >", font=("Arial", "10"),
               bg="black", fg="white", padx=9, pady=9, justify=CENTER, relief=GROOVE, command=image).grid(row=1,
                                                                                                          column=17)
        # BUTAO PARA AVANCAR OU VOLTAR A IMAGEN

        scrolling = Scrollbar(myLabel, bg="black", bd=10, relief=SUNKEN, troughcolor="black")  # SCROLLBAR PARA ROLAR

        texto = Text(myLabel, height=20, width=60, yscrollcommand=scrolling.set, spacing1=5,
                     font=("arial", "9", "bold"), fg="black", relief=RIDGE, bg="white")  # WIDGET DO TEXTO
        texto.tag_configure("center", justify=CENTER)  # JUSTIFICA TUDO NO CENTRO

        with open(r"Data\Extra\Sobre_Min.txt", "r", encoding="UTF-8") as arquivo:  # ABRE O ARQUIVO DE TEXTO
            arquivo = arquivo.readlines()  # LE AS LINHAS NO ARQUIVO
            for i in range(len(arquivo)):  # LOOP PARA OUTPUT DO TEXTO
                texto.insert(END, arquivo[i], CENTER)  # INSERI O TEXTO NA TELA

        texto.config(state=DISABLED)  # DESABILITA A EDICAO DO TEXTO

        scrolling.pack(fill=Y, side=RIGHT)  # MOSTRA O SCROLLBAR PARA O JGOADOR

        texto.pack(side=LEFT, fill=NONE)  # MOSTRA O TEXTO AO JOGADOR

        scrolling.config(command=texto.yview)  # MOSTRA A SCROLLBAR AO JOGADOR

        Button(myFrame, text="VOLTAR", font=("Arial", "10"),
               bg="black", fg="white", padx=9, pady=9, justify=CENTER, relief=GROOVE,
               command=lambda: (tela_Creditos.destroy(), self.Opt())).grid(row=29, column=15, columnspan=2)
        # BUTAO PARA SAIR DA TELA DE CREDITOS

        tela_Creditos.mainloop()  # FIM DA TELA DE CREDITOS


Jogo = Forca()
