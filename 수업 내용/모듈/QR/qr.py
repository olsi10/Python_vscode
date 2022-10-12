import qrcode

qr_d = 'www.naver.com'
qr_i = qrcode.make(qr_d)

save_path = qr_d + '.png'

qr_i.save(save_path)