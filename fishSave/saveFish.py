import flet as ft
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials

#------
#Firebase初期設定
#------
cred = credentials.Certificate("fishSave/token.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
#FirebaseのドキュメントIDを指定
docCan = db.collection("stateTrashBox").document("can")
docPet = db.collection("stateTrashBox").document("pet")

#------
#画面出力
#------
def main(page: ft.Page):
    #------
    #画面サイズ変数
    #------
    WIDTH=1470
    HEIGHT=956
    BAR_HEIGHT=HEIGHT*0.08

    page.title = "魚を救え！"
    page.window_minimizable =False
    page.window_maximizable = True
    page.window_resizable = True
    page.window_full_screen = False
    page.window_always_on_top = True
    #フォント
    page.fonts={
        "font": "/Users/hiratasoma/Documents/AI_TrushBox_hackU2024/fishSave/DotGothic16-Regular.ttf"
    }
    #缶の本数を取得
    canState = ['canNum']
    can = docCan.get(field_paths=canState).to_dict()
    can_s=can['canNum']
    #ペットボトルの本数を取得
    petState = ['petNum']
    pet = docPet.get(field_paths=petState).to_dict()
    pet_s=pet['petNum']

    #AppBar(上部バナー)
    page.appbar = ft.AppBar(
        leading=ft.Container(ft.Image(src="logo.png", height=BAR_HEIGHT*0.8, fit=ft.ImageFit.CONTAIN), margin=ft.margin.only(left=10, top=0, right=0, bottom=0), padding=0),
        toolbar_height=BAR_HEIGHT,
        bgcolor=ft.colors.BLUE_100,
        title=ft.Row([
            ft.Text(
                "魚を救え！",
                font_family="font",
                color=ft.colors.BLACK,
                size=40,
                weight=ft.FontWeight.W_900
            ),
            ft.Image(src="can.png", height=BAR_HEIGHT*0.6),
            ft.Text(
                str(can_s)+"本",
                font_family="font",
                color=ft.colors.BLACK,
                size=35
            ),
            ft.Image(src="pet.png", height=BAR_HEIGHT*0.6),
            ft.Text(
                str(pet_s)+"本",
                font_family="font",
                color=ft.colors.BLACK,
                size=35
            )
        ])
    )
    

    #------
    #画面表示部
    #------
    def route_change(e):
        #ページのクリア
        page.views.clear()

        #トップページ
        page.views.append(
            ft.View(
                "/",
                [
                    page.appbar,
                    ft.Container(
                        ft.Text(
                            "魚を救え！",
                            size=100,
                            color=ft.colors.BLACK,
                            font_family="font"
                        )
                    )
                ],
                bgcolor=ft.colors.BLUE_300
            )
        )

        #ページ更新
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

    #------
    #イベントの登録
    #------
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    #------
    #起動後の処理
    #------
    page.go(page.route)

#アプリの開始
ft.app(target=main)