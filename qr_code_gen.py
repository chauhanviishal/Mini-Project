import qrcode

def generate_qr_code(data, file_name="qr_code.png"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_name)

if __name__ == "__main__":
    # text_or_url = "https://www.ps4wallpapers.com/wp-content/uploads/2021/06/2021-06-17_60cb51028e747_wp4409290.png" 
    text_or_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  
    # text_or_url = "https://www.google.com/" 
    # text_or_url = ""
    # text_or_url = ""
    qr_code_file = "generated_qr_code.png"   # Output file name for the QR code image
    generate_qr_code(text_or_url, qr_code_file)
    print(f"QR code generated and saved as '{qr_code_file}'")
