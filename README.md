# VBO-DataOps-Airflow3
Data Engineering project for pipeline automation.
# DataOps & Airflow Pipeline Project

Bu proje, uçtan uca veri mühendisliği, otomasyon (CI/CD) ve orkestrasyon süreçlerini kurgulamak amacıyla geliştirilmiştir.

## Proje Mimarisi ve Çözümler

**Data Cleaning (Veri Temizliği): `dirty_store_transactions.csv` dosyası Pandas kullanılarak temizlenmiş, `drop_duplicates()` ve `fillna()` / `dropna()` metodları ile veri kalitesi artırılmıştır. (`clean_data.py`)
**Code Execution Environment (Çalışma Ortamı): Veri temizleme scripti Airflow üzerinde değil, izolasyonu sağlamak amacıyla `SSHOperator` kullanılarak doğrudan `spark_client` konteyneri üzerinde çalıştırılmıştır. (`dag_clean.py`)
**Data Sink (Veri Hedefi):Temizlenen veri, SQLAlchemy kullanılarak PostgreSQL üzerindeki `traindb` veritabanına, `clean_data_transactions` tablosuna "Full Load" (tam yükleme - `if_exists='replace'`) mantığıyla aktarılmıştır.
**CI/CD & Automation (Otomasyon):
  * Geliştirme süreçleri izole bir `dev` branch'inde yapılmış ve GitHub PR (Pull Request) ile `main` branch'ine merge edilmiştir.
  * Kodlar sunucuya manuel (sürükle-bırak vb.) kopyalanmamıştır. Airflow `docker-compose.yaml` içerisindeki `Git-Sync` konfigürasyonu, kişisel GitHub repository'me entegre edilmiş olup, `main` branch'teki güncellemeleri otomatik olarak deploy etmektedir.

## Karşılaşılan Zorluklar ve Donanımsal Limitasyonlar

Projedeki kodlama, CI/CD entegrasyonu ve DataOps süreçleri eksiksiz tasarlanmış olsa da, canlı test aşamasında donanımsal bir kısıtlamaya takılınmıştır:

* Kullanılan cihazın farklı mimariye sahip olması ve sağlanan Docker imajlarının (özellikle Airflow ve Spark) farklı mimariye göre derlenmiş olması bir uyumsuzluk yaratmıştır.
* Platformlarda zorlama (`platform: linux/amd64`) yapılmış olsa da, emülasyonun yarattığı performans kaybı ve aşırı CPU/RAM tüketimi nedeniyle `airflow-init` ve `scheduler` konteynerleri zaman aşımına uğrayıp "Waiting" durumunda kalmıştır.
* Bu teknik darboğaz nedeniyle sistem UI üzerinden veya terminalden başarılı bir şekilde trigger edilememiş ve veritabanına veri akışı canlı olarak görüntülenememiştir.
* Süreç canlıya alınamamış olsa da, Pipeline'ın ihtiyaç duyduğu tüm Python kodları, Git-Sync otomasyonu ve DAG mimarisi yapısal olarak doğru kurgulanıp teslim edilmiştir.

**Not: Mimarinin kurulduğuna dair GitHub PR süreçleri, RustFS Data Lake bağlantısı ve kod yapıları repository içerisindeki ekran görüntülerinde yer almaktadır.
