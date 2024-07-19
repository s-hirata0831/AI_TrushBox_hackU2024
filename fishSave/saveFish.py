import flet as ft
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
import threading
import writeCsv
import time
import csv

#------
#Firebase初期設定
#------
cred = credentials.Certificate("fishSave/token.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
# FirebaseのドキュメントIDを指定
docCan = db.collection("stateTrashBox").document("can")
docPet = db.collection("stateTrashBox").document("pet")

#------
#画面出力
#------
def main(page: ft.Page):
    #------
    #画面サイズ変数
    #------
    WIDTH = 1470
    HEIGHT = 956
    BAR_HEIGHT = HEIGHT * 0.08

    page.title = "魚を救え！"
    page.window_minimizable = False
    page.window_maximizable = True
    page.window_resizable = True
    page.window_full_screen = True
    page.window_always_on_top = True
    # フォント
    page.fonts = {
        "font": "/Users/hiratasoma/Documents/AI_TrushBox_hackU2024/fishSave/DotGothic16-Regular.ttf"
    }

    # 缶とペットボトルの本数を表示するテキスト
    can_text = ft.Text("0本", font_family="font", color=ft.colors.BLACK, size=35)
    pet_text = ft.Text("0本", font_family="font", color=ft.colors.BLACK, size=35)

    #缶を表示する
    canIm = ft.Image(
        src="canIm.png",
        height=HEIGHT*0.3,
        width=WIDTH*0.1,
        fit=ft.ImageFit.CONTAIN
    )

    #ペットボトルを表示する
    petIm = ft.Image(
        src="pet.png",
        height=HEIGHT*0.3,
        width=WIDTH*0.1,
        fit=ft.ImageFit.CONTAIN
    )

    # AppBar(上部バナー)
    page.appbar = ft.AppBar(
        leading=ft.Container(
            ft.Image(src="logo.png", height=BAR_HEIGHT * 0.8, fit=ft.ImageFit.CONTAIN),
            margin=ft.margin.only(left=10, top=0, right=0, bottom=0),
            padding=0
        ),
        toolbar_height=BAR_HEIGHT,
        bgcolor=ft.colors.BLUE_100,
        title=ft.Row([
            ft.Text(
                "魚を取り戻そう！",
                font_family="font",
                color=ft.colors.BLACK,
                size=40,
                weight=ft.FontWeight.W_900
            ),
            ft.Image(src="can.png", height=BAR_HEIGHT * 0.6),
            can_text,
            ft.Image(src="pet.png", height=BAR_HEIGHT * 0.6),
            pet_text
        ])
    )

    # 画面表示部
    def route_change(e):
        # ページのクリア
        page.views.clear()

        # トップページ
        page.views.append(
            ft.View(
                "/",
                [
                    page.appbar,
                    ft.Container(
                        content=ft.Column([
                            ft.Row([
                                canIm,
                                petIm,
                                canIm,
                                petIm,
                                canIm,
                                petIm,
                                canIm,
                                petIm,
                                canIm,
                                petIm
                            ], alignment=ft.MainAxisAlignment.CENTER, spacing=0),
                            ft.Row([
                                petIm,
                                canIm,
                                petIm,
                                canIm,
                                petIm,
                                canIm,
                                petIm,
                                canIm,
                                petIm,
                                canIm
                            ], alignment=ft.MainAxisAlignment.CENTER, spacing=0),
                            ft.Row([
                                canIm,
                                petIm,
                                canIm,
                                petIm,
                                canIm,
                                petIm,
                                canIm,
                                petIm,
                                canIm,
                                petIm
                            ], alignment=ft.MainAxisAlignment.CENTER, spacing=0)
                        ],alignment=ft.MainAxisAlignment.CENTER, spacing=0),
                        width=WIDTH,
                        height=HEIGHT - BAR_HEIGHT
                    )
                ],
                bgcolor=ft.colors.BLUE_300
            )
        )

        if page.route == "/1":
            page.views.append(
                ft.View(
                    "/1",
                    [
                        page.appbar,
                        ft.Container(
                            content=ft.Column([
                                ft.Row([
                                    ft.Text(
                                        "捨ててくれてありがとう！",
                                        size=100,
                                        font_family="font",
                                        color=ft.colors.BLACK
                                    )
                                ], alignment=ft.MainAxisAlignment.CENTER),
                                ft.Row([
                                    ft.Image(
                                        src="thanks.png",
                                        height=HEIGHT*0.5
                                    )
                                ], alignment=ft.MainAxisAlignment.CENTER)
                            ],alignment=ft.MainAxisAlignment.SPACE_EVENLY),
                            width=WIDTH,
                            height=HEIGHT*0.92
                        )
                    ],
                    bgcolor=ft.colors.BLUE_300
                )
            )

        if page.route == "/fish":
            with open
            page.views.append(
                ft.View(
                    "/fish",
                    [
                        page.appbar,
                        ft.Container
                    ]
                )
            )

        # ページ更新
        page.update()

    #------
    #画面遷移
    #------
    #現在のページを削除して前のページに戻る
    def view_pop(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    #TOPページへ戻る
    def open_00_top(e):
        page.views.pop(e)
        top_view = page.views[0]
        page.go(top_view.route)

    #ゴミを捨ててくれてありがとう画面
    def open_1():
        page.go("/1")

    #譜面自動生成
    def open_fish():
        page.go("/fish")

    # Firebaseからデータを取得して更新
    def update_data():
        can = docCan.get().to_dict()
        pet = docPet.get().to_dict()
        can_num = can.get('canNum', 0)
        pet_num = pet.get('petNum', 0)

        can_text.value = f"{can_num}本"
        pet_text.value = f"{pet_num}本"
        print("データを取得*2")

        print("ゴミが投入されたか確認します。")
        checkResult = writeCsv.writeNum(can_num, pet_num)
        if checkResult == True:
            #新たに追加された場合
            open_1()
            time.sleep(5)
            #譜面取得
            writeCsv.randomScr(can_num, pet_num)

        # ページを更新
        page.update()

    # 6秒ごとにデータを更新
    def periodic_update():
        update_data()
        threading.Timer(6, periodic_update).start()

    #------
    #イベントの登録
    #------
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    #------
    #起動後の処理
    #------
    page.go(page.route)
    periodic_update()

# アプリの開始
writeCsv.resetCsv()
ft.app(target=main)
