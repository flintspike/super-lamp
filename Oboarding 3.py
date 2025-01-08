import tkinter as tk
import json
from tkinter import ttk
from pathlib import Path
import webbrowser


root = tk.Tk()
root.title('Onboarding')
root.geometry()
window = tk.Frame()

progress_path = Path(r'''OnboardingProgress''')

def loader():
	global intranet_frame_checkbox_var
	global gmailsig_frame_checkbox_var
	global pfp_frame_checkbox_var
	global security_frame_checkbox_var
	global HR_frame_checkbox_var
	global salary_frame_checkbox_var
	global workday_frame_checkbox_var
	global mieshi_frame_checkbox_var
	global amex_frame_checkbox_var
	global mouse_frame_checkbox_var
	global calendar_frame_checkbox_var
	global okta_frame_checkbox_var

	if not progress_path.exists():
		return

	json_data = progress_path.read_text()
	load_data = json.loads(json_data)

	intranet_frame_checkbox_var.set(load_data.get("intranet_frame_checkbox_var"))
	gmailsig_frame_checkbox_var.set(load_data.get("gmailsig_frame_checkbox_var"))
	pfp_frame_checkbox_var.set(load_data.get("pfp_frame_checkbox_var"))
	security_frame_checkbox_var.set(load_data.get("security_frame_checkbox_var"))
	HR_frame_checkbox_var.set(load_data.get("HR_frame_checkbox_var"))
	salary_frame_checkbox_var.set(load_data.get("salary_frame_checkbox_var"))
	workday_frame_checkbox_var.set(load_data.get("workday_frame_checkbox_var"))
	mieshi_frame_checkbox_var.set(load_data.get("mieshi_frame_checkbox_var"))
	amex_frame_checkbox_var.set(load_data.get("amex_frame_checkbox_var"))
	mouse_frame_checkbox_var.set(load_data.get("mouse_frame_checkbox_var"))
	calendar_frame_checkbox_var.set(load_data.get("calendar_frame_checkbox_var"))
	okta_frame_checkbox_var.set(load_data.get("okta_frame_checkbox_var"))

def saver():
		intranet_frame_checkbox_var_completion = intranet_frame_checkbox_var.get()
		gmailsig_frame_checkbox_var_completion = gmailsig_frame_checkbox_var.get()
		pfp_frame_checkbox_var_completion = pfp_frame_checkbox_var.get()
		security_frame_checkbox_var_completion = security_frame_checkbox_var.get()
		HR_frame_checkbox_var_completion = HR_frame_checkbox_var.get()
		salary_frame_checkbox_var_completion = salary_frame_checkbox_var.get()
		workday_frame_checkbox_var_completion = workday_frame_checkbox_var.get()
		mieshi_frame_checkbox_var_completion = mieshi_frame_checkbox_var.get()
		amex_frame_checkbox_var_completion = amex_frame_checkbox_var.get()
		mouse_frame_checkbox_var_completion = mouse_frame_checkbox_var.get()
		calendar_frame_checkbox_var_completion = calendar_frame_checkbox_var.get()
		okta_frame_checkbox_var_completion = okta_frame_checkbox_var.get()

		save_data = {
			"intranet_frame_checkbox_var":intranet_frame_checkbox_var_completion,
			"gmailsig_frame_checkbox_var":gmailsig_frame_checkbox_var_completion,
			"pfp_frame_checkbox_var":pfp_frame_checkbox_var_completion,
			"security_frame_checkbox_var":security_frame_checkbox_var_completion,
			"HR_frame_checkbox_var":HR_frame_checkbox_var_completion,
			"salary_frame_checkbox_var":salary_frame_checkbox_var_completion,
			"workday_frame_checkbox_var":workday_frame_checkbox_var_completion,
			"mieshi_frame_checkbox_var":mieshi_frame_checkbox_var_completion,
			"amex_frame_checkbox_var":amex_frame_checkbox_var_completion,
			"mouse_frame_checkbox_var":mouse_frame_checkbox_var_completion,
			"calendar_frame_checkbox_var":calendar_frame_checkbox_var_completion,
			"okta_frame_checkbox_var":okta_frame_checkbox_var_completion
			}

		json_data = json.dumps(save_data)
		progress_path.write_text(json_data)

