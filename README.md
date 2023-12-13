# Sohbet Uygulaması

Bu, basit ve kullanıcı dostu bir sohbet uygulamasıdır. Uygulama, bir sunucu ve bir veya daha fazla istemciden oluşur ve ngrok aracılığıyla yerel bir sunucu oluşturarak kullanıcıların birbirleriyle iletişim kurmasını sağlar.

## Kurulum

1. Projeyi bilgisayarınıza klonlayın:

    ```bash
    git clone https://github.com/HlmA06/pychat-ngrok.git
    cd pychat-ngrok
    ```

2. Gerekli Python kütüphanelerini yükleyin:

    ```bash
    pip install -r requirements.txt
    ```

## Başlarken

### Sunucu Başlatma

1. `pychatngrokserver.py` dosyasını çalıştırın.
2. Bir port numarası belirtin ve enter tuşuna basın.
3. Ngrok tarafından oluşturulan URL'yi kullanarak sohbet odasına erişin.

### İstemci Başlatma

1. `pychatclient.py` dosyasını çalıştırın.
2. Bir kullanıcı adı belirtin.
3. Sunucunun Ngrok URL'sini ve port numarasını girin.

## Temel Komutlar

- **Genel Mesaj Gönderme:** Herhangi bir metin girdisi yazarak genel sohbet odasına mesaj gönderebilirsiniz.
  
  ```plaintext
  Selam! Herkes nasıl?

- **Özel Mesaj Gönderme:** /pm "kullanıcı adı" "mesaj" girdisi yazarak özel mesaj gönderebilirsiniz.
 
  ```plaintext
  /pm hilmi selam
