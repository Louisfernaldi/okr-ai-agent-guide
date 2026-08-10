# 6 jebakan yang paling sering bikin ditolak

Penilai bakal jalanin tiap ajuan lewat enam pertanyaan ini. **Agent wajib nyegat di depan**,
sebelum ngirim, bukan nunggu ditolak. Kalau nunggu ditolak, pemakai kebuang satu ronde
percuma.

Tanda di tiap jebakan:
- **[mesin]** = pemeriksa `kirim_ajuan.py --cek` yang mutusin, agent tinggal bacain hasilnya
- **[tanya]** = ga bisa dicek mesin, agent wajib nanya ke pemakai dan nimbang jawabannya
- **[penilai]** = agent ga punya cara mastiin, ini nyerah ke penilai. Agent tetap wajib
  ngingetin di depan biar pemakai ga kaget.

---

## Jebakan 1. Ukuranmu bisa MERAH ga? [mesin]

Cara ukurnya bakal dites ke data lama. **Wajib ada minggu yang hasilnya GAGAL.** Kalau
ukuranmu ga mungkin gagal apa pun yang terjadi, itu bukan timbangan, itu stiker. Contoh
stiker: "halamannya bisa dibuka". Begitu sekali hidup, dia ga akan pernah merah lagi
selamanya.

Ini juga alasan isian 4 wajib rincian per minggu: tanpa rincian mingguan, ga ada yang bisa
ngecek ukurannya pernah merah apa nggak.

Cara mesin ngecek: pakai arah yang ditanya di Langkah 3 (naik atau turun bagusnya), hitung
ada berapa minggu di isian 4 yang jatuh di sisi GAGAL dari ambang isian 5. Nol minggu di
sisi gagal berarti jebakan 1 kena.

Kalau kena, jangan cuma bilang "ditolak". Tunjukin angkanya: "delapan minggumu semuanya
udah di bawah 20%, jadi ambang 20% ga mungkin merah. Coba ambang yang lebih berani, atau
ukuran yang beda."

## Jebakan 2. Targetnya udah kecapai duluan ga? [mesin]

Kalau angka sebelum (isian 4) ternyata UDAH lebih bagus dari ambang (isian 5), berarti
targetnya udah lewat sebelum kuartal mulai. Itu bukan kabar baik, itu tanda ambangnya harus
dinaikin.

Cara mesin ngecek: rata-rata angka isian 4 dibanding ambang isian 5, pakai arah yang sama.
Rata-rata udah di sisi lolos berarti jebakan 2 kena.

## Jebakan 3. Buktinya kamu sendiri yang nulis ga? [tanya]

Kalau bukti satu-satunya adalah screenshot yang diambil sendiri, atau sheet yang diisi
sendiri, buktinya dianggap **belum cukup dan wajib ada pendamping**. Bukan haram, tapi ga
boleh berdiri sendirian. Bukti yang kuat itu jejak yang keluar sendiri dari sistem waktu
kerjaannya jalan, tanpa siapa pun ngetik apa-apa.

Yang agent tanya, sesudah isian 2 keisi:

> "Angka itu nyatetnya sendiri di sistem, atau ada bagian yang kamu ketik manual?"

Kalau jawabannya ada bagian manual, jangan langsung tolak. Ajak nyari pendamping: sistem
lain mana yang nyatet kejadian yang sama tanpa disentuh tangan. Tambahin nama sistem
pendamping itu ke isian 2.

## Jebakan 4. Jejaknya udah ada hari ini, atau baru ada setelah barangmu jadi? [tanya]

Kalau sistem pencatatnya baru lahir bareng barangnya, berarti ga ada angka "sebelum". Tanpa
angka sebelum, dampaknya ga bisa dinilai kuartal ini. Mending ketahuan sekarang daripada
bulan Oktober.

Yang agent tanya, sesudah isian 2 keisi:

> "Sistem yang kamu sebut itu udah jalan hari ini, atau baru ada nanti setelah barangmu
> jadi?"

Kalau jawabannya "baru ada nanti", angka isian 4 mustahil diambil. Berhenti di situ, ajak
cari jejak yang UDAH ada sekarang. Kalau nol ada jejak lama sama sekali, jujur bilang target
ini belum bisa dinilai kuartal ini, dan bantu cari target lain yang jejaknya udah jalan.

