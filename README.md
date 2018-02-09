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
Snort yang digunakan sebagai IPS diinstal pada application plane sedangkan Ryu sebagai controller terdapat di control plane. Tiap lalu lintas yang ada di jaringan akan terlebih dahulu melewati Ryu yang selanjutnya akan diperiksa oleh Snort berdasarkan pencocokan dengan basis data yang telah didefinisikan sebelumnya (ada di `myrules.rules`). Jika dinyatakan aman, maka oleh Ryu akan langsung diteruskan ke tujuan, namun jika terindikasi berbahaya, maka Snort akan mengirim peringatan serta mengatur lama waktu pemblokiran dengan durasi awal 10 menit. Jika host terus melakukan serangan dalam masa waktu kurang dari atau sama dengan 10 menit, maka waktu blokir akan ditetapkan sesuai dengan frekuensi dan jenis serangan.

Proses dimulai dari file log `alert.csv` yang merupakan keluaran dari Snort yang berisi timestamp, alamat IP asal, alamat IP tujuan, protokol, dan pesan. Oleh `hostInspector.sh` akan mengambil baris terakhir dari log dan mencari selisih waktu antara serangan terakhir dan serangan sebelumnya dari sebuah host. Fuzzy (semua file yang berekstensi .py) hanya akan dieksekusi jika selisih waktu (interval) penyerangan lebih kecil atau sama dengan 10 menit. Keluaran dari fuzzy adalah durasi waktu blokir dalam satuan detik yang nantinya akan berfungsi untuk menjeda proses. Berkas `block.sh` berfungsi untuk mengirimkan flow entry pemblokiran ke Ryu via REST API. Berkas `unblock.sh` akan dieksekusi setelah durasi telah mencapai 0 detik dan akan menghapus flow entry pemblokiran.

Adapun topologi yang digunakan adalah sebagai berikut.
<p align="center"><img src="https://github.com/rifqitama16/tugas-akhir/blob/master/doc/Topologi%202.png" width="600" height="400"></p>

## Cara Penggunaan
Lakukan proses instalasi Ryu, Mininet, dan Snort terlebih dahulu yang dokumentasinya dapat dibaca di situs web mereka masing-masing.

1. Jalankan Ryu.
`   ryu-manager ~/ryu/ryu/app/rest_firewall.py`

2. Jalankan Mininet dengan opsi controller remote (diarahkan ke Ryu yang telah running) serta custom topologi yang ada di file `topologi.py`.
`   mn --custom ~/mininet/custom/topologi.py --topo mytopo --controller remote`

3. Secara default lalu lintas dari dan ke seluruh host akan diblokir oleh Ryu sehingga diperlukan penambahan flow entry dengan cara menjalankan file `flowEntry.sh`.
`   bash ~/flowEntry.sh`

4. Jalankan Snort dengan interface menggunakan s1-eth1 (switch 1 port eth-1).
`   snort -A full -i s1-eth1 -c /etc/snort/snort.conf -l /var/log/snort`

5. Jalankan file `hostInspector.sh`.
`   bash ~/hostInspector.sh`

Untuk Pengujian, lakukan uji serangan yang sesuai dengan basis data serangan Snort di file `myrules.rules` yaitu port scanning dan DoS.
`   attacker nmap -v -n -sP --send-ip 192.168.0.0/29`
Sedangkan untuk DoS dapat memanfaatkan tools hping3.
`   attacker hping3 -c 100 -d 120 -S -w 64 -p 53 --flood server`

<p align="center"><img src="https://github.com/rifqitama16/tugas-akhir/blob/master/doc/1.png"></p>

## Hasil
<p align="center"><img src="https://github.com/rifqitama16/tugas-akhir/blob/master/doc/2.png" width="400" height="170"></p>
<p align="center"><img src="https://github.com/rifqitama16/tugas-akhir/blob/master/doc/hasil1-scanning(host-discovery).png" width="600" height="250"></p>
<p align="center"><img src="https://github.com/rifqitama16/tugas-akhir/blob/master/doc/hasil2-DoS.png" width="600" height="250"></p>

## Sumber Luar
* Paper IEEE (tba)
* Buku Tugas Akhir
* Referensi 1, Referensi 2, dan Referensi 3
