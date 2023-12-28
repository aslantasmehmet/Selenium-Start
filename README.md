
Pytest Decorators

-Test yürütme davranışını kontrol eden dekoratörler: Bu dekoratörler, testlerin ne zaman ve nasıl yürütüleceğini kontrol eder.
Örneğin, @pytest.mark.skip dekoratörü testi atlar, @pytest.mark.parametrize dekoratörü test fonksiyonunu farklı girdilerle çalıştırır ve @pytest.mark.xfail dekoratörü testin başarısız olmasını bekler.

-Test sonuçlarını kontrol eden dekoratörler: Bu dekoratörler, testlerin başarısız olması için gereken koşulları kontrol eder.
Örneğin, @pytest.mark.raises dekoratörü belirli bir hata türünün ortaya çıkmasını bekler.

-Test verilerini kontrol eden dekoratörler: Bu dekoratörler, testlere sağlanan verileri kontrol eder.
Örneğin, @pytest.mark.config dekoratörü testlere sağlanan konfigürasyon verilerini kontrol eder.

-Testleri raporlayan dekoratörler: Bu dekoratörler, testlerin sonuçlarını raporlar.
Örneğin, @pytest.mark.describe dekoratörü testleri gruplandırır ve @pytest.mark.tag dekoratörü testlere etiketler ekler.

Dekoratörleri kullanmanın bazı örnekleri şunlardır:
@pytest.mark.skip
# Bu dekoratör testi atlar. Örneğin, aşağıdaki kod belirli bir ortamda çalışan bir testi atlar:
@pytest.mark.skipif(os.environ.get("ENV") != "prod", reason="Bu test sadece üretim ortamında çalışır")
def test_production(self):

@pytest.mark.parametrize
# Bu dekoratör, test fonksiyonunu farklı girdilerle çalıştırır. Örneğin, aşağıdaki kod username ve password değişkenlerine farklı değerler atayarak test_login() testini çalıştırır:
@pytest.mark.parametrize("username, password", [("kullanici1", "parola1"), ("kullanici2", "parola2")])
def test_login(self, username, password):

@pytest.mark.xfail
# Bu dekoratör, testin başarısız olmasını bekler. Örneğin, aşağıdaki kod henüz tamamlanmamış bir testi işaretler:
@pytest.mark.xfail
def test_not_implemented(self):

Dekoratörleri kullanmanın bazı avantajları şunlardır:

- Testleri daha okunabilir ve yönetilebilir hale getirirler.
- Testleri tekrar kullanılabilir hale getirirler.
- Testlerin yürütülmesini daha esnek hale getirirler.

Dekoratörleri kullanmanın diğer birçok yolu vardır. Daha fazla bilgi için PyTest belgelerine başvurabilirsiniz.