def complete_check():

	complete_check_var = (
		intranet_frame_checkbox_var.get()+
		gmailsig_frame_checkbox_var.get()+
		pfp_frame_checkbox_var.get()+
		security_frame_checkbox_var.get()+
		HR_frame_checkbox_var.get()+
		salary_frame_checkbox_var.get()+
		workday_frame_checkbox_var.get()+
		mieshi_frame_checkbox_var.get()+
		amex_frame_checkbox_var.get()+
		mouse_frame_checkbox_var.get()+
		calendar_frame_checkbox_var.get()+
		okta_frame_checkbox_var.get()
		)
	print(complete_check_var)
	if complete_check_var == 0:
		print('COMPLETE')# REPLACE LATER WITH BUTTON UNLOCK
		complete.configure(state = 'enabled')
	else:
		pass
	saver()

welcome = ttk.Label(window, text = 'Welcome to WMJ!', font = 'bold 42')

user_data_frame = ttk.Frame(window)
#department = 
#employeeid = 
#email = 


intranet_frame = tk.Frame(window, highlightbackground="blue", highlightthickness = 1)
intranet_frame_label = ttk.Label(intranet_frame, 
	text =	'''
	イントラネットをチェック
	'''
	)
intranet_frame_checkbox_var = tk.IntVar(value = 1)
intranet_frame_checkbox = ttk.Checkbutton(
	intranet_frame, 
	text = 'Completed?', 
	onvalue = 0, 
	offvalue = 1, 
	variable = intranet_frame_checkbox_var, 
	command = complete_check
	)
intranet_frame_checkbox.pack(side = 'left')
intranet_frame_label.pack(side = 'left', padx = 20)

gmailsig_frame = tk.Frame(window, highlightbackground="blue", highlightthickness = 1)
gmailsig_frame_label = ttk.Label(gmailsig_frame, 
	text ='''
	Gmailの署名を設定する
	'''
	)
gmailsig_frame_checkbox_var = tk.IntVar(value = 1)
gmailsig_frame_checkbox = ttk.Checkbutton(
	gmailsig_frame, 
	text = 'Completed?', 
	onvalue = 0, 
	offvalue = 1, 
	variable = gmailsig_frame_checkbox_var, 
	command = complete_check
	)
gmailsig_frame_checkbox.pack(side = 'left')
gmailsig_frame_label.pack(side = 'left', padx = 20)

pfp_frame = tk.Frame(window, highlightbackground="blue", highlightthickness = 1)
pfp_frame_label = ttk.Label(pfp_frame, 
	text =	'''
	Slack & Googleのプロフィール写真をアップする
	'''
	)
pfp_frame_checkbox_var = tk.IntVar(value = 1)
pfp_frame_checkbox = ttk.Checkbutton(
	pfp_frame, 
	text = 'Completed?', 
	onvalue = 0, 
	offvalue = 1, 
	variable = pfp_frame_checkbox_var, 
	command = complete_check
	)
pfp_frame_checkbox.pack(side = 'left')
pfp_frame_label.pack(side = 'left', padx = 20)

security_frame = tk.Frame(window, highlightbackground="blue", highlightthickness = 1)
security_frame_label = ttk.Label(security_frame, 
	text ='''
	情報セキュリティ遵守表明書を提出
	'''
	)
security_frame_checkbox_var = tk.IntVar(value = 1)
security_frame_checkbox = ttk.Checkbutton(
	security_frame, 
	text = 'Completed?', 
	onvalue = 0, 
	offvalue = 1, 
	variable = security_frame_checkbox_var, 
	command = complete_check
	)
