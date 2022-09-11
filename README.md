# Tugas 2 PBP
Link hasil deploy aplikasi : [link](https://tugas-django-bryan-1.herokuapp.com/katalog/)

## Request-Response Django Lifecycle
<img width="491" alt="image" src="https://user-images.githubusercontent.com/88226713/189522302-0e3f9028-ca2e-4a72-8cd2-399cc94abaa2.png">

* Ketika user / client melakukan _request_ untuk ke server melalui _link_ url atau _form_, django akan mencocokan url yang di-_request_ dengan url yang sudah didefinisikan pada file urls.py.
* Setiap url akan dipetakan ke fungsi tertentu yang berada pada file views.py yang akan memanggil fungsi _view_. 
* Fungsi view ini akan melakukan _query_ terhadap database dengan memanggil objek yang terdapat pada models.py sebagai penghubung. 
* Setelah itu view function akan mengembalikan _response_  dengan format HTML (berkas html).
* Lalu hasilnya akan dirender oleh template yang akan men-_display_ konten yang akan dilihat oleh user / client.

# Virtual Environment in Django
Virtual environment merupakan sebuah wadah virtual yang digunakan untuk menampung _dependecies_ dan _library_ agar terisolasi dari _dependencies_ utama. 

Setiap proyek yang akan kita kerjakan, memerlukan _third-party packages_ Python yang unik. Bila kita terus mengunduh semua packages di _environment_ yang sama pada setiap projek, hal itu dapat merusak alat sistem atau proyek sebelumnya yang mempunyai _dependencies_ mereka masing-masing.

Oleh karena itu, setiap kita memulai suatu proyek baru, kita harus meng-_setup_ _virtual environment_ yang baru dengan _dependencies_ dan versinya tertentu untuk sebuah proyek. 
