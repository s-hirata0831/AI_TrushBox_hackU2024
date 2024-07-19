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

# BOMを除去する関数
def remove_bom(text):
    if text.startswith('\ufeff'):
        return text[1:]
    return text

# BOMを除去しつつCSVを読み込む関数
def read_csv_without_bom(file_path):
    with open(file_path, 'r', encoding='utf-8') as rf:
        reader = csv.reader(rf)
        rows = [list(map(remove_bom, row)) for row in reader]
    return rows


#------
#画面出力
#------
def main(page: ft.Page):
    #------
    #画面サイズ変数
    #------
    #macBookは1470*956
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

    #ぴえん魚を表示する
    pienIm = ft.Image(
        src="pien.png",
        height=HEIGHT*0.3,
        width=WIDTH*0.1,
        fit=ft.ImageFit.CONTAIN
    )

    Im2 = ft.Image(
        src="02.png",
        height=HEIGHT*0.3,
        width=WIDTH*0.1,
        fit=ft.ImageFit.CONTAIN
    )
    Im3 = ft.Image(
        src="03.png",
        height=HEIGHT*0.3,
        width=WIDTH*0.1,
        fit=ft.ImageFit.CONTAIN
    )
    Im4 = ft.Image(
        src="04.png",
        height=HEIGHT*0.3,
        width=WIDTH*0.1,
        fit=ft.ImageFit.CONTAIN
    )
    Im5 = ft.Image(
        src="05.png",
        height=HEIGHT*0.3,
        width=WIDTH*0.1,
        fit=ft.ImageFit.CONTAIN
    )
    Im6 = ft.Image(
        src="06.png",
        height=HEIGHT*0.3,
        width=WIDTH*0.1,
        fit=ft.ImageFit.CONTAIN
    )
    Im7 = ft.Image(
        src="07.png",
        height=HEIGHT*0.3,
        width=WIDTH*0.1,
        fit=ft.ImageFit.CONTAIN
    )
    Im8 = ft.Image(
        src="08.png",
        height=HEIGHT*0.3,
        width=WIDTH*0.1,
        fit=ft.ImageFit.CONTAIN
    )
    Im9 = ft.Image(
        src="09.png",
        height=HEIGHT*0.3,
        width=WIDTH*0.1,
        fit=ft.ImageFit.CONTAIN
    )
    Im10 = ft.Image(
        src="10.png",
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
        # ccページのクリア
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
            rows = read_csv_without_bom('fishSave/state.csv')
            if int(rows[0][0]) == 0:
                a00 = canIm
            elif int(rows[0][0]) == 1:
                a00 = pienIm
            elif int(rows[0][0]) == 2:
                a00 = Im5
            
            if int(rows[0][1]) == 0:
                a01 = petIm
            elif int(rows[0][1]) == 1:
                a01 = pienIm
            elif int(rows[0][1]) == 2:
                a01 = Im2
            
            if int(rows[0][2]) == 0:
                a02 = canIm
            elif int(rows[0][2]) == 1:
                a02 = pienIm
            elif int(rows[0][2]) == 2:
                a02 = Im3

            if int(rows[0][3]) == 0:
                a03 = petIm
            elif int(rows[0][3]) == 1:
                a03= pienIm
            elif int(rows[0][3]) == 2:
                a03 = Im4

            if int(rows[0][4]) == 0:
                a04 = canIm
            elif int(rows[0][4]) == 1:
                a04 = pienIm
            elif int(rows[0][4]) == 2:
                a04 = Im5

            if int(rows[0][5]) == 0:
                a05 = petIm
            elif int(rows[0][5]) == 1:
                a05 = pienIm
            elif int(rows[0][5]) == 2:
                a05 = Im8

            if int(rows[0][6]) == 0:
                a06 = canIm
            elif int(rows[0][6]) == 1:
                a06 = pienIm
            elif int(rows[0][6]) == 2:
                a06 = Im9

            if int(rows[0][7]) == 0:
                a07 = petIm
            elif int(rows[0][7]) == 1:
                a07 = pienIm
            elif int(rows[0][7]) == 2:
                a07 = Im10

            if int(rows[0][8]) == 0:
                a08 = canIm
            elif int(rows[0][8]) == 1:
                a08 = pienIm
            elif int(rows[0][8]) == 2:
                a08 = Im4
            
            if int(rows[0][9]) == 0:
                a09 = petIm
            elif int(rows[0][9]) == 1:
                a09 = pienIm
            elif int(rows[0][9]) == 2:
                a09 = Im2

            if int(rows[1][0]) == 0:
                a10 = petIm
            elif int(rows[1][0]) == 1:
                a10 = pienIm
            elif int(rows[1][0]) == 2:
                a10 = Im10
            
            if int(rows[1][1]) == 0:
                a11 = canIm
            elif int(rows[1][1]) == 1:
                a11 = pienIm
            elif int(rows[1][1]) == 2:
                a11 = Im9
            
            if int(rows[1][2]) == 0:
                a12 = petIm
            elif int(rows[1][2]) == 1:
                a12 = pienIm
            elif int(rows[1][2]) == 2:
                a12 = Im3

            if int(rows[1][3]) == 0:
                a13 = canIm
            elif int(rows[1][3]) == 1:
                a13= pienIm
            elif int(rows[1][3]) == 2:
                a13 = Im8

            if int(rows[1][4]) == 0:
                a14 = petIm
            elif int(rows[1][4]) == 1:
                a14 = pienIm
            elif int(rows[1][4]) == 2:
                a14 = Im2

            if int(rows[1][5]) == 0:
                a15 = canIm
            elif int(rows[1][5]) == 1:
                a15 = pienIm
            elif int(rows[1][5]) == 2:
                a15 = Im4

            if int(rows[1][6]) == 0:
                a16 = petIm
            elif int(rows[1][6]) == 1:
                a16 = pienIm
            elif int(rows[1][6]) == 2:
                a16 = Im5

            if int(rows[1][7]) == 0:
                a17 = canIm
            elif int(rows[1][7]) == 1:
                a17 = pienIm
            elif int(rows[1][7]) == 2:
                a17 = Im8

            if int(rows[1][8]) == 0:
                a18 = petIm
            elif int(rows[1][8]) == 1:
                a18 = pienIm
            elif int(rows[1][8]) == 2:
                a18 = Im4
            
            if int(rows[1][9]) == 0:
                a19 = canIm
            elif int(rows[1][9]) == 1:
                a19 = pienIm
            elif int(rows[1][9]) == 2:
                a19 = Im3

            if int(rows[2][0]) == 0:
                a20 = canIm
            elif int(rows[2][0]) == 1:
                a20 = pienIm
            elif int(rows[2][0]) == 2:
                a20 = Im6
            
            if int(rows[2][1]) == 0:
                a21 = petIm
            elif int(rows[2][1]) == 1:
                a21 = pienIm
            elif int(rows[2][1]) == 2:
                a21 = Im7
            
            if int(rows[2][2]) == 0:
                a22 = canIm
            elif int(rows[2][2]) == 1:
                a22 = pienIm
            elif int(rows[2][2]) == 2:
                a22 = Im4

            if int(rows[2][3]) == 0:
                a23 = petIm
            elif int(rows[2][3]) == 1:
                a23= pienIm
            elif int(rows[2][3]) == 2:
                a23 = Im2

            if int(rows[2][4]) == 0:
                a24 = canIm
            elif int(rows[2][4]) == 1:
                a24 = pienIm
            elif int(rows[2][4]) == 2:
                a24 = Im6

            if int(rows[2][5]) == 0:
                a25 = petIm
            elif int(rows[2][5]) == 1:
                a25 = pienIm
            elif int(rows[2][5]) == 2:
                a25 = Im7

            if int(rows[2][6]) == 0:
                a26 = canIm
            elif int(rows[2][6]) == 1:
                a26 = pienIm
            elif int(rows[2][6]) == 2:
                a26 = Im5

            if int(rows[2][7]) == 0:
                a27 = petIm
            elif int(rows[2][7]) == 1:
                a27 = pienIm
            elif int(rows[2][7]) == 2:
                a27 = Im4

            if int(rows[2][8]) == 0:
                a28 = canIm
            elif int(rows[2][8]) == 1:
                a28 = pienIm
            elif int(rows[2][8]) == 2:
                a28 = Im6
            
            if int(rows[2][9]) == 0:
                a29 = petIm
            elif int(rows[2][9]) == 1:
                a29 = pienIm
            elif int(rows[2][9]) == 2:
                a29 = Im7
            
            page.views.append(
                ft.View(
                    "/fish",
                    [
                        page.appbar,
                        ft.Container(
                            content=ft.Column([
                                ft.Row([a00,a01,a02,a03,a04,a05,a06,a07,a08,a09],
                                       alignment=ft.MainAxisAlignment.CENTER, spacing=0),
                                ft.Row([a10,a11,a12,a13,a14,a15,a16,a17,a18,a19],
                                       alignment=ft.MainAxisAlignment.CENTER, spacing=0),
                                ft.Row([a20,a21,a22,a23,a24,a25,a26,a27,a28,a29],
                                       alignment=ft.MainAxisAlignment.CENTER, spacing=0)
                            ], alignment=ft.MainAxisAlignment.CENTER, spacing=0),
                            width=WIDTH,
                            height=HEIGHT - BAR_HEIGHT
                        )
                    ],
                    bgcolor=ft.colors.BLUE_300
                )
            )

        # ページ更新
        page.update()

    #------
    #画面遷移
    #------
    #現在のページを削除して前のページに戻る
    def view_pop():
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
        cNum = can_num % 2
        pNum = pet_num % 2

        print("ゴミが投入されたか確認します。")
        checkResult = writeCsv.writeNum(can_num, pet_num)
        if checkResult:
            if cNum == 0 or pNum == 0:
                #新たに追加された場合
                open_1()
                time.sleep(2)
                #譜面取得
                writeCsv.randomScr(can_num, pet_num)
                open_fish()

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