security_frame_checkbox.pack(side = 'left')
security_frame_label.pack(side = 'left', padx = 20)

HR_frame = tk.Frame(window, highlightbackground="blue", highlightthickness = 1)
HR_frame_label = ttk.Label(HR_frame, 
	text =	'''
	【社員のみ】 勤怠システムにログインをしてみよう
	組織コード：e472
	ログインID：社員番号6桁 ”０”から始まる番号です
	初期パスワード：社員番号6桁 ”０”から始まる番号です
	※ログイン後はパスワードを必ず変更してください
	'''
	)
HR_frame_checkbox_var = tk.IntVar(value = 1)
HR_frame_checkbox = ttk.Checkbutton(
	HR_frame, 
	text = 'Completed?', 
	onvalue = 0, 
	offvalue = 1, 
	variable = HR_frame_checkbox_var, 
	command = complete_check
	)
HR_frame_checkbox.pack(side = 'left')
HR_frame_label.pack(side = 'left', padx = 20)

salary_frame = tk.Frame(window, highlightbackground="blue", highlightthickness = 1)
salary_frame_label = ttk.Label(salary_frame, 
	text ='''
	【社員のみ】 給与明細システムにログインをしてみよう
	ログインＩＤ ： 社員番号6桁 ”０”から始まる番号です
	初期パスワード ： WMJ+誕生日（yyyymmdd）
	※WMJは半角大文字
	（1977年1月1日生まれの場合 → WMJ19770101 ）
	★初めての給与支給日の前日よりログイン可能です。
	'''
	)
salary_frame_checkbox_var = tk.IntVar(value = 1)
salary_frame_checkbox = ttk.Checkbutton(
	salary_frame, 
	text = 'Completed?', 
	onvalue = 0, 
	offvalue = 1, 
	variable = salary_frame_checkbox_var, 
	command = complete_check
	)
salary_frame_checkbox.pack(side = 'left')
salary_frame_label.pack(side = 'left', padx = 20)

workday_frame = tk.Frame(window, highlightbackground="blue", highlightthickness = 1)
workday_frame_label = ttk.Label(workday_frame, 
	text =	'''
	【社員のみ】 Workdayシステムにログインをしてみよう
	➡プロフィール写真をアップしてください
	➡ Inboxあるタスクはゼロ(0)にしてください
	'''
	)
workday_frame_checkbox_var = tk.IntVar(value = 1)
workday_frame_checkbox = ttk.Checkbutton(
	workday_frame, 
	text = 'Completed?', 
	onvalue = 0, 
	offvalue = 1, 
	variable = workday_frame_checkbox_var, 
	command = complete_check
	)
workday_frame_checkbox.pack(side = 'left')
workday_frame_label.pack(side = 'left', padx = 20)

mieshi_frame = tk.Frame(window, highlightbackground="blue", highlightthickness = 1)
mieshi_frame_label = ttk.Label(mieshi_frame, 
	text ='''
	【社員のみ】:identification_card: 名刺を作成しよう
	企業コード： wmj (小文字）
	ユーザーID： 社員番号6桁 ”０”から始まる番号ですパスワード ： 
	社員番号6桁 ”０”から始まる番号です

	※社員以外の方の名刺作成は、
	所属の本部長の承認証明と社員番号を
	<Yuki.Sato@warnermusic.com, 
	Kazuko.Nishimaki@warnermusic.com>
	宛てに送り、Corezoのアカウント申請をしてください。
	'''
	)
mieshi_frame_checkbox_var = tk.IntVar(value = 1)
mieshi_frame_checkbox = ttk.Checkbutton(
	mieshi_frame, 
	text = 'Completed?', 
	onvalue = 0, 
	offvalue = 1, 
	variable = mieshi_frame_checkbox_var, 
	command = complete_check
	)
mieshi_frame_checkbox.pack(side = 'left')
mieshi_frame_label.pack(side = 'left', padx = 20)

