import tkinter as tk
from tkinter import *
import random
import sqlite3 
import time

def loginPage(logdata):
    sup.destroy()
    global login
    login = Tk()
    
    user_name = StringVar()
    password = StringVar()
    
    login_canvas = Canvas(login,width=720,height=480,bg="blue")
    login_canvas.pack()

    login_frame = Frame(login_canvas,bg="white")
    login_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    heading = Label(login_frame,text="TRI-QUEST LOGIN",fg="black",bg="white")
    heading.config(font=('calibri 30'))
    heading.place(relx=0.2,rely=0.1)

    #USER NAME
    ulabel = Label(login_frame,text="User",fg='black',bg='white')
    ulabel.place(relx=0.21,rely=0.4)
    uname = Entry(login_frame,bg='#d3d3d3',fg='black',textvariable = user_name)
    uname.config(width=42)
    uname.place(relx=0.31,rely=0.4)

    #PASSWORD
    plabel = Label(login_frame,text="Senha",fg='black',bg='white')
    plabel.place(relx=0.215,rely=0.5)
    pas = Entry(login_frame,bg='#d3d3d3',fg='black',show="*",textvariable = password)
    pas.config(width=42)
    pas.place(relx=0.31,rely=0.5)

    def check():
        for a,b,c,d in logdata:
            if b == uname.get() and c == pas.get():
                menu()
                break
        else:
            error = Label(login_frame,text="User ou senha errada!",fg='black',bg='white')
            error.place(relx=0.37,rely=0.7)
    
    #LOGIN BUTTON
    log = Button(login_frame,text='Login',padx=5,pady=5,width=5,command=check)
    log.configure(width = 15,height=1, activebackground = "#33B5E5", relief = FLAT)
    log.place(relx=0.4,rely=0.6)
    
    
    login.mainloop()

def signUpPage():
    root.destroy()
    global sup
    sup = Tk()
    
    fname = StringVar()
    uname = StringVar()
    passW = StringVar()
    country = StringVar()
    
    
    sup_canvas = Canvas(sup,width=720,height=440,bg="red")
    sup_canvas.pack()

    sup_frame = Frame(sup_canvas,bg="white")
    sup_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    heading = Label(sup_frame,text="Cadastrar usuário",fg="black",bg="white")
    heading.config(font=('calibri 35'))
    heading.place(relx=0.2,rely=0.1)

    #full name
    flabel = Label(sup_frame,text="Nome",fg='black',bg='white')
    flabel.place(relx=0.21,rely=0.4)
    fname = Entry(sup_frame,bg='#d3d3d3',fg='black',textvariable = fname)
    fname.config(width=42)
    fname.place(relx=0.31,rely=0.4)

    #username
    ulabel = Label(sup_frame,text="User",fg='black',bg='white')
    ulabel.place(relx=0.21,rely=0.5)
    user = Entry(sup_frame,bg='#d3d3d3',fg='black',textvariable = uname)
    user.config(width=42)
    user.place(relx=0.31,rely=0.5)
    
    
    #password
    plabel = Label(sup_frame,text="Senha",fg='black',bg='white')
    plabel.place(relx=0.215,rely=0.6)
    pas = Entry(sup_frame,bg='#d3d3d3',fg='black',show="*",textvariable = passW)
    pas.config(width=42)
    pas.place(relx=0.31,rely=0.6)
    
    
    
    #country
    clabel = Label(sup_frame,text="Cidade",fg='black',bg='white')
    clabel.place(relx=0.215,rely=0.7)
    c = Entry(sup_frame,bg='#d3d3d3',fg='black',textvariable = country)
    c.config(width=42)
    c.place(relx=0.31,rely=0.7)
    def addUserToDataBase():
        
        Nome = fname.get()
        User = user.get()
        Senha = pas.get()
        Cidade = c.get()
        
        conn = sqlite3.connect('quiz.db')
        create = conn.cursor()
        create.execute('CREATE TABLE IF NOT EXISTS userSignUp(NOME text, USERNAME text,PASSWORD text,COUNTRY text)')
        create.execute("INSERT INTO userSignUp VALUES (?,?,?,?)",(Nome,User,Senha,Cidade))
        conn.commit()
        create.execute('SELECT * FROM userSignUp')
        z=create.fetchall()
        print(z)
