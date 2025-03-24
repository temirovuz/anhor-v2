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

| Code  | Title                   | Description                                                                                   |
|-------|-------------------------|-----------------------------------------------------------------------------------------------|
| `200` | `OK`                    | So'rov muvaffaqiyatli bajarildi (masalan. foydalanganda `GET`, `PATCH`, `PUT` yoki `DELETE`). |
| `201` | `Created`               | Yangi resurs yaratildi (masalan, POST so'rovi orqali).                                        |
| `400` | `Bad request`           | So'rov noto'g'ri yuborilgan (masalan, majburiy maydonlar yo'q)                                |
| `401` | `Unauthorized`          | Foydalanuvchi avtorizatsiyadan o'tmagan.                                                      |
| `403` | `Forbidden`             | Foydalanuvchiga ruxsat yo'q (avtorizatsiyadan o'tgan bo'lsa ham).                             |
| `404` | `Not found`             | So'ralgan resurs topilmadi.                                                                   |
| `500` | `Internal server error` | Serverda kutilmagan xato yuz berdi.                                                           |
| `502` | `Bad Gateway`           | Gateway yoki proxy server noto'g'ri javob qaytardi.                                           |
| `503` | `Service Unavailable`   | Server hozircha ishlamayapti (vaqtincha).                                                     |

<br>
<br>
<br>

### Employee example

* ``Post method``

   
       {
           "status": "yangi",
           "full_name": "Temirov Muhammad"
       }

* ``Get method``


       [
         {
           "id": 3,
           "status": "yangi",
           "full_name": "user - 1"
         },
         {
           "id": 4,
           "status": "yangi",
           "full_name": "user - 2"
         },
         {
           "id": 5,
           "status": "yangi",
           "full_name": "user - 3"
         },
         {
           "id": 6,
           "status": "yangi",
           "full_name": "user - 4"
         },
         {
           "id": 7,
           "status": "yangi",
           "full_name": "user - 5"
         }
       ]

### Daily Production example

* ``Post method``

   
       {
         "date": "2025-03-24",
         "product": 4,
         "quantity": 1000
       }

* ``Get method``

   
       [
         {
           "id": 1,
           "date": "2025-03-24",
           "product_name": "Anhor 1 litr",
           "quantity": 10,
           "total_amount": "1000.00"
         },
         {
           "id": 2,
           "date": "2025-03-24",
           "product_name": "shafaq 1 litr",
           "quantity": 100,
           "total_amount": "12000.00"
         },
         {
           "id": 3,
           "date": "2025-03-24",
           "product_name": "4.2 anhor",
           "quantity": 1000,
           "total_amount": "250000.00"
         }
       ]

### Attendance check In example

* ``Post method``
   
   
       {
          "employee_ids": [2, 3, 5, 6, 7],
          "check_in_time": "2025-03-23T09:00:00Z"
       }

* ``Get method``

   
       {
         "count": 13,
         "employees": [
           {
               "id": 3,
               "status": "yangi",
               "full_name": "user - 1"
           },
           {
               "id": 4,
               "status": "yangi",
               "full_name": "user - 2"
           },
           {
               "id": 5,
               "status": "yangi",
               "full_name": "user - 3"
           },
           {
               "id": 6,
               "status": "yangi",
               "full_name": "user - 4"
           },
           {
               "id": 7,
               "status": "yangi",
               "full_name": "user - 5"
           }
         ]
       }



### Attendance check out example

* ``Post method``


       {
          "employee_ids": [2, 3, 5, 6, 7],
          "check_out_time": "2025-03-24T09:00:00Z"
       }

* ``Get method``

   
       {
         "success": true,
         "message": "Successfully checked out 5 employees",
         "processed": [
           {
               "id": 2,
               "status": "yangi",
               "full_name": "Temirov Jahaongir"
           },
           {
               "id": 3,
               "status": "yangi",
               "full_name": "user - 1"
           },
           {
               "id": 5,
               "status": "yangi",
               "full_name": "user - 3"
           },
           {
               "id": 6,
               "status": "yangi",
               "full_name": "user - 4"
           },
           {
               "id": 7,
               "status": "yangi",
               "full_name": "user - 5"
           }
         ],
         "not_processed": [],
         "attendances": [
           {
               "id": 6,
               "employee": 2,
               "employee_name": "Temirov Jahaongir",
               "check_in": "2025-03-23T14:00:00+05:00",
               "check_out": "2025-03-24T14:00:00+05:00",
               "worked_hours": "24.00"
           },
           {
               "id": 7,
               "employee": 3,
               "employee_name": "user - 1",
               "check_in": "2025-03-23T14:00:00+05:00",
               "check_out": "2025-03-24T14:00:00+05:00",
               "worked_hours": "24.00"
           },
           {
               "id": 8,
               "employee": 5,
               "employee_name": "user - 3",
               "check_in": "2025-03-23T14:00:00+05:00",
               "check_out": "2025-03-24T14:00:00+05:00",
               "worked_hours": "24.00"
           },
           {
               "id": 9,
               "employee": 6,
               "employee_name": "user - 4",
               "check_in": "2025-03-23T14:00:00+05:00",
               "check_out": "2025-03-24T14:00:00+05:00",
               "worked_hours": "24.00"
           },
           {
               "id": 10,
               "employee": 7,
               "employee_name": "user - 5",
               "check_in": "2025-03-23T14:00:00+05:00",
               "check_out": "2025-03-24T14:00:00+05:00",
               "worked_hours": "24.00"
           }
        ]
   
    }