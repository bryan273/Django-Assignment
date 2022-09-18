# My Watchlist
Deployment link : [link](https://tugas-django-bryan-1.herokuapp.com/mywatchlist)

# Perbedaan JSON, XML, dan HTML
* HTML atau HyperText Markup Language merupakan sebuah markup language yang berfokus pada penyajian data. Biasanya data yang direpresentasikan lebih ditujukan untuk Web. 
* JSON atau JavaScript Object Notation merupakan suatu format yang dibuat di atas JavaScript untuk merepresentasikan data dalam bentuk key dan value. JSON dapat digunakan untuk melakukan penyimpanan dan pertukaran data dengan cepat dikarenakan strukturnya yang dapat menyimpan data dalam bentuk array, tetapi lebih sulit untuk dibaca oleh manusia daripada XML. 
* XML atau Extensible Markup Language merupakan suatu markup language yang digunakan untuk menyederhanakan proses penyimpanan dan pengiriman data antarserver. XML cenderung menyimpan data dalam format teks sederhana seperti tree yang mirip dengan HTML. Format ini cenderung mudah dibaca oleh manusia dibandingkan format JSON, tetapi pertukaran data akan berlangsung lebih lama.

# Alasan diperlukan data delivery dalam pengimplementasian platform
Di dalam suatu platform terkadang ada pertukaran data antara clients dan juga server. Data delivery diperuntukkan untuk memudahkan suatu platform dalam melakukan pengiriman data. Data tersebut tentu memerlukan berbagai format dalam pertukarannya. Format yang kerapkali digunakan antara lain adalah HTML, JSON, dan XML. Dengan adanya format ini, data yang kompleks dapat diatur dalam format tertentu yang dapat dipahami oleh berbagai bahasa pemrograman dan API, sehingga dapat mempermudah pengiriman data.

# Langkah-langkah implementasi
1. Untuk membuat suatu aplikasi, digunakan perintah `python manage.py startapp mywatchlist` di directory repository yang ingin dibuat.
2. Menambahkan `path('mywatchlist/', include('mywatchlist.urls')),` di urls.py pada `urlpatterns` di django_project untuk menghubungkan ke urls.py pada mywatchlist. Kemudian pada urls.py di mywatchlist ditambahkan:
`urlpatterns = [
    ...,
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    ...
]`
Penambahan ini bertujuan untuk mapping path tertentu terhadap fungsi view yang ingin ditampilkan
3. Membuat model baru pada models.py di mywatchlist bernama MyWatchList dengan fields watched, title, rating, release_date, dan review. Setelah itu dilakukan migrasi agar model terbuat pada database.

# Postman
## JSON
<img width="637" alt="image" src="https://user-images.githubusercontent.com/88226713/190852912-c4559b00-4d4b-4d9c-91c6-4dec3216ab65.png">

## XML
<img width="635" alt="image" src="https://user-images.githubusercontent.com/88226713/190852923-4d4771f2-35fe-4f68-b753-8b15358704f3.png">

## HTML
<img width="641" alt="image" src="https://user-images.githubusercontent.com/88226713/190852937-252d65aa-ce67-40b0-9584-dbf0f84cbc16.png">
