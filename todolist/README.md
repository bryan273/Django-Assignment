# To Do List

Deployment Link : [link](https://tugas-django-bryan-1.herokuapp.com/todolist)
## Kegunaan {% csrf_token %}
Ketika end-user ingin merender halaman form, server akan menghasilkan token (csrf token). Token ini digunakan untuk memastikan setiap permintaan yang masuk sesuai dengan token yang dihasilkan. Bila permintaan yang masuk tidak berisi token, maka suatu request tidak akan dieksekusi. Jika token ini tidak ada, serangan dari sembarang orang (bisa melakukan delete account atau logout) dapat terjadi. Sehingga token ini dibutuhkan untuk mencegah serangan.

## Membuat elemen form secara manual
Kita dapat membuat form secara manual tanpa menggunakan generator {{ form.as_table }} dengan cara membuat elemen `<form>` yang memungkinkan user melakukan hal-hal seperti memasukkan teks, memilih opsi, dan sebagainya. Kemudian form tersebut diisi dengan elemen `<input>` yang dapat digunakan untuk menerima bermacam-macam input, seperti text, password, dan lainnya. Setelah itu, dibuat <input type="submit"> untuk men-submit form tersebut.
 
## Alur Data
Ketika user meng-klik submit form, data tersebut dapat diakses menggunakan HTTP request POST. Setelah itu kita dapat mengecek validitas data tersebut terlebih dahulu. Bila sudah, data tersebut akan disimpan ke dalam database. Setelah itu, kita dapat mengakses data tersebut menggunakan `Models.objects.filter(user=request.user)` (data yang diakses di-filter sesuai user yang sedang mengakses). Kemudian, kita masukkan ke context pada fungsi views yang selanjutnya akan dirender ke html dan akan di-loop untuk setiap data yang akan ditampilkan ke user.

## Implementasi 
1. Membuat app baru todolist dengan menjalankan `python manage.py startapp todolist`
2. Menambahkan 'todolist' pada settings.py folder project_django. Menambahkan `path('todolist/', include('todolist.urls'))`, di urls.py project django untuk routing ke urls di todolist. 
3. Membuat Models dan fieldsnya di models.py serta membuat user fieldnya berupa foreginkey ke User
4. Membuat fungsi views yaitu login, logout, register, show to do list, dan create to do list yang terhubung file html tertentu. Kemudian membuat restriksi agar user harus login dahulu jika ingin melihat atau meng-create to do list dengan menambahkan @login_required(login_url='/todolist/login/')
5. Membuat halaman html yang menampilkan data to do list dengan me-looping dan dua buah button untuk logout, tambah task baru
6. Membuat template untuk create form di create.html dengan input title dan description. Kemudian ada button submit todo dan menghandle todo yang baru ke to do list
7. Menambahkan path di urls.py todolist yang dirouting ke fungsi register, login, create-task, delete
8. Deploy ke heroku dan membuat 2 user dengan masing-masing 3 dummy list to do.
