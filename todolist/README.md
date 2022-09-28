# Kegunaan {% csrf_token %}
csrf_token. Django memiliki tag {% csrf_token %} yang diimplementasikan untuk menghindari serangan berbahaya. Ini menghasilkan token di sisi server saat merender halaman dan memastikan untuk memeriksa ulang token ini untuk setiap permintaan yang masuk kembali. Jika permintaan yang masuk tidak berisi token, permintaan tersebut tidak akan dieksekusi.

Ketika end-user ingin merender halaman form, server akan menghasilkan token (csrf token). Token ini digunakan untuk memastikan setiap permintaan yang masuk sesuai dengan token yang dihasilkan. Bila permintaan yang masuk tidak berisi token, maka suatu request tidak akan dieksekusi. Jika token ini tidak ada, serangan dari sembarang orang (bisa melakukan delete account atau logout) dapat terjadi. Sehingga token ini dibutuhkan untuk mencegah serangan.

# Alur Data
Ketika user meng-klik submit form, data tersebut dapat diakses menggunakan HTTP request POST. Setelah itu kita dapat mengecek validitas data tersebut terlebih dahulu. Bila sudah, data tersebut akan disimpan ke dalam database. Setelah itu, kita dapat mengakses data tersebut menggunakan `Models.objects.filter(user=request.user)` (data yang diakses di-filter sesuai user yang sedang mengakses). Kemudian, kita masukkan ke context pada fungsi views yang selanjutnya akan dirender ke html dan akan di-loop untuk setiap data yang akan ditampilkan ke user.
