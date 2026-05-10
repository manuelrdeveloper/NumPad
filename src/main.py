import flet as ft


def main(page: ft.Page):
    page.title = "NumPad"
    img = ft.Image(src="assets/logo.png")
    page.add(img)


ft.app(target=main)
