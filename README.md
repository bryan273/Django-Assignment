# Tugas 2 PBP
Link hasil deploy aplikasi : [link](https://tugas-django-bryan-1.herokuapp.com/katalog/)

## Request-Response Django Lifecycle
<img width="491" alt="image" src="https://user-images.githubusercontent.com/88226713/189522302-0e3f9028-ca2e-4a72-8cd2-399cc94abaa2.png">

* Ketika user / client melakukan _request_ untuk ke server melalui _link_ url atau _form_, django akan mencocokan url yang di-_request_ dengan url yang sudah didefinisikan pada file urls.py.
* Setiap url akan dipetakan ke fungsi tertentu yang berada pada file views.py yang akan memanggil fungsi _view_. 
* Fungsi view ini akan melakukan _query_ terhadap database dengan memanggil objek yang terdapat pada models.py sebagai penghubung. 
* Setelah itu view function akan mengembalikan _response_  dengan format HTML (berkas html).
* Lalu hasilnya akan dirender oleh template yang akan men-_display_ konten yang akan dilihat oleh user / client.
