import cv2
import numpy as np
import gradio as gr

# Mavi renk dışında her şeyi griye çeviren filtre
def apply_blue_isolation(frame, lower_color1=(0, 100, 100), upper_color1=(10, 255, 255), lower_color2=(160, 100, 100), upper_color2=(180, 255, 255)):
    # Görüntüyü HSV renk uzayına dönüştür
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Mavi rengi maskelemek için iki ayrı aralık kullanıyoruz
    mask1 = cv2.inRange(hsv, lower_color1, upper_color1)
    mask2 = cv2.inRange(hsv, lower_color2, upper_color2)
    mask = cv2.bitwise_or(mask1, mask2)

    # Görüntüyü gri tonlarına çevir
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame_colored = cv2.cvtColor(gray_frame, cv2.COLOR_GRAY2BGR)

    # Mavi alanları koruyup diğer bölgeleri gri yap
    output = np.where(mask[:, :, None] != 0, frame, gray_frame_colored)

    return output

# Gradio arayüzü tanımlanıyor
with gr.Blocks() as demo:
    gr.Markdown("## Mavi Renk Dışında Her Şeyi Griye Çevirme Uygulaması")
    gr.Markdown(
        "Bu uygulama, yüklediğiniz görüntüde mavi renkte olan bölgeleri koruyup, diğer renkleri gri tonlarına çevirir."
    )

    # Kullanıcıdan resim yüklemesi beklenen alan
    input_image = gr.Image(label="Bir Görüntü Yükleyin", type="numpy")

    # Uygulanan filtre sonucu gösterilen çıktı görüntüsü
    output_image = gr.Image(label="Filtre Sonucu")

    # Görüntü yüklendiğinde filtre fonksiyonunu çağırır
    input_image.upload(fn=apply_blue_isolation, inputs=input_image, outputs=output_image)

# Gradio arayüzünü başlatır
demo.launch()



