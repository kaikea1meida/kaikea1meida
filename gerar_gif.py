from PIL import Image, ImageDraw, ImageFont

frame1 = [
    "    ..                     ..     ",
    "  pd' .g8\"\"8q.     .g8\"\"8q. `bq   ",
    " 6P .dP'    `YM. .dP'    `YM. YA  ",
    "6M' dM'      `MM dM'      `MM `Mb ",
    "MN  MM        MM MM        MM  8M ",
    "MN  MM.      ,MP MM.      ,MP  8M ",
    "YM. `Mb.    ,dP' `Mb.    ,dP' ,M9 ",
    " Mb   `\"bmmd\"'     `\"bmmd\"'   dM  ",
    "  Yq.                       .pY   ",
    "    ``                     ''     "
]

frame2 = [
    "    ..                    ..      ",
    "  pd'                      `bq    ",
    " 6P                          YA   ",
    "6M'                          `Mb  ",
    "MN                            8M  ",
    "MN mmmmmmmmmmm    mmmmmmmmmmm 8M  ",
    "YM.                          ,M9  ",
    " Mb                          dM   ",
    "  Yq.                      .pY    ",
    "    ``                    ''      "
]

def create_ascii_gif(frames, filename="animacao_jogo.gif"):
    images = []
    width, height = 480, 240
    bg_color = (13, 17, 23, 255)
    text_color = (201, 209, 217, 255)
    
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", 14)
    except:
        font = ImageFont.load_default()

    for frame_lines in frames:
        img = Image.new("RGBA", (width, height), bg_color)
        d = ImageDraw.Draw(img)
        
        y = 35
        for line in frame_lines:
            d.text((30, y), line, fill=text_color, font=font)
            y += 16
            
        images.append(img)
    
    images[0].save(
        filename,
        save_all=True,
        append_images=images[1:],
        optimize=False,
        duration=400,
        loop=0
    )
    print("GIF gerado com sucesso!")

if __name__ == "__main__":
    create_ascii_gif([frame1, frame2])