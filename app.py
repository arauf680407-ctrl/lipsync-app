import streamlit as st
import time
import requests

st.set_page_config(
    page_title="Lip Sync Generator AI",
    page_icon="🎬",
    layout="centered"
)

st.title("🎬 Lip Sync Video Generator")
st.markdown("Aplikasi generator untuk menyelaraskan pergerakan bibir wajah dengan file suara/audio.")

# Sidebar untuk konfigurasi API Key
with st.sidebar:
    st.header("⚙️ Pengaturan API")
    api_provider = st.selectbox(
        "Pilih Layanan AI API",
        ["Replicate (Wav2Lip)", "D-ID", "Sync Labs"]
    )
    
    api_key = st.text_input(
        f"Masukkan {api_provider} API Key",
        type="password",
        help="Dapatkan API Key dari dashboard layanan yang Anda pilih."
    )
    
    st.info("💡 **Tips Pemula:** Menggunakan Replicate atau D-ID sangat direkomendasikan karena menyediakan kredit gratis untuk uji coba.")

# Area Upload File
st.subheader("1. Unggah Media")
col1, col2 = st.columns(2)

with col1:
    st.markdown("**Karakter / Wajah**")
    uploaded_image = st.file_uploader(
        "Pilih foto atau video (JPG, PNG, MP4)",
        type=["jpg", "jpeg", "png", "mp4"]
    )
    if uploaded_image:
        if uploaded_image.name.endswith(('.mp4')):
            st.video(uploaded_image)
        else:
            st.image(uploaded_image, caption="Media Karakter Loaded", use_container_width=True)

with col2:
    st.markdown("**Audio Suara**")
    uploaded_audio = st.file_uploader(
        "Pilih file suara (MP3, WAV)",
        type=["mp3", "wav"]
    )
    if uploaded_audio:
        st.audio(uploaded_audio)

st.divider()

# Tombol Eksekusi Generator
st.subheader("2. Proses Lip Sync")

if st.button("🚀 Generate Video Lip Sync", type="primary", use_container_width=True):
    if not api_key:
        st.error("⚠️ Silakan masukkan API Key Anda di menu sidebar kiri terlebih dahulu!")
    elif not uploaded_image or not uploaded_audio:
        st.warning("⚠️ Silakan lengkapi media karakter dan audio suara sebelum memproses!")
    else:
        with st.status("Sedang memproses Lip Sync AI...", expanded=True) as status:
            st.write("📤 Mengunggah berkas ke server AI...")
            time.sleep(1.5)
            
            st.write("🧬 Menganalisis titik wajah dan sinkronisasi gelombang suara...")
            time.sleep(2)
            
            st.write("🎬 Meng-generate kerangka video lip sync...")
            time.sleep(2)
            
            # Simulasi Integrasi API
            # Pada implementasi produksi, request HTTP API dikirimkan di sini
            status.update(label="✅ Proses Lip Sync Selesai!", state="complete", expanded=False)
            
        st.success("Video berhasil dibuat!")
        
        # Output Hasil (Placeholder contoh / integrasi hasil API)
        st.subheader("Hasil Video:")
        st.video("https://www.w3schools.com/html/mov_bbb.mp4")
        
        st.download_button(
            label="📥 Download Video Hasil",
            data=b"dummy_video_data",
            file_name="lipsync_result.mp4",
            mime="video/mp4"
        )