Tanda bahaya buat agent: pemakai bisa nyebut delapan angka mingguan dengan lancar tapi ga
bisa jawab dari mana ngambilnya. Itu tanda angkanya dikarang. Kalau curiga, minta dia
sebutin cara ngitung satu minggu saja dari awal sampai akhir.

## Jebakan 5. Angkamu bisa bagus lewat jalan yang salah ga? [mesin + tanya]

Contoh nyata: "cetak ulang label turun" bisa turun karena kerjaannya bagus, bisa juga turun
karena minggu itu kita hampir ga ngirim apa-apa.

Obatnya satu **angka penjaga**: angka kedua yang dilapor barengan, gunanya cuma mbedain dua
sebab itu. Di contoh tadi, angka penjaganya jumlah pengiriman minggu itu. Kalau cetak ulang
turun tapi jumlah pengiriman juga ikut anjlok, ketahuan itu bukan hasil kerjaannya.

Angka penjaga ini pemakai yang nulis, tempatnya di isian 8. Ambangnya wajib berupa angka,
ditulis di awal, bukan "pokoknya jangan jelek". Kalau targetnya ga mungkin dijagain angka
apa pun, itu tanda ukurannya kelewat gampang diakalin, dan itu bakal balik ke pemakai waktu
dinilai.

**[mesin]** Pemeriksa cuma bisa mastiin `penjaga_nama` keisi dan `penjaga_ambang` beneran
angka.

**[tanya]** Dua aturan turunan di bawah ini agent yang wajib baca sendiri dari isian 3, ga
ada mesinnya:

- **Aturan penyebut.** Kalau ukurannya berbentuk persen, yang jadi pembagi wajib dibatesin
  ke kelompok yang emang relevan. "Pesanan manual dibagi TOTAL semua pesanan" itu bocor:
  begitu order Shopee naik, persennya turun sendiri tanpa ngapa-ngapain. Agent baca isian 3,
  cari kata "dibagi", lalu tanya: "pembaginya itu semua pesanan, atau cuma pesanan yang
  sejenis?"
- **Aturan rata-rata, bukan total.** Ukuran berbentuk "total per hari" hampir selalu kebawa
  ramai-sepinya order. Pakai rata-rata per satuan kerjaan (per order, per desain, per
  pesanan), bukan jumlah total. Agent baca isian 3, kalau nemu "jumlah total per hari" atau
  sejenisnya, tawarin diubah jadi rata-rata per satuan.

## Jebakan 6. Satu kerjaan dipecah jadi banyak target ga? [penilai]

Satu barang dipecah jadi 5 target sama dengan minta 5 nilai dari 1 kerjaan. Yang dicek
barang yang disentuh, bukan cara nulis kalimatnya.

Agent ga bisa mastiin ini, karena agent cuma lihat satu ajuan dan ga tahu ajuan lain yang
udah masuk. Jadi ini nyerah ke penilai. Yang agent lakuin cuma satu, ditanya sekali sebelum
kirim:

> "Kuartal ini kamu ngajuin berapa target? Kalau lebih dari satu, semuanya dari barang yang
> beda, atau dari satu barang yang sama?"

Kalau jawabannya dari satu barang yang sama, ingetin di depan: penilai bakal gabungin jadi
satu, jadi mending digabung sendiri sekarang biar ga bolak-balik.

---

## Ringkasan buat agent

| Jebakan | Siapa yang mutusin | Kapan dicek |
|---|---|---|
| 1. Bisa merah ga | mesin | sesudah isian 4, 5, dan arah |
| 2. Udah kecapai duluan | mesin | sesudah isian 4, 5, dan arah |
| 3. Bukti tulis sendiri | tanya | sesudah isian 2 |
| 4. Jejaknya udah ada belum | tanya | sesudah isian 2, sebelum isian 4 |
| 5. Bisa bagus lewat jalan salah | mesin buat ada-nya, tanya buat mutunya | sesudah isian 3 dan 8 |
| 6. Satu kerjaan dipecah banyak | penilai | ditanya sekali sebelum kirim |
