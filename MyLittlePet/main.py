import flet as ft
from flet import *
from config import *
from ui.components import create_chat_layout


class Message:
    def __init__(self, user: str, text: str, message_type: str):
        self.user = user
        self.text = text
        self.message_type = message_type


def main(page: ft.Page):
    def route_change(e):
        page.views.clear()
        if e.route == "/":
            page.views.append(
                ft.View(
                    "/",
                    controls=[
                        ft.Stack(
                            controls=[
                                ft.Container(
                                    width=287,
                                    height=585,
                                    bgcolor="#FFDD78",
                                ),
                                ft.Column(
                                    controls=[
                                        ft.CircleAvatar(
                                            foreground_image_src="https://i.postimg.cc/pTCt4Mwv/Blue-Modern-Minimal-Pet-Clinic-Logo-3.png",
                                            width=156,
                                            height=151,
                                        ),
                                        ft.CupertinoButton(
                                            "Login",
                                            color="white",
                                            bgcolor=ft.colors.BROWN_500,
                                            width=200,
                                            border_radius=25,
                                            on_click=lambda _: page.go(
                                                "/login"),
                                        ),
                                        ft.CupertinoButton(
                                            "Cadastro",
                                            color="white",
                                            bgcolor=ft.colors.BROWN_500,
                                            width=200,
                                            border_radius=25,
                                            on_click=lambda _: page.go(
                                                "/cadastro"),
                                        ),
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    spacing=20,
                                ),
                            ],
                            expand=True,
                            width=BG_WIDTH,
                            height=BG_HEIGHT,
                            alignment=ft.alignment.center,
                        ),
                    ],
                )
            )

        elif e.route == "/cadastro":
            width_inner = 287
            height_inner = 505
            button_width = 200
            button_height = 79
            spacing = (height_inner - (2 * button_height)) // 3
            side_margin = (width_inner - button_width) // 2
            page.views.append(
                ft.View(
            "/cadastro",
            controls=[
                ft.Stack(
                    controls=[
                        ft.Container(
                            width=287,
                            height=585,
                            bgcolor="#FFDD78",
                        ),
                        ft.Container(
                            width=width_inner,
                            height=height_inner,
                            bgcolor="#C2690A",
                            border_radius=12,
                            alignment=ft.alignment.center,
                        ),
                        ft.Container(
                            width=button_width,
                            height=button_height,
                            border_radius=25,
                            bgcolor="#779030",
                            top=spacing,
                            left=side_margin,
                            content=ft.Text(
                                "Sou Pai/Mãe de Pet",
                                size=24,
                                weight=ft.FontWeight.W_400,
                                color=ft.colors.WHITE,
                                text_align=ft.TextAlign.CENTER,
                            ),
                            # Função para navegação para "/cadastro_contratante"
                            on_click=lambda e: page.go(
                                "/cadastro_contratante"),
                        ),
                        ft.Container(
                            width=button_width,
                            height=button_height,
                            border_radius=25,
                            bgcolor="#779030",
                            top=spacing + button_height + spacing,
                            left=side_margin,
                            content=ft.Text(
                                "Estou Aqui Para Pets",
                                size=24,
                                weight=ft.FontWeight.W_400,
                                color=ft.colors.WHITE,
                                text_align=ft.TextAlign.CENTER,
                            ),
                            # Função para navegação para "/cadastro"
                            on_click=lambda e: page.go("/cadastro_contratado"),
                        ),
                    ],
                    alignment=ft.alignment.center,
                    expand=True,
                ),
            ],
                )
        )
    

        elif e.route == "/cadastro_contratante":
            page.views.append(
                ft.View(
                    "/cadastro_contratante",
                    controls=[
                ft.Container(
                    content=ft.Text(
                        "Sou Contratante",
                        weight=ft.FontWeight.BOLD,
                        color='white',
                        text_align='center',
                        size=15,
                    ),
                    bgcolor='#788C30',
                    width=150,
                    border_radius=25,
                    height=40,
                    padding=ft.Padding(top=10, right=10, bottom=10, left=10),
                ),
                ft.Container(
                    content=ft.Column(
                        [
                            ft.TextField(
                                label="Nome Completo",
                                width=400,
                                height=40,
                                label_style=ft.TextStyle(color='#B0B0B0'),
                                bgcolor='#F0F0F0',
                                content_padding=ft.Padding(
                                    top=10, right=10, bottom=10, left=10),
                            ),
                            ft.TextField(
                                label="RG",
                                width=400,
                                height=40,
                                label_style=ft.TextStyle(color='#B0B0B0'),
                                bgcolor='#F0F0F0',
                                content_padding=ft.Padding(
                                    top=10, right=10, bottom=10, left=10),
                            ),
                            ft.Dropdown(
                                label="Tipo de Pet",
                                icon_enabled_color='black',
                                options=[
                                    ft.dropdown.Option("Cão"),
                                    ft.dropdown.Option("Gato"),
                                ],
                                width=300,
                                height=40,
                                bgcolor='#F0F0F0',
                                color='black',
                            ),
                            ft.Container(
                                content=ft.Text(
                                    "Dados bancários:",
                                    weight=ft.FontWeight.BOLD,
                                    color='white',
                                    text_align='center',
                                    size=15,
                                ),
                                bgcolor='#788C30',
                                width=150,
                                border_radius=25,
                                height=40,
                                padding=ft.Padding(
                                    top=10, right=10, bottom=10, left=10),
                            ),
                            ft.TextField(
                                label="Número do banco",
                                width=400,
                                height=40,
                                label_style=ft.TextStyle(color='#B0B0B0'),
                                bgcolor='#F0F0F0',
                                content_padding=ft.Padding(
                                    top=10, right=10, bottom=10, left=10),
                            ),
                            ft.TextField(
                                label="Agência",
                                width=400,
                                height=40,
                                label_style=ft.TextStyle(color='#B0B0B0'),
                                bgcolor='#F0F0F0',
                                content_padding=ft.Padding(
                                    top=10, right=10, bottom=10, left=10),
                            ),
                            ft.TextField(
                                label="Conta",
                                width=400,
                                height=40,
                                label_style=ft.TextStyle(color='#B0B0B0'),
                                bgcolor='#F0F0F0',
                                content_padding=ft.Padding(
                                    top=10, right=10, bottom=10, left=10),
                            ),
                            ft.TextField(
                                label="Senha",
                                password=True,
                                can_reveal_password=True,
                                height=40,
                                width=400,
                                label_style=ft.TextStyle(color='#B0B0B0'),
                                bgcolor='#F0F0F0',
                                content_padding=ft.Padding(
                                    top=10, right=10, bottom=10, left=10),
                            ),
                            ft.ElevatedButton(
                                text="Cadastro",
                                width=120,
                                height=40,
                                bgcolor='#788C30',
                                color='#232624',
                                on_click=cadastrar,
                            ),
                            ft.Text("", color=ft.colors.GREEN),
                            ft.Row(
                                controls=[
                                    ft.Text("Já tem uma conta?",
                                            color=ft.colors.BLACK),
                                    ft.GestureDetector(
                                        content=ft.Text(
                                            "Logar",
                                            color=ft.colors.BLUE,
                                            weight=ft.FontWeight.BOLD,
                                        ),
                                        on_tap=lambda e: page.go("/login"),
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=10,
                    ),
                    width=500,
                    padding=20,
                    bgcolor="#BF5F0B",
                    border_radius=20,
                    shadow=ft.BoxShadow(
                        spread_radius=2,
                        blur_radius=10,
                        color=ft.colors.BLACK12,
                        offset=ft.Offset(4, 4),
                    ),
                    alignment=ft.alignment.center,
                ),
            ],
                    )
                )

        elif e.route == "/cadastro_contratado":
            page.views.append(
                ft.View(
            "/cadastro_contratado",
            controls=[
                ft.Container(
                    content=ft.Text(
                        "Sou Contratatado",
                        weight=ft.FontWeight.BOLD,
                        color='white',
                        text_align='center',
                        size=15,
                    ),
                    bgcolor='#788C30',
                    width=150,
                    border_radius=25,
                    height=40,
                    padding=ft.Padding(top=10, right=10, bottom=10, left=10),
                ),
                ft.Container(
                    content=ft.Column(
                        [
                            ft.TextField(
                                label="Nome Completo",
                                width=400,
                                height=40,
                                label_style=ft.TextStyle(color='#B0B0B0'),
                                bgcolor='#F0F0F0',
                                content_padding=ft.Padding(
                                    top=10, right=10, bottom=10, left=10),
                            ),
                            ft.TextField(
                                label="RG",
                                width=400,
                                height=40,
                                label_style=ft.TextStyle(color='#B0B0B0'),
                                bgcolor='#F0F0F0',
                                content_padding=ft.Padding(
                                    top=10, right=10, bottom=10, left=10),
                            ),
                            ft.Dropdown(
                                label="Serviço ofertado",
                                icon_enabled_color='black',
                                options=[
                                    ft.dropdown.Option("Banho"),
                                    ft.dropdown.Option("Tosa"),
                                ],
                                width=300,
                                height=40,
                                bgcolor='#F0F0F0',
                                color='black',
                            ),
                            ft.Container(
                                content=ft.Text(
                                    "Dados bancários:",
                                    weight=ft.FontWeight.BOLD,
                                    color='white',
                                    text_align='center',
                                    size=15,
                                ),
                                bgcolor='#788C30',
                                width=150,
                                border_radius=25,
                                height=40,
                                padding=ft.Padding(
                                    top=10, right=10, bottom=10, left=10),
                            ),
                            ft.TextField(
                                label="Número do banco",
                                width=400,
                                height=40,
                                label_style=ft.TextStyle(color='#B0B0B0'),
                                bgcolor='#F0F0F0',
                                content_padding=ft.Padding(
                                    top=10, right=10, bottom=10, left=10),
                            ),
                            ft.TextField(
                                label="Agência",
                                width=400,
                                height=40,
                                label_style=ft.TextStyle(color='#B0B0B0'),
                                bgcolor='#F0F0F0',
                                content_padding=ft.Padding(
                                    top=10, right=10, bottom=10, left=10),
                            ),
                            ft.TextField(
                                label="Conta",
                                width=400,
                                height=40,
                                label_style=ft.TextStyle(color='#B0B0B0'),
                                bgcolor='#F0F0F0',
                                content_padding=ft.Padding(
                                    top=10, right=10, bottom=10, left=10),
                            ),
                            ft.TextField(
                                label="Senha",
                                password=True,
                                can_reveal_password=True,
                                height=40,
                                width=400,
                                label_style=ft.TextStyle(color='#B0B0B0'),
                                bgcolor='#F0F0F0',
                                content_padding=ft.Padding(
                                    top=10, right=10, bottom=10, left=10),
                            ),
                            ft.ElevatedButton(
                                text="Cadastro",
                                width=120,
                                height=40,
                                bgcolor='#788C30',
                                color='#232624',
                                on_click=cadastrar,
                            ),
                            ft.Text("", color=ft.colors.GREEN),
                            ft.Row(
                                controls=[
                                    ft.Text("Já tem uma conta?",
                                            color=ft.colors.BLACK),
                                    ft.GestureDetector(
                                        content=ft.Text(
                                            "Logar",
                                            color=ft.colors.BLUE,
                                            weight=ft.FontWeight.BOLD,
                                        ),
                                        on_tap=lambda e: page.go("/login"),
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=10,
                    ),
                    width=500,
                    padding=20,
                    bgcolor="#BF5F0B",
                    border_radius=20,
                    shadow=ft.BoxShadow(
                        spread_radius=2,
                        blur_radius=10,
                        color=ft.colors.BLACK12,
                        offset=ft.Offset(4, 4),
                    ),
                    alignment=ft.alignment.center,
                ),
            ],
        )
                )

        elif e.route == "/login":
            page.views.append(
                ft.View(
                    "/login",
                    controls=[
                        ft.Stack(
                            expand=True,
                            controls=[
                                ft.Container(
                                    bgcolor="#73513D",
                                    width=BG_WIDTH,
                                    height=BG_HEIGHT,
                                ),
                                ft.Container(
                                    width=245,
                                    height=505,
                                    bgcolor="#C2690A",
                                    border_radius=12,
                                    alignment=ft.alignment.center,
                                ),
                                ft.Container(
                                    top=20,
                                    left=50,
                                    content=ft.Column(
                                        controls=[
                                            ft.Container(
                                                width=157,
                                                height=46,
                                                border_radius=20,
                                                bgcolor="#779030",
                                                content=ft.Column(
                                                    controls=[
                                                        ft.Text("Login", color="white", size=24)],
                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                                ),
                                            ),
                                        ],
                                        alignment=ft.MainAxisAlignment.START,
                                        spacing=10,
                                    ),
                                ),
                                ft.Container(
                                    top=80,
                                    left=20,
                                    right=20,
                                    alignment=ft.alignment.center,
                                    content=ft.Column(
                                        controls=[
                                            ft.Text(
                                                "Email", color="white", size=20),
                                            ft.TextField(
                                                width=205.97,
                                                height=35,
                                                border_radius=5,
                                                bgcolor="white",
                                                color="black",
                                            ),
                                            ft.Text(
                                                "Senha", color="white", size=20),
                                            ft.TextField(
                                                width=205.97,
                                                height=35,
                                                border_radius=5,
                                                bgcolor="white",
                                                color="black",
                                            ),
                                        ],
                                        alignment=ft.MainAxisAlignment.START,
                                        spacing=10,
                                    ),
                                ),
                                ft.Container(
                                    top=230,
                                    left=10,
                                    right=10,
                                    alignment=ft.alignment.center,
                                    content=ft.Column(
                                        controls=[
                                            ft.TextButton(
                                                "Esqueceu a sua senha?",
                                                style=ft.ButtonStyle(
                                                    color="#000000"),
                                            ),
                                            ft.Row(
                                                controls=[
                                                    ft.Text(
                                                        "Não tem uma conta ainda?", size=10, weight=ft.FontWeight.W_400, color="#000000"),
                                                    ft.TextButton(
                                                        "Registrar agora",
                                                        style=ft.ButtonStyle(
                                                            color=ft.colors.GREY,
                                                            bgcolor="#C2690A",
                                                            padding=ft.Padding(
                                                                top=0, right=0, bottom=0, left=1),
                                                        ),
                                                        on_click=lambda _: page.go(
                                                            "/cadastro"),
                                                    ),
                                                ],
                                                alignment=ft.MainAxisAlignment.START,
                                                spacing=10,
                                            ),
                                        ],
                                        alignment=ft.MainAxisAlignment.START,
                                        spacing=10,
                                    ),
                                ),
                                ft.Container(
                                    top=350,
                                    left=20,
                                    right=20,
                                    alignment=ft.alignment.center,
                                    content=ft.ElevatedButton(
                                        content=ft.Text("Google"),
                                        on_click=lambda e: None,
                                        bgcolor=ft.colors.WHITE,
                                        color="red",
                                        width=207,
                                        height=40,
                                        style=ft.ButtonStyle(
                                            text_style=ft.TextStyle(
                                                size=15, weight=ft.FontWeight.W_700)
                                        ),
                                    ),
                                ),
                                ft.Container(
                                    top=400,
                                    left=20,
                                    right=20,
                                    alignment=ft.alignment.center,
                                    content=ft.ElevatedButton(
                                        content=ft.Text("Facebook"),
                                        on_click=lambda e: None,
                                        bgcolor=ft.colors.WHITE,
                                        color="blue",
                                        width=207,
                                        height=40,
                                        style=ft.ButtonStyle(
                                            text_style=ft.TextStyle(
                                                size=15, weight=ft.FontWeight.W_700)
                                        ),
                                    ),
                                ),
                                ft.Container(
                                    top=450,
                                    left=50,
                                    right=50,
                                    alignment=ft.alignment.center,
                                    content=ft.ElevatedButton(
                                        content=ft.Icon(ft.icons.PLAY_ARROW),
                                        on_click=lambda e: page.go(
                                            "/tela_inicial"),
                                        bgcolor="#779030",
                                        color="black",
                                        width=136,
                                        height=38,
                                    ),
                                ),
                            ],
                            alignment=ft.alignment.center,
                        ),
                    ],
                )
            )

        elif e.route == "/tela_inicial":
            page.views.append(
                ft.View(
                    "/tela_inicial",
                    controls=[
                        ft.Stack(
                            controls=[
                                ft.Container(
                                    bgcolor="#73513D",
                                    width=287.38,
                                    height=450,
                                    border_radius=20,
                                    alignment=ft.alignment.center,
                                    margin=ft.margin.only(top=70),
                                ),
                                ft.Container(
                                    top=20,
                                    left=65,
                                    right=65,
                                    alignment=ft.alignment.center,
                                    content=ft.Container(
                                        content=ft.Text(
                                            "Tela Inicial",
                                            weight=ft.FontWeight.BOLD,
                                            color="white",
                                            text_align="center",
                                            size=15,
                                        ),
                                        bgcolor="#8C5120",
                                        padding=ft.padding.symmetric(
                                            horizontal=20, vertical=10),
                                        border_radius=50,
                                    ),
                                ),
                                ft.Container(
                                    top=100,
                                    left=20,
                                    right=20,
                                    alignment=ft.alignment.center,
                                    content=ft.ElevatedButton(
                                        text="Ver Serviços Agendados",
                                        width=200,
                                        height=80,
                                        style=ft.ButtonStyle(
                                            shape=ft.RoundedRectangleBorder(
                                                radius=25),
                                            bgcolor="#779030",
                                            text_style=ft.TextStyle(
                                                weight=ft.FontWeight.W_400,
                                                size=24,
                                                color="#FFFFFF",
                                            ),
                                        ),
                                        on_click=lambda e: print("Button clicked") or page.go(
                                            "/servicos_agendados"),
                                    ),
                                ),
                                ft.Container(
                                    top=200,
                                    left=20,
                                    right=20,
                                    alignment=ft.alignment.center,
                                    content=ft.ElevatedButton(
                                        text="Ver Horários Agendados",
                                        width=200,
                                        height=80,
                                        style=ft.ButtonStyle(
                                            shape=ft.RoundedRectangleBorder(
                                                radius=25),
                                            bgcolor="#779030",
                                            text_style=ft.TextStyle(
                                                weight=ft.FontWeight.W_400,
                                                size=24,
                                                color="#FFFFFF",
                                            ),
                                        ),
                                        on_click=None,
                                    ),
                                ),
                                ft.Container(
                                    top=300,
                                    left=20,
                                    right=20,
                                    alignment=ft.alignment.center,
                                    content=ft.ElevatedButton(
                                        text="Contrate Um Serviço",
                                        width=200,
                                        height=80,
                                        style=ft.ButtonStyle(
                                            shape=ft.RoundedRectangleBorder(
                                                radius=25),
                                            bgcolor="#779030",
                                            text_style=ft.TextStyle(
                                                weight=ft.FontWeight.W_400,
                                                size=24,
                                                color="#FFFFFF",
                                            ),
                                        ),
                                        on_click=None,
                                    ),
                                ),
                                navigation_bar,
                            ],
                            width=BG_WIDTH,
                            height=BG_HEIGHT,
                            expand=True,
                        ),
                    ],
                )
            )

        elif e.route == "/servicos_agendados":
            page.views.append(
                ft.View(
                    "/servicos_agendados",
                    controls=[
                        ft.Stack(
                            controls=[
                                # Background
                                ft.Container(
                                    bgcolor="#73513D",
                                    width=BG_WIDTH,
                                    height=460,
                                    border_radius=20,
                                    margin=ft.margin.only(top=50),
                                ),
                                # Column for service buttons
                                ft.Column(
                                    controls=[
                                        create_button("Lucas Silva da Costa", "/descricao_servico"),
                                        create_button("Ana Clara Macedo", "/descricao_servico"),
                                        create_button("Julia Soares Silva", "/descricao_servico"),
                                        create_button("Luiz Mariano Marcos", "/descricao_servico"),
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    spacing=5,
                                    expand=True,
                                ),
                                # Navigation row
                                ft.Row(
                                    controls=[
                                        ft.IconButton(
                                            icon=ft.icons.ARROW_BACK,
                                            icon_size=30,
                                            on_click=lambda e: page.go("/tela_inicial"),
                                            icon_color="black",
                                        ),
                                        ft.Container(
                                            content=ft.Text(
                                                "Serviços Agendados",
                                                weight=ft.FontWeight.BOLD,
                                                color="white",
                                                text_align="center",
                                                size=15,
                                            ),
                                            padding=ft.padding.only(
                                                left=20, right=20, top=10, bottom=10
                                            ),
                                            bgcolor="#8C5120",
                                            border_radius=50,
                                        ),
                                    ],
                                    alignment=ft.MainAxisAlignment.START,
                                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                    bottom=480,
                                    spacing=2,
                                ),
                                # Navigation bar (assumed to be defined elsewhere)
                                navigation_bar,
                            ],
                            width=287,
                            height=585,
                            expand=True,
                        ),
                    ],
                )
            )

        elif e.route == "/descricao_servico":
            page.views.append(
                ft.View(
                    "/descricao_servico",
                    controls=[
                        ft.Stack(
                            controls=[
                                ft.Container(
                                    width=287,
                                    height=585,
                                    bgcolor="#FFDD78",
                                ),
                                ft.Column(
                                    [
                                        ft.Container(
                                            expand=True,
                                            margin=0,
                                            padding=0,
                                            content=ft.Stack(
                                                controls=[
                                                    # Fundo principal
                                                    ft.Container(
                                                        bgcolor="#FFDD78",
                                                        expand=True,
                                                    ),
                                                    # Container marrom (central)
                                                    ft.Container(
                                                        width=264,
                                                        height=460,
                                                        bgcolor="#7D5D42",
                                                        border_radius=15,
                                                        alignment=ft.alignment.center,
                                                    ),
                                                    # Container verde (conteúdo interno)
                                                    ft.Container(
                                                        width=240,
                                                        height=270,
                                                        bgcolor="#7D8E4E",
                                                        border_radius=15,
                                                        margin=ft.margin.only(
                                                            bottom=30),
                                                        padding=0,
                                                        alignment=ft.alignment.center,
                                                        content=ft.Column(
                                                            controls=[
                                                                ft.Row(
                                                                    controls=[
                                                                        ft.Icon(
                                                                            name=ft.icons.PEOPLE,
                                                                            color="black",
                                                                            size=24,
                                                                        ),
                                                                        ft.Text(
                                                                            "Lucas da Silva Costa",
                                                                            color="white",
                                                                            size=18,
                                                                            weight="bold",
                                                                        ),
                                                                    ],
                                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                                    spacing=10,
                                                                ),
                                                                ft.Row(
                                                                    controls=[
                                                                        ft.Icon(
                                                                            name=ft.icons.CALENDAR_MONTH_OUTLINED,
                                                                            color="black",
                                                                            size=24,
                                                                        ),
                                                                        ft.Text(
                                                                            "10/04/2024",
                                                                            color="white",
                                                                            size=18,
                                                                            weight="bold",
                                                                        ),
                                                                    ],
                                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                                    spacing=10,
                                                                ),
                                                                ft.Row(
                                                                    controls=[
                                                                        ft.Icon(
                                                                            name=ft.icons.PETS,
                                                                            color="black",
                                                                            size=24,
                                                                        ),
                                                                        ft.Text(
                                                                            "Gato",
                                                                            color="white",
                                                                            size=18,
                                                                            weight="bold",
                                                                        ),
                                                                    ],
                                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                                    spacing=10,
                                                                ),
                                                                ft.Row(
                                                                    controls=[
                                                                        ft.Icon(
                                                                            name=ft.icons.LOCK_CLOCK,
                                                                            color="black",
                                                                            size=24,
                                                                        ),
                                                                        ft.Text(
                                                                            "14h",
                                                                            color="white",
                                                                            size=18,
                                                                            weight="bold",
                                                                        ),
                                                                    ],
                                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                                    spacing=10,
                                                                ),
                                                                ft.Container(
                                                                    alignment=ft.alignment.center,
                                                                    margin=ft.margin.only(
                                                                        top=20),
                                                                    content=ft.ElevatedButton(
                                                                        content=ft.Container(
                                                                            content=ft.Icon(
                                                                                name=ft.icons.MESSAGE,
                                                                                color=ft.colors.WHITE,
                                                                            ),
                                                                            width=40,
                                                                            height=40,
                                                                        ),
                                                                        bgcolor="#8C5120",
                                                                        on_click=lambda e: page.go("/chat"),
                                                                    ),
                                                                ),
                                                            ],
                                                            alignment=ft.MainAxisAlignment.CENTER,
                                                            spacing=15,
                                                        ),
                                                    ),
                                                    # Título "Informações"
                                                    ft.Container(
                                                        content=ft.Text(
                                                            "Informações",
                                                            color="white",
                                                            size=18,
                                                            weight="bold",
                                                        ),
                                                        bgcolor="#8B4513",
                                                        width=200,
                                                        height=40,
                                                        border_radius=20,
                                                        alignment=ft.alignment.center,
                                                        margin=ft.margin.only(top=20),
                                                        border=ft.border.all(
                                                            1, ft.colors.BLACK),
                                                    ),
                                                ],
                                                alignment=ft.alignment.center,
                                            ),
                                        ),
                                    ],
                                    expand=True,
                                ),
                                navigation_bar,
                            ],
                        ),
                    ],
                )
            )

        elif e.route == "/chat":
            page.views.append(
                ft.View(
                    "/chat",
                    controls=[
                        ft.Stack(
                            controls=[
                                ft.Container(
                                    width=287,
                                    height=585,
                                    bgcolor="#FFDD78",
                                ),
                                ft.Column(
                                    [
                                        chat_layout,
                                    ],
                                    expand=True,
                                ),
                                navigation_bar,
                            ],
                            width=287,
                            height=585,
                        ),
                    ],
                )
            )
        page.update()

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.title = "MyLittlePet"
    page.bgcolor = "#FFDD78"
    page.window_width = 287
    page.window_height = 585

    page.on_route_change = route_change

    def create_button(text, route):
        avatar = ft.Container(
            width=40,
            height=40,
            bgcolor="#FFFFFF",
            border_radius=20,
            content=ft.Icon(
                name=ft.icons.PETS,
                color="#779030",
                size=24,
            ),
            alignment=ft.alignment.center,
        )
        return ft.Container(
            content=ft.ElevatedButton(
                width=257,
                height=74,
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=15),
                    bgcolor="#779030",
                    text_style=ft.TextStyle(
                        weight=ft.FontWeight.W_400,
                        size=20,
                        color="#FFFFFF",
                    ),
                ),
                on_click=lambda e: page.go(route),  # Define a rota ao clicar no botão
                content=ft.Row(
                    [
                        avatar,
                        ft.Text(
                            text,
                            size=15,
                            weight=ft.FontWeight.W_700,
                            color="#FFFFFF",
                            text_align=ft.TextAlign.START,
                            max_lines=1,
                            overflow=ft.TextOverflow.ELLIPSIS,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.START,
                    spacing=10,
                ),
            ),
            alignment=ft.alignment.center,
            margin=ft.margin.only(top=10),
        )

    def on_button_click(e):
        print(f"Botão clicado: {e.control.content.value}")

    chat = ft.ListView(
        expand=True,
        spacing=10,
        auto_scroll=True,
    )

    new_message = ft.TextField(
        hint_text="Digite sua mensagem...",
        autofocus=True,
        shift_enter=True,
        min_lines=1,
        max_lines=5,
        filled=True,
        expand=True,
    )

    def on_message(message):
        is_user_message = message.user == page.session.get("user_name")
        chat.controls.append(
            ft.Row(
                controls=[
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Text(
                                    f"{message.user}:",
                                    size=12,
                                    weight="bold",
                                    color="white" if is_user_message else "black",
                                ),
                                ft.Text(
                                    message.text,
                                    size=14,
                                    color="white" if is_user_message else "black",
                                ),
                            ],
                            spacing=5,
                        ),
                        padding=10,
                        border_radius=8,
                        bgcolor=CHAT_USER_MESSAGE_BG if is_user_message else CHAT_OTHER_MESSAGE_BG,
                        margin=ft.margin.symmetric(vertical=5),
                        alignment=ft.alignment.center_left
                        if not is_user_message
                        else ft.alignment.center_right,
                    )
                ],
                alignment=ft.MainAxisAlignment.END if is_user_message else ft.MainAxisAlignment.START,
            )
        )
        chat.update()

    def send_click(e):
        if new_message.value.strip():
            page.pubsub.send_all(
                Message(
                    user=page.session.get("user_name"),
                    text=new_message.value,
                    message_type="chat_message",
                )
            )
            new_message.value = ""
            new_message.update()

    def cadastrar(e):
        if not nome_input.value or not registro_input.value or not senha_input.value:
            msg.value = "Por favor, preencha todos os campos."
            page.update()
            return
        msg.value = f"Cadastro realizado com sucesso! Bem-vindo, {nome_input.value}!"
        nome_input.value = ""
        registro_input.value = ""
        senha_input.value = ""
        tipoPet_input.value = None
        banco_input.value = ""
        agencia_input.value = ""
        conta_input.value = ""
        page.update()

    def join_click(e):
        if not user_name.value.strip():
            user_name.error_text = "Nome não pode estar vazio!"
            user_name.update()
        else:
            page.session.set("user_name", user_name.value)
            page.dialog.open = False
            page.pubsub.send_all(
                Message(
                    user=user_name.value,
                    text=f"{user_name.value} entrou no chat.",
                    message_type="login_message",
                )
            )
            page.update()

    user_name = ft.TextField(label="Digite seu nome")

    page.dialog = ft.AlertDialog(
        open=True,
        modal=True,
        title=ft.Text("Bem-vindo!"),
        content=ft.Column([user_name], tight=True),
        actions=[
            ft.ElevatedButton(
                text="Entrar no chat",
                on_click=join_click
            )
        ],
        actions_alignment="end",
    )

    page.pubsub.subscribe(on_message)

    # Criando o layout do chat usando o componente
    chat_layout = create_chat_layout(chat, new_message, send_click)

    def navigation_change(e):
        index = e.control.selected_index
        if index == 0:  # Home
            page.go("/tela_inicial")
        elif index == 1:  # Profile
            pass  # Adicionar navegação para perfil depois

    navigation_bar = ft.Container(
        content=ft.NavigationBar(
            destinations=[
                ft.NavigationDestination(icon=ft.icons.HOME, label="Início"),
                ft.NavigationDestination(icon=ft.icons.PERSON, label="Perfil"),
            ],
            bgcolor="#BF5F0B",
            indicator_color="#DE8A18",
            on_change=navigation_change,
        ),
        height=80,
        width=page.window_width,
        alignment=ft.alignment.center,
        padding=0,
        margin=0,
        bgcolor="#BF5F0B",
        bottom=0,
    )

    page.go("/")


ft.app(target=main)
