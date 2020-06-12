#Instituto Tecnologico de Estudios Superiores de Monterrey
#Ricardo Adolfo González Terán
#A01769410
#Anatanael Jesús Miranda Faustino
#A01769232
#Actvidad en este programa: Solicitudes de Valores al usuario

#----IMPORTS---

import time 

#----CLASES----

class Videos():
    def __init__(self,ID="",Titulo="",Duracion=0,Calificacion=0):
        self.ID=ID
        self.Titulo=Titulo
        self.Duracion=Duracion
        self.Calificacion=Calificacion  

    def pide_datos(self):
        vi_li=[]
        v=Pide_Valor("Indica el titulo: ", ciclo="si",li=1,ls=30)
        self.Titulo=v.pide_cadena()
        v=Pide_Valor("Indica la duración: ", tipo="int",ciclo="si",li=1,ls=500)
        self.Duracion=str(v.pide_numero())
        Z=Pide_Valor("Indica la calificación: ", tipo="int",ciclo="si",li=1,ls=5)
        self.Calificacion=str(Z.pide_numero())
        vi_li.append(self.ID)
        vi_li.append(","+self.Titulo)
        vi_li.append(","+self.Duracion)
        vi_li.append(","+self.Calificacion)
        return vi_li

    def muestra_datos(self):
        print("El ID es: ", self.ID,"\nEl titulo es: ",self.Titulo,"\nla duración es: ",self.Duracion,"\nLa calificación es: ",self.Calificacion, end=" ")

class Peliculas (Videos):
    def __init__(self,ID="",Titulo="",Duracion=0,Calificacion=0,Audiencia="",Genero=""):
        super().__init__(ID,Titulo,Duracion,Calificacion)
        self.Audiencia=Audiencia
        self.Genero=Genero
     
    def pide_datos(self):
        pvi_li=super().pide_datos()
        p=Pide_Valor("Indica la audiencia: ", ciclo="si",li=1,ls=15)
        self.Audiencia=p.pide_cadena()
        p=Pide_Valor("Indica el genero: ",ciclo="si",li=1,ls=15)
        self.Genero=p.pide_cadena()
       
        pvi_li.append(","+self.Audiencia)
        pvi_li.append(","+self.Genero)
       
        return pvi_li
    def muestra_datos(self):
        super().muestra_datos()
        print("\nLa audiencia para esta serie es: ",self.Audiencia,"\nLa genero para esta serie es: ",self.Genero, end=" ")

class Serie (Peliculas):
    def __init__(self,ID="",Titulo="",Duracion=0,Calificacion=0,Audiencia="",Genero="",Temporada=0,Episodio=0,Til_episodio=""):
        super().__init__(ID,Titulo,Duracion,Calificacion,Audiencia,Genero)
        self.Temporada=Temporada
        self.Episodio=Episodio
        self.Til_episodio=Til_episodio

    def pide_datos(self):
        s_lis=super().pide_datos()
    
        
        s=Pide_Valor("¿Cual es la temporada?: ", tipo="int",ciclo="si",li=1,ls=500)
        self.Temporada=str(s.pide_numero())
        s=Pide_Valor("Indica numero de episodio: ", tipo="int",ciclo="si",li=1,ls=500)
        self.Episodio=str(s.pide_numero())
        s=Pide_Valor("Indica el titulo del episodio : ",ciclo="si",li=1,ls=30)
        self.Til_episodio=str(s.pide_cadena())
        
        s_lis.append(","+self.Temporada)
        s_lis.append(","+self.Episodio)
        s_lis.append(","+self.Til_episodio)
        return s_lis

    def muestra_datos(self):
        super().muestra_datos()
        print("\nLa temporada es: ",self.Temporada,"\nEl episodio es: ",self.Episodio,"\nEl tilulo del episodio es: ",self.Til_episodio, end=" ")

class Documental (Serie):
    def __init__(self,ID,Titulo="",Duracion=0,Calificacion=0,Audiencia="",Genero="",Temporada=0,Episodio=0,Til_episodio="",Tema=""):
        super().__init__(ID,Titulo,Duracion,Calificacion,Audiencia,Genero,Temporada,Episodio,Til_episodio)
        self.Tema=Tema
     
    def pide_datos(self):
        d_lis=super().pide_datos()
        d=Pide_Valor("Tema : ",ciclo="si",li=1,ls=30)
        self.Tema=str(d.pide_cadena())
        
        d_lis.append(","+self.Tema)

        return d_lis


    def muestra_datos(self):
        super().muestra_datos()
        print("\nEl tema del documental es: ", self.Tema)

