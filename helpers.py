def write(font, color, text, window, pos, align=True):
    text = font.render(text, True, color)
    if align:  # align the text vertically
        text_width = text.get_width()
        pos = (pos[0] - text_width / 2, pos[1])
    window.blit(text, pos)


def write_screen_stats(font, color, window, score):
    write(font, color, f"Score : {score}", window, (10, 10), align=False)


def write_on_lose(font, color, window):
    width = window.get_width()
    height = window.get_height()
    c = height / 2
    write(font, color, "Play Again ? ( Y / N )", window, (width / 2, c))
