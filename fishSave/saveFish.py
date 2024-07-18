import flet as ft

#------
#画面出力
#------
def main(page: ft.Page):
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