#        L2.config(text="Username is "+z[0][0]+"\nPassword is "+z[-1][1])
        conn.close()
        loginPage(z)
    def gotoLogin():
        conn = sqlite3.connect('quiz.db')
        create = conn.cursor()
        conn.commit()
        create.execute('SELECT * FROM userSignUp')
        z=create.fetchall()
        loginPage(z)
    #signup BUTTON
    sp = Button(sup_frame,text='Cadastrar',padx=5,pady=5,width=5,command = addUserToDataBase,bg='green')
    sp.configure(width = 15,height=1, activebackground = "#33B5E5", relief = FLAT)
    sp.place(relx=0.4,rely=0.8)

    log = Button(sup_frame,text='Já tem uma conta ?',padx=5,pady=5,width=5,command = gotoLogin,bg="white",fg='blue')
    log.configure(width = 16,height=1, activebackground = "#33B5E5", relief = FLAT)
    log.place(relx=0.4,rely=0.9)

    sup.mainloop()

def menu():
    login.destroy()
    global menu 
    menu = Tk()
    
    
    menu_canvas = Canvas(menu,width=720,height=440,bg="blue")
    menu_canvas.pack()

    menu_frame = Frame(menu_canvas,bg="white")
    menu_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    
    
    wel = Label(menu_canvas,text=' B E M  V I N D O  A O  T R I - Q U E S T ',fg="white",bg="#101357")
    wel.config(font=('Broadway 22'))
    wel.place(relx=0.1,rely=0.02)
    
    
    level = Label(menu_frame,text='Selecione um tema !!',bg="white",font="calibri 18")
    level.place(relx=0.25,rely=0.3)
    


    var = IntVar()
    educação = Radiobutton(menu_frame,text='Educação',bg="white",font="calibri 16",value=1,variable = var)
    educação.place(relx=0.25,rely=0.4)

    
    Saúde = Radiobutton(menu_frame,text='Saúde',bg="white",font="calibri 16",value=2,variable = var)
    Saúde.place(relx=0.25,rely=0.5)
    
    Sustentabilidade = Radiobutton(menu_frame,text='Sustentabilidade',bg="white",font="calibri 16",value=3,variable = var)
    Sustentabilidade.place(relx=0.25,rely=0.6)
    
    
    def navigate():
        
        x = var.get()
        print(x)
        if x == 1:
            menu.destroy()
            easy()
        elif x == 2:
            menu.destroy()
            medium()
        
        elif x == 3:
            menu.destroy()
            difficult()
        else:
            pass
    letsgo = Button(menu_frame,text="Começar",bg="white",font="calibri 12",command=navigate)
    letsgo.place(relx=0.25,rely=0.8)
    menu.mainloop()
