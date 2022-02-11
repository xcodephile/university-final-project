# university-final-project a.k.a. Skripsi
<i>Perancangan adaptive Intrusion Prevention System (IPS) untuk pencegahan penyerangan di jaringan Software-Defined Network (SDN) menggunakan logika fuzzy.</i>

Pengembangan sistem ini melibatkan:
* [Ryu](https://osrg.github.io/ryu/) sebagai SDN controller
* [Mininet](http://mininet.org/) sebagai emulator jaringan
* [Snort](https://www.snort.org) sebagai IPS dengan jenis signature-based

## Daftar Isi
* [Deskripsi](https://github.com/rifqitama16/tugas-akhir#deskripsi)
* [Cara Kerja](https://github.com/rifqitama16/tugas-akhir#cara-kerja)
* [Cara Penggunaan](https://github.com/rifqitama16/tugas-akhir#cara-penggunaan)
* [Hasil](https://github.com/rifqitama16/tugas-akhir#hasil)

## Deskripsi
Semakin tinggi lalu lintas yang hilir mudik melewati suatu jaringan, semakin tinggi pula kemungkinan terjadinya ancaman keamanan siber. Salah satu solusi untuk mencegahnya yaitu menggunakan perangkat lunak bernama Snort yang dapat mendeteksi aktivitas mencurigakan dengan cara memindai lalu lintas yang masuk dan keluar. Jika terbukti berbahaya, maka Snort akan melakukan pemblokiran akses berdasarkan alamat IP selama beberapa saat.

Namun muncul satu masalah, Snort tidak dapat beradaptasi terhadap frekuensi dan jenis serangan. Ini berarti durasi waktu pemblokiran akan tetap statis dengan lama waktu yang telah ditentukan sebelumnya, meskipun host melakukan penyerangan dalam frekuensi tinggi dan severity tinggi.

Logika Fuzzy diimplementasikan untuk mengatasi masalah tersebut sehingga tercipta IPS yang dapat beradaptasi terhadap frekuensi serangan dan jenis serangan.

## Cara Kerja
Snort diinstal di application plane dan Ryu ditempatkan di control plane. Semua lalu lintas akan terlebih dahulu melewati Ryu dan selanjutnya akan diperiksa oleh Snort berdasarkan pencocokan dengan basis data yang telah didefinisikan sebelumnya (lihat file `myrules.rules` di repositori). Jika dinyatakan aman, maka Ryu akan meneruskan ke tujuan. Namun jika terindikasi berbahaya, Snort akan mengirim peringatan serta mengatur lama waktu pemblokiran dengan durasi awal 10 menit. Jika host terus melakukan serangan dalam masa waktu kurang dari atau sama dengan 10 menit, maka waktu pemblokiran akan bertambah sesuai dengan frekuensi dan jenis serangan.

Proses dimulai dari file log `alert.csv` yang merupakan output dari Snort yang berisi informasi timestamp, alamat IP asal, alamat IP tujuan, protokol, dan pesan. File `hostInspector.sh` akan mengambil baris terakhir dari log tersebut dan mencari selisih waktu antara serangan terakhir dan serangan sebelumnya dari host yang sama. Fuzzy (semua file yang berekstensi `*.py`) hanya akan dieksekusi jika selisih waktu penyerangan lebih kecil atau sama dengan 10 menit. Output dari fuzzy adalah durasi waktu blokir dalam satuan detik yang nantinya akan berfungsi untuk menjeda proses. File `block.sh` berfungsi untuk mengirimkan flow entry pemblokiran ke Ryu via REST API. File `unblock.sh` akan dieksekusi setelah durasi telah mencapai 0 detik dan akan menghapus flow entry pemblokiran.

Adapun topologi yang digunakan adalah sebagai berikut.
<p align="center"><img src="https://github.com/rifqitama16/tugas-akhir/blob/master/doc/Topologi%202.png" width="550" height="400"></p>

## Instalasi dan Konfigurasi
Lakukan proses instalasi Ryu, Mininet, dan Snort terlebih dahulu yang dokumentasinya dapat dibaca di situs web mereka masing-masing.

1. Jalankan Ryu.

    `ryu-manager ~/ryu/ryu/app/rest_firewall.py`

2. Jalankan Mininet dengan opsi controller remote (diarahkan ke Ryu yang telah running) serta custom topologi yang ada di file `topologi.py`.

    `mn --custom ~/mininet/custom/topologi.py --topo mytopo --controller remote --switch ovsk,protocols=OpenFlow13`

3. Secara default lalu lintas dari dan ke seluruh host akan diblokir oleh Ryu sehingga diperlukan penambahan flow entry dengan cara menjalankan file `flowEntry.sh`.

    `bash ~/flowEntry.sh`

4. Jalankan Snort dengan interface menggunakan s1-eth1 (switch 1 port eth-1).

    `snort -i s1-eth1 -c /etc/snort/snort.conf -l /var/log/snort`

5. Jalankan file `hostInspector.sh`.

    `bash ~/hostInspector.sh`

## Pengujian

Untuk Pengujian, lakukan uji serangan yang sesuai dengan basis data serangan Snort di file `myrules.rules` yaitu host discovery (menggunakan metode port scanning) dan DoS agar peringatan bahwa telah terjadi serangan dapat tersimpan ke /var/log/snort/alert.csv.

`attacker nmap -v -n -sP --send-ip 192.168.0.0/29`

Sedangkan untuk DoS dapat memanfaatkan tools hping3.

`attacker hping3 -c 100 -d 120 -S -w 64 -p 53 --flood server`

<p align="center"><img src="https://github.com/rifqitama16/tugas-akhir/blob/master/doc/1.png"></p>

## Hasil
Berikut contoh tangkapan layar ketika mencoba ping ke host yang sedang diblokir.

<p align="center"><img src="https://github.com/rifqitama16/tugas-akhir/blob/master/doc/2.png" width="370" height="130"></p>

Dua gambar di bawah ini menjelaskan bagaimana hubungan antara interval (selisih) waktu serangan suatu host dengan durasi blokir untuk masing-masing jenis serangan.

### Host Discovery
<p align="center"><img src="https://github.com/rifqitama16/tugas-akhir/blob/master/doc/hasil1-scanning(host-discovery).png" width="600" height="240"></p>

## DoS
<p align="center"><img src="https://github.com/rifqitama16/tugas-akhir/blob/master/doc/hasil2-DoS.png" width="600" height="240"></p>

## Tautan Eksternal
* [Paper IEEE](https://ieeexplore.ieee.org/document/8528735)
* [Buku Tugas Akhir](https://repository.telkomuniversity.ac.id/pustaka/138374/perancangan-dan-implementasi-adaptive-intrusion-prevention-system-ips-untuk-pencegahan-penyerangan-pada-arsitektur-software-defined-network-sdn-.html)
* [Referensi 1](http://ieeexplore.ieee.org/document/6834762/), [Referensi 2](http://ieeexplore.ieee.org/document/7014181/), dan [Referensi 3](http://ieeexplore.ieee.org/document/4599918/)
