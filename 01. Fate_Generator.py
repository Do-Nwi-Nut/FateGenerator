import tkinter as tk
import random
from tkinter import font

class KeywordApp:
    def __init__(self, master):
        self.master = master
        master.title("Keyword Generator")

        self.custom_font = font.Font(family='NotoSansCJKjp-Light.otf', size=10)
        self.title_font = font.Font(family='NotoSansCJKjp-Light.otf', size=12)
        self.custom_symbol_font = font.Font(family='NotoSansCJKjp-Light.otf', size=15)  # 여기서 폰트 크기 조정

        # Hide the default title bar
        master.overrideredirect(True)

        self.title_bar = tk.Frame(master, bg='#202124', relief='raised', bd=2)
        self.title_bar.pack(fill=tk.X)

        self.title_label = tk.Label(self.title_bar, text="[운명 생성기]", bg='#202124', fg='white', font=self.title_font)
        self.title_label.pack(side=tk.LEFT, padx=10)

        self.close_button = tk.Button(self.title_bar, text="X", command=master.quit, bg='#202124', fg='white', bd=0, font=self.title_font)
        self.close_button.pack(side=tk.RIGHT)

        self.maximize_button = tk.Button(self.title_bar, text="🗖", command=self.toggle_maximize, bg='#202124', fg='white', bd=0, font=self.title_font)
        self.maximize_button.pack(side=tk.RIGHT)

        self.minimize_button = tk.Button(self.title_bar, text="-", command=master.iconify, bg='#202124', fg='white', bd=0, font=self.title_font)
        self.minimize_button.pack(side=tk.RIGHT, padx=5)

        self.title_bar.bind("<B1-Motion>", self.move_window)

        self.content_frame = tk.Frame(master, bg='#202124', padx=0)
        self.content_frame.pack(fill=tk.BOTH, expand=True, pady=(2, 0))

        self.keyword_labels = []
        self.symbol_labels = []

        for i in range(6):
            keyword_label = tk.Label(self.content_frame, text="", bg='#202124', fg='white', font=self.title_font)
            keyword_label.grid(row=i, column=1, pady=5)
            self.keyword_labels.append(keyword_label)

            symbol_label = tk.Label(self.content_frame, text="", bg='#202124', fg='white', font=self.custom_symbol_font, anchor=tk.CENTER)  # 여기서 폰트 크기 조정
            symbol_label.grid(row=i, column=2, pady=5)
            self.symbol_labels.append(symbol_label)

            # Add an empty label for spacing
            spacer_label = tk.Label(self.content_frame, text="", bg='#202124', fg='white', font=self.title_font)
            spacer_label.grid(row=i, column=0, padx=0)

        self.create_button = tk.Button(self.content_frame, text="운명 생성", command=self.create_keywords, width=10, bg='#3c4043', fg='white', activebackground='#5f6368', activeforeground='white', font=self.custom_font)
        self.create_button.grid(row=6, column=0, pady=5)

        self.shuffle_button = tk.Button(self.content_frame, text="운명 섞기", command=self.shuffle_keywords, width=10, bg='#3c4043', fg='white', activebackground='#5f6368', activeforeground='white', font=self.custom_font)
        self.shuffle_button.grid(row=6, column=1, pady=5)

        self.quit_button = tk.Button(self.content_frame, text="종료", command=master.quit, width=10, bg='#3c4043', fg='white', activebackground='#5f6368', activeforeground='white', font=self.custom_font)
        self.quit_button.grid(row=6, column=2, pady=5)

        self.keywords = ["치유", "순수", "이성", "질서", "지혜", "서약", "선량", "범죄", "성실", "생명", "관용", "해방", "조화", "창조", "신뢰", "정직", "변화", "결합", "엄격", "용기", "행운", "비호", "추락", "자애", "절단", "속임수", "구원", "무지", "탐욕", "분실"]
        self.symbols = ['🌱', '🌿', '☘️', '🍃', '🍂', '🍁', '🍄', '🌰', '🌳', '🌲', '🌴', '🌵', '🌷', '🌹', '🌺', '🌻', '🌼', '💐', '🌸', '🌎', '🌍', '🌏', '💫', '🔥', '⚡', '🌙', '🌟', '⭐', '🌠', '🌌', '☄️', '💥', '🌈', '☁️', '⛅', '🌤', '🌥', '🌦', '🌧', '🌨', '🌩', '🌪', '🌫', '🌬', '🌀', '☔', '☂️', '⚡', '🔥', '💧', '💦', '☘', '🍓', '🍒', '🍎', '🍏', '🍊', '🍋', '🍌', '🍉', '🍇', '🍈', '🍑', '🍐', '🍍', '🥝', '🥥', '🥑', '🌶', '🥒', '🥕', '🥔', '🥜', '🥐', '🥖', '🥞', '🥨', '🥚', '🍳', '🥘', '🍲', '🥫', '🌮', '🍕', '🍘', '🍙', '🍚', '🍛', '🍜', '🍝', '🍠', '🍢', '🍣', '🍤', '🍥', '🥮', '🍡', '🥟', '🥠', '🥡', '🍦', '🍧', '🍨', '🍩', '🍪', '🎂', '🍰', '🥤', '🍫', '🍬', '🍭', '🍮', '🍯', '🍼', '🥛', '☕', '🍵', '🍾', '🍷', '🍸', '🍹', '🍺', '🍻', '🥂', '🥃', '🍽', '🍴', '🥄', '🔪', '🥇', '🥈', '🥉', '🏅', '🎖', '🏆', '🎫', '🎟', '🎼', '🎵', '🎶', '🎧', '🎤', '🎬', '🎭', '🎨', '🎰', '🎲', '🔇', '🔈', '🔉', '🔊', '📢', '📣', '📯', '🔔', '🔕', '🎷', '🎸', '🎹', '🎺', '🎻', '📻', '📱', '📲', '☎️', '📞', '📟', '📠', '🔋', '🔌', '💻', '💽', '💾', '💿', '📀', '🎥', '🎞', '📽', '🎬', '📺', '📷', '📸', '📹', '📼', '🔍', '🔎', '🔬', '🔭', '📡', '🕯', '🔦', '🏮', '📔', '📕', '📖', '📗', '📘', '📙', '📚', '📓', '📒', '📃', '📜', '📄', '📰', '🗞', '📑', '🔖', '🏷', '💰', '💴', '💵', '💶', '💷', '💸', '💳', '💹', '💱', '💲', '✉️', '📧', '📨', '📩', '📤', '📥', '📦', '📫', '📪', '📬', '📭', '📮', '🗳', '✏️', '✒️', '📝', '📁', '📂', '📅', '📆', '📇', '📈', '📉', '📊', '📋', '📌', '📍', '📎', '📏', '📐', '✂️', '🗃', '🗄', '🗑', '🔒', '🔓', '🔏', '🔐', '🔑', '🗝', '🔨', '🔫', '⛏', '⚒', '⛓', '🔗', '⚔', '🗡', '🔪', '⚙', '⚖', '⛓', '🗜', '⚗', '⚘', '⚖', '⚔', '⚰', '⚱', '+', '-', '×', '÷', '=', '<', '>', '≤', '≥', '≠', '±', '∓', '∕', '∙', '√', '∛', '∜', '∝', '∞', '∟', '∩', '∪', '∫', '∴', '∵', '∷', '∼', '≃', '≅', '≈', '≡', '⋆', '⋘', '⋙', '⋚', '⋛', '⋜', '⋝', '⋞', '⋟', '⋠', '⋡', '⋢', '⋣', '⋪', '⋫', '⋬', '⋭', '⋲', '⋳', '¬', '∧', '∨', '∃', '∄', '∁', '∃', '⊂', '⊃', '⊆', '⊇', 'ก', 'ข', 'ฃ', 'ค', 'ฅ', 'ฆ', 'ง', 'จ', 'ฉ', 'ช', 'ซ', 'ฌ', 'ญ', 'ฎ', 'ฏ', 'ฐ', 'ฑ', 'ฒ', 'ณ', 'ด', 'ต', 'ถ', 'ท', 'ธ', 'น', 'บ', 'ป', 'ผ', 'ฝ', 'พ', 'ฟ', 'ภ', 'ม', 'ย', 'ร', 'ฤ', 'ล', 'ฦ', 'ว', 'ศ', 'ษ', 'ส', 'ห', 'ฬ', 'อ', 'ฮ']
        self.selected_keywords = []

    def move_window(self, event):
        self.master.geometry(f'+{event.x_root}+{event.y_root}')

    def toggle_maximize(self):
        if self.master.state() == "zoomed":
            self.master.state('normal')
        else:
            self.master.state('zoomed')

    def create_keywords(self):
        self.selected_keywords = random.sample(self.keywords, 6)
        self.show_keywords()

    def shuffle_keywords(self):
        random.shuffle(self.selected_keywords)
        self.show_keywords()

    def show_keywords(self):
        labels = ["주인공의 현재:", "주인공의 가까운 미래:", "주인공의 과거:", "조력자:", "적:", "결말:"]
        for i in range(6):
            keyword = self.selected_keywords[i]
            symbol = random.choice(self.symbols)
            if random.random() < 0.5:  # 확률적으로 '-'를 붙일지 결정 (예: 50% 확률)
                keyword = '-' + keyword
            self.keyword_labels[i].config(text=labels[i] + ' ' + keyword.rjust(15, ' '))
            self.symbol_labels[i].config(text=symbol)

root = tk.Tk()
app = KeywordApp(root)
root.mainloop()