def easy():
    
    global e
    e = Tk()
    
    easy_canvas = Canvas(e,width=720,height=440,bg="#101357")
    easy_canvas.pack()

    easy_frame = Frame(easy_canvas,bg="white")
    easy_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    
    def countDown():
        check = 0
        for k in range(10, 0, -1):
            
            if k == 1:
                check=-1
            timer.configure(text=k)
            easy_frame.update()
            time.sleep(1)
            
        timer.configure(text="Times up!")
        if check==-1:
            return (-1)
        else:
            return 0
    global score
    score = 0

    educação = [
                 [
                     "Marque a opção em que há erro na identificação da classe da \n"
                     "palavra destacada:",
                     "Júlia é uma executiva sem parâmetros. – Preposição",
                     "Ricardo odeia que lhe digam o que é certo. – Artigo",
                     "Os homens assistemperplexos àrevolução hormonal.– Adjetivo",
                     "Nenhuma das alternativas"
                 ] ,
                 [
                     "Até hoje, no Brasil,usamos como referência o calendário:",
                    "Judaico",
                    "Cristão.",
                    "Indígina",
                    "Romano"
                     
                 ],
                [
                    "Quais as maiores pandemias da história?",
                    "Varíola e hipertensão",
                    "Peste negra e covid-19",
                    "Cólera e colesterol",
                    "Dengue"
                ],
                [
                    "Nesses pares, ambos são mamíferos:?",
                    "Baleia azul e golfinhos",
                    "Morcegos e galinhas",
                    "Girafas e tartarugas",
                    "Galinha e leão"
                ],
                [
                    "O que foi a Guerra Fria?",
                    "Um conflito de base ideológica.",
                    "Queda do Muro de Berlin.",
                    "Uma guerra sangrenta.",
                    "Conflito entre Alemanha e Itália."

                ]
            ]
    answer = [
                "Ricardo odeia que lhe digam o que é certo. – Artigo",
                "Cristão",
                "Peste negra e covid-19",
                "aleia azul e golfinhos",
                "Um conflito de base ideológica."
             ]
    li = ['',0,1,2,3,4]
    x = random.choice(li[1:])
    
    ques = Label(easy_frame,text =educação[x][0],font="calibri 12",bg="white")
    ques.place(relx=0.5,rely=0.2,anchor=CENTER)

    var = StringVar()
    
    a = Radiobutton(easy_frame,text=educação[x][1],font="calibri 10",value=educação[x][1],variable = var,bg="white")
    a.place(relx=0.5,rely=0.42,anchor=CENTER)

    b = Radiobutton(easy_frame,text=educação[x][2],font="calibri 10",value=educação[x][2],variable = var,bg="white")
    b.place(relx=0.5,rely=0.52,anchor=CENTER)

    c = Radiobutton(easy_frame,text=educação[x][3],font="calibri 10",value=educação[x][3],variable = var,bg="white")
    c.place(relx=0.5,rely=0.62,anchor=CENTER) 

    d = Radiobutton(easy_frame,text=educação[x][4],font="calibri 10",value=educação[x][4],variable = var,bg="white")
    d.place(relx=0.5,rely=0.72,anchor=CENTER) 
    
    li.remove(x)
    
    timer = Label(e)
    timer.place(relx=0.8,rely=0.82,anchor=CENTER)
    
    
    
    def display():
        
        if len(li) == 1:
                e.destroy()
                showMark(score)
        if len(li) == 2:
            nextQuestion.configure(text='Fim',command=calc)
                
        if li:
            x = random.choice(li[1:])
            ques.configure(text =educação[x][0])
            
            a.configure(text=educação[x][1],value=educação[x][1])
      
            b.configure(text=educação[x][2],value=educação[x][2])
      
            c.configure(text=educação[x][3],value=educação[x][3])
      
            d.configure(text=educação[x][4],value=educação[x][4])
            
            li.remove(x)
            print(li)
            y = countDown()
            if y == -1:
                display()

            
    def calc():
        global score
        if (var.get() in answer):
            score+=1
        display()
    
    submit = Button(easy_frame,command=calc,text="Confirmar")
    submit.place(relx=0.5,rely=0.82,anchor=CENTER)
    
    nextQuestion = Button(easy_frame,command=display,text="Pular")
    nextQuestion.place(relx=0.87,rely=0.82,anchor=CENTER)
    
    y = countDown()
    if y == -1:
        display()
    e.mainloop()
    
    
