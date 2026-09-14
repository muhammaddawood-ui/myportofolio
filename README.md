Nama: Muhammad Dawood Alfathiin
NPM: 2506610456
Kelas: PBP F

========== TUGAS 1 ========== 
Pertanyaan Reflektif:
1. Iya, <section>, <nav>, dan beberapa komponen lain telah digunakan. Keberadaan <section> memudahkan saya untuk memahami bagian-bagian seperti header/footer, dan saya personally mengadjust <nav>, menambahkan satu button navigasi "Experience". Hal ini tentu sangat membantu karena struktur webnya jadi mudah diakses, bisa lompat antar section. 
2. Tantangan terbesarnya terletak pad amenyusun struktur Experience Title & Period/Span, karena title di layar sempit overflow sedangkan masih harus ada periode di sebelah kanan. Selain itu, jika periode terlalu sempit maka teksnya akan terpotong (misal, "April-", dibawahnya "current"). Di sini, saya memprioritaskan experience title denggan menggunakan flex-wrap, sehingga jika space layar tidak cukup, periode otomatis terdorong ke bawah (baris baru).
3. Batasan yang menurut saya notice akan menjadi hambatan/menyulitkan kedepannya adalah setiap saya menambah experience baru, saya harus hardcode manual di HTMLnya, mencari sectionnya, menambah experience-thing baru disitu.

Deklarasi AI:
Dalam menulis tugas ini, saya TIDAK MENYALIN/MENGAMBIL JAWABAN DARI AI. Saya menggunakan AI sebagai sarana mempelajari HTML & CSS, dan penyusunan website ini banyak melakukan trial & error (Add new section/div/p/text/dsb --> refresh --> edit) hingga tampilan websitenya sesuai dengan apa yang saya inginkan. Saya memulai dari mengupdate HTMLnya langsung (of which, sangat bodoh) hingga mulai membayangkan website sebagai sebuah lahan kosong yang perlu diisi kontainer-kontainer yang diatur CSS, mengambil referensi CV ATS standar sebagai struktur Experience, dan menuliskan sesuai kemampuan yang ada.


========== TUGAS 2 ========== 
1. Alur Pengguna:
A. Pengguna membuka https://domain-lo.com/projects/ --> Browser kirim request ke server dengan path /projects
B. Masuk ke portofolio/urls.py, lalu ke main/urls.py (non-admin), lalu fungsi show_projects dipanggil.
C. Di views.py, show_project dieksekusi, dan query dan dikumpulkan dalam context, lalu dipanggil render(reqeust, "projects.html", context.)
D. projects.html menerima konteks tersebut, dan memproses tag-tag seperti {{ nickname }}, diisi dengan data dari context dengan hasil akhir HTML murni.
E. HTML dikirim balik ke browser, dan di render sebagai halaman akhir yang dilihat pengguna.

2. Data harus di model karena beberapa jika ditulis langsung di projects.html:
A. Tidak scalable. Setiap menambah project baru, perlu edit file dari HTML langsung, dan deploy ulang.
B. Ketika website berkembang, fitur fitur baru muncul, tanpa data yang terstruktur di model, perlu adjustment yang TIDAK sedikit.
C. Tidak ada constraint tipe data, default value, required - yang membuat item-item pada website tidak konsisten.

3. Makemigrations membaca perubahan models.py, lalu membuat file migrations di main/migrations/ (contohnya, dalam kasus ini dilakukan 2 makemigrations yang membuat 2 instruksi database karena kesalahan dalam pembuatan).
Sedangkan migrate mengeksekusi file migration yang ada, dan benar benar merubah skema database sesuai instruksi yang ada pada file-file tersebut.

Deklarasi AI:
Seperti pada Tugas 1, saya menggunakan AI untuk mempelajari konsep konsep, menggunakan Tutorial sebagai basis belajar. Namun dalam tahap ini, saya eksplisit menggunakan AI untuk mendeteksi kesalahan pada pembuatan class Project di models. Awalnya karena ketidaktelitian saya, is_ongoing sebagai function saya tidak sentuh (karena template dari is_ongoing experience), namun tidak sadar bertabrakan dengan variable is_ongoing yang baru saya buat, sehingga saat makemigrations dijalankan, is_ongoing masih dilihat sebagai function dan tidak terdeteksi perubahan. Saya memasukkan potongan kode tersebut ke AI, dan menemukan masalahnya. Baru setelah hal tersebut saya hapus, saya makemigrations ulang dan masalah terselesaikan ^^