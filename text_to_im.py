from PIL import Image, ImageDraw, ImageFont

def text_to_ascii_image(text, output_image_path, font_size=4):

    font = ImageFont.load_default()

    lines = text.splitlines()
    max_line_length = max([len(line) for line in lines])

    char_width, char_height = font.getsize("A")

    image_width = char_width * max_line_length
    image_height = char_height * len(lines)

    image = Image.new('RGB', (image_width, image_height), color='white')
    draw = ImageDraw.Draw(image)

    y = 0
    for line in lines:
        draw.text((0, y), line, font=font, fill='black')
        y += char_height

    image.save(output_image_path)

def main():
    input_text_file = "out.txt"
    output_image_path = "output.png"

    with open(input_text_file, 'r') as file:
        text = file.read()

    text_to_ascii_image(text, output_image_path)

if __name__ == "__main__":
    main()
