import streamlit as st
import requests
import sqlite3
import math
import json
import os

# ==========================================
# KONFIGURASI UTAMA
# ==========================================
# PERINGATAN: Gunakan st.secrets atau environment variables untuk API Key!
# Contoh: GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]

# KAMUS_DATABASE — disinkronisasi otomatis dari seluruh keywords di tb_komponen (220 Komponen)
KAMUS_DATABASE = (
    "2.4ghz, 32bit, 4g, 8 bit, 9-axis, ac, adc, adaptor, ai, air, air laut, air turun, akselerasi, akses, akses premium, aktuator mini, akuarium, akurat, "
    "akustik, alamat, alamat sama, alarm, alarm waktu, aliran, altimeter, altitude, aluminium, ambil, amonia, ampere, amplifier, analog, analog digital, "
    "analog output, android, angin, angka, angkat, animasi, anti air, anti false alarm, antarmuka, api, arah, arus, arus besar, arus bolak balik, asam, "
    "asap, asap knalpot, atap, atas, atur, atur daya, audio, awet, ayun, baca, badai, bahan kimia, bahaya, bakar, baling, banjir, banyak baris, banyak node, "
    "banyak perangkat, banyak pin, banyak sensor, barang, barcode, barometer, basa, basah, batas, baterai, bawah, beban, beku, bel pintu, belanja, bening, "
    "bentur, berat, berisik, bersih, besar, besi, biji, bilangan, biomedis, biometrik, bising, ble, blood pressure, bluetooth, bms, bocor, boom, boost converter, "
    "bpm, breadboard, broker, buck, buck converter, buffer, buka, buka kran, bangunan, bumper, bunyi, cadangan, cahaya, cair, cairan, can bus, capit, cas, cat, "
    "catu daya, cctv, celup, cepat, charge, cloud, cnc, co, co2, colok, color, counter, csv, cuaca, dahi, dapur, darah, darurat, dasar, dashboard, data, daun, "
    "daya, daya alam, dc to ac, dc to dc, debit, debu, dekat, dekorasi, demam, dengar, derajat, desa, detak, deteksi, deteksi air, deteksi api, deteksi dini, "
    "deteksi garis, deteksi jalur, deteksi logam, deteksi objek, deteksi suara, deteksi warna, detektor, detektor asap, diabetes, diastol, digital audio, "
    "digit, dimmer, dinamo, dingin, dip, discharge, disipasi, dispenser, do, dorong, dosis, driver, drone, dual, dual core, ec, ecg, efisien, efisiensi, ekg, "
    "ekspansi, elektro, elektrokardiogram, elektronika, elektronika dasar, emg, emosi, emulasi, encoder, end effector, energi, engsel, es, esc, ethernet, file, "
    "filter, firmware, fisik, flex, foto, fotosintesis, frekuensi napas, gabah, galvanik, gambar, garam, garis, gas, gas beracun, gas organik, gateway, gelombang, "
    "gelap, gempa, genangan, genggam, gerak, gerakan, gerakan tubuh, gerimis, geser, getar, getaran, glonass, glukosa, g-force, goyang, gps, gram, grafik, "
    "grafik warna, grayscale, grid, gripper, grow light, gsm, gsr, gudang, gulir, guncangan, gyro, halangan, halus, hambatan, hdmi, heatsink, hemat, hemat baterai, "
    "hemat daya, hias, hid, hidrolik, hidroponik, hijau, hitam, hitam putih, hitung, hitung tetes, hp, hubung, hujan, hutan, i2c, i2s, i2s dac, ic, identifikasi, "
    "identitas, ikan, imu, indeks uv, indikator, indoor farm, induksi, induktif, industri, informasi, infrared, infus, input, instalasi, intensitas, interface, "
    "internet, inventaris, inverter, ios, iot, ip, ir, irradiasi, isi ulang, jadwal, jagung, jalan, jalur, jam, jantung, jarak, jarak dekat, jarak jauh, "
    "jarak menengah, jarak petir, jarak tempuh, jari, jaringan, jatuh, jauh, jemur, jendela, jernih, jumper, kabel, kabel utp, kadar air, kait, kalender, "
    "kalium, kamera, kamera termal, kanan, kapasitif, kapasitor, karakter, karbon dioksida, karbon monoksida, kartu, kartu sim, katup, kawat, keamanan, "
    "keamanan rumah, kebakaran, kebun, kecepatan, kecepatan air, kecepatan tinggi, kecil, kejut, kelembapan, kelembapan presisi, kemiringan, kencang, "
    "kendali, kendali jarak jauh, kendaraan, kenop, keracunan, keras, kering, keringat, keruh, kesehatan, kesehatan tanaman, ketik, ketinggian, keyboard, "
    "kilat, kilogram, kimia, kipas, kiri, klik, klorofil, kode, kolam, kompas, kompas angin, kompak, kompatibel, kompleks, komponen pasif, komunikasi, "
    "kondensator, konduktivitas, konfigurasi, koneksi, konektor, kontak, kontraksi, kontrol, kontrol ac, kontrol dc, konversi, koordinat, kota, kotor, "
    "kran, ktp, kualitas air, kualitas udara, kuat, kulit, kulkas, kunci, kunci pintar, kwh, laboratorium, lacak, lagu, lampu, lampu otomatis, lan, langkah, "
    "larutan, laser, laut, layout, layar, lebar, led, lengan robot, lentur, level, level shifter, lewat, lidar, lihat, line follower, line following, lintasan, "
    "lipat ganda, listrik, listrik ac, listrik dc, listrik gratis, liter, lithium, log, logam, lokasi, lora, lorawan, low energy, low power, lpwan, lte, "
    "lumpur, lurus, luar ruangan, lux, magnet, malam, maling, manual, manusia, massa, masuk, matahari, matrix, mdpl, medan, medan magnet, medis, mekanik, "
    "mekanik berat, melodi, merah, memori, mengalir, menu, mesh, mesin, micropython, mikrofon, mikrokontroler, mineral, miring, ml, mobil, modbus, mode, "
    "modul, modul kecil, monitor, monitoring, monitoring baterai, mosfet, motor, motor bldc, motor langkah, mouse, mp3, mqtt, muatan, multi channel, multi servo, "
    "multi tombol, multiplexer, mungil, murah, murni, musik, musik sederhana, nada, nadi, naik tegangan, napas, navigasi, nb-iot, nfc, nitrogen, nilai, nirkabel, "
    "non-invasif, non-volatile, north, notifikasi, npk, nutrisi, nyala, obstacle, odometri, offline, offline logging, offline to online, ohm, oksigen, "
    "oksigen terlarut, oled, on off, optik, orientasi, otak, otomatis, otomotif, otot, outdoor, overcharge, ozon, pabrik, padi, palang, panas, panas tubuh, "
    "panel, panel surya, panjang, pantau, pantul, papan, papan iklan, paralel, parkir, partikel, paru, pasien, pasif, pasang, password, pcb, pecah kaca, "
    "pelosok, pembatas arus, pembayaran, pemicu, pemula, pemutus, pencahayaan, pencet, pencuri, pendingin, penerangan, penerima, pengatur, pengatur tegangan, "
    "pengeras, penggerak, pengirim, pengisian, peningkat, penuh, penurun, penurun voltase, penyimpan muatan, penyimpanan, penyimpanan eksternal, pernapasan, "
    "peringatan, perlindungan, permanen, persisten, pertanian, pertanian presisi, pesan, peta, peta panas, petir, ph, photoelectric, pigmen, pin, pintu, pipa, "
    "pir, piston, pixel, pln, pm25, poe, pointer, polaritas, polusi, pompa, portabel, posisi, postur, power, power delivery, power supply, presisi, presisi 16bit, "
    "presisi tinggi, printer 3d, produk, propane, propeller, prostetik, proteksi baterai, prototipe, proximity, psikologi, pupuk, putar, putar lagu, putaran, pwm, "
    "pyranometer, qr code, raba, radar, radiasi, radio, rangkaian, rakit, rc, real time, reed switch, regulasi, rekam, remote, resistor, rfid, rfid jauh, "
    "rgb, ringan, ringkas, rintangan, rintik, robot, roda, rotasi, router, rpm, rpm tinggi, ruangan, rumah, rumah pintar, rumah sakit, saklar, salinitas, "
    "saluran, sambung, sambungan, sandi, sarung tangan, satelit, scan, scan jari, sdcard, sedot, seimbang, sel, selang, seluler, semprot, sendi, sensor kontak, "
    "sensor network, sentuh, sentuh fisik, senyawa, serial, server, servo, settings, shield, siang, sidik, silinder, simpan, simpan listrik, sinyal, sinyal jantung, "
    "siram, sirine, sirkuit, sirkulasi, sistol, skor, smart, smart home, smart lock, smartphone, sms, socket, solder, soldering, solenoid, sortir, speaker, spi, "
    "spo2, stabil, stasiun cuaca, stepper, storm, stream, streaming, stres, subur, sudut, suhu, suhu ekstrem, suhu tanah, suhu tubuh, suplai, surya, surveillance, "
    "switch, switching, tabrak, tabrakan, tag, tambak, tampil, tanah, tanaman, tanda, tandon, tangan, tanggal, tanpa kabel, tanpa kontak, tanpa sentuh, "
    "tanpa solder, tanpa suara, tap, tap jari, tarik, tds, tegangan, tegangan ac, tegangan tinggi, teks, teks berjalan, telinga, telepon, tembak, tembaga, "
    "tempat, temperatur, termal, termometer, tepuk, terang, terbang, tes, tes darah, tetes, tetesan, throttle, tilt, timbangan, timer, tiup, titik, toggle, "
    "tol, tombol, torsi, torsi tinggi, touch, touchscreen, tracker, trafo, tremor, trigger, tv, tubuh, tulisan, turun tegangan, tutup, tv, uart, udara, "
    "udara bertekanan, udara kotor, ui, ujung, ukur air, ukur berat, ukur daya, ukur watt, ultraviolet, unik, usb, utara, utama, uv, vane, vektor, ventilasi, "
    "vibrasi, video, video call, visi, visual, vital, voc, vokal, voltase, volume, vr, wajah, waktu, warna, warni, watt, watt per meter, wearable, web, "
    "web server, wifi, wired, zigbee"
)

