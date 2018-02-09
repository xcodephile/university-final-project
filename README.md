# tugas-akhir
Perancangan adaptive Intrusion Prevention System (IPS) untuk pencegahan penyerangan di jaringan Software-Defined Network (SDN) menggunakan metode fuzzy logic. Pengembangan sistem ini melibatkan:
* [Ryu](https://osrg.github.io/ryu/) sebagai SDN controller
* [Mininet](http://mininet.org/) sebagai emulator jaringan
* [Snort](https://www.snort.org) sebagai IPS dengan jenis signature-based

## Daftar Isi
* [Deskripsi](github.com/rifqitama16/tugas-akhir#deskripsi)
* [Cara Kerja](github.com/rifqitama16/tugas-akhir#cara-kerja)
* [Cara Penggunaan](github.com/rifqitama16/tugas-akhir#cara-penggunaan)
* [Hasil](github.com/rifqitama16/tugas-akhir#hasil)

## Deskripsi
Semakin tinggi lalu lintas yang ada pada jaringan, semakin tinggi pula kemungkinan terjadinya ancaman keamanan cyber. Terdapat beberapa cara untuk menangani masalah ini, salah satunya menggunakan Snort yang dapat mendeteksi aktivitas mencurigakan dalam sebuah jaringan dengan cara memindai lalu lintas inbound dan outbound. Jika terbukti berbahaya, maka Snort akan melakukan pemblokiran akses terhadap attacker host berdasarkan alamat IP-nya dalam beberapa saat.

Namun terdapat satu masalah yang kemudian muncul, yaitu Snort tidak dapat beradaptasi terhadap frekuensi serangan. Ini berarti durasi waktu pemblokiran akan tetap statis dengan lama waktu yang telah ditentukan sebelumnya, meskipun host melakukan penyerangan dalam frekuensi yang tinggi.

Fuzzy logic diimplementasikan untuk mengatasi masalah tersebut sehingga tercipta IPS yang dapat beradaptasi terhadap frekuensi serangan dan jenis serangan.

## Cara Kerja
<p align="center"><img src="https://github.com/rifqitama16/tugas-akhir/blob/master/doc/Topologi%202.png" width="700" height="500"></p>

Snort yang digunakan sebagai IPS diinstal pada application plane sedangkan Ryu sebagai controller terdapat di control plane. Tiap lalu lintas yang ada di jaringan akan terlebih dahulu melewati Ryu yang selanjutnya akan diperiksa oleh Snort berdasarkan pencocokan dengan basis data yang telah didefinisikan sebelumnya. Jika dinyatakan aman, maka oleh Ryu akan langsung diteruskan ke tujuan, namun jika terindikasi berbahaya, maka Snort akan mengirim peringatan serta mengatur lama waktu pemblokiran dengan durasi awal 10 menit. Jika host terus melakukan serangan dalam masa waktu kurang dari atau sama dengan 10 menit, maka waktu blokir akan ditetapkan sesuai dengan frekuensi dan jenis serangan.

Proses dimulai dari berkas alert.csv yang merupakan keluaran dari Snort yang berisi timestamp, alamat IP asal, alamat IP tujuan, protokol, dan pesan. Oleh hostInspector.sh akan mengambil baris terakhir dari log dan mencari selisih waktu antara serangan terakhir dan serangan sebelumnya dari sebuah host. Fuzzy hanya akan dieksekusi jika selisih waktu (interval) penyerangan lebih kecil atau sama dengan 10 menit. Keluaran dari fuzzy adalah durasi waktu blokir dalam satuan detik yang nantinya akan berfungsi untuk menjeda proses. Berkas block.sh berfungsi untuk mengirimkan flow entry pemblokiran ke Ryu via REST API. Berkas unblock.sh akan dieksekusi setelah durasi telah mencapai 0 detik dan akan menghapus flow entry
pemblokiran.

## Cara Penggunaan
<p align="center"><img src="https://github.com/rifqitama16/tugas-akhir/blob/master/doc/1.png"></p>

## Hasil
<p align="center"><img src="https://github.com/rifqitama16/tugas-akhir/blob/master/doc/2.png" width="400" height="170"></p>
<p align="center"><img src="https://github.com/rifqitama16/tugas-akhir/blob/master/doc/hasil1-scanning(host-discovery).png" width="600" height="250"></p>
<p align="center"><img src="https://github.com/rifqitama16/tugas-akhir/blob/master/doc/hasil2-DoS.png" width="600" height="250"></p>
