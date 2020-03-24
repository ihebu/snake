def write(font, color, text, window, pos, align=True):
    text = font.render(text, True, color)
    if align:  # align the text vertically
        text_width = text.get_width()
        pos = (pos[0] - text_width / 2, pos[1])
    window.blit(text, pos)


def write_screen_stats(font, color, window, score, high_score):
    c = 10
    words = [
        "Score : " + str(score),
        "High Score : " + str(high_score),
        "Press P to pause/continue",
    ]
    for word in words:
        write(font, color, word, window, (10, c), align=False)
        c += 20


def write_on_lose(font, color, window, score):
    width = window.get_width()
    height = window.get_height()
    c = height / 2
    words = ["You Lose", "Score : " + str(score), "Play Again ?", "Y / N"]
    for word in words:
        write(font, color, word, window, (width / 2, c))
        c += 25


def write_on_pause(font, color, window):
    width = window.get_width()
    height = window.get_height()
    c = height / 2
    words = ["Game Paused", "Press P to continue"]
    for word in words:
        write(font, color, word, window, (width / 2, c))
        c += 20


def get_high_score():
    try:
        with open("high_score.txt") as file:
            high_score = int(file.read())
            return high_score
    except:
        return 0


def set_high_score(score):
    with open("high_score.txt", "w") as file:
        file.write(str(score))
