def get_high_score():
    try:
        with open("high_score.txt") as f:
            high_score = int(f.read())
            return high_score
    except:
        return 0


def set_high_score(score):
    with open("high_score.txt", "w") as f:
        f.write(str(score))


def write(font, color, text, window, pos, align=True):
    text = font.render(text, True, color)
    if align:  # align the text vertically
        text_width = text.get_width()
        pos = (pos[0] - text_width / 2, pos[1])
    window.blit(text, pos)


def write_screen_stats(font, color, window, score, high_score):
    words = [
        f"Score : {score}",
        f"High Score : {high_score}",
        "Press P to pause/continue",
    ]
    for i in range(3):
        write(font, color, words[i], window, (10, 10 + 20 * i), align=False)


def write_on_lose(font, color, window):
    width = window.get_width()
    height = window.get_height()
    c = height / 2
    words = ["You Lose", "Play Again ? [Y / N ]"]
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
