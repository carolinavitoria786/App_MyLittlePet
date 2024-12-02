import flet as ft

class Message:
    def __init__(self, user: str, text: str, message_type: str):
        self.user = user
        self.text = text
        self.message_type = message_type

def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.title = "MyLittlePet"
    page.bgcolor = "#FFDD78"
    page.window_width = 287
    page.window_height = 585
    page.padding = 0

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

    def on_message(message: Message):
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
                        bgcolor="#0078D7" if is_user_message else "#E1E1E1",
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
        actions=[ft.ElevatedButton(text="Entrar no chat", on_click=join_click)],
        actions_alignment="end",
    )

    page.pubsub.subscribe(on_message)

    chat_layout = ft.Stack(
        [
            ft.Container(
                width=287,
                height=400,
                bgcolor="#7D5D42",
                margin=ft.margin.only(top=70),
                border_radius=5,
            ),
            ft.Column(
                [
                    ft.Container(
                        content=chat,
                        bgcolor="#FFFFFF",
                        width=250,
                        height=320,
                        border_radius=10,
                        padding=10,
                        margin=ft.margin.only(left=10, right=10, top=55),
                        border=ft.border.all(1, ft.colors.BLACK),  
                    ),
                    ft.Row(
                        controls=[
                            new_message,
                            ft.ElevatedButton(
                                "Enviar",
                                on_click=send_click,
                                bgcolor="#C2690A", 
                                color=ft.colors.WHITE,  
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,  
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            ft.Container(
                content=ft.Text("Chat", color="white", size=18, weight="bold"),
                bgcolor="#8B4513",
                width=200,
                height=40,
                border_radius=20,
                alignment=ft.alignment.center,
                margin=ft.margin.only(bottom=420, top=20),
                border=ft.border.all(1, ft.colors.BLACK),
            ),
        ],
        alignment=ft.alignment.center,
        height=470,
    )

    navigation_bar = ft.Container(
        content=ft.NavigationBar(
            destinations=[
                ft.NavigationBarDestination(
                    icon=ft.icons.HOME_ROUNDED, label="Tela Inicial"
                ),
                ft.NavigationBarDestination(
                    icon=ft.icons.PERSON_ROUNDED, label="Perfil"
                ),
            ],
            bgcolor="#BF5F0B",  
            indicator_color="#DE8A18",  
        ),
        height=80, 
        width=page.window_width, 
        alignment=ft.alignment.center,  
        padding=0,
        margin=0,
        bgcolor="#BF5F0B",
    )

    page.add(
        ft.Column(
            [
                chat_layout,  
                navigation_bar,  
            ],
            alignment=ft.MainAxisAlignment.START,  
            spacing=0,  
        ),
    )

    page.update()

ft.app(target=main)