def medium():
    
    global m
    m = Tk()
    
    med_canvas = Canvas(m,width=720,height=440,bg="#101357")
    med_canvas.pack()

    med_frame = Frame(med_canvas,bg="white")
    med_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    
    def countDown():
        check = 0
        for k in range(10, 0, -1):
            
            if k == 1:
                check=-1
            timer.configure(text=k)
            med_frame.update()
            time.sleep(1)
            
        timer.configure(text="Times up!")
        if check==-1:
            return (-1)
        else:
            return 0
        
    global score
    score = 0
    
    Saúde = [
                [
                    "Os caracteres sexuais primários, presentes desde o nascimento\n"
                    " de um indivíduo, são determinadas por genes presentes:",
                     "Nos cromossomos sexuais X e Y.",
                     "Apenas no cromossomo X",
                     "Apenas no cromossomo Y",
                     "Todas estão incorretas."
                ],
                [
                    "Os métodos contraceptivos hormonais são eficazes por que:",
                    "Inibem a movimentação dos espermatozoides.",
                    "Provocam o fechamento das tubas uterinas.",
                    "Impedem a ovulação.",
                    "Ajudam na gravidez"
                ],
                [
                    "Qual é o hormônio que será detectado \n"
                    "na urina para indicar se a mulher está grávida?",
                    "Testosterona",
                    "Gonadotrofina coriônica.",
                    "Prolactina.",
                    "Creatina."
                ],
                [
                    "O HIV é um exemplo de vírus envelopado. Marque a \n"
                    "alternativa que explica corretamente essa definição.",
                    "São vírus envolvidos por um envelope proteico.",
                    "São vírus envolvidos por uma parede celular",
                    "São vírus envolvidos por um envelope lipoproteico.",
                    "Todos estão corretas"
                ],
                [
                    "Além de sustentação do corpo, são funções dos ossos:",
                    "Armazenar cálcio e fósforo; produzir hemácias e leucócitos.",
                    "Armazenarcálcio e fósforo; produz glicogênio",
                    "Armazenaglicogênio; produz hemácias e leucócitos.",
                    "Armazenar ferro e cálcio; produzir leucócitos."
                ],
            ]
    respostas = [
            "Nos cromossomos sexuais X e Y.",
            "Impedem a ovulação.",
            "Gonadotrofina coriônica.",
            "33",
            "Armazenar cálcio e fósforo; produzir hemácias e leucócitos."
            ]
    
    li = ['',0,1,2,3,4]
    x = random.choice(li[1:])
    
    ques = Label(med_frame,text =Saúde[x][0],font="calibri 12",bg="white")
    ques.place(relx=0.5,rely=0.2,anchor=CENTER)

    var = StringVar()
    
    a = Radiobutton(med_frame,text=Saúde[x][1],font="calibri 10",value=Saúde[x][1],variable = var,bg="white")
    a.place(relx=0.5,rely=0.42,anchor=CENTER)

    b = Radiobutton(med_frame,text=Saúde[x][2],font="calibri 10",value=Saúde[x][2],variable = var,bg="white")
    b.place(relx=0.5,rely=0.52,anchor=CENTER)

    c = Radiobutton(med_frame,text=Saúde[x][3],font="calibri 10",value=Saúde[x][3],variable = var,bg="white")
    c.place(relx=0.5,rely=0.62,anchor=CENTER) 

    d = Radiobutton(med_frame,text=Saúde[x][4],font="calibri 10",value=Saúde[x][4],variable = var,bg="white")
    d.place(relx=0.5,rely=0.72,anchor=CENTER) 
    
    li.remove(x)
    
    timer = Label(m)
    timer.place(relx=0.8,rely=0.82,anchor=CENTER)
    
    
    
    def display():
        
        if len(li) == 1:
                m.destroy()
                showMark(score)
        if len(li) == 2:
            proximaquest.configure(text='Fim',command=calc)
                
        if li:
            x = random.choice(li[1:])
            ques.configure(text =Saúde[x][0])
            
            a.configure(text=Saúde[x][1],value=Saúde[x][1])
      
            b.configure(text=Saúde[x][2],value=Saúde[x][2])
      
            c.configure(text=Saúde[x][3],value=Saúde[x][3])
      
            d.configure(text=Saúde[x][4],value=Saúde[x][4])
            
            li.remove(x)
            print(li)
            y = countDown()
            if y == -1:
                display()

            
    def calc():
        global score
        if (var.get() in respostas):
            score+=1
        display()
    
    submit = Button(med_frame,command=calc,text="Confirmar")
    submit.place(relx=0.5,rely=0.82,anchor=CENTER)
    
    proximaquest = Button(med_frame,command=display,text="Pular")
    proximaquest.place(relx=0.87,rely=0.82,anchor=CENTER)
    
    y = countDown()
    if y == -1:
        display()
    m.mainloop()
