import flet as ft
from flet import AppBar, ElevatedButton, View

def main(page: ft.Page):
    page.title = "Un viaje a través del tiempo"
    page.bgcolor = "purple"
    page.window_width = 800
    page.window_height = 800

    img_height = 105
    img_width = 105
    border_radius = 25 

    # Audios acontecimientos
    intro=ft.Audio(src="intro.mp3", volume=1, balance=0)
    page.overlay.append(intro)
    luna=ft.Audio(src="luna.mp3", volume=1, balance=0)
    page.overlay.append(luna)
    reni=ft.Audio(src="revindu.mp3", volume=1, balance=0)
    page.overlay.append(reni)
    revc=ft.Audio(src="revcient.mp3", volume=1, balance=0)
    page.overlay.append(revc)
    org=ft.Audio(src="orgespc.mp3", volume=1, balance=0)
    page.overlay.append(org)
    imp=ft.Audio(src="imprenta.mp3", volume=1, balance=0)
    page.overlay.append(imp)
    enrg=ft.Audio(src="energia.mp3", volume=1, balance=0)
    page.overlay.append(enrg)
    compus=ft.Audio(src="compus.mp3", volume=1, balance=0)
    page.overlay.append(compus)
    albert=ft.Audio(src="albert.mp3", volume=1, balance=0)
    page.overlay.append(albert)
    adn=ft.Audio(src="adn.mp3", volume=1, balance=0)
    page.overlay.append(adn)
    #audios stem en tecnologia
    software=ft.Audio(src="software.mp3", volume=1, balance=0)
    page.overlay.append(software)
    ia=ft.Audio(src="IA.mp3", volume=1, balance=0)
    page.overlay.append(ia)
    robotica=ft.Audio(src="robotica.mp3", volume=1, balance=0)
    page.overlay.append(robotica)
    ar=ft.Audio(src="ar.mp3", volume=1, balance=0)
    page.overlay.append(ar)
    big=ft.Audio(src="big.mp3", volume=1, balance=0)
    page.overlay.append(big)
    ciberseguridad=ft.Audio(src="ciberseguridad.mp3", volume=1, balance=0)
    page.overlay.append(ciberseguridad)
    lot=ft.Audio(src="loT.mp3", volume=1, balance=0)
    page.overlay.append(lot)
    energias=ft.Audio(src="energias.mp3", volume=1, balance=0)
    page.overlay.append(energias)
    computacion=ft.Audio(src="computacion.mp3", volume=1, balance=0)
    page.overlay.append(computacion)
    #Audios stem en la sociedad y cultura
    empleo=ft.Audio(src="Empleo.mp3", volume=1, balance=0)
    page.overlay.append(empleo)
    informacion=ft.Audio(src="Informacion.mp3", volume=1, balance=0)
    page.overlay.append(informacion)
    educacion=ft.Audio(src="Educacion.mp3", volume=1, balance=0)
    page.overlay.append(educacion)
    salud=ft.Audio(src="Salud.mp3", volume=1, balance=0)
    page.overlay.append(salud)
    cultural=ft.Audio(src="ICultural.mp3", volume=1, balance=0)
    page.overlay.append(cultural)
    geograficas=ft.Audio(src="Geográficas.mp3", volume=1, balance=0)
    page.overlay.append(geograficas)
    igualdad=ft.Audio(src="Igualdad.mp3", volume=1, balance=0)
    page.overlay.append(igualdad)
    vida=ft.Audio(src="Vida.mp3", volume=1, balance=0)
    page.overlay.append(vida)
    eticos=ft.Audio(src="Éticos.mp3", volume=1, balance=0)
    page.overlay.append(eticos)
    #Audios de personajes importantes
    marie=ft.Audio(src="marie.mp3", volume=1, balance=0)
    page.overlay.append(marie)
    alan=ft.Audio(src="alan.mp3", volume=1, balance=0)
    page.overlay.append(alan)
    ada=ft.Audio(src="ada.mp3", volume=1, balance=0)
    page.overlay.append(ada)
    nikola=ft.Audio(src="nikola.mp3", volume=1, balance=0)
    page.overlay.append(nikola)
    isaac=ft.Audio(src="isaac.mp3", volume=1, balance=0)
    page.overlay.append(isaac)
    rosalind=ft.Audio(src="rosalind.mp3", volume=1, balance=0)
    page.overlay.append(rosalind)
    thomas=ft.Audio(src="thomas.mp3", volume=1, balance=0)
    page.overlay.append(thomas)
    galileo=ft.Audio(src="galileo.mp3", volume=1, balance=0)
    page.overlay.append(galileo)
    grace=ft.Audio(src="grace.mp3", volume=1, balance=0)
    page.overlay.append(grace)   
    #STEM en la educacionm
    enseñanza=ft.Audio(src="enseñanza.mp3", volume=1, balance=0)
    page.overlay.append(enseñanza)
    pensamiento=ft.Audio(src="pensamiento.mp3", volume=1, balance=0)
    page.overlay.append(pensamiento)
    colaboracion=ft.Audio(src="colaboración.mp3", volume=1, balance=0)
    page.overlay.append(colaboracion)
    tecnologia=ft.Audio(src="tecnologia.mp3", volume=1, balance=0)
    page.overlay.append(tecnologia)
    resolucion=ft.Audio(src="resolucion.mp3", volume=1, balance=0)
    page.overlay.append(resolucion)
    futuro=ft.Audio(src="futuro.mp3", volume=1, balance=0)
    page.overlay.append(futuro)
    creatividad=ft.Audio(src="creatividad.mp3", volume=1, balance=0)
    page.overlay.append(creatividad)
    cientifica=ft.Audio(src="cientifica.mp3", volume=1, balance=0)
    page.overlay.append(cientifica)
    carreras=ft.Audio(src="carreras.mp3", volume=1, balance=0)
    page.overlay.append(carreras)

    stem=ft.Audio(src="stem.mp3", volume=1, balance=0)
    page.overlay.append(stem)


    def StopAll():
        intro.pause()
        luna.pause()
        reni.pause()
        revc.pause()
        org.pause()
        imp.pause()
        enrg.pause()
        compus.pause()
        albert.pause()
        adn.pause()
        software.pause()
        ia.pause()
        ar.pause()
        big.pause()
        ciberseguridad.pause()
        computacion.pause()
        lot.pause()
        energias.pause()
        empleo.pause()
        informacion.pause()
        educacion.pause()
        salud.pause()
        cultural.pause()
        geograficas.pause()
        igualdad.pause()
        vida.pause()
        eticos.pause()
        marie.pause()
        ada.pause()
        alan.pause()
        nikola.pause()
        isaac.pause()
        rosalind.pause()
        thomas.pause()
        galileo.pause()
        grace.pause()
        enseñanza.pause()
        pensamiento.pause()
        colaboracion.pause()
        tecnologia.pause()
        resolucion.pause()
        futuro.pause()
        creatividad.pause()
        cientifica.pause()
        carreras.pause()
        stem.pause()


    def play_intro(e):
        StopAll()
        intro.play()

    def play_luna(e):
        StopAll()
        luna.play()

    def play_reni(e):
        StopAll()
        reni.play()
    
    def play_revc(e):
        StopAll()
        revc.play()

    def play_org(e):
        StopAll()
        org.play()

    def play_imp(e):
        StopAll()
        imp.play()

    def play_enrg(e):
        StopAll()
        enrg.play()

    def play_reni(e):
        StopAll()
        compus.play()

    def play_albert(e):
        StopAll()
        albert.play()

    def play_compus(e):
        StopAll()
        compus.play()
    
    def play_adn(e):
        StopAll()
        adn.play()

    def play_software(e):
        StopAll()
        software.play()

    def play_ia(e):
        StopAll()
        ia.play()

    def play_robotica(e):
        StopAll()
        robotica.play()
    
    def play_ar(e):
        StopAll()
        ar.play()

    def play_big(e):
        StopAll()
        big.play()

    def play_ciberseguridad(e):
        StopAll()
        ciberseguridad.play()

    def play_computacion(e):
        StopAll()
        computacion.play()

    def play_lot(e):
        StopAll()
        lot.play()

    def play_energias(e):
        StopAll()
        energias.play()

    def play_empleo(e):
        StopAll()
        empleo.play()
    
    def play_informacion(e):
        StopAll()
        informacion.play()

    def play_educacion(e):
        StopAll()
        educacion.play()

    def play_salud(e):
        StopAll()
        salud.play()

    def play_cultural(e):
        StopAll()
        cultural.play()
    
    def play_geograficas(e):
        StopAll()
        geograficas.play()

    def play_igualdad(e):
        StopAll()
        igualdad.play()

    def play_vida(e):
        StopAll()
        vida.play()

    def play_eticos(e):
        StopAll()
        eticos.play()

    def play_marie(compuse):
        StopAll()
        marie.play()

    def play_alan(e):
        StopAll()
        alan.play()

    def play_ada(e):
        StopAll()
        ada.play()
    
    def play_nikola(e):
        StopAll()
        nikola.play()

    def play_isaac(e):
        StopAll()
        isaac.play()

    def play_rosalind(e):
        StopAll()
        rosalind.play()

    def play_thomas(e):
        StopAll()
        thomas.play()
    
    def play_galileo(e):
        StopAll()
        galileo.play()

    def play_grace(e):
        StopAll()
        grace.play()

    def play_enseñanza(e):
        StopAll()
        enseñanza.play()

    def play_pensamiento(e):
        StopAll()
        pensamiento.play()

    def play_colaboracion(compuse):
        StopAll()
        colaboracion.play()

    def play_tecnologia(e):
        StopAll()
        tecnologia.play()

    def play_resolucion(e):
        StopAll()
        resolucion.play()
    
    def play_futuro(e):
        StopAll()
        futuro.play()

    def play_creatividad(e):
        StopAll()
        creatividad.play()

    def play_cientifica(e):
        StopAll()
        cientifica.play()
    
    def play_carreras(e):
        StopAll()
        carreras.play()

    def play_stem(e):
        StopAll()
        stem.play()

    # Botones
    btn1 = ElevatedButton(content=ft.Image(src="orespc.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="org"), on_click=play_org)
    btn2 = ElevatedButton(content=ft.Image(src="luna.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="luna"), on_click=play_luna)
    btn3 = ElevatedButton(content=ft.Image(src="crencient.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="revc"), on_click=play_revc)  
    btn4 = ElevatedButton(content=ft.Image(src="elec.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="enrg"), on_click=play_enrg)
    btn5 = ElevatedButton(content=ft.Image(src="gemhum.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="adn"), on_click=play_adn)
    btn6 = ElevatedButton(content=ft.Image(src="compu.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="compus"), on_click=play_compus)
    btn7 = ElevatedButton(content=ft.Image(src="ind.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="reni"), on_click=play_reni)
    btn8 = ElevatedButton(content=ft.Image(src="imp.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="imp"), on_click=play_imp)
    btn9 = ElevatedButton(content=ft.Image(src="albert.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="albert"), on_click=play_albert)
    btn10 = ElevatedButton(content=ft.Image(src="software.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="software"), on_click=play_software)
    btn11 = ElevatedButton(content=ft.Image(src="IA.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="ia"), on_click=play_ia)
    btn12 = ElevatedButton(content=ft.Image(src="ar.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="ar"), on_click=play_ar)
    btn13 = ElevatedButton(content=ft.Image(src="robotica.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="robotica"), on_click=play_robotica)
    btn14 = ElevatedButton(content=ft.Image(src="big.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="big"), on_click=play_big)
    btn15 = ElevatedButton(content=ft.Image(src="ciberseguridad.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="ciberseguridad"), on_click=play_ciberseguridad)
    btn16 = ElevatedButton(content=ft.Image(src="computacion.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="computacion"), on_click=play_computacion)
    btn17 = ElevatedButton(content=ft.Image(src="lot.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="lot"), on_click=play_lot)
    btn18 = ElevatedButton(content=ft.Image(src="energias.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="energias"), on_click=play_energias)
    btn19 = ElevatedButton(content=ft.Image(src="Empleo.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="empleo"), on_click=play_empleo)
    btn20 = ElevatedButton(content=ft.Image(src="Informacion.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="informacion"), on_click=play_informacion)
    btn21 = ElevatedButton(content=ft.Image(src="Educacion.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="educacion"), on_click=play_educacion)
    btn22 = ElevatedButton(content=ft.Image(src="Salud.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="salud"), on_click=play_salud)
    btn23 = ElevatedButton(content=ft.Image(src="ICultural.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="cultural"), on_click=play_cultural)
    btn24 = ElevatedButton(content=ft.Image(src="Geográficas.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="geograficas"), on_click=play_geograficas)
    btn25 = ElevatedButton(content=ft.Image(src="Igualdad.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="igualdad"), on_click=play_igualdad)
    btn26 = ElevatedButton(content=ft.Image(src="Vida.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="vida"), on_click=play_vida)
    btn27 = ElevatedButton(content=ft.Image(src="Éticos.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="eticos"), on_click=play_eticos)
    btn28 = ElevatedButton(content=ft.Image(src="marie.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="marie"), on_click=play_marie)
    btn29 = ElevatedButton(content=ft.Image(src="ada.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="ada"), on_click=play_ada)
    btn30 = ElevatedButton(content=ft.Image(src="alan.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="alan"), on_click=play_alan)
    btn31 = ElevatedButton(content=ft.Image(src="nikola.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="nikola"), on_click=play_nikola)
    btn32 = ElevatedButton(content=ft.Image(src="isaac.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="isaac"), on_click=play_isaac)
    btn33 = ElevatedButton(content=ft.Image(src="rosalind.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="rosalind"), on_click=play_rosalind)
    btn34 = ElevatedButton(content=ft.Image(src="thomas.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="thomas"), on_click=play_thomas)
    btn35 = ElevatedButton(content=ft.Image(src="galileo.tiff", width=img_width, height=img_height, border_radius=border_radius, semantics_label="galileo"), on_click=play_galileo)
    btn36 = ElevatedButton(content=ft.Image(src="grace.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="grace"), on_click=play_grace)
    btn37 = ElevatedButton(content=ft.Image(src="enseñanza.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="enseñanza"), on_click=play_enseñanza)
    btn38 = ElevatedButton(content=ft.Image(src="pensamiento.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="pensamiento"), on_click=play_pensamiento)
    btn39 = ElevatedButton(content=ft.Image(src="colaboracion.avif", width=img_width, height=img_height, border_radius=border_radius, semantics_label="colaboracion"), on_click=play_colaboracion)
    btn40 = ElevatedButton(content=ft.Image(src="tecnologia.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="tecnologia"), on_click=play_tecnologia)
    btn41 = ElevatedButton(content=ft.Image(src="resolucion.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="resolucion"), on_click=play_resolucion)
    btn42 = ElevatedButton(content=ft.Image(src="futuro.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="futuro"), on_click=play_futuro)
    btn43 = ElevatedButton(content=ft.Image(src="creatividad.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="creatividad"), on_click=play_creatividad)
    btn44 = ElevatedButton(content=ft.Image(src="cientifica.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="cientifica"), on_click=play_cientifica)
    btn45 = ElevatedButton(content=ft.Image(src="carreras.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="carreras"), on_click=play_carreras)

    def route_change(route):
        # Limpiar las vistas anteriores
        page.views.clear()

        # Vista de portada
        if page.route == '/':
            page.views.append(
                ft.View(
                    "/",
                    controls=[
                        ft.AppBar(
                            title=ft.Text("Un viaje a través del tiempo"),
                            bgcolor="purple"
                        ),
                        ft.Container(
                            ft.Column(
                                controls=[
                                    ft.ElevatedButton(
                                        'Temas que veremos',
                                        on_click=lambda _: page.go('/temas')  
                                    ),
                                    ft.Image(src="portada.png", width=400, height=200, fit=ft.ImageFit.CONTAIN),
                                    ft.Text("Integrantes del equipo:", size=24, weight="bold", color="black", text_align="center"),
                                    ft.Column(
                                        controls=[
                                            ft.Text("• Robledo Hernández Valeria"),
                                            ft.Text("• Zaragoza Villa Joselyn Esmeralda             Programación"),
                                            ft.Text("• Ruíz Ramos Alyn Dannae                        3 b"),
                                            ft.Text("• López Martínez Alison Valentina              CETIS 50"),
                                            ft.Text("• Hernández Sánchez Samuel                     Emplea framework"),
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                                spacing=10
                            ),
                            bgcolor=page.bgcolor,
                            expand=True
                        )
                    ],
                    bgcolor=page.bgcolor
                )
            )
        
        # Vista de temas
        elif page.route == '/temas':
            page.views.append(
                ft.View(
                    "/temas",
                    controls=[
                        ft.AppBar(
                            title=ft.Text("Temas que trataremos"),
                            bgcolor="purple"
                        ),
                        ft.Container(
                            ft.Column(
                                controls=[
                                     ElevatedButton(
                                        'Acontecimientos que le dan origen al STEM',
                                        on_click=lambda _: [StopAll(), page.go('/origen')]),
                                    ft.ElevatedButton(
                                        "En la tecnología, ¿Cómo se usa el STEM?",
                                        on_click=lambda _: [StopAll(), page.go('/usos'),]),
                                    ft.ElevatedButton(
                                        'La influencia de STEM en la sociedad y la cultura',
                                        on_click=lambda _: [StopAll(), page.go('/influencia')]),
                                    ft.ElevatedButton(
                                        'Personajes clave',
                                        on_click=lambda _: [StopAll(), page.go('/personajes')]),
                                    ft.ElevatedButton(
                                        'STEM en la educación',
                                        on_click=lambda _: [StopAll(), page.go('/educación')]),
                                    ElevatedButton(
                                        "Escucha el intro",
                                        on_click=play_intro
                                    ),
                                    ElevatedButton(
                                        "¿Qué es STEM?",
                                        on_click=play_stem
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER
                            ),
                            expand=True
                        )
                    ],
                    bgcolor=page.bgcolor,
                )
            )

        page.update()

        # Vista de acontecimientos
        if page.route == '/origen':
            page.views.append(
                View(
                    "/origen",
                    controls=[
                        AppBar(
                            title=ft.Text("Origen del STEM"),
                            bgcolor="gray"
                        ),
                        ft.Container(
                            ft.Column(
                                controls=[
                                    ElevatedButton(
                                        'Volver a los temas',
                                        on_click=lambda _: page.go('/temas')
                                    ),
                                    
                                    ft.Text("Han influenciado muchos acontecimientos al surgimiento del STEM, aqui te presentamos algunos de los más importantes:"),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            btn1,btn2, btn3, btn4
                                        ]
                                    ),
                                    ft.Row(
                                      alignment="center",
                                      controls=[
                                        btn5, btn6, btn7,btn8
                                      ]  
                                    ),
                                    ft.Row(
                                       alignment="center",
                                        controls=[
                                          btn9
                                        ] 
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER
                            ),
                            bgcolor=page.bgcolor,
                            expand=True
                        )
                    ]
                )
            )
        if page.route == '/usos':
            page.views.append(
                View(
                    "/usos",
                    controls=[
                        AppBar(
                            title=ft.Text("Formas de uso del STEM en la tecnología"),
                            bgcolor="yellow"
                        ),
                        ft.Container(
                            ft.Column(
                                controls=[
                                    ElevatedButton(
                                        'Volver a los temas',
                                        on_click=lambda _: page.go('/temas')
                                    ),
                                    ft.Text("El STEM tiene muchas formas de ser usado en la tecnología, aqui te mostramos las más importantes:"),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            btn10,btn11, btn12, btn13
                                        ]
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            btn14, btn15, btn16, btn17
                                        ]
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            btn18
                                        ]
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.START
                            ),
                            bgcolor=page.bgcolor,
                            expand=True
                        )
                    ]
                )
            )
        # La influencia de STEM en la sociedad y la cultura
        elif page.route == '/influencia':
            page.views.append(
                View(
                    "/influencia",
                    controls=[
                        AppBar(
                            title=ft.Text("La influencia de STEM en la sociedad y la cultura"),
                            bgcolor="orange"
                        ),
                        ft.Container(
                            ft.Column(
                                controls=[
                                    ElevatedButton(
                                        'Volver a los temas',
                                        on_click=lambda _: page.go('/temas')
                                    ),
                                    ft.Text("El impacto de STEM en la sociedad es profundo y multidimensional. No solo ha cambiado cómo trabajamos, aprendemos y nos relacionamos, sino que también ha transformado la cultura, la salud, la sostenibilidad y las estructuras sociales."),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            btn19, btn20, btn21, btn22
                                        ]
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            btn23, btn24, btn25, btn26
                                        ]
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            btn27
                                        ]
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.START
                            ),
                            bgcolor=page.bgcolor,
                            expand=True
                        )
                    ]
                )
            )
        #Personajes clave
        if page.route == '/personajes':
            page.views.append(
                View(
                    "/personajes",
                    controls=[
                        AppBar(
                            title=ft.Text("Personajes clave en el STEM"),
                            bgcolor="gray"
                        ),
                        ft.Container(
                            ft.Column(
                                controls=[
                                    ElevatedButton(
                                        'Volver a los temas',
                                        on_click=lambda _: page.go('/temas')
                                    ),
                                    
                                    ft.Text("Estos personajes no solo contribuyeron significativamente a sus respectivos campos, sino que también transformaron el mundo tal como lo conocemos hoy. Sus logros en ciencia, tecnología, ingeniería y matemáticas siguen influyendo en la sociedad moderna, y su legado inspira a generaciones de científicos, ingenieros, programadores y pensadores."),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            btn28,btn29, btn30, btn31
                                        ]
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            btn32, btn33, btn34, btn35
                                        ]
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            btn36
                                        ]
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.START
                            ),
                            bgcolor=page.bgcolor,
                            expand=True
                        )
                    ]
                )
            )
        #stem en la educación
        elif page.route == '/educación':
            page.views.append(
                View(
                    "/educación",
                    controls=[
                        AppBar(
                            title=ft.Text("STEM en la educaión"),
                            bgcolor="gray"
                        ),
                        ft.Container(
                            ft.Column(
                                controls=[
                                    ElevatedButton(
                                        'Volver a los temas',
                                        on_click=lambda _: page.go('/temas')
                                    ),
                                    
                                    ft.Text("El enfoque STEM en la educación está preparando a los estudiantes para los desafíos y las oportunidades del futuro. "),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            btn37,btn38, btn39, btn40
                                        ]
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            btn41, btn42, btn43, btn44
                                        ]
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            btn45
                                        ]
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.START
                            ),
                            bgcolor=page.bgcolor,
                            expand=True
                        )
                    ]
                )
            )        
        page.update()
    
    page.on_route_change = route_change
    page.go(page.route)

ft.app(target=main, assets_dir="assets")