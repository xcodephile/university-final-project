# tugas-akhir
Perancangan adaptive Intrusion Prevention System (IPS) untuk pencegahan penyerangan di jaringan Software-Defined Network (SDN) menggunakan metode fuzzy logic. Pengembangan sistem ini melibatkan:
* [Ryu](https://osrg.github.io/ryu/) sebagai SDN controller
* [Mininet](http://mininet.org/) sebagai emulator jaringan
* [Snort](https://www.snort.org) sebagai IPS dengan jenis signature-based

## Daftar Isi
* [Deskripsi](github.com/rifqitama16/tugas-akhir#deskripsi)
* [Cara Penggunaan](github.com/rifqitama16/tugas-akhir#cara-penggunaan)

## Deskripsi
Semakin tinggi lalu lintas yang ada pada jaringan, semakin tinggi pula kemungkinan terjadinya ancaman keamanan cyber. Terdapat beberapa cara untuk menangani masalah ini, salah satunya menggunakan Snort yang dapat mendeteksi aktivitas mencurigakan dalam sebuah jaringan dengan cara memindai lalu lintas inbound dan outbound. Jika terbukti berbahaya, maka Snort akan melakukan pemblokiran akses terhadap attacker host berdasarkan alamat IP-nya dalam beberapa saat.

Namun terdapat satu masalah yang kemudian muncul, yaitu Snort tidak dapat beradaptasi terhadap frekuensi serangan. Ini berarti durasi waktu pemblokiran akan tetap statis dengan lama waktu yang telah ditentukan sebelumnya, meskipun host melakukan penyerangan dalam frekuensi yang tinggi.

Fuzzy logic diimplementasikan untuk mengatasi masalah tersebut sehingga tercipta IPS yang dapat beradaptasi terhadap frekuensi serangan dan jenis serangan.

## Cara Kerja
![Topologi](https://github.com/rifqitama16/tugas-akhir/blob/master/doc/Topologi%202.png)
![Flow Chart](https://github.com/rifqitama16/tugas-akhir/blob/master/doc/Flowchart%20-%20Block%20Diagram.png)

## Cara Penggunaan
![Contoh](https://github.com/rifqitama16/tugas-akhir/blob/master/doc/1.png)


## Hasil
![Hasil 1](https://github.com/rifqitama16/tugas-akhir/blob/master/doc/2.png)
![Hasil 2](https://github.com/rifqitama16/tugas-akhir/blob/master/doc/hasil1-scanning(host-discovery).png)
![Hasil 3](https://github.com/rifqitama16/tugas-akhir/blob/master/doc/hasil2-DoS.png)
