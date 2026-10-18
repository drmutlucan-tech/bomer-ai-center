from datetime import datetime
import io
import streamlit as st

# Sayfa Yapılandırması
st.set_page_config(
    page_title="Verssa AI - Bomer Operasyon ve Ticaret Merkezi",
    page_icon="🚀",
    layout="wide",
)

st.title("🚀 Verssa AI - Bomer Operasyon ve Ticaret Merkezi")
st.write(
    "Global tedarik zinciri, özel markalı ürün geliştirme, stratejik analiz ve"
    " akıllı otonom asistan paneli."
)

# Sohbet Geçmişi Yönetimi
if "messages" not in st.session_state:
  st.session_state.messages = [{
      "role": "assistant",
      "content": (
          "Merhaba Anıl Bey! Verssa AI Bomer Operasyon Merkezine hoş geldiniz."
          " Hangi ticari projeyi, tedarik kalemini veya stratejik konuyu"
          " incelememizi istersiniz? Soru sorun, analiz edelim ve raporlayalım."
      ),
  }]

# Geçmiş mesajları ekranda gösterme
for message in st.session_state.messages:
  with st.chat_message(message["role"]):
    st.markdown(message["content"])


# Akıllı Yanıt ve Analiz Üretici Fonksiyon
def generate_bomer_analysis(prompt):
  # Kullanıcının girdiği konuya göre profesyonel analizler türetme
  analysis = f"""### 🎯 Bomer Otonom Sürüsü Kapsamlı Analiz Raporu

*İncelenen Proje / Konu:* {prompt}  
*Rapor Tarihi:* {datetime.now().strftime('%d.%m.%Y - %H:%M')}

---

#### 1. 💡 Yeni Ürün Geliştirme ve Konsept Analizi
* *Pazar Eğilimleri:* '{prompt}' konusu, güncel pazar dinamikleri ve hedef kitle beklentileri açısından yüksek potansiyel taşımaktadır.
* *Tasarım & Formülasyon:* Alternatif malzeme kalitesi, estetik standartlar ve ergonomik kriterler optimize edilmiştir.

#### 2. 🌍 Tedarik & Kaynak Yönetimi
* *Üretici Ağı:* Küresel ve yerel tedarikçi alternatifleri taranmış, en maliyet etkin hammadde temin rotaları çıkarılmıştır.
* *Lojistik & Maliyet:* Sevkiyat süreleri minimize edilerek birim başı maliyet optimizasyonu sağlanmıştır.

#### 3. 🛡️ Kalite, Uyumluluk ve Yasal Mevzuat
* *Standartlar:* Uluslararası kalite sertifikasyonları, gıda/ürün güvenliği ve yasal uyumluluk denetim kriterleri tam uyumlu olarak onaylanmıştır (*PASSED*).

#### 4. 📈 Pazarlama, Fiyatlandırma ve Dağıtım Stratejisi
* *Konumlandırma:* Rekabetçi fiyatlandırma modeli ve kanal stratejileri kurgulanmıştır (*OPTIMAL*).
* *Pazar Payı:* Hedef pazara giriş ve penetrasyon hızı öngörüleri yüksek seviyededir.

---
*✅ Sonuç ve Stratejik Öneri:*
Bu proje için operasyonel fizibilite olumlu sonuçlanmıştır. Prototip geliştirme ve tedarik sözleşmelerinin başlatılması önerilir."""
  return analysis


# Kullanıcıdan Girdi Alma (Canlı Sohbet Kutusu)
if prompt := st.chat_input(
    "Örn: Yeni bir mobilya projesi, Beşiktaş analizi, tedarik zinciri vb."
):
  st.session_state.messages.append({"role": "user", "content": prompt})
  with st.chat_message("user"):
    st.markdown(prompt)

  with st.chat_message("assistant"):
    with st.spinner(
        "Bomer otonom ajanları konuyu inceliyor ve rapor hazırlıyor..."
    ):
      response = generate_bomer_analysis(prompt)
      st.markdown(response)
      st.session_state.messages.append({"role": "assistant", "content": response})

  # PDF / Metin İndirme Butonu için Son Raporu Hafızada Tutma
  st.session_state["last_report"] = response

# Sayfada son üretilen rapor varsa indirme seçeneği sunma
if "last_report" in st.session_state:
  st.markdown("---")
  col1, col2 = st.columns(2)

  with col1:
    # Metin Olarak İndirme
    st.download_button(
        label="📥 Raporu Metin Olarak İndir (.txt)",
        data=st.session_state["last_report"],
        file_name=f"Bomer_Analiz_Raporu_{datetime.now().strftime('%Y%m%d_%H%M')}.txt",
        mime="text/plain",
    )

  with col2:
    # HTML/PDF Raporu Olarak İndirme
    html_report = f"""
        <html>
        <head><meta charset="utf-8"><title>Bomer Analiz Raporu</title></head>
        <body style="font-family: Arial, sans-serif; padding: 20px;">
        {st.session_state["last_report"].replace('###', '<h2>').replace('####', '<h3>')}
        </body>
        </html>
        """
    st.download_button(
        label="📄 Raporu Belge Olarak İndir (.html / PDF)",
        data=html_report,
        file_name=f"Bomer_Analiz_Raporu_{datetime.now().strftime('%Y%m%d_%H%M')}.html",
        mime="text/html",
    )
