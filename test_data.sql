INSERT INTO hotels (name, location, services, rooms_quantity, image_id) VALUES 
('Cosmos Collection Altay Resort', 'Республика Алтай, Майминский район, село Урлу-Аспак, Лесхозная улица, 20', '["Wi-Fi", "Бассейн", "Парковка", "Кондиционер в номере"]', 15, 1),
('Skala', 'Республика Алтай, Майминский район, поселок Барангол, Чуйская улица 40а', '["Wi-Fi", "Парковка"]', 23, 2),
('Ару-Кёль', 'Республика Алтай, Турочакский район, село Артыбаш, Телецкая улица, 44А', '["Парковка"]', 30, 3),
('Гостиница Сыктывкар', 'Республика Коми, Сыктывкар, Коммунистическая улица, 67', '["Wi-Fi", "Парковка", "Тренажёрный зал"]', 55, 4),
('Palace', 'Республика Коми, Сыктывкар, Первомайская улица, 62', '["Wi-Fi", "Парковка", "Кондиционер в номере"]', 22, 5),
('Bridge Resort', 'посёлок городского типа Сириус, Фигурная улица, 45', '["Wi-Fi", "Парковка", "Кондиционер в номере", "Тренажёрный зал"]', 45, 6);

INSERT INTO rooms (hotel_id, name, price, quantity, services, image_id) VALUES
(1, 'Улучшенный с террасой и видом на озеро', 24500, 5, '["Бесплатный Wi‑Fi", "Кондиционер (с климат-контролем)"]', 7),
(1, 'Делюкс Плюс', 22450, 10, '["Бесплатный Wi‑Fi", "Кондиционер"]', 8),
(2, 'Номер на 2-х человек', 4570, 15, '[]', 9),
(2, 'Номер на 3-х человек', 4350, 8, '[]', 10),
(3, 'Номер полулюкс семейный с 1 двуспальной кроватью', 7080, 20, '["Холодильник"]', 11),
(3, '2-комнатный номер люкс комфорт', 9815, 10, '[]', 12),
(4, 'Стандарт двухместный', 4300, 20, '["Бесплатный Wi‑Fi", "Холодильник"]', 13),
(4, 'Стандарт улучшенный ПЛЮС', 4700, 35, '["Бесплатный Wi‑Fi", "Холодильник", "Ванная комната", "Кондиционер"]', 14),
(5, 'Номер стандарт с 2 односпальными кроватями (с завтраком)', 5000, 15, '[]', 15),
(5, 'Номер полулюкс премиум (с завтраком)', 8000, 7, '[]', 16),
(6, 'Стандарт (типовой корпус)', 8125, 45, '[]', 17);

INSERT INTO users (email, hashed_password) VALUES 
('fedor@moloko.ru', 'tut_budet_hashed_password_1'),
('sharik@moloko.ru', 'tut_budet_hashed_password_2');

INSERT INTO bookings (room_id, user_id, date_from, date_to, price) VALUES
(1, 1, '2023-06-15', '2023-06-30', 24500),
(7, 2, '2023-06-25', '2023-07-10', 4300);