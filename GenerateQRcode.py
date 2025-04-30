
import qrcode
import os

# 定义页面映射：键为文件名，值为页面 URL
pages = {
    'Level1': 'https://tadeqin.github.io/MixedRealityQR/Level1.html',
    'Level2': 'https://tadeqin.github.io/MixedRealityQR/Level2.html',
    'Level3': 'https://tadeqin.github.io/MixedRealityQR/Level3.html',
    'Level4': 'https://tadeqin.github.io/MixedRealityQR/Level4.html'
}
os.makedirs(r'.\out', exist_ok=True)
# 生成并保存二维码图片
for name, url in pages.items():
    img = qrcode.make(url)
    img.save(rf'.\out\{name}.png')
    print(f"Saved QR code for {url} as {name}.png")
