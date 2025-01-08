import os
import tkinter as tk
from tkinter import ttk

# Data for the 2x13 spreadsheet
data = [
    ("イントラネットをチェック", "Google Site ※HRサイトは社員専用"),
    ("Gmailの署名を設定する", "署名の設定ガイド"),
    ("Slack & Googleのプロフィール写真をアップする", "Slackの更新方法、Googleの更新方法"),
    ("情報セキュリティ遵守表明書を提出", "提出フォーム"),
    ("【社員のみ】勤怠システムにログインをしてみよう", "組織コード：e472、ログインIDとパスワードは\n社員番号6桁（“0”始まり）、ログイン後はパスワード変更"),
    ("WEB版URL、携帯アプリをチェック", "アプリ未インストールの場合「JOE就業＿アプリマニュアル」参照"),
    ("【社員のみ】HR関連マニュアルをCheck", "SharePoint"),
    ("【社員のみ】給与明細システムにログインをしてみよう", "ログインIDと初期パスワード：社員番号6桁\n（“0”始まり）、WMJ+誕生日（yyyymmdd）"),
    ("【社員のみ】Workdayシステムにログインをしてみよう", "プロフィール写真アップ、Inboxタスクをゼロに"),
    ("サイトURLとWorkdayマニュアル", "チェック必須"),
    ("【社員のみ】名刺を作成しよう", "企業コード：wmj、ユーザーIDとパスワードは社員番号6桁"),
    ("名刺発注サイト【COREZO】", "表面：和文／裏面：英文で作成、申請時本部長承認必要"),
    ("【社員のみ必須】AMEX Corporate Cardを作成", "入社1ヶ月を目途に申請、一般社員と役員で申請書類が異なる"),
    ("一般社員用、Operating Committee用申請書一式", "HRの指定がない申請は不可"),
    ("【オプション】マウスやヘッドセットの貸与申請", "ハードウェアリクエスト（SNOW）"),
    ("【オプション】Google Calendarをチェック", "会議室予約方法"),
    ("【オプション】Okta設定&パスワード変更90日ごと変更必須。変更後は必ずWiFiとPCに新しいパスワードで入り直してください", "[Oktaガイド]")
]

# Create the main window
root = tk.Tk()
root.title("Onboarding")

# Create a Treeview widget to display the data
tree = ttk.Treeview(root, columns=("Completed", "Item", "Description"), show="headings", height=len(data))
tree.tag_configure("center", anchor="center")
tree.column("Completed", anchor="center", width=100)
tree.column("Item", anchor="w", width=300)
tree.column("Description", anchor="center", width=600)

# Add the heading for the "Completed" column
tree.heading("Completed", text="Completed")
tree.heading("Item", text="Item")
tree.heading("Description", text="Description")

# Function to create a Checkbutton widget in a frame inside the treeview
def create_checkbox(parent, row):
    var = tk.BooleanVar(value=False)  # Initially set the checkbox as unchecked
    checkbutton = tk.Checkbutton(parent, variable=var)
    checkbutton.grid(row=0, column=0, padx=5, pady=5)
    return var  # return the variable to track checkbox state

# Insert the data into the Treeview, with checkbuttons in the "Completed" column
checkbox_vars = []  # To hold the BooleanVar objects for each row
for item, description in data:
    item_id = tree.insert("", "end", values=("", item, description))  # Empty string for the checkbox column
    checkbox_var = create_checkbox(tree, item_id)
    checkbox_vars.append(checkbox_var)

# Pack the Treeview widget
tree.pack(fill="both", expand=True)

# Run the application
root.mainloop()
