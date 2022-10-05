# My To Do List

Deployment Link : [link](https://tugas-django-bryan-1.herokuapp.com/todolist/)

## Perbedaan dari Inline, Internal, dan External CSS
Perbedaan dari inline, internal, external terdapat pada cara penggunaan CSS di file HTML-nya.
- Internal CSS dituliskan dengan tag khusus yaitu `<style>`. Style ini ditulis di file HTML pada bagian header. Setelah itu, kita dapat menuliskan CSS di dalam tag ini.
- Inline CSS merupakan CSS yang dituliskan pada suatu elemen yang ada pada HTML `<p style = "color:#009900; font-size:50px;font-style:italic; text-align:center;">GeeksForGeeks</p>`. Inline biasanya diperuntukkan untuk 1 elemen, sehingga lebih fleksibel. Internal digunakan untuk menambahkan banyak style pada 1 file HTML.
- Eksternal CSS biasanya dituliskan dengan tag `<link>` pada header. Untuk eskternal CSS, kita perlu mengimport filenya ke html. Eksternal baik digunakan jika ingin menambahkan style yang cukup banyak dan kompleks pada beberapa file HTML.

## Tag HTML5
- `<h1>` hingga `<h6>` , tag ini digunakan untuk header. h1 merepresentasikan header dengan ukuran terbesar. Sementara semakin tinggi angka `h` nya , semakin kecil ukurannya.
- `<p>`, tag ini digunakan untuk merepresentasikan paragraf.
- `<a>`, tag ini digunakan untuk menambahkan _hyperlink_ pada dokumen HTML.
- `<title>`, tag ini digunakan untuk mengatur judul halaman.
- `<div>`, tag ini berfungsi sebagai wadah atau container untuk elemen lain di dalamnya.

## CSS Selector

- ID Selector, digunakan untuk menambah style pada suatu ID sebagai _selector_-nya. Untuk menggunakan ID Selector, dipakai '#' diikuti nama ID.
- Class Selector, digunakan untuk menambah style pada suatu elemen dengan class sebagai _selector_-nya. Untuk menggunakan Class Selector, dipakai '.' diikuti nama class
- Element Selector, digunakan untuk menambah style dengan tag sebagai _selector_. Pengunannya diawali dengan nama_tag {...}.

## Implementasi
1. Digunakan library tailwind untuk _styling_ app todolist. Instalasi library tailwind, disesuaikan dengan cara pada [link](https://django-tailwind.readthedocs.io/en/latest/installation.html).
2. Styling login,create,register,todolist dengan metode mirip seperti inline css
3. Melakukan centering pada setiap page
4. Kustomisasi tombol berdasar referensi [link](https://tailwind-elements.com/docs/standard/components/login-form/)
5. Menambahkan navbar pada todolist
6. Menambahkan card pada todolist disertai fitur delete dan juga change status to do list dalam bentuk card
7. Menambahkan style responsive dengan breakpoints yang telah disediakan. Contoh : max-w-[80%] mx-auto