amex_frame = tk.Frame(window, highlightbackground="blue", highlightthickness = 1)
amex_frame_label = ttk.Label(amex_frame, 
	text =	'''
	【社員のみ必須】 AMEX Corporate Cardを作成
	※入社1ヶ月を目途に申請をお願いします。
	※一般社員とOperating Committeeのカード
	種類が違うので、ご申請は間違わないようお願いします。
	'''
	)
amex_frame_checkbox_var = tk.IntVar(value = 1)
amex_frame_checkbox = ttk.Checkbutton(
	amex_frame, 
	text = 'Completed?', 
	onvalue = 0, 
	offvalue = 1, 
	variable = amex_frame_checkbox_var, 
	command = complete_check
	)
amex_frame_checkbox.pack(side = 'left')
amex_frame_label.pack(side = 'left', padx = 20)

mouse_frame = tk.Frame(window, highlightbackground="blue", highlightthickness = 1)
mouse_frame_label = ttk.Label(mouse_frame, 
	text ='''
	【オプション】マウスやヘッドセットの貸与申請
	'''
	)
mouse_frame_checkbox_var = tk.IntVar(value = 1)
mouse_frame_checkbox = ttk.Checkbutton(
	mouse_frame, 
	text = 'Completed?', 
	onvalue = 0, 
	offvalue = 1, 
	variable = mouse_frame_checkbox_var, 
	command = complete_check
	)
mouse_frame_checkbox.pack(side = 'left')
mouse_frame_label.pack(side = 'left', padx = 20)

calendar_frame = tk.Frame(window, highlightbackground="blue", highlightthickness = 1)
calendar_frame_label = ttk.Label(calendar_frame, 
	text =	'''
	【オプション】Google Calendarをチェック
	'''
	)
calendar_frame_checkbox_var = tk.IntVar(value = 1)
calendar_frame_checkbox = ttk.Checkbutton(
	calendar_frame, 
	text = 'Completed?', 
	onvalue = 0, 
	offvalue = 1, 
	variable = calendar_frame_checkbox_var, 
	command = complete_check
	)
calendar_frame_checkbox.pack(side = 'left')
calendar_frame_label.pack(side = 'left', padx = 20)

okta_frame = tk.Frame(window, highlightbackground="blue", highlightthickness = 1)
okta_frame_label = ttk.Label(okta_frame, 
	text ='''
	【オプション】Okta設定&パスワード変更
	※90日ごと変更必須。変更後は必ず
	WiFiとPCに新PWで入り直してください。
	'''
	)
okta_frame_checkbox_var = tk.IntVar(value = 1)
okta_frame_checkbox = ttk.Checkbutton(
	okta_frame, 
	text = 'Completed?', 
	onvalue = 0, 
	offvalue = 1, 
	variable = okta_frame_checkbox_var, 
	command = complete_check
	)
okta_frame_checkbox.pack(side = 'left')
okta_frame_label.pack(side = 'left', padx = 20)

complete = ttk.Button(window, text = 'Finshed!', state = 'disabled', command = lambda: root.quit())

window.pack(expand = True, fill = 'both')

welcome.pack()

intranet_frame.pack(expand = True, fill = 'both')
gmailsig_frame.pack(expand = True, fill = 'both')
pfp_frame.pack(expand = True, fill = 'both')
security_frame.pack(expand = True, fill = 'both')
HR_frame.pack(expand = True, fill = 'both')
salary_frame.pack(expand = True, fill = 'both')
workday_frame.pack(expand = True, fill = 'both')
mieshi_frame.pack(expand = True, fill = 'both')
amex_frame.pack(expand = True, fill = 'both')
mouse_frame.pack(expand = True, fill = 'both')
calendar_frame.pack(expand = True, fill = 'both')
okta_frame.pack(expand = True, fill = 'both')


complete.pack(pady = 20)

loader()

root.mainloop()