class Validaciones():

    def __init__(self, lim_sup = "", lim_in = "", tipo = "", opciones_menu = ""):
        self.lim_sup = lim_sup
        self.lim_in = lim_in
        self. tipo = tipo
        self.opciones_menu = opciones_menu

    def validar_opcion_menu(self):
            
        while 1:
            opcion = input("->")
            try:
                while 1:     
                    opcion = int(opcion)
                    if opcion>=1 and opcion <=self.opciones_menu:  
                        return   opcion
                    else:
                        print("Numero de opción no valida (ERRx002)")
                        break                          
            except ValueError:
                print("La opcion seleccionada no es un numero (ERRx001)")

    def validacion_del_id(self, usuario_id):

        while 1:

            validar_id=usuario_id
            id_contenido=validar_id.upper()
            id_contenido=id_contenido[0]
            if id_contenido == "P" or id_contenido == "S":
                break
            elif id_contenido == "D":
                break
            else:
                print("No se pudo determinar el tipo de contenido\n Ingrese nuevamente el ID recuerde que el primer caracter debe ser P, S ó D: ")
                while 1:

                    validar__id=Pide_Valor("Cual es el ID: ",5,5,ciclo="si")
                    validar_id=validar__id.pide_cadena()
                    id_contenido=validar_id.upper()
                    id_contenido=id_contenido[0]
                    if id_contenido == "P" or id_contenido == "S":
                        break
                    elif id_contenido == "D":
                        break
                    else:
                        print("No se pudo determinar el tipo de contenido\n Ingrese nuevamente el ID recuerde que el primer caracter debe ser P, S ó D")
                        pass
                break

                
                
        while 1:

            #Validacion de la clasificación
            
            clasif_contenido = validar_id[1]
            clasif_contenido= clasif_contenido.upper()

            if clasif_contenido == "A" or clasif_contenido == "B":
                break
            elif clasif_contenido == "C" or clasif_contenido == "D":
                break
            else:
                print("No se pudo determinar la clasificacion del contenido\n")
                while 1:
                    #Validacion de la clasificación
                
                    clasif_contenido =input("Rescribe el segundo caracter de tu ID, Recuerda que debe de estar entre A, B, C ó D\n ->")
                    clasif_contenido= clasif_contenido.upper()
                    if clasif_contenido == "A" or clasif_contenido == "B":
                        validar_id=validar_id[0]+clasif_contenido+validar_id[2:5]
                        break
                    elif clasif_contenido == "C" or clasif_contenido == "D":
                        validar_id=validar_id[0]+clasif_contenido+validar_id[2:5]
                        break
                    else:
                        print("No se pudo determinar la clasificacion del contenido\n")
                break
        while 1:
            validar_nuid=validar_id[2:5]
            if not validar_nuid.isnumeric():
                print("Detectado que los ultimos 3 valores del ID no son numericos:  ")
                numerid_id=Pide_Valor("Debe de ingresar los ultimos tres digitos de su ID, recuerde que estos deben ser Numericos: ",li=100,ls=999,ciclo="si",tipo="int")
                numer_id=str(numerid_id.pide_numero())
                validar_id=validar_id[0]+validar_id[1]+str(numer_id)
                break
            else:
                break

        return validar_id

class CSV():

    def leer(self,archive):
        name_file=archive
        file_=open(name_file+".csv","r")
        _datos_lec=file_.readlines()
        _datos_lec.pop(0)
        file_.close()
        return _datos_lec
    
    
    def crear(self):
        print("Se creo un CSV con el nombre \"videos\"")
        name_file="Videos"
        file_=open(name_file+".csv","w")
        file_.write("ID"+",Titulo"+",Duración"+",Calificación"+",Audiencia"+",Genero"+",Temporada"+",Episodio"+",Titulo del episodio"+",Tema"+"\n")
        file_.close()
        
        return name_file
        

    def escribir(self,lectura,x,name): 
        file_=lectura
        
        x=x
        x.append("\n")

        file_list=file_+x
        _file_=open(name+".csv","w+")
        _file_.write("ID"+",Titulo"+",Duración"+",Calificación"+",Audiencia"+",Genero"+",Temporada"+",Episodio"+",Titulo del episodio"+",Tema"+"\n")
        for i in range (len (file_list)):
            _file_.write(file_list[i])
        _file_.close()
    
    def buscar(self, id_):
        for key in general_dic.keys():
            for key_2 in general_dic[key].keys():
                for valor in general_dic[key][key_2].values():
                    if valor.ID == id_ :
                        return "X"

