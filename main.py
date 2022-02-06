from unicodedata import name
import qrcode


def get_qrcode(url='https://google.com', name='default'):
    """QR code generator"""
    
    qr = qrcode.make(data=url)
    qr.save(stream=f'qr_codes/{name}.png')
    
    return f'QR code was created! Open the {name}.png'


def main():
    print(get_qrcode(url='https://www.youtube.com/c/PythonToday/videos', name='youtube'))
    print(get_qrcode(url='https://instagram.com', name='instagram'))
    
    
if __name__ == '__main__':
    main()
