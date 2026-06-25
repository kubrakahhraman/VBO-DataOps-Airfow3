# VBO-DataOps-Airfow3# VBO-DataOps-Airflow3
Data Engineering project for pipeline automation.
# DataOps & Airflow Pipeline Project

Bu proje, uçtan uca veri mühendisliği, otomasyon (CI/CD) ve orkestrasyon süreçlerini kurgulamak amacıyla geliştirilmiştir.

## Proje Mimarisi ve Çözümler

* **Data Cleaning (Veri Temizliği):** `dirty_store_transactions.csv` dosyası Pandas kullanılarak temizlenmiş, `drop_duplicates()` ve `fillna()` / `dropna()` metodları ile veri kalitesi artırılmıştır. (`clean_data.py`)
* **Code Execution Environment (Çalışma Ortamı):** Veri temizleme scripti Airflow üzerinde değil, izolasyonu sağlamak amacıyla `SSHOperator` kullanılarak doğrudan `spark_client` konteyneri üzerinde çalıştırılmıştır. (`dag_clean.py`)
* **Data Sink (Veri Hedefi):** Temizlenen veri, SQLAlchemy kullanılarak PostgreSQL üzerindeki `traindb` veritabanına, `clean_data_transactions` tablosuna "Full Load" (tam yükleme - `if_exists='replace'`) mantığıyla aktarılmıştır.
* **CI/CD & Automation (Otomasyon):**
  * Geliştirme süreçleri izole bir `dev` branch'inde yapılmış ve GitHub PR (Pull Request) ile `main` branch'ine merge edilmiştir.
  * Kodlar sunucuya manuel (sürükle-bırak vb.) kopyalanmamıştır. Airflow `docker-compose.yaml` içerisindeki `Git-Sync` konfigürasyonu, kişisel GitHub repository'me entegre edilmiş olup, `main` branch'teki güncellemeleri otomatik olarak deploy etmektedir.

**Not:** Mimarinin kurulduğuna dair GitHub PR süreçleri, RustFS Data Lake bağlantısı ve kod yapıları repository içerisindeki `Screenshots` klasöründe yer almaktadır.