def difficult():
    
       
    global h
    h = Tk()
    
    hard_canvas = Canvas(h,width=720,height=440,bg="#101357")
    hard_canvas.pack()

    hard_frame = Frame(hard_canvas,bg="white")
    hard_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    
    def countDown():
        check = 0
        for k in range(10, 0, -1):
            
            if k == 1:
                check=-1
            timer.configure(text=k)
            hard_frame.update()
            time.sleep(1)
            
        timer.configure(text="O tempo acabou!")
        if check==-1:
            return (-1)
        else:
            return 0
        
    global score
    score = 0
    
    Sustentabilidade = [
                [
       "O que é sustentabilidade Social?",
        "Distribuição de renda com redução das diferenças sociais e melhoria\n"
        " da qualidade de vida.",
        "Manutenção do meio ambiente do planeta Terra.",
        "Conjunto de ações que uma empresa toma, visando o respeito ao meio ambiente.",
        "Conjunto de ações que beneficiam a sociedade e as corporações que \n"
        "são tomadas pelas empresas."
    ],
    [
        "Qual das alternativas abaixo é um exemplo de reciclagem??",
        "Acúmulo de matéria prima.",
        "Coleta Seletiva.",
        "Reutilização de matéria-prima.",
        "Incineração."
    ],
    [
     "O chamado tripé da sustentabilidade é baseado em três princípios quais são eles?",
        "Social, sentimental e ambiental.",
        "Social, ambiental e politico.",
        "Ambiental, econômico e social.",
        "Ambiental, econômico e politico."
    ],
    [
        "Sustentabilidade social tem haver com:",
        "Meio ambiente.",
        "Vida pessoal.",
        "Reciclagem de lixo.",
        "Vida social."
    ],
    [
        "Lavar louça durante 15 minutos gasta cerca de:",
        "65 garrafas pet de 2 litros.",
        "55 garrafas pet de 2 litros.",
        "45 garrafas pet de 2 litros.",
        "35 garrafas pet de 2 litros"
    ] 
            
]
    answer = [
            "Distribuição de renda com redução das diferenças sociais e melhoria da qualidade de vida.",
            "Coleta Seletiva.",
            "Ambiental, econômico e social.",
            "Vida social.",
            "55 garrafas pet de 2 litros."
            ]
    
    li = ['',0,1,2,3,4]
    x = random.choice(li[1:])
    
    ques = Label(hard_frame,text =Sustentabilidade[x][0],font="calibri 12",bg="white")
    ques.place(relx=0.5,rely=0.2,anchor=CENTER)

    var = StringVar()
    
    a = Radiobutton(hard_frame,text=Sustentabilidade[x][1],font="calibri 10",value=Sustentabilidade[x][1],variable = var,bg="white")
    a.place(relx=0.5,rely=0.42,anchor=CENTER)

    b = Radiobutton(hard_frame,text=Sustentabilidade[x][2],font="calibri 10",value=Sustentabilidade[x][2],variable = var,bg="white")
    b.place(relx=0.5,rely=0.52,anchor=CENTER)

    c = Radiobutton(hard_frame,text=Sustentabilidade[x][3],font="calibri 10",value=Sustentabilidade[x][3],variable = var,bg="white")
    c.place(relx=0.5,rely=0.62,anchor=CENTER) 

    d = Radiobutton(hard_frame,text=Sustentabilidade[x][4],font="calibri 10",value=Sustentabilidade[x][4],variable = var,bg="white")
    d.place(relx=0.5,rely=0.72,anchor=CENTER) 
    
    li.remove(x)
    
    timer = Label(h)
    timer.place(relx=0.8,rely=0.82,anchor=CENTER)
    
    
    
    def display():
        
        if len(li) == 1:
                h.destroy()
                showMark(score)
        if len(li) == 2:
            nextQuestion.configure(text='Fim',command=calc)
                
        if li:
            x = random.choice(li[1:])
            ques.configure(text =Sustentabilidade[x][0])
            
            a.configure(text=Sustentabilidade[x][1],value=Sustentabilidade[x][1])
      
            b.configure(text=Sustentabilidade[x][2],value=Sustentabilidade[x][2])
      
            c.configure(text=Sustentabilidade[x][3],value=Sustentabilidade[x][3])
      
            d.configure(text=Sustentabilidade[x][4],value=Sustentabilidade[x][4])
            
            li.remove(x)
            print(li)
            y = countDown()
            if y == -1:
                display()

            
    def calc():
        global score
        if (var.get() in answer):
            score+=1
        display()
    
    submit = Button(hard_frame,command=calc,text="Confirmar")
    submit.place(relx=0.5,rely=0.82,anchor=CENTER)

    nextQuestion = Button(hard_frame,command=display,text="Pular")
    nextQuestion.place(relx=0.87,rely=0.82,anchor=CENTER)
    
    y = countDown()
    if y == -1:
        display()
    h.mainloop()

def showMark(mark):
    global sh
    sh = Tk()
    
    show_canvas = Canvas(sh,width=720,height=440,bg="#101357")
    show_canvas.pack()

    show_frame = Frame(show_canvas,bg="white")
    show_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)
    
    st = "Você acertou "+str(mark)
    mlabel = Label(show_canvas,text=st,fg="black")
    mlabel.place(relx=0.5,rely=0.2,anchor=CENTER)
    
    sh.mainloop()
def start():
    global root 
    root = Tk()
    canvas = Canvas(root,width = 720,height = 440)
    canvas.grid(column = 0 , row = 1)
    img = PhotoImage(file="back.png")
    canvas.create_image(50,10,image=img,anchor=NW)

    button = Button(root, text='Start',command = signUpPage)
    button.configure(width = 102,height=2, activebackground = "#33B5E5", bg ='green', relief = RAISED)
    button.grid(column = 0 , row = 2)

    root.mainloop()

if __name__=='__main__':
    start()
