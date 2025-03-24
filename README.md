## Anhor Korxonasining ishchilar davomatini olib boruvchi loyiha

1. **Product** - (Maxsulotlar)
    * ``name`` - Maxsulot nomi
    * ``price_per_unit`` - 1 dona chiqaril maxsulot uchun tolanadigan summa.
2. **Employee** - (Ishchilar)
    * ``status`` - Ishchi statusi yani (``yangi``, ``doimiy`` ``...``)
    * ``full_name`` - Ishchining ``Ism familiasi``
3. **Daily Production** - (Kunlik ishlab chiqarish)
    * ``date`` - Sana yani qaysi kunga tegishli ekanligi
    * ``product`` - Mahsulot
    * ``quantity`` - Mahsulot chiqarilgan soni
    * ``total_amount`` - To'lanadigan summa ``avtomatik hisoblanadi``
4. **Attendance** - (Ishchilar davomati)
    * ``employee`` - Ishchi
    * ``check_in`` - Kelish vaqti
    * ``check_out`` - Ketish vaqti
    * ``worked_hours`` - kun davomida ishlagan vaqti (``Avtomatik hisoblanadi``)
5. **SalaryRecord** - (Ishchilar olgan ish haqqilari ro'yxati)
    * ``employee`` - Ishchi
    * ``start_date`` - ish haqini boshlanish sanasi
    * ``end_date`` - ish haqini tugash sanasi
    * ``total_amount`` - Oladigan ish haqqisi (``Avtomatik hisoblanadi``)

* ``requirements.txt`` Loyiha uchun kerakli **package**lar.

      pip install -r requirements.txt

## Api ``Qo'llanma``

<br>

| Method   | Description                                                                                    |
|----------|------------------------------------------------------------------------------------------------|
| `GET`    | Bitta element yoki elementlar to'plamini olish uchun ishlatiladi.                              |
| `POST`   | Yangi narsalarni yaratishda foydalaniladi, masalan: yangi ishchi, maxsulot ...                 |
| `PATCH`  | Elementdagi bir yoki bir nechta maydonlarni yangilash uchun ishlatiladi.                       |
| `PUT`    | Butun elementni (barcha maydonlarni) yangi ma'lumotlar bilan almashtirish uchun foydalaniladi. |
| `DELETE` | Elementni o'chirish uchun ishlatiladi.                                                         |

<br>

| Method   | URL                                      | Description                           |
|----------|------------------------------------------|---------------------------------------|
| `GET`    | `/api/employee`                          | Barcha ishchilarni olish.             |
| `POST`   | `/api/employee`                          | Yangi ishchi yaratish.                |
| `GET`    | `/api/employee/28`                       | №28 ishchini olish.                   |
| `PATCH`  | `/api/employee/28`                       | Ishchini ma'lumotlarni yangilash #28. |
| `DELETE` | `/api/employee/28` or `/api/employee/50` | Ishchini o'chirish                    |

<br>
<br>

## HTTP javob holati kodlari

Bu API ishlatayotganda server tomonidan qaytariladigan muhim status xabarlaridir. Har bir kod ma'lum bir holatni
bildiradi va tushunish oson bo'lishi uchun turlarga bo'lingan.

### Asosiy HTTP Status Kodlari:

| Code  | Title                   | Description                                                                                                                                                     |
|-------|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `200` | `OK`                    | So'rov muvaffaqiyatli bajarildi (masalan. foydalanganda `GET`, `PATCH`, `PUT` yoki `DELETE`).                                                                   |
| `201` | `Created`               | Yangi resurs yaratildi (masalan, POST so'rovi orqali).                                                                                                          |
| `400` | `Bad request`           | So'rov noto'g'ri yuborilgan (masalan, majburiy maydonlar yo'q)                                                                                                  |
| `401` | `Unauthorized`          | Foydalanuvchi avtorizatsiyadan o'tmagan.                                                                                                                        |
| `403` | `Forbidden`             | Foydalanuvchiga ruxsat yo'q (avtorizatsiyadan o'tgan bo'lsa ham).                                                                                               |
| `404` | `Not found`             | So'ralgan resurs topilmadi.                                                                                                                                     |
| `500` | `Internal server error` | Serverda kutilmagan xato yuz berdi.                                                                                                                             |
| `502` | `Bad Gateway`           | Gateway yoki proxy server noto'g'ri javob qaytardi.                                                                                                             |
| `503` | `Service Unavailable`   | Server hozircha ishlamayapti (vaqtincha).                                                                                                                       |