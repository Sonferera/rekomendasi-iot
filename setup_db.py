import sqlite3

print("Memperbarui database SQLite: Menambahkan 200++ komponen IoT lengkap dengan Protokol & Harga...")

conn = sqlite3.connect('database_iot_v2.db')
cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS tb_komponen')

cursor.execute('''
CREATE TABLE tb_komponen (
    id_komponen TEXT PRIMARY KEY,
    nama_komponen TEXT,
    kategori TEXT,
    tegangan TEXT,
    protokol TEXT,
    harga TEXT,
    keywords TEXT
)
''')

data_komponen = [
    # ==============================
    # MIKROKONTROLER (K01 - K15)
    # ==============================
    ('K01', 'ESP32 DevKit V1', 'Mikrokontroler', '3.3V', 'Multiple', 'Rp 65.000', 'otak, mikrokontroler, wifi, bluetooth, internet, kendali, utama, iot, nirkabel, dual core'),
    ('K02', 'Arduino Uno R3', 'Mikrokontroler', '5V', 'Multiple', 'Rp 85.000', 'otak, mikrokontroler, dasar, pemula, offline, kabel, serial, papan, kendali'),
    ('K03', 'NodeMCU ESP8266', 'Mikrokontroler', '3.3V', 'Multiple', 'Rp 45.000', 'otak, wifi, internet, iot, modul, kendali, murah, nirkabel'),
    ('K04', 'Arduino Nano', 'Mikrokontroler', '5V', 'Multiple', 'Rp 40.000', 'otak, mikrokontroler, kecil, ringkas, offline, pemula, kabel, serial, kompak'),
    ('K05', 'Arduino Mega 2560', 'Mikrokontroler', '5V', 'Multiple', 'Rp 145.000', 'otak, mikrokontroler, besar, banyak pin, offline, kompleks, serial, papan'),
    ('K06', 'Raspberry Pi Pico W', 'Mikrokontroler', '3.3V', 'Multiple', 'Rp 115.000', 'otak, mikrokontroler, wifi, murah, python, micropython, kendali, dual core'),
    ('K07', 'STM32 Blue Pill', 'Mikrokontroler', '3.3V', 'Multiple', 'Rp 35.000', 'otak, mikrokontroler, cepat, presisi, kendali, motor, offline, 32bit'),
    ('K08', 'ESP32-CAM', 'Mikrokontroler', '5V', 'Multiple', 'Rp 85.000', 'otak, kamera, foto, video, wifi, iot, surveillance, kendali, rekam, stream'),
    ('K09', 'Arduino Pro Mini', 'Mikrokontroler', '3.3V-5V', 'Multiple', 'Rp 35.000', 'otak, mikrokontroler, kecil, baterai, hemat daya, offline, kompak, pemula'),
    ('K10', 'Wemos D1 Mini', 'Mikrokontroler', '3.3V', 'Multiple', 'Rp 40.000', 'otak, wifi, internet, iot, modul, kecil, shield, kendali, nirkabel'),
    ('K11_MC', 'Arduino Leonardo', 'Mikrokontroler', '5V', 'Multiple', 'Rp 130.000', 'otak, mikrokontroler, usb, hid, keyboard, mouse, serial, pemula, emulasi'),
    ('K12_MC', 'ESP32-S3 DevKit', 'Mikrokontroler', '3.3V', 'Multiple', 'Rp 95.000', 'otak, mikrokontroler, wifi, bluetooth, ai, ml, vektor, iot, dual core, usb'),
    ('K13_MC', 'RP2040 Zero', 'Mikrokontroler', '3.3V', 'Multiple', 'Rp 55.000', 'otak, mikrokontroler, kecil, murah, python, micropython, dual core, kompak'),
    ('K14_MC', 'STM32 Nucleo F446RE', 'Mikrokontroler', '3.3V', 'Multiple', 'Rp 250.000', 'otak, mikrokontroler, cepat, arm, industri, presisi, offline, 32bit, pwm, adc'),
    ('K15_MC', 'Arduino Due', 'Mikrokontroler', '3.3V', 'Multiple', 'Rp 350.000', 'otak, mikrokontroler, besar, 32bit, arm, banyak pin, presisi, serial, audio'),

    # ==============================
    # SENSOR — LINGKUNGAN (K11 - K20)
    # ==============================
    ('K16', 'Sensor Suhu DHT11', 'Sensor', '5V', 'Digital', 'Rp 15.000', 'suhu, cuaca, panas, dingin, ruangan, temperatur, kelembapan, udara'),
    ('K17', 'Sensor Suhu DHT22', 'Sensor', '5V', 'Digital', 'Rp 55.000', 'suhu, cuaca, panas, dingin, ruangan, temperatur, kelembapan, udara, presisi'),
    ('K18', 'Sensor Tekanan BME280', 'Sensor', '3.3V', 'I2C / SPI', 'Rp 45.000', 'tekanan, cuaca, mdpl, ketinggian, barometer, suhu, kelembapan presisi'),
    ('K19', 'Sensor Tekanan BMP180', 'Sensor', '3.3V', 'I2C', 'Rp 25.000', 'tekanan, cuaca, ketinggian, barometer, altitude, suhu'),
    ('K20', 'Sensor Cahaya BH1750', 'Sensor', '3.3V', 'I2C', 'Rp 20.000', 'cahaya, lux, terang, gelap, siang, malam, intensitas, pencahayaan'),
    ('K21', 'Sensor Cahaya LDR', 'Sensor', '5V', 'Analog', 'Rp 5.000', 'cahaya, terang, gelap, siang, malam, matahari, lampu otomatis, analog'),
    ('K22', 'Sensor Curah Hujan', 'Sensor', '5V', 'Analog / Digital', 'Rp 18.000', 'hujan, rintik, basah, cuaca, badai, air turun, atap, gerimis'),
    ('K23', 'Sensor Kualitas Udara MQ-135', 'Sensor', '5V', 'Analog / Digital', 'Rp 22.000', 'udara, polusi, co2, amonia, kualitas udara, bersih, kotor, gas beracun, asap knalpot'),
    ('K24', 'Sensor Gas MQ-2', 'Sensor', '5V', 'Analog / Digital', 'Rp 18.000', 'gas, bocor, asap, api, kebakaran, dapur, deteksi, udara kotor, propane'),
    ('K25', 'Sensor Gas MQ-7 (CO)', 'Sensor', '5V', 'Analog / Digital', 'Rp 25.000', 'gas, karbon monoksida, co, kebakaran, keracunan, dapur, deteksi, udara kotor'),
    ('K26_ENV', 'Sensor Tekanan BMP388', 'Sensor', '3.3V', 'I2C / SPI', 'Rp 75.000', 'tekanan, barometer, altimeter, drone, cuaca, ketinggian, presisi tinggi, suhu'),
    ('K27_ENV', 'Sensor CO2 MH-Z19B', 'Sensor', '5V', 'UART / PWM', 'Rp 195.000', 'co2, kualitas udara, karbon dioksida, ventilasi, ruangan, gas, polusi, bersih'),
    ('K28_ENV', 'Sensor VOC SGP30', 'Sensor', '3.3V', 'I2C', 'Rp 95.000', 'voc, gas organik, kualitas udara, bahan kimia, senyawa, polusi, ruangan'),
    ('K29_ENV', 'Sensor Ozon MQ-131', 'Sensor', '5V', 'Analog', 'Rp 45.000', 'ozon, gas, udara, polusi, kualitas udara, lingkungan, deteksi'),
    ('K30_ENV', 'Sensor Debu PM2.5 GP2Y1010AU', 'Sensor', '5V', 'Analog', 'Rp 85.000', 'debu, partikel, pm25, polusi, kualitas udara, asap, halus, lingkungan'),

    # ==============================
    # SENSOR — GERAK & JARAK (K31 - K45)
    # ==============================
    ('K31', 'Sensor Ultrasonik HC-SR04', 'Sensor', '5V', 'Digital', 'Rp 15.000', 'jarak, halangan, deteksi, radar, pantul, dekat, jauh, rintangan, parkir'),
    ('K32', 'Sensor Gerak PIR HC-SR501', 'Sensor', '5V', 'Digital', 'Rp 12.000', 'gerak, manusia, lewat, maling, deteksi, keamanan, otomatis, tubuh'),
    ('K33', 'Sensor Jarak IR Tajam GP2Y0A21', 'Sensor', '5V', 'Analog', 'Rp 85.000', 'jarak, infrared, halangan, dekat, robot, analog, rintangan, pantul'),
    ('K34', 'Sensor LIDAR TF-Luna', 'Sensor', '5V', 'UART / I2C', 'Rp 350.000', 'jarak, lidar, presisi, laser, peta, robot, navigasi, akurat'),
    ('K35', 'Sensor Gyroscope MPU6050', 'Sensor', '3.3V-5V', 'I2C', 'Rp 25.000', 'miring, jatuh, seimbang, gyro, akselerasi, kemiringan, orientasi, sudut, imu'),
    ('K36', 'Sensor Getar SW-420', 'Sensor', '3.3V-5V', 'Digital', 'Rp 10.000', 'getar, gempa, goyang, guncangan, mesin, tabrakan, tremor, kejut'),
    ('K37', 'Sensor Magnetik Hall Effect', 'Sensor', '5V', 'Digital / Analog', 'Rp 15.000', 'magnet, medan, logam, besi, dekat, induksi, polaritas, rpm'),
    ('K38', 'Accelerometer ADXL345', 'Sensor', '3.3V', 'I2C / SPI', 'Rp 30.000', 'akselerasi, miring, jatuh, gerakan, sudut, orientasi, g-force, tilt'),
    ('K39', 'Limit Switch', 'Sensor', '5V', 'Digital', 'Rp 5.000', 'saklar, sentuh, batas, mekanik, ujung, tekan, bentur, halangan, tabrak'),
    ('K40', 'Sensor Tabrakan (Collision Sensor)', 'Sensor', '5V', 'Digital', 'Rp 12.000', 'tabrak, bentur, halangan, robot, bumper, batas, sentuh fisik'),
    ('K41_MOT', 'Sensor IMU ICM-20948', 'Sensor', '3.3V', 'I2C / SPI', 'Rp 155.000', 'imu, gyro, akselerasi, magnetometer, orientasi, drone, robot, 9-axis, gerak, sudut'),
    ('K42_MOT', 'Sensor Magnetometer HMC5883L', 'Sensor', '3.3V', 'I2C', 'Rp 25.000', 'kompas, arah, utara, medan magnet, orientasi, navigasi, robot, drone'),
    ('K43_MOT', 'Sensor Infrared Line Tracker', 'Sensor', '5V', 'Digital', 'Rp 8.000', 'garis, jalur, line follower, robot, hitam, putih, deteksi jalur, lintasan'),
    ('K44_MOT', 'Sensor Proximity Kapasitif', 'Sensor', '5V', 'Digital', 'Rp 35.000', 'proximity, dekat, tanpa sentuh, kapasitif, objek, deteksi, industri'),
    ('K45_MOT', 'Sensor Arus Eddy (Induktif)', 'Sensor', '5V', 'Digital', 'Rp 45.000', 'logam, induktif, proximity, besi, aluminium, tembaga, deteksi logam, industri'),

    # ==============================
    # SENSOR — AIR & CAIRAN (K46 - K55)
    # ==============================
    ('K46', 'Water Level Sensor', 'Sensor', '5V', 'Analog', 'Rp 10.000', 'air, banjir, tandon, penuh, cair, kolam, genangan, deteksi air'),
    ('K47', 'Sensor pH Air', 'Sensor', '5V', 'Analog', 'Rp 180.000', 'ph, asam, basa, air, kolam, kualitas air, hidroponik, akuarium, cairan'),
    ('K48', 'Sensor Kekeruhan Air (Turbidity)', 'Sensor', '5V', 'Analog / Digital', 'Rp 120.000', 'keruh, jernih, kotor, lumpur, air, kualitas air, bening, partikel'),
    ('K49', 'Water Flow Sensor YF-S201', 'Sensor', '5V', 'Digital (PWM)', 'Rp 45.000', 'debit, aliran, liter, air, pipa, kran, ukur air, volume, kecepatan air'),
    ('K50', 'Sensor TDS (Total Dissolved Solids)', 'Sensor', '3.3V-5V', 'Analog', 'Rp 85.000', 'air, mineral, tds, kualitas air, hidroponik, murni, larutan, mineral'),
    ('K51', 'Sensor Kelembapan Tanah', 'Sensor', '5V', 'Analog', 'Rp 12.000', 'tanah, kelembapan, air, siram, kebun, tanaman, basah, kering, pertanian'),
    ('K52', 'Sensor Tetesan Cairan (IV Drop)', 'Sensor', '5V', 'Digital', 'Rp 150.000', 'tetes, infus, cair, cairan, medis, rumah sakit, tetesan, hitung tetes'),
    ('K53', 'Sensor Debit Air Ultrasonik', 'Sensor', '5V', 'UART', 'Rp 250.000', 'debit, aliran, pipa, air, volume, kecepatan air, ultrasonik, non-invasif'),
    ('K54_AIR', 'Sensor Salinitas Air', 'Sensor', '5V', 'Analog', 'Rp 120.000', 'salinitas, garam, laut, air laut, konduktivitas, akuarium, tambak, ikan'),
    ('K55_AIR', 'Sensor DO (Dissolved Oxygen)', 'Sensor', '5V', 'Analog', 'Rp 285.000', 'oksigen terlarut, do, air, kolam, ikan, akuarium, hidroponik, kualitas air'),

    # ==============================
    # SENSOR — LISTRIK & DAYA (K56 - K65)
    # ==============================
    ('K56', 'Sensor Tegangan ZMPT101B', 'Sensor', '5V', 'Analog', 'Rp 35.000', 'voltase, tegangan, pln, listrik ac, ukur daya, arus bolak balik'),
    ('K57', 'Sensor Arus ACS712', 'Sensor', '5V', 'Analog', 'Rp 25.000', 'arus, ampere, konsumsi, daya, listrik dc, beban, ukur watt'),
    ('K58', 'Sensor Berat (Load Cell) + HX711', 'Sensor', '5V', 'Digital (2-Wire)', 'Rp 40.000', 'berat, timbangan, massa, beban, kilogram, gram, ukur berat, muatan'),
    ('K59', 'Sensor Energi PZEM-004T', 'Sensor', '5V', 'UART', 'Rp 95.000', 'energi, kwh, watt, arus, voltase, pln, listrik ac, konsumsi daya, monitoring'),
    ('K60', 'Sensor Kapasitif Tanpa Sentuh', 'Sensor', '5V', 'Digital', 'Rp 20.000', 'sentuh, kapasitif, tanpa kontak, jari, raba, otomatis, proximity'),
    ('K61', 'Sensor Suara KY-038', 'Sensor', '5V', 'Analog / Digital', 'Rp 12.000', 'suara, tepuk, bising, deteksi suara, mikrofon, dengar, kencang, akustik'),
    ('K62', 'Sensor Detak Jantung MAX30102', 'Sensor', '3.3V', 'I2C', 'Rp 45.000', 'jantung, detak, nadi, darah, oksigen, spo2, kesehatan, medis, pasien, monitor'),
    ('K63_EL', 'Sensor Arus INA219', 'Sensor', '3.3V-5V', 'I2C', 'Rp 25.000', 'arus, tegangan, daya, watt, ampere, monitoring, baterai, efisiensi, ukur daya'),
    ('K64_EL', 'Sensor Arus INA3221', 'Sensor', '3.3V', 'I2C', 'Rp 65.000', 'arus, tegangan, 3 channel, daya, watt, monitoring baterai, multi channel, efisiensi'),
    ('K65_EL', 'Sensor Petir AS3935', 'Sensor', '3.3V', 'I2C / SPI', 'Rp 125.000', 'petir, kilat, badai, jarak petir, cuaca, deteksi, keselamatan, outdoor'),

    # ==============================
    # SENSOR — IDENTIFIKASI (K66 - K77)
    # ==============================
    ('K66', 'RFID Reader RC522', 'Sensor', '3.3V', 'SPI', 'Rp 22.000', 'kartu, akses, scan, tap, identifikasi, masuk, baca, keamanan, ktp, rfid'),
    ('K67', 'Modul RFID UHF', 'Sensor', '5V', 'UART', 'Rp 450.000', 'kartu, akses, scan, jarak jauh, parkir, tol, identifikasi, rfid jauh'),
    ('K68', 'Sensor Sidik Jari AS608', 'Sensor', '3.3V', 'UART', 'Rp 160.000', 'jari, sidik, biometrik, akses, keamanan, identitas, tap jari, scan jari'),
    ('K69', 'Sensor Warna TCS3200', 'Sensor', '5V', 'Digital', 'Rp 35.000', 'warna, color, cat, rgb, sortir, barang, deteksi warna, pigmen'),
    ('K70', 'Modul Kamera OV2640', 'Sensor', '3.3V', 'SCCB / SPI', 'Rp 45.000', 'kamera, foto, video, gambar, lihat, pantau, cctv, visual, rekam, stream'),
    ('K71', 'Sensor Suhu Non-Kontak MLX90614', 'Sensor', '3.3V-5V', 'I2C', 'Rp 145.000', 'suhu, termometer, tembak, tanpa sentuh, panas tubuh, mesin, dahi, medis'),
    ('K72', 'Sensor Api (Flame Sensor)', 'Sensor', '5V', 'Analog / Digital', 'Rp 10.000', 'api, panas, bakar, kebakaran, nyala, terang, deteksi api, bahaya'),
    ('K73_ID', 'Modul Kamera HM01B0 (Grayscale)', 'Sensor', '1.8V', 'SPI', 'Rp 95.000', 'kamera, gambar, grayscale, hitam putih, visi, visual, ai, ml, deteksi objek'),
    ('K74_ID', 'Sensor Wajah AMG8833 (Thermal)', 'Sensor', '3.3V', 'I2C', 'Rp 250.000', 'termal, panas, wajah, manusia, tubuh, kamera termal, grid, peta panas, deteksi'),
    ('K75_ID', 'Barcode Scanner GM65', 'Sensor', '5V', 'UART', 'Rp 185.000', 'barcode, qr code, scan, produk, inventaris, belanja, identifikasi, kode'),
    ('K76_ID', 'Sensor NFC PN532', 'Sensor', '3.3V-5V', 'I2C / SPI / UART', 'Rp 75.000', 'nfc, tap, kartu, smartphone, akses, identifikasi, pembayaran, dekat, kontak'),
    ('K77_ID', 'Sensor Iris Mata', 'Sensor', '5V', 'UART', 'Rp 850.000', 'iris, mata, biometrik, keamanan, identitas, akses premium, unik, tingkat tinggi'),

    # ==============================
    # AKTUATOR (K78 - K95)
    # ==============================
    ('K78', 'Solenoid Door Lock 12V', 'Aktuator', '12V', 'Power / Relay', 'Rp 65.000', 'pintu, kunci, fisik, keamanan, tutup, kait, magnet, otomatis, akses'),
    ('K79', 'Motor Servo SG90', 'Aktuator', '5V', 'PWM', 'Rp 18.000', 'palang, putar, engsel, penggerak, rotasi, ayun, buka, tutup, mekanik, presisi'),
    ('K80', 'Motor Servo MG996R', 'Aktuator', '5V', 'PWM', 'Rp 60.000', 'palang, putar, torsi, penggerak, rotasi, lengan robot, mekanik, presisi, kuat'),
    ('K81', 'Motor DC Gearbox', 'Aktuator', '3V-6V', 'Power / PWM', 'Rp 15.000', 'roda, jalan, putar, mobil, robot, penggerak, dinamo, baling'),
    ('K82', 'Motor Stepper NEMA 17', 'Aktuator', '12V', 'Digital (Driver)', 'Rp 110.000', 'motor, presisi, cnc, printer 3d, putar, langkah, derajat, mekanik berat, geser'),
    ('K83', 'Solenoid Valve 1/2 Inch', 'Aktuator', '12V', 'Power / Relay', 'Rp 55.000', 'katup, kran, air, tutup, buka kran, saluran, pipa, cairan, otomatis'),
    ('K84', 'Pompa Air Mini 5V', 'Aktuator', '5V', 'Power / Relay', 'Rp 20.000', 'pompa, air, sedot, siram, semprot, mengalir, akuarium, cairan, dorong'),
    ('K85', 'Pompa Peristaltik', 'Aktuator', '12V', 'Power / Relay', 'Rp 75.000', 'pompa, cairan, dosis, akurat, kimia, selang, laboratorium, presisi, hidroponik'),
    ('K86', 'Linear Actuator 12V', 'Aktuator', '12V', 'Power / Relay', 'Rp 350.000', 'dorong, tarik, mekanik berat, lurus, angkat, tekan, hidrolik, panjang, geser'),
    ('K87', 'Peltier Thermoelectric Cooler', 'Aktuator', '12V', 'Power / Relay', 'Rp 45.000', 'dingin, kulkas, beku, es, pendingin, panas, suhu ekstrem, dispenser'),
    ('K88', 'Kipas Pendingin (Fan) 12V', 'Aktuator', '12V', 'Power / PWM', 'Rp 15.000', 'angin, kipas, tiup, dingin, sirkulasi, ventilasi, suhu, pendingin'),
    ('K89', 'Servo Linear SG90', 'Aktuator', '5V', 'PWM', 'Rp 35.000', 'geser, dorong, tarik, kecil, ringan, presisi, aktuator mini'),
    ('K90', 'Buzzer Aktif 5V', 'Output', '5V', 'Digital', 'Rp 5.000', 'suara, alarm, peringatan, bunyi, notifikasi, sirine, berisik, tanda'),
    ('K91_ACT', 'Motor BLDC 2204', 'Aktuator', '7V-14V', 'Digital (ESC)', 'Rp 165.000', 'motor, bldc, drone, kecepatan tinggi, propeller, udara, terbang, esc, rpm tinggi'),
    ('K92_ACT', 'ESC (Electronic Speed Controller) 30A', 'Aktuator', '7V-14V', 'PWM', 'Rp 95.000', 'esc, motor bldc, drone, kecepatan, kontrol, throttle, rpm, terbang'),
    ('K93_ACT', 'Motor Servo Waterproof DS3230', 'Aktuator', '6V', 'PWM', 'Rp 145.000', 'servo, anti air, waterproof, torsi tinggi, robot, outdoor, kuat, mekanik berat'),
    ('K94_ACT', 'Vibration Motor (ERM)', 'Aktuator', '3V-5V', 'Digital / PWM', 'Rp 12.000', 'getar, vibrasi, notifikasi, haptic, sinyal, tanda, wearable, getaran'),
    ('K95_ACT', 'Pneumatik Solenoid 2/2 Way', 'Aktuator', '24V', 'Power / Relay', 'Rp 185.000', 'pneumatik, udara bertekanan, katup, piston, silinder, industri, angin, dorong'),

    # ==============================
    # OUTPUT & DISPLAY (K96 - K115)
    # ==============================
    ('K96', 'LCD I2C 16x2', 'Output', '5V', 'I2C', 'Rp 35.000', 'layar, teks, visual, monitor, informasi, tulisan, baca, tampil, karakter'),
    ('K97', 'LCD I2C 20x4', 'Output', '5V', 'I2C', 'Rp 65.000', 'layar, teks, visual, monitor, informasi, besar, tampil, karakter, banyak baris'),
    ('K98', 'Layar OLED 0.96 Inch I2C', 'Output', '3.3V-5V', 'I2C', 'Rp 30.000', 'layar, teks, visual, monitor, informasi, tulisan, baca, tampil, oled, grafik, mungil'),
    ('K99', 'Layar OLED 1.3 Inch SH1106', 'Output', '3.3V-5V', 'I2C', 'Rp 45.000', 'layar, teks, visual, oled, grafik, lebar, informasi, tampil, presisi'),
    ('K100', 'Layar TFT LCD 2.4 Inch', 'Output', '5V', 'SPI / Parallel', 'Rp 80.000', 'layar, warna, visual, monitor, gambar, ui, interface, sentuh, grafik warna'),
    ('K101', 'Layar TFT ILI9341 3.5 Inch', 'Output', '3.3V', 'SPI', 'Rp 160.000', 'layar, warna, besar, visual, monitor, gambar, ui, grafik, dashboard'),
    ('K102', 'LED Strip NeoPixel WS2812B', 'Output', '5V', 'Digital', 'Rp 45.000', 'lampu, warna, warni, hias, animasi, rgb, terang, cahaya, dekorasi, led'),
    ('K103', 'LED Matrix 8x8 MAX7219', 'Output', '5V', 'SPI', 'Rp 25.000', 'lampu, animasi, teks berjalan, matrix, pixel, tampil, indikator'),
    ('K104', 'Modul MP3 DFPlayer Mini', 'Output', '5V', 'UART', 'Rp 20.000', 'suara, lagu, musik, mp3, audio, speaker, bunyi, vokal, putar lagu'),
    ('K105', 'Seven Segment Display TM1637', 'Output', '5V', 'I2C', 'Rp 15.000', 'angka, tampil, jam, hitung, skor, digit, bilangan, timer, counter'),
    ('K106', 'Amplifier Audio PAM8403', 'Modul Daya', '5V', 'Analog', 'Rp 10.000', 'suara, keras, speaker, pengeras, volume, audio, boom, amplifier'),
    ('K107_OUT', 'Layar E-Paper 2.9 Inch', 'Output', '3.3V', 'SPI', 'Rp 185.000', 'layar, e-paper, e-ink, teks, hemat daya, hitam putih, tag, label, luar ruangan'),
    ('K108_OUT', 'LED RGB Common Cathode', 'Output', '5V', 'Digital / PWM', 'Rp 3.000', 'lampu, warna, rgb, merah, hijau, biru, indikator, cahaya, led'),
    ('K109_OUT', 'Layar Dot Matrix P10 LED', 'Output', '5V', 'SPI', 'Rp 95.000', 'papan iklan, teks berjalan, besar, lampu, matrix, led, tampil, outdoor'),
    ('K110_OUT', 'Modul MAX98357 I2S Amplifier', 'Output', '5V', 'I2S', 'Rp 35.000', 'audio, speaker, i2s, digital audio, pengeras, suara, i2s dac, musik'),
    ('K111_OUT', 'Layar HDMI 5 Inch Touchscreen', 'Output', '5V', 'HDMI / DSI', 'Rp 450.000', 'layar, hdmi, sentuh, touchscreen, raspberry, besar, tampil, ui, dashboard'),
    ('K112_OUT', 'Modul DAC MCP4725', 'Output', '3.3V-5V', 'I2C', 'Rp 20.000', 'dac, analog output, tegangan, sinyal, gelombang, konversi, kontrol'),
    ('K113_OUT', 'Buzzer Pasif 5V', 'Output', '5V', 'PWM', 'Rp 5.000', 'suara, nada, melodi, bunyi, musik sederhana, peringatan, alarm, notifikasi'),
    ('K114_OUT', 'Laser Diode 650nm 5V', 'Output', '5V', 'Digital / Analog', 'Rp 8.000', 'laser, titik, cahaya, merah, tembak, pointer, sinar, deteksi garis'),
    ('K115_OUT', 'Strip LED COB 12V', 'Output', '12V', 'Power / PWM', 'Rp 35.000', 'lampu, cob, led, terang, putih, rumah, penerangan, dekorasi, pencahayaan'),

    # ==============================
    # INPUT (K116 - K125)
    # ==============================
    ('K116', 'Keypad Matrix 4x4', 'Input', '5V', 'Digital', 'Rp 15.000', 'tombol, ketik, angka, sandi, password, pin, pencet, akses, input'),
    ('K117', 'Sensor Sentuh TTP223', 'Input', '5V', 'Digital', 'Rp 5.000', 'sentuh, jari, raba, kapasitif, tombol, pencet, tap, kulit'),
    ('K118', 'Rotary Encoder EC11', 'Input', '5V', 'Digital', 'Rp 12.000', 'putar, kenop, volume, navigasi, menu, gulir, arah, klik, encoder'),
    ('K119', 'Joystick Analog 2-Axis', 'Input', '5V', 'Analog', 'Rp 18.000', 'arah, kendali, gerak, kanan, kiri, atas, bawah, robot, kendali jarak jauh'),
    ('K120', 'Push Button Tactile', 'Input', '5V', 'Digital', 'Rp 2.000', 'tombol, pencet, tekan, saklar, input, on off, manual, trigger'),
    ('K121', 'Potensiometer 10K', 'Input', '5V', 'Analog', 'Rp 5.000', 'putar, atur, analog, volume, level, kenop, nilai, kontrol'),
    ('K122_IN', 'Keypad Matrix 4x3', 'Input', '5V', 'Digital', 'Rp 12.000', 'tombol, angka, sandi, password, pin, pencet, input, numerik, akses'),
    ('K123_IN', 'Sliding Switch', 'Input', '5V', 'Digital', 'Rp 3.000', 'geser, mode, saklar, on off, pilih, switch, manual, toggle'),
    ('K124_IN', 'DIP Switch 8-bit', 'Input', '5V', 'Digital', 'Rp 8.000', 'dip, konfigurasi, mode, alamat, pengaturan, input, manual, 8 bit'),
    ('K125_IN', 'Sensor Getaran Sentuh TTP226', 'Input', '5V', 'Digital', 'Rp 12.000', 'sentuh, 8 tombol, kapasitif, touch, panel, input, jari, tap, multi tombol'),

    # ==============================
    # KOMUNIKASI (K126 - K145)
    # ==============================
    ('K126', 'Modul Bluetooth HC-05', 'Komunikasi', '5V', 'UART', 'Rp 45.000', 'bluetooth, nirkabel, hp, smartphone, sambungan, jarak dekat, komunikasi'),
    ('K127', 'Modul Bluetooth BLE HM-10', 'Komunikasi', '3.3V', 'UART', 'Rp 65.000', 'bluetooth, ble, low energy, hp, smartphone, ios, android, hemat baterai'),
    ('K128', 'Modul LoRa SX1278', 'Komunikasi', '3.3V', 'SPI', 'Rp 85.000', 'lora, jarak jauh, sinyal, radio, komunikasi, nirkabel, hutan, desa, pelosok'),
    ('K129', 'Modul GSM SIM800L', 'Komunikasi', '3.7V-4.2V', 'UART', 'Rp 65.000', 'sms, telepon, sinyal, seluler, kartu sim, pesan, jarak jauh, komunikasi'),
    ('K130', 'Modul 4G LTE SIM7600', 'Komunikasi', '5V', 'UART', 'Rp 450.000', '4g, lte, internet, seluler, cepat, kota, data, iot, komunikasi'),
    ('K131', 'Modul Ethernet W5500', 'Komunikasi', '3.3V', 'SPI', 'Rp 75.000', 'ethernet, lan, kabel utp, internet, jaringan, router, stabil, offline to online'),
    ('K132', 'Modul Transceiver NRF24L01', 'Komunikasi', '3.3V', 'SPI', 'Rp 18.000', 'radio, sinyal, jarak menengah, remote, kontrol, nirkabel, rc, 2.4ghz'),
    ('K133', 'Modul WiFi ESP-01', 'Komunikasi', '3.3V', 'UART', 'Rp 25.000', 'wifi, internet, iot, modul kecil, sambungan, nirkabel, web'),
    ('K134', 'Modul GPS NEO-6M', 'Komunikasi', '3.3V-5V', 'UART', 'Rp 85.000', 'lokasi, peta, koordinat, lacak, posisi, satelit, tracker, tempat, gps'),
    ('K135', 'Modul ZigBee XBee', 'Komunikasi', '3.3V', 'UART', 'Rp 280.000', 'zigbee, mesh, jaringan, sensor network, banyak node, smart home, nirkabel'),
    ('K136_COM', 'Modul LoRaWAN RAK811', 'Komunikasi', '3.3V', 'UART / I2C', 'Rp 195.000', 'lorawan, lora, jarak jauh, cloud, iot, gateway, server, nirkabel, pelosok'),
    ('K137_COM', 'Modul WiFi ESP32-S2', 'Komunikasi', '3.3V', 'Multiple', 'Rp 75.000', 'wifi, internet, iot, usb, embedded, low power, nirkabel, cloud'),
    ('K138_COM', 'Modul GSM SIM7070G NB-IoT', 'Komunikasi', '3.3V', 'UART', 'Rp 195.000', 'nb-iot, lpwan, gsm, sms, iot, hemat daya, seluler, kartu sim, jarak jauh'),
    ('K139_COM', 'Modul CAN Bus MCP2515', 'Komunikasi', '5V', 'SPI', 'Rp 35.000', 'can bus, otomotif, mobil, industri, jaringan, kendaraan, komunikasi, protokol'),
    ('K140_COM', 'Modul RS485 MAX485', 'Komunikasi', '5V', 'UART', 'Rp 15.000', 'rs485, industri, kabel, modbus, jarak jauh, serial, protokol, wired'),
    ('K141_COM', 'Modul Infrared Remote NEC', 'Komunikasi', '5V', 'Digital', 'Rp 12.000', 'infrared, remote, kendali jarak jauh, tv, ir, penerima, pengirim, kontrol'),
    ('K142_COM', 'Modul GPS GLONASS BN-880', 'Komunikasi', '3.3V-5V', 'UART', 'Rp 145.000', 'gps, glonass, lokasi, presisi tinggi, drone, koordinat, satelit, navigasi, tracker'),
    ('K143_COM', 'Modul Ethernet ENC28J60', 'Komunikasi', '3.3V', 'SPI', 'Rp 25.000', 'ethernet, lan, internet, jaringan, kabel, murah, wired, arduino, web server'),
    ('K144_COM', 'Modul MQTT Bridge WiFi', 'Komunikasi', '5V', 'UART', 'Rp 85.000', 'mqtt, wifi, iot, cloud, broker, pesan, nirkabel, protokol, server'),
    ('K145_COM', 'Modul 433MHz RF Transmitter/Receiver', 'Komunikasi', '5V', 'Digital', 'Rp 12.000', 'radio, rf, 433mhz, remote, nirkabel, sinyal, kendali, jarak menengah'),

    # ==============================
    # MODUL DAYA (K146 - K165)
    # ==============================
    ('K146', 'Modul Relay 1 Channel', 'Modul Daya', '5V', 'Digital', 'Rp 10.000', 'saklar, daya, arus, pemutus, sambung, listrik, pemicu, tegangan tinggi'),
    ('K147', 'Modul Relay 4 Channel', 'Modul Daya', '5V', 'Digital', 'Rp 35.000', 'saklar, daya, arus, banyak perangkat, pemutus, listrik, otomatis, rumah pintar'),
    ('K148', 'Modul Relay Solid State (SSR)', 'Modul Daya', '5V', 'Digital', 'Rp 45.000', 'saklar, daya, arus, pemutus, tanpa suara, awet, ac, tegangan tinggi'),
    ('K149', 'Driver Motor L298N', 'Modul Daya', '12V', 'Digital / PWM', 'Rp 25.000', 'driver, penggerak, dinamo, mobil, robot, roda, arah, putaran, kontrol dc'),
    ('K150', 'Driver Motor L9110S', 'Modul Daya', '5V-12V', 'Digital / PWM', 'Rp 12.000', 'driver, penggerak, kecil, dinamo, mobil, robot, arah, putaran, hemat'),
    ('K151', 'Modul Step Down XL4015', 'Modul Daya', 'In: 8-36V', 'Power', 'Rp 20.000', 'turun tegangan, penurun, voltase, dc to dc, buck converter, adaptor, suplai'),
    ('K152', 'Modul Step Up MT3608', 'Modul Daya', 'In: 2-24V', 'Power', 'Rp 15.000', 'naik tegangan, peningkat, voltase, dc to dc, boost converter, lipat ganda'),
    ('K153', 'Modul Pengisi Baterai TP4056', 'Modul Daya', '5V', 'Power', 'Rp 5.000', 'cas, baterai, lithium, charge, isi ulang, power, perlindungan'),
    ('K154', 'Panel Surya 5V 1W', 'Modul Daya', 'Output: 5V', 'Power', 'Rp 25.000', 'matahari, panas, jemur, listrik gratis, panel, surya, daya alam, siang'),
    ('K155', 'Baterai Li-ion 18650', 'Modul Daya', '3.7V', 'Power', 'Rp 35.000', 'baterai, sel, daya, cadangan, simpan listrik, portabel, tanpa kabel'),
    ('K156_PWR', 'Modul DC-DC Buck LM2596', 'Modul Daya', 'In: 4-40V', 'Power', 'Rp 12.000', 'turun tegangan, dc to dc, buck, penurun voltase, suplai, hemat, efisien'),
    ('K157_PWR', 'Modul Step Down 5A LM2596HV', 'Modul Daya', 'In: 4-60V', 'Power', 'Rp 25.000', 'turun tegangan, arus besar, dc to dc, buck, suplai, efisien, industri'),
    ('K158_PWR', 'Driver Stepper Motor A4988', 'Modul Daya', '8V-35V', 'Digital / PWM', 'Rp 20.000', 'driver, stepper, motor langkah, cnc, printer 3d, presisi, kontrol'),
    ('K159_PWR', 'Driver Stepper Motor DRV8825', 'Modul Daya', '8.2V-45V', 'Digital / PWM', 'Rp 25.000', 'driver, stepper, motor langkah, cnc, printer 3d, presisi, microstepping'),
    ('K160_PWR', 'Modul Relay 8 Channel', 'Modul Daya', '5V', 'Digital', 'Rp 75.000', 'saklar, daya, arus, banyak perangkat, rumah pintar, industri, kontrol ac'),
    ('K161_PWR', 'Panel Surya 6V 3W', 'Modul Daya', 'Output: 6V', 'Power', 'Rp 75.000', 'matahari, panel, surya, daya alam, listrik gratis, portabel, outdoor, siang'),
    ('K162_PWR', 'Modul BMS 3S Li-ion', 'Modul Daya', '12.6V', 'Power', 'Rp 25.000', 'bms, proteksi baterai, lithium, overcharge, discharge, seimbang, keselamatan'),
    ('K163_PWR', 'Modul Inverter 12V ke 220V', 'Modul Daya', '12V', 'Power', 'Rp 185.000', 'inverter, dc to ac, listrik, konversi, mobil, portabel, darurat, tegangan ac'),
    ('K164_PWR', 'Modul Pengatur PWM 25A', 'Modul Daya', '10-50V', 'PWM', 'Rp 45.000', 'pwm, kontrol kecepatan, motor, dimmer, atur daya, switching, pengatur'),
    ('K165_PWR', 'Power Supply 12V 5A', 'Modul Daya', 'AC to 12V', 'Power', 'Rp 85.000', 'suplai, adaptor, 12v, daya, trafo, catu daya, stabil, listrik, power supply'),

    # ==============================
    # MODUL WAKTU & PENYIMPANAN (K166 - K170)
    # ==============================
    ('K166', 'Modul RTC DS3231', 'Modul Waktu', '3.3V-5V', 'I2C', 'Rp 25.000', 'waktu, jam, tanggal, jadwal, kalender, real time, alarm waktu, presisi'),
    ('K167', 'Modul MicroSD Card', 'Aksesoris', '3.3V', 'SPI', 'Rp 15.000', 'simpan, data, log, rekam, sdcard, penyimpanan, file, csv, offline logging'),
    ('K168', 'Modul EEPROM 24C256', 'Aksesoris', '3.3V-5V', 'I2C', 'Rp 15.000', 'simpan, data, memori, konfigurasi, non-volatile, persisten, settings'),
    ('K169_WK', 'Modul RTC DS1302', 'Modul Waktu', '3.3V-5V', 'SPI', 'Rp 15.000', 'waktu, jam, tanggal, jadwal, kalender, real time, alarm, murah'),
    ('K170_WK', 'Modul Flash SPI W25Q128', 'Aksesoris', '3.3V', 'SPI', 'Rp 20.000', 'simpan, data, flash, memori, 16mb, firmware, penyimpanan eksternal, spi'),

    # ==============================
    # AKSESORIS & PENDUKUNG (K171 - K185)
    # ==============================
    ('K171', 'Kabel Jumper DuPont', 'Aksesoris', '-', 'Passive', 'Rp 15.000', 'kabel, sambung, kawat, hubung, rakit, prototipe, jumper, koneksi'),
    ('K172', 'Breadboard Solderless', 'Aksesoris', '-', 'Passive', 'Rp 20.000', 'papan, rakit, colok, prototipe, tes, sirkuit, tanpa solder, dasar'),
    ('K173', 'Modul I2C Multiplexer TCA9548A', 'Aksesoris', '3.3V-5V', 'I2C', 'Rp 30.000', 'multiplexer, i2c, banyak sensor, paralel, alamat sama, ekspansi'),
    ('K174', 'Logic Level Converter 3.3V-5V', 'Aksesoris', '-', 'Passive', 'Rp 10.000', 'tegangan, konversi, 3.3v, 5v, antarmuka, kompatibel, level shifter'),
    ('K175', 'Power Supply Module HW-131', 'Modul Daya', 'In: 6-12V', 'Power', 'Rp 18.000', 'suplai, daya, 5v, 3.3v, breadboard, tes, prototipe, stabil'),
    ('K176_ACC', 'Header Pin 40-pin Male', 'Aksesoris', '-', 'Passive', 'Rp 3.000', 'pin, header, sambung, pasang, konektor, male, soldering, papan'),
    ('K177_ACC', 'Header Pin 40-pin Female', 'Aksesoris', '-', 'Passive', 'Rp 3.000', 'pin, header, sambung, pasang, konektor, female, socket, papan'),
    ('K178_ACC', 'PCB Lubang (Perfboard)', 'Aksesoris', '-', 'Passive', 'Rp 10.000', 'pcb, papan, rangkaian, solder, permanen, prototipe, layout, komponen'),
    ('K179_ACC', 'Modul USB Type-C PD', 'Aksesoris', '5V-20V', 'Power', 'Rp 25.000', 'usb, type-c, power delivery, cas, cepat, adaptor, pengisian, suplai'),
    ('K180_ACC', 'Heat Sink Aluminium', 'Aksesoris', '-', 'Passive', 'Rp 8.000', 'heatsink, pendingin, aluminium, panas, termal, ic, mosfet, suhu, disipasi'),
    ('K181_ACC', 'Resistor Kit (600 pcs)', 'Aksesoris', '-', 'Passive', 'Rp 35.000', 'resistor, hambatan, ohm, elektronika dasar, pembatas arus, komponen pasif'),
    ('K182_ACC', 'Kapasitor Elektrolit Kit', 'Aksesoris', '-', 'Passive', 'Rp 30.000', 'kapasitor, kondensator, filter, penyimpan muatan, elektronika, pasif, buffer'),
    ('K183_ACC', 'Dioda Zener Kit', 'Aksesoris', '-', 'Passive', 'Rp 20.000', 'dioda, zener, pengatur tegangan, regulasi, perlindungan, komponen pasif'),
    ('K184_ACC', 'Modul ADC ADS1115', 'Aksesoris', '3.3V-5V', 'I2C', 'Rp 25.000', 'adc, analog digital, presisi 16bit, konversi, sensor analog, ekspansi, input'),
    ('K185_ACC', 'Modul PWM PCA9685', 'Aksesoris', '3.3V-5V', 'I2C', 'Rp 30.000', 'pwm, 16 channel, servo, led, ekspansi, kontrol, multi servo, driver'),

    # ==============================
    # SENSOR — KESEHATAN & MEDIS (K186 - K195)
    # ==============================
    ('K186', 'Sensor Suhu Air DS18B20', 'Sensor', '3.3V-5V', 'Digital (1-Wire)', 'Rp 35.000', 'suhu, air, celup, anti air, panas, dingin, cair, kolam'),
    ('K187_MED', 'Sensor EMG (Elektromyografi)', 'Sensor', '3.3V-5V', 'Analog', 'Rp 185.000', 'emg, otot, kontraksi, gerakan tubuh, prostetik, medis, elektro, biomedis'),
    ('K188_MED', 'Sensor EEG AD8232 (ECG)', 'Sensor', '3.3V', 'Analog', 'Rp 75.000', 'ecg, ekg, jantung, sinyal jantung, medis, elektrokardiogram, pasien, monitoring'),
    ('K189_MED', 'Sensor Tekanan Darah BMP', 'Sensor', '5V', 'UART', 'Rp 350.000', 'tekanan darah, blood pressure, sistol, diastol, medis, kesehatan, pasien'),
    ('K190_MED', 'Sensor Gula Darah (Glukosa)', 'Sensor', '5V', 'Analog', 'Rp 450.000', 'gula darah, glukosa, diabetes, kesehatan, medis, tes darah, pasien'),
    ('K191_MED', 'Sensor Pernapasan (Respiration)', 'Sensor', '3.3V-5V', 'Analog', 'Rp 185.000', 'napas, pernapasan, paru, frekuensi napas, medis, pasien, monitoring, vital'),
    ('K192_MED', 'Sensor Galvanik Kulit (GSR)', 'Sensor', '3.3V-5V', 'Analog', 'Rp 55.000', 'gsr, kulit, keringat, stres, emosi, galvanik, psikologi, biometrik'),
    ('K193_MED', 'Sensor Suhu Tubuh LM35', 'Sensor', '5V', 'Analog', 'Rp 15.000', 'suhu tubuh, temperatur, analog, presisi, sederhana, demam, kesehatan, panas'),
    ('K194_MED', 'Sensor Detak Jantung Pulse Sensor', 'Sensor', '5V', 'Analog', 'Rp 35.000', 'jantung, detak, nadi, bpm, kesehatan, jari, telinga, optik, pasien'),
    ('K195_MED', 'Sensor Sudut Sendi (Flex Sensor)', 'Sensor', '5V', 'Analog', 'Rp 75.000', 'flex, lentur, sudut, sendi, tangan, sarung tangan, vr, gerak, postur'),

    # ==============================
    # SENSOR — PERTANIAN & LINGKUNGAN (K196 - K205)
    # ==============================
    ('K196_AGR', 'Sensor NPK Tanah', 'Sensor', '5V', 'UART / RS485', 'Rp 350.000', 'npk, nitrogen, fosfor, kalium, tanah, nutrisi, pertanian, kebun, subur, pupuk'),
    ('K197_AGR', 'Sensor Intensitas UV', 'Sensor', '3.3V', 'Analog / I2C', 'Rp 25.000', 'uv, ultraviolet, matahari, sinar, indeks uv, kulit, tanaman, outdoor'),
    ('K198_AGR', 'Sensor Klorofil Tanaman', 'Sensor', '5V', 'Analog', 'Rp 285.000', 'klorofil, daun, hijau, tanaman, fotosintesis, kesehatan tanaman, pertanian presisi'),
    ('K199_AGR', 'Sensor Kadar Air Biji-bijian', 'Sensor', '5V', 'UART', 'Rp 450.000', 'kadar air, biji, padi, jagung, gabah, panen, gudang, kering, simpan'),
    ('K200_AGR', 'Anemometer Kecepatan Angin', 'Sensor', '5V', 'Analog / Digital', 'Rp 185.000', 'angin, kecepatan angin, cuaca, stasiun cuaca, outdoor, storm, bencana'),
    ('K201_AGR', 'Sensor Arah Angin (Vane)', 'Sensor', '5V', 'Analog', 'Rp 125.000', 'arah angin, vane, cuaca, stasiun cuaca, kompas angin, outdoor, north'),
    ('K202_AGR', 'Sensor Radiasi Matahari (Pyranometer)', 'Sensor', '5V', 'Analog', 'Rp 650.000', 'radiasi, matahari, surya, irradiasi, panel surya, energi, pertanian, watt per meter'),
    ('K203_AGR', 'Sensor Suhu Tanah DS18B20 Stainless', 'Sensor', '3.3V-5V', 'Digital (1-Wire)', 'Rp 45.000', 'suhu tanah, temperatur, tanah, pertanian, kebun, celup, anti air, presisi'),
    ('K204_AGR', 'Sensor Konduksi Elektrik Tanah (EC)', 'Sensor', '5V', 'Analog', 'Rp 185.000', 'ec, konduktivitas, tanah, garam, salinitas, pertanian presisi, nutrisi, tanah'),
    ('K205_AGR', 'Sensor Cahaya PAR (Photosynthetically Active)', 'Sensor', '5V', 'Analog', 'Rp 350.000', 'par, cahaya, fotosintesis, tanaman, indoor farm, grow light, pertanian, intensitas'),

    # ==============================
    # MODUL KEAMANAN & SMART HOME (K206 - K215)
    # ==============================
    ('K206_SEC', 'Kamera CCTV IP PoE', 'Sensor', '48V PoE', 'Ethernet', 'Rp 350.000', 'kamera, cctv, ip, poe, pantau, rekam, keamanan, outdoor, streaming, jaringan'),
    ('K207_SEC', 'Sensor PIR Dual Element', 'Sensor', '12V', 'Digital', 'Rp 45.000', 'pir, gerak, manusia, keamanan, alarm, anti false alarm, detektor, dual'),
    ('K208_SEC', 'Sensor Asap Photoelectric', 'Sensor', '12V', 'Digital', 'Rp 85.000', 'asap, kebakaran, detektor asap, alarm, bahaya, photoelectric, bangunan, instalasi'),
    ('K209_SEC', 'Sensor Buka Tutup Pintu (Reed Switch)', 'Sensor', '5V', 'Digital', 'Rp 15.000', 'pintu, jendela, buka, tutup, reed switch, magnet, alarm, keamanan, sensor kontak'),
    ('K210_SEC', 'Siren Alarm 12V', 'Output', '12V', 'Power / Relay', 'Rp 35.000', 'sirine, alarm, bunyi keras, peringatan, keamanan, bahaya, luar ruangan'),
    ('K211_SEC', 'Smart Lock Bluetooth', 'Aktuator', '5V', 'Bluetooth', 'Rp 650.000', 'kunci pintar, smart lock, bluetooth, akses, smartphone, keamanan rumah, nirkabel'),
    ('K212_SEC', 'Modul GSM Alarm', 'Komunikasi', '12V', 'UART', 'Rp 185.000', 'alarm, gsm, sms, telepon, keamanan, darurat, notifikasi, pencuri, jarak jauh'),
    ('K213_SEC', 'Doorbell Cerdas WiFi', 'Input', '5V', 'WiFi', 'Rp 450.000', 'bel pintu, wifi, kamera, smart, video call, keamanan, rumah pintar, notifikasi'),
    ('K214_SEC', 'Sensor Pecah Kaca', 'Sensor', '12V', 'Digital', 'Rp 65.000', 'pecah kaca, jendela, keamanan, alarm, detektor, vibrasi, rumah, bangunan'),
    ('K215_SEC', 'Sensor Asap Gas Kombinasi', 'Sensor', '12V', 'Digital', 'Rp 95.000', 'asap, gas, kombinasi, dapur, kebakaran, alarm, bahaya, deteksi dini, co'),

    # ==============================
    # MODUL ROBOTIKA (K216 - K220)
    # ==============================
    ('K216_ROB', 'Sensor Garis Array TCRT5000', 'Sensor', '5V', 'Analog / Digital', 'Rp 25.000', 'garis, line following, robot, tcrt5000, array, deteksi jalur, putih, hitam, lintasan'),
    ('K217_ROB', 'Shield Motor Arduino L293D', 'Modul Daya', '5V-12V', 'Digital / PWM', 'Rp 35.000', 'shield, motor, arduino, l293d, driver, robot, roda, penggerak, otomatis'),
    ('K218_ROB', 'Servo Gripper 3D Printed', 'Aktuator', '5V', 'PWM', 'Rp 185.000', 'gripper, capit, ambil, lengan robot, end effector, servo, robot, genggam'),
    ('K219_ROB', 'Sensor Obstacle 3-Channel IR', 'Sensor', '5V', 'Digital', 'Rp 25.000', 'obstacle, rintangan, ir, infrared, 3 channel, robot, mobil, deteksi, bumper'),
    ('K220_ROB', 'Modul Encoder Roda (Wheel Encoder)', 'Sensor', '5V', 'Digital', 'Rp 35.000', 'encoder, roda, rpm, kecepatan, jarak tempuh, robot, odometri, navigasi'),
]

cursor.executemany('INSERT INTO tb_komponen VALUES (?, ?, ?, ?, ?, ?, ?)', data_komponen)
conn.commit()

total = cursor.execute('SELECT COUNT(*) FROM tb_komponen').fetchone()[0]
conn.close()

print(f"Berhasil! File 'database_iot_v2.db' selesai dibuat dengan total {total} komponen.")