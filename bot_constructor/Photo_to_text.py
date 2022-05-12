import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def Photo_to_text(path):
	img = cv2.imread(path)
	img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
	config = r'--oem 3 --psm 6'
	data = pytesseract.image_to_data(img, config=config)
	for i, el in enumerate(data.splitlines()):
		if i == 0:
			continue
		el = el.split()
	return pytesseract.image_to_string(img, config=config)

#print(Photo_to_text('F:/Python/bot_constructor/Files/AgACAgIAAxkBAAPOYmmAJxBlXTu6W3Go9uYOf19yunEAAn28MRszfklLsScjo-CWmsIBAAMCAANtAAMkBA.png'))