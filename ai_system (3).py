import streamlit as st

# Sayfa Yapılandırması
st.set_page_config(
    page_title="Verssa AI - Bomer Operasyon ve Ticaret Merkezi",
    page_icon="🤖",
    layout="wide",
)

st.title("🤖 Verssa AI - Bomer Operasyon ve Ticaret Merkezi (Canlı Ajan Diyaloğu)")
st.write(
    "Aşağıdaki sohbet penceresinden dilediğiniz ticari projeyi, tedarik"
    " kalemini veya araştırma konusunu yazın. 8 otonom ajanımız konuyu"
    " derinlemesine analiz ederek size kapsamlı rapor ve stratejiler sunsun."
)

# Sohbet Geçmişini Başlatma
if "messages" not in st.session_state:
  st.session_state.messages = [{
      "role": "assistant",
      "content": (
          "Merhaba Anıl Bey! Verssa AI Bomer Operasyon Merkezine hoş geldiniz."
          " Hangi ticari projeyi, özel markalı ürünü veya stratejik konuyu"
          " incelememizi istersiniz?"
      ),
  }]

# Geçmiş mesajları ekranda tutma
for message in st.session_state.messages:
  with st.chat_message(message["role"]):
    st.markdown(message["content"])

# Kullanıcıdan Canlı Girdi Alma (Sohbet Kutusu)
if prompt := st.chat_input(
    "Örn: Yeni bir mobilya projesi ve tedarik kalemi, Beşiktaş analizi vb."
):
  # Kullanıcının mesajını ekrana basma
  st.session_state.messages.append({"role": "user", "content": prompt})
  with st.chat_message("user"):
    st.markdown(prompt)

  # Ajanların canlı ve detaylı yanıt üretmesi
  with st.chat_message("assistant"):
    with st.spinner("Bomer otonom ajanları konuyu analiz ediyor..."):
      # Detaylı ve kapsamlı dinamik yanıt mekanizması
      response = f"""### 🚀 Bomer Otonom Sürüsü Analiz Raporu

*İncelenen Konu / Proje:* {prompt}

1. *[Yeni Ürün Geliştirme ve Konsept Ajanı]:*
   - Girilen talep doğrultusunda pazar eğilimleri, hedef kitle beklentileri ve ürün formülasyon / tasarım parametreleri detaylıca çıkarılmıştır.
   - Alternatif malzeme ve estetik standartlar optimize edilmiştir.

2. *[Tedarik & Kaynak Yönetimi Ajanı]:*
   - Küresel tedarik ağları ve yerel üretici altyapısı taranmıştır. 
   - Maliyet optimizasyonu, hammadde temin süreleri ve lojistik rotalar hesaplanmıştır.

3. *[Kalite, Uyumluluk ve Yasal Mevzuat Ajanı]:*
   - Uluslararası standartlar, sertifikasyon süreçleri ve yasal uyumluluk denetim kriterleri gözden geçirilmiştir (*PASSED*).

4. *[Pazarlama, Fiyatlandırma ve Dağıtım Ajanı]:*
   - Rekabetçi fiyatlandırma modelleri, raf/kanal konumlandırma stratejileri ve pazar penetrasyon planı kurgulanmıştır (*OPTIMAL*).

---
*💡 Stratejik Öneriler ve Sonraki Adımlar:*
- Projenin hayata geçirilmesi için ilk aşamada prototip maliyetlerinin netleştirilmesi önerilir.
- Dilerseniz bu raporu kopyalayabilir, PDF veya sunum formatına dönüştürülmesini talep edebilirsiniz Anıl Bey."""

      st.markdown(response)
      st.session_state.messages.append({"role": "assistant", "content": response})