KATEGORI_ICON = {
    'Mikrokontroler': '🧠',
    'Sensor':         '🔍',
    'Aktuator':       '⚙️',
    'Output':         '📺',
    'Komunikasi':     '📡',
    'Modul Daya':     '⚡',
    'Input':          '🎛️',
    'Aksesoris':      '🧰',
    'Modul Waktu':    '🕐',
}

# ==========================================
# CUSTOM CSS
# ==========================================
def inject_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600&family=Inter:wght@300;400;500;600;700&display=swap');

    html, body, [data-testid="stAppViewContainer"] { background-color: #0D0F14 !important; color: #E2E8F0 !important; }
    [data-testid="stHeader"] { background: transparent !important; }
    [data-testid="stSidebar"] { display: none; }
    section[data-testid="stMain"] > div { padding-top: 0 !important; }

    .hero-banner { background: linear-gradient(135deg, #0D0F14 0%, #111827 40%, #0F172A 100%); border-bottom: 1px solid #1E293B; padding: 3rem 2rem 2.5rem; text-align: center; position: relative; overflow: hidden; }
    .hero-banner::before { content: ''; position: absolute; top: -60px; left: 50%; transform: translateX(-50%); width: 600px; height: 200px; background: radial-gradient(ellipse, rgba(99,102,241,0.15) 0%, transparent 70%); pointer-events: none; }
    .hero-badge { display: inline-block; background: rgba(99,102,241,0.12); border: 1px solid rgba(99,102,241,0.4); color: #818CF8; font-family: 'JetBrains Mono', monospace; font-size: 0.7rem; letter-spacing: 0.15em; padding: 0.35rem 1rem; border-radius: 999px; margin-bottom: 1.2rem; text-transform: uppercase; }
    .hero-title { font-family: 'Inter', sans-serif; font-size: 2.4rem; font-weight: 700; color: #F8FAFC; line-height: 1.2; margin: 0 0 0.6rem; }
    .hero-title span { background: linear-gradient(90deg, #818CF8, #38BDF8); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
    .hero-subtitle { color: #64748B; font-size: 0.95rem; font-family: 'Inter', sans-serif; font-weight: 400; margin: 0; }

    .stats-bar { display: flex; justify-content: center; gap: 2rem; padding: 1.2rem 2rem; background: #111827; border-bottom: 1px solid #1E293B; flex-wrap: wrap; }
    .stat-item { text-align: center; }
    .stat-number { font-family: 'JetBrains Mono', monospace; font-size: 1.3rem; font-weight: 600; color: #818CF8; }
    .stat-label { font-size: 0.7rem; color: #475569; text-transform: uppercase; letter-spacing: 0.08em; font-family: 'Inter', sans-serif; }

    .main-wrapper { max-width: 900px; margin: 0 auto; padding: 2rem 1.5rem; }
    .input-label { font-family: 'JetBrains Mono', monospace; font-size: 0.72rem; color: #475569; letter-spacing: 0.12em; text-transform: uppercase; margin-bottom: 0.5rem; }
    
    [data-testid="stTextArea"] textarea { background: #111827 !important; border: 1px solid #1E293B !important; border-radius: 10px !important; color: #E2E8F0 !important; font-family: 'Inter', sans-serif !important; font-size: 0.95rem !important; padding: 1rem !important; transition: border-color 0.2s !important; resize: vertical !important; }
    [data-testid="stTextArea"] textarea:focus { border-color: #6366F1 !important; box-shadow: 0 0 0 3px rgba(99,102,241,0.15) !important; }
    [data-testid="stTextArea"] textarea::placeholder { color: #334155 !important; }
    [data-testid="stTextArea"] label { display: none !important; }

    [data-testid="stButton"] > button { background: linear-gradient(135deg, #6366F1, #4F46E5) !important; color: white !important; border: none !important; border-radius: 8px !important; font-family: 'Inter', sans-serif !important; font-weight: 600 !important; font-size: 0.9rem !important; padding: 0.6rem 2rem !important; letter-spacing: 0.02em !important; transition: all 0.2s !important; width: 100% !important; }
    [data-testid="stButton"] > button:hover { background: linear-gradient(135deg, #818CF8, #6366F1) !important; box-shadow: 0 4px 20px rgba(99,102,241,0.35) !important; transform: translateY(-1px) !important; }

    .result-header { font-family: 'JetBrains Mono', monospace; font-size: 0.65rem; color: #475569; letter-spacing: 0.15em; text-transform: uppercase; margin-bottom: 1.5rem; padding-bottom: 0.75rem; border-bottom: 1px solid #1E293B; }
    .insight-grid { display: grid; grid-template-columns: 1fr 1.6fr; gap: 1rem; margin-bottom: 1.5rem; }
    .insight-card { background: #111827; border: 1px solid #1E293B; border-radius: 10px; padding: 1.2rem 1.4rem; }
    .insight-card.keywords { border-left: 3px solid #6366F1; }
    .insight-card.summary  { border-left: 3px solid #10B981; }
    .insight-card-label { font-family: 'JetBrains Mono', monospace; font-size: 0.65rem; color: #475569; text-transform: uppercase; letter-spacing: 0.12em; margin-bottom: 0.7rem; }
    .keyword-pill { display: inline-block; background: rgba(99,102,241,0.12); border: 1px solid rgba(99,102,241,0.3); color: #A5B4FC; font-family: 'JetBrains Mono', monospace; font-size: 0.75rem; padding: 0.2rem 0.65rem; border-radius: 999px; margin: 0.2rem; }
    .summary-text { color: #CBD5E1; font-size: 0.88rem; font-family: 'Inter', sans-serif; line-height: 1.6; font-style: italic; }

    .section-header { display: flex; align-items: center; gap: 0.75rem; margin: 2rem 0 1rem; }
    .section-icon { font-size: 1.1rem; }
    .section-title { font-family: 'Inter', sans-serif; font-weight: 600; font-size: 1rem; color: #E2E8F0; }
    .section-count { background: rgba(99,102,241,0.15); border: 1px solid rgba(99,102,241,0.3); color: #818CF8; font-family: 'JetBrains Mono', monospace; font-size: 0.7rem; padding: 0.1rem 0.55rem; border-radius: 999px; margin-left: auto; }

    .comp-card { background: #111827; border: 1px solid #1E293B; border-radius: 12px; padding: 1.25rem 1.5rem; margin-bottom: 0.75rem; transition: border-color 0.2s, transform 0.2s; position: relative; overflow: hidden; }
    .comp-card:hover { border-color: #334155; transform: translateY(-1px); }
    .comp-card::before { content: ''; position: absolute; top: 0; left: 0; width: 3px; height: 100%; background: linear-gradient(180deg, #6366F1, #38BDF8); border-radius: 3px 0 0 3px; }
    .comp-card-top { display: flex; align-items: flex-start; justify-content: space-between; margin-bottom: 0.6rem; }
    .comp-name { font-family: 'Inter', sans-serif; font-weight: 600; font-size: 0.95rem; color: #F1F5F9; }
    .comp-category { font-family: 'JetBrains Mono', monospace; font-size: 0.65rem; color: #475569; margin-top: 0.2rem; }
    .comp-score-badge { display: flex; flex-direction: column; align-items: flex-end; flex-shrink: 0; }
    .score-ring { font-family: 'JetBrains Mono', monospace; font-size: 1.1rem; font-weight: 600; line-height: 1; }
    .score-ring.high  { color: #10B981; }
    .score-ring.mid   { color: #F59E0B; }
    .score-ring.low   { color: #6366F1; }
    .score-label { font-size: 0.6rem; color: #475569; text-transform: uppercase; letter-spacing: 0.1em; margin-top: 0.15rem; }

    .score-bar-track { width: 100%; height: 3px; background: #1E293B; border-radius: 999px; margin: 0.6rem 0; overflow: hidden; }
    .score-bar-fill { height: 100%; border-radius: 999px; transition: width 0.6s ease; }
    .fill-high { background: linear-gradient(90deg, #10B981, #34D399); }
    .fill-mid  { background: linear-gradient(90deg, #F59E0B, #FCD34D); }
    .fill-low  { background: linear-gradient(90deg, #6366F1, #818CF8); }

    .ai-reason { background: rgba(99,102,241,0.06); border: 1px solid rgba(99,102,241,0.18); border-radius: 7px; padding: 0.65rem 1rem; margin-top: 0.5rem; }
    .ai-reason-label { font-family: 'JetBrains Mono', monospace; font-size: 0.6rem; color: #6366F1; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 0.3rem; }
    .ai-reason-text { font-size: 0.88rem; color: #fafbfc !important; font-family: 'Inter', sans-serif; line-height: 1.6; }
    
    .voltage-tag { display: inline-block; background: rgba(56,189,248,0.1); border: 1px solid rgba(56,189,248,0.2); color: #38BDF8; font-family: 'JetBrains Mono', monospace; font-size: 0.68rem; padding: 0.18rem 0.6rem; border-radius: 4px; margin-top: 0.5rem; }
    .kw-tag { font-family: 'JetBrains Mono', monospace; font-size: 0.65rem; color: #fafbfc !important; }
    .section-divider { border: none; border-top: 1px solid #1E293B; margin: 1.5rem 0; }
    .empty-state { text-align: center; padding: 2rem; color: #334155; font-family: 'Inter', sans-serif; font-size: 0.88rem; background: #111827; border: 1px dashed #1E293B; border-radius: 10px; }
    
    [data-testid="stSpinner"] { color: #6366F1 !important; }
    #MainMenu, footer, [data-testid="stToolbar"] { display: none !important; }
    </style>
    """, unsafe_allow_html=True)


# ==========================================
# DATABASE
# ==========================================
def ambil_data_komponen():
    try:
        conn = sqlite3.connect('database_iot_v2.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tb_komponen")
        data = [dict(row) for row in cursor.fetchall()]
        conn.close()
        return data
    except sqlite3.Error as err:
        st.error(f"Gagal membaca database: {err}")
        return []

def ambil_statistik():
    try:
        conn = sqlite3.connect('database_iot_v2.db')
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM tb_komponen")
        total = cursor.fetchone()[0]
        cursor.execute("SELECT COUNT(DISTINCT kategori) FROM tb_komponen")
        kategori = cursor.fetchone()[0]
        conn.close()
        return total, kategori
    except sqlite3.Error:
        return 0, 0


# ==========================================
# AI TAHAP 1: EKSTRAKSI KEYWORDS
# ==========================================
def ekstrak_keywords_tahap1(input_teks):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {
                "role": "system",
                "content": "Kamu adalah sistem pengekstraksi kata kunci. Balas HANYA dengan JSON murni dengan key: 'keywords' (array string) dan 'alasan_global' (string)."
            },
            {
                "role": "user",
                "content": f"""KAMUS: [{KAMUS_DATABASE}]

TUGAS:
1. Analisis kalimat pengguna dan ekstrak kata kunci dari KAMUS.
2. ATURAN MIKROKONTROLER: Wajib masukkan minimal 2 kata dari kelompok [otak, mikrokontroler] dan 1 status jaringan [wifi, lora, seluler, offline].
3. ATURAN SENSOR/FISIK: Pilih 8-12 kata kunci tambahan yang relevan. Jika ada kata layar, wajib masukkan lcd/oled. Jika pompa/motor, wajib masukkan relay.
4. Buat 1 kalimat kesimpulan umum di key 'alasan_global'.
5. Output HARUS format JSON murni.

Kalimat Pengguna: '{input_teks}'"""
            }
        ],
        "response_format": {"type": "json_object"},
        "temperature": 0.1
    }

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=15)
        if response.status_code == 200:
            hasil_json = response.json()
            content = json.loads(hasil_json['choices'][0]['message']['content'])
            return {
                "keywords": content.get("keywords", []),
                "alasan_global": content.get("alasan_global", "")
            }
    except requests.exceptions.RequestException:
        pass
    return None


# ==========================================
# AI TAHAP 2: PENALARAN KOMPONEN SPESIFIK
# ==========================================
def generate_alasan_tahap2(input_teks, daftar_nama_komponen):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    
    list_komponen_str = ", ".join(daftar_nama_komponen)
    
    payload = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {
                "role": "system",
                "content": "Kamu adalah Senior Hardware Engineer. Balas HANYA dengan JSON murni dengan key: 'alasan_komponen' (object key-value) dan 'catatan_inferensi' (string)."
            },
            {
                "role": "user",
                "content": f"""Proyek: '{input_teks}'
Daftar Komponen Terpilih: [{list_komponen_str}]

TUGAS:
1. Pada key 'alasan_komponen', buat pasangan key-value di mana key adalah NAMA KOMPONEN yang tertulis di atas, dan valuenya adalah alasan MENGAPA komponen itu dipilih.
2. ATURAN PENULISAN ALASAN (MUTLAK):
   - Alasan HARUS berupa Prinsip Kerja Fisika, Elektronika, atau Mekanika spesifik terhadap proyek ini.
   - JANGAN PERNAH memakai frasa bodoh seperti: "bekerja secara otomatis", "tanpa campur tangan manusia", atau "sesuai kebutuhan".
   - Contoh Benar (Sensor PIR): "Mendeteksi perubahan pancaran inframerah dari suhu tubuh penyusup di area tanpa video."
   - Contoh Benar (Relay): "Berfungsi sebagai saklar elektrik terisolasi untuk mengontrol arus besar pada pompa."
3. ATURAN SELF-CORRECTION (SANGAT PENTING):
   - Kamu bertindak sebagai pengawas (Safety Net). Jika ada komponen di daftar yang SANGAT TIDAK RELEVAN secara hukum fisika/mekanika dengan deskripsi proyek (Contoh: menggunakan Kunci Pintu / Solenoid Door Lock untuk sistem air/kebun), KAMU DILARANG KERAS MENGARANG ALASAN/HALUSINASI!
   - Jika menemukan ketidakcocokan fatal seperti itu, isi value alasan komponen tersebut HANYA dengan kalimat mutlak ini: "Tidak digunakan dalam proyek ini, sistem salah pilih karena fungsi mekanis/elektrisnya tidak relevan dengan kebutuhan proyek."
4. Pada key 'catatan_inferensi', tulis 1-2 kalimat logis tentang arsitektur keseluruhan atau alasan mengapa ada komponen tambahan yang tidak diminta (misalnya sensor dipasang untuk antisipasi).
5. Output HARUS format JSON murni.
"""
            }
        ],
        "response_format": {"type": "json_object"},
        "temperature": 0.1
    }

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=15)
        if response.status_code == 200:
            hasil_json = response.json()
            content = json.loads(hasil_json['choices'][0]['message']['content'])
            return {
                "alasan_komponen": content.get("alasan_komponen", {}),
                "catatan_inferensi": content.get("catatan_inferensi", "")
            }
    except requests.exceptions.RequestException:
        pass
    return None


# ==========================================
# COSINE SIMILARITY
# ==========================================
def hitung_cosine_similarity(user_tokens, db_tokens):
    semua_kata = list(set(user_tokens + db_tokens))
    vektor_user = [1 if kata in user_tokens else 0 for kata in semua_kata]
    vektor_db   = [1 if kata in db_tokens  else 0 for kata in semua_kata]
    
    dot_product = sum(u * d for u, d in zip(vektor_user, vektor_db))
    mag_user = math.sqrt(sum(u**2 for u in vektor_user))
    mag_db   = math.sqrt(sum(d**2 for d in vektor_db))
    
    if mag_user * mag_db == 0:
        return 0.0
    return dot_product / (mag_user * mag_db)


# ==========================================
# HELPER: RENDER KOMPONEN CARD
# ==========================================
def render_komponen_card(item, alasan_komponen_dict):
    skor = item['skor_persen']
    db_tokens = [k.strip() for k in item['keywords'].split(',')]

    if skor >= 50:
        score_cls, bar_cls = "high", "fill-high"
    elif skor >= 25:
        score_cls, bar_cls = "mid", "fill-mid"
    else:
        score_cls, bar_cls = "low", "fill-low"

    # Tarik alasan berdasarkan NAMA KOMPONEN dari dictionary Tahap 2
    nama_komp = item['nama_komponen']
    alasan = alasan_komponen_dict.get(nama_komp, "Komponen ini terdeteksi memiliki relevansi teknis dengan parameter proyek.")
    alasan_html = f'<div class="ai-reason"><div class="ai-reason-label">✦ Alasan AI</div><div class="ai-reason-text">{alasan}</div></div>'

    kw_preview = ", ".join(db_tokens[:6])
    if len(db_tokens) > 6:
        kw_preview += f" +{len(db_tokens)-6} lainnya"

    kategori = item['kategori']
    icon = KATEGORI_ICON.get(kategori, '📦')

    # DITULIS RATA KIRI (Zero Indentation) agar tidak dianggap blok kode oleh Markdown Streamlit
    card_html = f"""
<div class="comp-card">
<div class="comp-card-top">
<div>
<div class="comp-name">{icon} {nama_komp}</div>
<div class="comp-category">{kategori} · {item.get('id_komponen', 'N/A')}</div>
</div>
<div class="comp-score-badge">
<div class="score-ring {score_cls}">{skor}%</div>
<div class="score-label">match</div>
</div>
</div>
<div class="score-bar-track">
<div class="score-bar-fill {bar_cls}" style="width: {min(skor*1.5, 100)}%"></div>
</div>

<div style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
<span class="voltage-tag">⚡ {item.get('tegangan', '-')}</span>
<span class="voltage-tag" style="color: #A78BFA; border-color: rgba(167,139,250,0.3); background: rgba(167,139,250,0.1);">🔌 {item.get('protokol', '-')}</span>
<span class="voltage-tag" style="color: #34D399; border-color: rgba(52,211,153,0.3); background: rgba(52,211,153,0.1);">💰 {item.get('harga', '-')}</span>
</div>

{alasan_html}
<div class="kw-tag" style="margin-top:0.6rem;">🏷 {kw_preview}</div>
</div>
"""
    st.markdown(card_html, unsafe_allow_html=True)


# ==========================================
# MAIN APP
# ==========================================
def main():
    st.set_page_config(
        page_title="IoT Component Finder", 
        page_icon="🔌", 
        layout="wide", 
        initial_sidebar_state="collapsed"
    )
    inject_css()

    total_komp, total_kat = ambil_statistik()
    
    st.markdown(f"""
    <div class="hero-banner">
        <div class="hero-badge">⚙ RAG Pipeline + Content-Based Filtering</div>
        <h1 class="hero-title">IoT <span>Component</span> Finder</h1>
        <p class="hero-subtitle">Deskripsikan proyekmu — AI akan analisis kebutuhan dan rekomendasikan komponen yang tepat.</p>
    </div>
    <div class="stats-bar">
    <div class="stat-item"><div class="stat-number">{total_komp}</div><div class="stat-label">Komponen</div></div>
    <div class="stat-item"><div class="stat-number">{total_kat}</div><div class="stat-label">Kategori</div></div>
    <div class="stat-item"><div class="stat-number">Llama 3.3</div><div class="stat-label">AI RAG Engine</div></div>
    <div class="stat-item"><div class="stat-number">Cosine</div><div class="stat-label">Similarity</div></div>
    </div>
    <div class="main-wrapper">

    <div style="display: flex; justify-content: flex-start; width: 100%;">
    <div class="input-label" style="text-align: left; margin-bottom: 0.8rem;">// DESKRIPSI PROYEK</div>
    </div>
    """, unsafe_allow_html=True)

    input_user = st.text_area("desc", placeholder="Contoh: Alat otomatis penyiram kebun...", height=120, label_visibility="collapsed")
    
    btn_col, _ = st.columns([1, 2])
    with btn_col: 
        analyze_btn = st.button("⚡  Analisis & Cari Komponen", type="primary")

    st.markdown('<hr class="section-divider">', unsafe_allow_html=True)

    if analyze_btn:
        if not input_user.strip():
            st.markdown('<div class="empty-state">⚠️ Masukkan deskripsi proyek terlebih dahulu.</div>', unsafe_allow_html=True)
            return

        # TAHAP 1: Ekstrak Kata Kunci
        with st.spinner("Tahap 1: Mengekstrak parameter arsitektur IoT..."):
            hasil_tahap1 = ekstrak_keywords_tahap1(input_user)

        if not hasil_tahap1 or not hasil_tahap1["keywords"]:
            st.error("🚨 Gangguan koneksi API atau deskripsi tidak dapat diproses. Coba lagi.")
            return
            
        keywords_terpilih = hasil_tahap1["keywords"]
        alasan_global     = hasil_tahap1["alasan_global"]

        # HITUNG MATEMATIKA LOKAL
        daftar_komponen = ambil_data_komponen()
        hasil_rekomendasi = []
        for komp in daftar_komponen:
            db_tokens = [k.strip() for k in komp['keywords'].split(',')]
            skor = hitung_cosine_similarity(keywords_terpilih, db_tokens)
            if skor > 0:
                komp['skor_persen'] = round(skor * 100, 2)
                hasil_rekomendasi.append(komp)
        hasil_rekomendasi.sort(key=lambda x: x['skor_persen'], reverse=True)

        # SPLIT KATEGORI
        mcu_list        = [x for x in hasil_rekomendasi if x['kategori'] == 'Mikrokontroler']
        sensor_list     = [x for x in hasil_rekomendasi if x['kategori'] == 'Sensor']
        aktuator_list   = [x for x in hasil_rekomendasi if x['kategori'] == 'Aktuator']
        output_list     = [x for x in hasil_rekomendasi if x['kategori'] == 'Output']
        komunikasi_list = [x for x in hasil_rekomendasi if x['kategori'] == 'Komunikasi']
        daya_list       = [x for x in hasil_rekomendasi if x['kategori'] in ['Modul Daya']]
        input_list      = [x for x in hasil_rekomendasi if x['kategori'] == 'Input']
        lainnya_list    = [x for x in hasil_rekomendasi if x['kategori'] in ['Aksesoris', 'Modul Waktu']]

        # AMBIL NAMA KOMPONEN PEMENANG UNTUK TAHAP 2
        komponen_pemenang = (mcu_list[:2] + sensor_list[:4] + aktuator_list[:3] + 
                             output_list[:3] + komunikasi_list[:3] + daya_list[:3] + 
                             input_list[:2] + lainnya_list[:2])
        nama_komponen_terpilih = [k['nama_komponen'] for k in komponen_pemenang]

        # TAHAP 2: Generate Alasan Spesifik Komponen
        with st.spinner("Tahap 2: Merumuskan alasan teknis komponen berdasarkan prinsip elektronika..."):
            hasil_tahap2 = generate_alasan_tahap2(input_user, nama_komponen_terpilih)
        
        alasan_komponen_dict = hasil_tahap2.get("alasan_komponen", {}) if hasil_tahap2 else {}
        catatan_inferensi = hasil_tahap2.get("catatan_inferensi", "") if hasil_tahap2 else ""

        # ── RENDER UI ──
        kw_pills = "".join([f'<span class="keyword-pill">{kw}</span>' for kw in keywords_terpilih])
        st.markdown(f"""
        <div class="result-header">// hasil analisis AI</div>
        <div class="insight-grid">
            <div class="insight-card keywords">
                <div class="insight-card-label">Kata Kunci Terdeteksi</div>
                {kw_pills}
            </div>
            <div class="insight-card summary">
                <div class="insight-card-label">Kesimpulan Proyek</div>
                <div class="summary-text">"{alasan_global}"</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        panels = [
            ("🧠", "Mikrokontroler Utama — Otak Sistem", mcu_list[:2]),
            ("🔍", "Sensor — Input Data Sistem", sensor_list[:4]),
            ("⚙️", "Aktuator — Penggerak Fisik", aktuator_list[:3]),
            ("📺", "Output & Display", output_list[:3]),
            ("📡", "Modul Komunikasi", komunikasi_list[:3]),
            ("⚡", "Modul Daya & Power", daya_list[:3]),
            ("🎛️", "Modul Input & Kontrol", input_list[:2]),
            ("🧰", "Aksesoris & Pendukung", lainnya_list[:2])
        ]

        for icon, title, c_list in panels:
            if c_list:
                st.markdown(f'<div class="section-header"><span class="section-icon">{icon}</span><span class="section-title">{title}</span><span class="section-count">{len(c_list)} relevan</span></div>', unsafe_allow_html=True)
                for item in c_list:
                    render_komponen_card(item, alasan_komponen_dict)
        
        if not mcu_list:
            st.markdown('<div class="empty-state">💡 Disarankan: ESP32 atau Arduino Uno R3 sebagai pengendali standar.</div>', unsafe_allow_html=True)

        # ── CATATAN INFERENSI AI ──
        if catatan_inferensi:
            st.markdown(f"""
            <hr class="section-divider" style="margin-top: 3rem;">
            <div class="insight-card summary" style="border-left-color: #38BDF8; background: rgba(56, 189, 248, 0.03);">
                <div class="insight-card-label" style="color: #38BDF8;">💡 Catatan Logika AI</div>
                <div class="summary-text" style="font-style: normal; color: #E2E8F0;">
                    {catatan_inferensi}
                </div>
            </div>
            """, unsafe_allow_html=True)

        # ── DISCLAIMER / PENAFIAN ──
        st.markdown("""
        <div style="background: rgba(245, 158, 11, 0.05); border: 1px dashed rgba(245, 158, 11, 0.3); border-radius: 8px; padding: 1.2rem; margin-top: 1.5rem; margin-bottom: 1rem;">
            <div style="color: #F59E0B; font-family: 'JetBrains Mono', monospace; font-size: 0.75rem; font-weight: 600; letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 0.5rem;">
                ⚠️ Penafian (Disclaimer) Engineer
            </div>
            <div style="color: #94A3B8; font-family: 'Inter', sans-serif; font-size: 0.85rem; line-height: 1.6;">
                Sistem ini beroperasi sebagai <b>Sistem Pendukung Keputusan (Decision Support System)</b> berbasis <i>Artificial Intelligence</i>. Rekomendasi di atas dihasilkan dari perhitungan probabilitas matematis <i>(Cosine Similarity)</i> dan tidak bersifat mutlak. Keputusan akhir mengenai desain arsitektur IoT, kompatibilitas pin, serta keselamatan kelistrikan (tegangan/arus) tetap sepenuhnya berada di tangan perancang sistem. Pastikan untuk selalu memvalidasi spesifikasi dengan membaca <i>datasheet</i> resmi komponen sebelum melakukan perakitan fisik perangkat keras.
            </div>
        </div>
        """, unsafe_allow_html=True)

        # ── FOOTER ──
        total_tampil = sum(len(l) for _, _, l in panels)
        st.markdown(f"""
        <div style="text-align:center; color:#334155; font-family:'JetBrains Mono',monospace; font-size:0.72rem; padding: 1.5rem 0 2rem;">
            ✦ menampilkan {total_tampil} komponen paling relevan dari {total_komp} komponen dalam database
        </div>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()