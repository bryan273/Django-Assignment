# To Do List

Deployment Link : [link](https://tugas-django-bryan-1.herokuapp.com/todolist)

## Perbedaan Asynchronous dan Synchronous Programming

Synchronous programming merupakan program yang menjalankan fungsi satu per satu atau per line. Hal ini berarti bila kita ingin menjalankan beberapa fungsi atau code, kita harus menunggu parameter atau fungsi sebelumnya untuk selesai eksekusi.

Asynchronous programming berkebalikan dengan synchronous, yaitu instruksi dapat dilaksanakan secara bersamaan. Fungsi asynchronous di dalam web adalah  membuat web menjadi efisien tanpa menunggu refresh page untuk menunggu instruksi berikutnya. Dalam ajax, instruksi akan diproses secara asinkron di server-side.

## Event-Driven Programming
Event-Driven Programming merupakan suatu konsep di mana alur program bergantung pada aksi yang user lakukan. Semisal ketika mouse diclick, mouse digerakkan, dan lain-lain. Salah satu contohnya adalah ketika user mengklik "Add Task" akan memunculkan modal (pop up).

## Penerapan Asynchronous Programming AJAX
Ketika user melalukan event driven programming, Ajax akan menampung data yang akan dikirimkan ke server agar ada update data secara asinkron. Atau ketika kondisi AJAX get dan post, data yang didapatkan akan dikirimkan ke server dan akan di-update tanpa perlu di-reload

## Implementasi
1. Membuat fungsi show_ajax pada views.py yang akan mereturn JSONResponse berupa data yang telah di-POST.
2. Membuat route di urls.py ke todolist/json dan memanggil fungsi show_ajax
3. Membuat fungsi bernama loadData untuk merender cards todolist dengan method GET dari todolist/json. Render kemudian dimasukkan kedalam card
4. Membuat document.ready agar saat pertama kali website direfresh, akan loadData
5. Membuat modal sesuai referensi https://getbootstrap.com/docs/5.2/components/modal/
6. Memasukkan kode untuk membuat todo di dalam modal, dan ketika submit akan diarahkan untuk memanggil fungsi add_ajax
7. Setelah disubmit, akan dikirimkan response ajax POST ke todolist/add
8. Setelah itu diambil data yang di post dan ditambahkan ke card
9. Membuat fungsi delete dengan ajax supaya bersifat asinkronus dengan fungsi delDB
