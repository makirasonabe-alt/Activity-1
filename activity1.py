from PIL import Image, ImageDraw, ImageFont

# Create a blank white canvas (500x500 pixels)
canva = Image.new("RGB", (500,500), "white")
draw = ImageDraw.Draw(canva)

# Load fonts with different sizes
font_path = ImageFont.truetype("Poppins/Poppins-Black.ttf", 22)
font_first = ImageFont.truetype("Poppins/Poppins-Black.ttf", 14)

# Add text captions on the canvas
draw.text((26, 25), "POV: naay gibilin activity inyong teacher pag\n intrams", 14, font=font_path)
draw.text((26, 80), "Sila pag intrams", 22, font=font_path)
draw.text((178, 305), "Ako", 22, font=font_path)

# Open images
image1 = Image.open("image1.png")
image2 = Image.open("image3.png")
image3 = Image.open("image4.png")
image4 = Image.open("image2.png")
image5 = Image.open("cramming-study.jpg")

# Resize images to fit layout
rimage1 = image1.resize((184, 263))
rimage2 = image2.resize((215, 263))
rimage3 = image3.resize((178, 263))
rimage4 = image4.resize((208, 198))
rimage5 = image5.resize((267, 218))

# Paste images onto the canvas at specific positions
canva.paste(rimage1, (-31, 120), rimage1)
canva.paste(rimage2, (77, 42), rimage2)
canva.paste(rimage3, (190, 40), rimage3)
canva.paste(rimage4, (292, 94), rimage4)
canva.paste(rimage5, (242, 282))

# Show the result
canva.show()

# Save the final output as PNG
canva.save("CSELEC3_BSCS3A_RasonabeMarkNino_Activity1.png")