class Pide_Valor():
    def __init__(self, letrero, li=0, ls=0, ciclo="no", tipo="float"):
        self.letrero=letrero
        self.li=li
        self.ls=ls
        self.ciclo=ciclo.upper()
        self.tipo=tipo

    def __del__(self):
        pass

    def error(self):
        input(self.letrero)

    def pide_cadena(self):
        while True:
            cad=input(self.letrero)
            if (self.ciclo=="NO"): return cad
            else:
                if (self.li==0) and (self.ls==0): return cad
                else:
                    if len(cad)<self.li or len(cad)>self.ls:
                        er="Error, la cadena debe estar entre "+str(self.li)+" y "+str(self.ls)+" caracteres ..."
                        oe=Pide_Valor(er)
                        oe.error()
                        del oe
                    else: return cad
        # Termina ciclo while true
    # termina pide_cadena

    def pide_numero(self):
        while True:
            cad=input(self.letrero)
            if not cad.isnumeric():
                oe=Pide_Valor("Error, la cadena contiene caracteres no validos ...")
                oe.error()
                del oe
            else:
                if self.tipo=="int" : numero=int(cad)
                else: numero=float(cad)
                if self.ciclo=="NO": return numero
                else:
                    if (self.li==0) and (self.ls==0): return numero
                    else:
                        if numero<self.li or numero>self.ls:
                            er="Error, valor fuera de rango entre "+str(self.li)+" y "+str(self.ls)+" ..."
                            oe=Pide_Valor(er)
                            oe.error()
                            del oe
                        else : return numero

class Valores_usuario():
    def menu_op1(self):

        while True:
            val_id=Pide_Valor("¿Cual es el ID?",5,5,ciclo="si")
            id_usuario=val_id.pide_cadena()
            id_completo = Validaciones().validacion_del_id(id_usuario)
            id_completo=id_completo.upper()
            search = CSV()
            searched = search.buscar(id_completo)
            if searched == "X":
                print("El ID ingresado esta duplicado, intentelo de nuevo")
            else:
                break
        
        if id_completo[0] == "P":
            peili= Peliculas(id_completo)
            x=peili.pide_datos()
            x.append(",,,,")
        
        elif id_completo[0] == "S":
            peili= Serie(id_completo)
            x=peili.pide_datos()
            x.append(",")
        
        elif id_completo[0] == "D":
            peili= Documental(id_completo)
            x=peili.pide_datos()
        
        return x 
    
    
    
    def tomar_limites_(self):
        limite_infe=int(input("Desde que calificación quiere visualizar  ")) 

        limite_supe=int(input("¿Cual es limite? ")) 

        return limite_infe,limite_supe

    def tomar_id(self):
        print("Ingrese el ID que desea buscar: ")
        id_name = str(input("-->"))
        return id_name
    
    def tomar_titulo(self):
        print("Ingrese el titulo que desea buscar: ")
        title = str(input("-->"))
        return title
    
    def tomar_genero(self):
        print("Ingrese el genero que desea buscar: ")
        genre = str(input("-->"))
        return genre

class Archivadora():

    def archivadora_general (self,archivo):

        readline_archi=CSV().leer(archivo)
        global general_dic
        general_dic={}
        n=0
        for line in readline_archi:
            fields = line.split(",") 
            id = fields[0]
            titulo=fields[1]
            genero=fields[2]
            duración=fields[3]
            calificaci=fields[4]
            audien=fields[5]
            temporada=fields[6]
            episodio=fields[7]
            til_epi=fields[8]
            tema=fields[9]
            cla=id[1]
            id_key=id[0]
            cla=cla.lower()
            id_key=id_key.lower()
            if id_key =="p":
                x=self.archivar_peliculas(id,titulo, genero,duración,calificaci,audien)

            elif id_key == "s": 
                x=self.archivar_series(id,titulo, genero,duración,calificaci,audien,temporada,episodio,til_epi)
            
            elif id_key =="d":
                x=self.archivar_documentales(id,titulo, genero,duración,calificaci,audien,temporada,episodio,til_epi,tema)
            
            general_dic[n]=x
            n=n+1
        return general_dic
     
         
    def archivar_peliculas(self,id,titulo, genero,duración,calificaci,audien):
        global peliculas 
        peliculas={}
        peli_clasi={}
        cla=id[1]
        id_key=id[0]
        peliculon=Peliculas(id,titulo,genero,duración,calificaci,audien)
        peli_clasi[cla]=peliculon
        peliculas[id_key]=peli_clasi


        return peliculas

    
    def archivar_series(self,id_key_ser,titulo,genero,duración,calificaci,audien,temporada,episodio,til_epi):


        global serie_dic
        serie_dic={}
        serie_cla={}
        serie_obj=Serie(id_key_ser,titulo,genero,duración,calificaci,audien,temporada,episodio,til_epi)
        cla=id_key_ser[1]
    
        id_key__serie=id_key_ser[0]

       
        serie_cla[cla]=serie_obj
        serie_dic[id_key__serie]=serie_cla
        
        return serie_dic
           
    
    def archivar_documentales(self,id,titulo,genero,duración,calificaci,audien,temporada,episodio,til_epi,tema):
        global archivar_documentales_dic
        archivar_documentales_dic={}
        document_cla={}
        document_obj=Documental(id,titulo,genero,duración,calificaci,audien,temporada,episodio,til_epi,tema)
        key=id[1]
        id_key=id[0]
        document_cla[key]=document_obj
        archivar_documentales_dic[id_key]=document_cla
        return  archivar_documentales_dic
        #time.sleep(4)
        
        
            #documental=

