import streamlit as st
import pandas as pd
import os

# Konfigurasi Halaman
st.set_page_config(page_title="Katalog Anggrek", layout="wide")
st.markdown("""
<style>

/* Background */
.stApp {
    background-color: #F8BBD0;
}

/* Semua teks utama */
.stApp, .stApp p, .stApp span, .stApp div {
    color: #880E4F !important;
}

/* Judul utama */
h1 {
    color: #F33A77 !important;
}

/* Header kategori */
h2 {
    color: #C71585 !important;
}

/* NAMA PRODUK (INI YANG PENTING) */
[data-testid="stMarkdownContainer"] h3 {
    color: #AD1457 !important;
}

/* Harga */
[data-testid="stMarkdownContainer"] h3 strong {
    color: #2E7D32 !important;
}

/* Status */
[data-testid="stMarkdownContainer"] p {
    color: #880E4F !important;
}

hr {
    border-color: #F33A77 !important;
}
.stButton > button {
    background-color: white !important;
    color: #880E4F !important;
    border: 2px solid #F33A77 !important;
    border-radius: 12px !important;
    font-weight: bold !important;
}

</style>
""", unsafe_allow_html=True)

# 1. Tampilkan Banner Canva
if os.path.exists("anggrekku.png"):
    st.image("anggrekku.png", use_container_width=True)

st.title("🌸 Dendro Garden")
st.divider()

try:
    if os.path.exists("data_anggrek1.csv"):
        df = pd.read_csv("data_anggrek1.csv")
        df = df.dropna(subset=['foto'])
        
        daftar_kategori = df['kategori'].unique()
        
        for kat in daftar_kategori:
            st.header(f"🌿 Anggrek Jenis {kat.capitalize()}")
            data_per_kat = df[df['kategori'] == kat]
            
            cols = st.columns(4)
            
            for index, row in data_per_kat.reset_index().iterrows():
                nama_foto = str(row['foto']).strip()
                
                with cols[index % 4]:
                    if os.path.exists(nama_foto):
                        st.image(nama_foto, use_container_width=True)
                        st.subheader(row['nama'])
                        
                        # --- HARGA & STATUS DENGAN FONT LEBIH BESAR ---
                        st.markdown(f"### **Rp {row['harga']:,}**") 
                        st.markdown(f"**Status:** {row['status']}")
                    else:
                        st.warning(f"Foto {nama_foto} tidak ditemukan")
            st.divider()
            
    else:
        st.error("File 'data_anggrek1.csv' tidak ditemukan!")

except Exception as e:
    st.error(f"Terjadi kesalahan: {e}")

st.divider()
st.header("🌱Tips Perawatan Anggrek")

with st.expander("📹Video Tutorial"):
    st.video("https://youtu.be/hLxmGAFebxM?si=4A52-sJ_d_GlPMwz")

# --- BAGIAN KONTAK & ALAMAT (FOOTER) ---
st.write("") # Memberi ruang kosong
st.write("")
st.divider()
st.subheader("📍 Hubungi Kami")
col_info1, col_info2 = st.columns(2)

with col_info1:
    st.markdown("""
    **Alamat Galeri:** Jl. C. Simanjuntak No. 60,  
    Terban, Kecamatan Gondokusuman, Kota Yogyakarta,  
    Daerah Istimewa Yogyakarta.
    """)

with col_info2:
    # Ganti nomor HP di bawah ini dengan nomor Anda (gunakan format 62)
    no_hp = "6288980183889" 
    pesan_wa = "Halo, saya tertarik memesan anggrek di katalog Anda."
    link_wa = f"https://wa.me/{no_hp}?text={pesan_wa.replace(' ', '%20')}"
    
    st.markdown(f"**WhatsApp:**")
    st.link_button("📱 Pesan Sekarang via WhatsApp", link_wa)

st.caption("© 2026 Toko Anggrek Digital - Semua Hak Dilindungi")
