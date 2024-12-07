from pywebio import start_server
from pywebio.input import input
from pywebio.output import put_text, put_image, put_button
import qrcode
from io import BytesIO

def app():
    put_text("مرحبًا! أدخل رابطًا لتحويله إلى باركود.")
    
    # إدخال الرابط
    url = input("أدخل الرابط:", type="text", placeholder="https://example.com")
    
    if url:
        # إنشاء باركود
        qr = qrcode.QRCode(version=1, box_size=10, border=4)
        qr.add_data(url)
        qr.make(fit=True)
        
        img = qr.make_image(fill="black", back_color="white")
        
        # حفظ الصورة في الذاكرة
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)
        
        # عرض الباركود
        put_text("تم إنشاء الباركود بنجاح!")
        put_image(buffer.getvalue(), width="300px")
        
        # عرض زر لتحميل الصورة
        put_button("تحميل الباركود", onclick=lambda: download_barcode(buffer))

def download_barcode(buffer):
    buffer.seek(0)
    from pywebio.output import download
    return download("barcode.png", buffer.getvalue())

start_server(app, port=34345, debug=True)