class Mostrar_listas():

    def lista_general(self,op,busquedas):
        if op==1:
            for key in  general_dic.keys():
                for key_2da in general_dic[key].keys():
                    for valor in general_dic[key][key_2da].values():
                        if busquedas == key_2da:
                            print("-"*37)
                            valor.muestra_datos()
                            print("\n"+"-"*37)
                            time.sleep(1)
                            
        elif op==2:
            for key in  general_dic.keys():
                for key_2da in general_dic[key].keys():
                    for valor in general_dic[key][key_2da].values():
                        print("-"*37)
                        valor.muestra_datos()
                        print("\n"+"-"*37)
                        time.sleep(1)

        elif op==8:
            limite_inf_cal,limite_superior_cal=Valores_usuario().tomar_limites_()
            for key in  general_dic.keys():
                for key_2da in general_dic[key].keys():
                    for valor in general_dic[key][key_2da].values():
                        if int(valor.Calificacion) >=limite_inf_cal and int(valor.Calificacion)<= limite_superior_cal: 
                            
                            print("-"*37)
                            valor.muestra_datos()
                            print("\n"+"-"*37)
                
                            time.sleep(1.2)
        
        elif op == 3:

            while True:

                request = Valores_usuario()
                request = request.tomar_titulo()

                for key in general_dic.keys():
                    for key_2 in general_dic[key].keys():
                        for valor in general_dic[key][key_2].values():
                            if request in valor.Titulo:
                                print("-"*37)
                                valor.muestra_datos()
                                print("\n"+"-"*37)
                                time.sleep(1.5)
                
                print("Desea buscar otro titulo?")
                print("1. Si")
                print("2. Regresar al menú principal")
                option = Validaciones("","","",2)
                option = option.validar_opcion_menu()

                if option == 1:
                    pass
                if option == 2:
                    break

        elif op == 4:

            while True:

                request = Valores_usuario()
                request = request.tomar_genero()

                for key in general_dic.keys():
                    for key_2 in general_dic[key].keys():
                        for valor in general_dic[key][key_2].values():
                            if request in valor.Genero:
                                print("-"*37)
                                valor.muestra_datos()
                                print("\n"+"-"*37)
                                time.sleep(1.5)

                                
                print("Desea buscar otro genero?")
                print("1. Si")
                print("2. Regresar al menú principal")
                option = Validaciones("","","",2)
                option = option.validar_opcion_menu()

                if option == 1:
                    pass
                if option == 2:
                    break
  
class Consultas():

    def consulta_por_id(self):

        while True:
       
            identifier = Valores_usuario()
            id_name = identifier.tomar_id()
            search = CSV()
            search = search.buscar(id_name)
            if search == "X":
                for key in general_dic.keys():
                    for key_2 in general_dic[key].keys():
                        for valor in general_dic[key][key_2].values():
                            if valor.ID == id_name :
                                print("-"*37)
                                valor.muestra_datos()
                                print("\n"+"-"*37)
            else: 
                print("-"*37)
                print("No se encontro el ID solicitado")
                print("-"*37)

            print("Desea buscar otro ID?")
            print("1. Si")
            print("2. Regresar al menú principal")
            option = Validaciones("","","",2)
            option = option.validar_opcion_menu()

            if option == 1:
                pass
            if option == 2:
                break
        
    
