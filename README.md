# Microservice-With-Flask
Membuat Microservice Sederhana Menggunakan Flask 

1. Server 1

Server 1 terhubung dengan API Public yang berisi database  universitas di United States untuk API Public database universitas di United States menggunakan API berikut :

http://universities.hipolabs.com/search?country=United+States

2. Server 2

Server 2 terhubung dengan API Pivate yang berisi database mahasiswa dari berbagai negara dengan database local sendiri 



3. Server GateWay 

Server Gateway disini berperan sebagai sebuah penghubung antara server 1 dan server 2 sehingga ketika mahasiswa ingin mengakses API tidak perlu mengakses server 1 dan server 2 secara satu persatu namun hanya perlu tersambung pada server gateway ini . Dibawah ini merupakan link dokumentasi API server gateway untuk terhubung dengan server 1 dan server 2 

Berikut dokumentasi API yang dibuat dengan aplikasi Postman : 

https://documenter.getpostman.com/view/11726998/Uz59NKH4

