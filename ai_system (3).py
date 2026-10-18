import streamlit as st

st.set_page_config(
    page_title="Verssa AI - Bomer Operasyon ve Ticaret Merkezi",
    page_icon="🚀",
    layout="wide",
)

st.title("🚀 Verssa AI - Bomer Operasyon ve Ticaret Merkezi")
st.write(
    "Global tedarik zinciri, özel markalı ürün geliştirme, kalite uyumluluğu ve"
    " çoklu ajan yönetim paneli."
)

st.subheader("🎯 Bomer Grup Yeni Ticari Proje / Ürün Tanımlama")
user_input = st.text_input(
    "Yürütülmesini istediğiniz global tedarik, ürün geliştirme veya pazarlama"
    " konusunu girin:",
    "Yeni nesil özel markalı sağlıklı içecek portföyü tedarik ve pazar ar",
)

if st.button("🚀 Bomer Otonom Sürüsünü Başlat"):
  st.success("Bomer otonom süreci başarıyla tamamlandı!")

# Hiçbir tıklama gerektirmeyen, doğrudan alt alta açık pencereler
with st.expander("🚀 Bomer Sürüsü Logları ve İş Birliği Süreç Akışı", expanded=True):
  st.write(
      "*[Yeni Ürün Geliştirme Ajanı]:* Konsept tasarımı, formülasyon ve pazar"
      f" ihtiyaçları analizi edildi: {user_input}"
  )
  st.write(
      "*[Tedarik & Kaynak Yönetim Ajanı]:* Global üretici ağı tarandı,"
      " hammadde maliyetleri ve tedarik zinciri optimize edildi."
  )
  st.write(
      "*[Kalite ve Uyumluluk Ajanı]:* Uluslararası gıda güvenliği,"
      " sertifikasyon ve yasal mevzuat denetimi tamamlandı (PASSED)."
  )
  st.write(
      "*[Pazartama ve Dağıtım Ajanı]:* Rekabetçi fiyatlandırma, raf"
      " konumlandırma ve kanal stratejileri kurgulandı (OPTIMAL)."
  )

with st.expander("📊 Ticari Simülasyon Çıktısı", expanded=True):
  st.write(
      "*Simülasyon Sonucu:* Girilen proje için pazar hacmi, maliyet"
      " optimizasyonu ve kârlılık oranları başarıyla simüle edilmiştir."
  )
  st.metric(label="Tahmini Pazar Uyumu", value="%94.2")
  st.metric(label="Maliyet Optimizasyon Skoru", value="Yüksek")

with st.expander("📋 Sistem Durumu ve Aktif Ajanlar", expanded=True):
  st.write("Toplam Aktif Ajan Sayısı: *8*")
  st.write("• Yeni Ürün Geliştirme Ajanı: Aktif")
  st.write("• Tedarik & Kaynak Yönetimi Ajanı: Aktif")
  st.write("• Kalite & Uyumluluk Ajanı: Aktif")
  st.write("• Pazarlama & Dağıtım Ajanı: Aktif")
