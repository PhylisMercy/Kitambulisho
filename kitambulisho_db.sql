




INSERT INTO `Counties` (`name`, `id`, `created_at`, `updated_at`) VALUES
('Nairobi', '233fcf11-16de-4f98-b2f5-1bbab0374867', '2023-06-03 16:02:19', '2023-06-03 16:02:19'),
('Mombasa', 'a4055bf7-bc5a-4267-8e47-f28164ef5dbe', '2023-06-03 16:02:19', '2023-06-03 16:02:19'),
('Uasin Gishu', 'a67f6549-2490-4f69-8192-94d0497dccc6', '2023-06-03 16:02:19', '2023-06-03 16:02:19');

INSERT INTO `cities` (`name`, `county_id`, `id`, `created_at`, `updated_at`) VALUES
('Huruma', 'a67f6549-2490-4f69-8192-94d0497dccc6', '50b817c0-5c85-4047-add4-e9426c3e1b59', '2023-06-03 16:02:34', '2023-06-03 16:02:34'),
('Langas', 'a67f6549-2490-4f69-8192-94d0497dccc6', 'a85a104f-1c8f-44ed-92d0-7ae779fe7011', '2023-06-03 16:02:35', '2023-06-03 16:02:35'),
('Eldoret', 'a67f6549-2490-4f69-8192-94d0497dccc6', 'b46115e9-d16c-41a4-b5e3-4e59c55cf8ee', '2023-06-03 16:02:34', '2023-06-03 16:02:34');

INSERT INTO `users` (`email`, `password`, `first_name`, `last_name`, `id`, `created_at`, `updated_at`) VALUES
('staff@Kenyaree.co.ke', 'd9d48fcce0c571984f698848d6d35fbf', 'John', 'Connor', '62de0569-ceb5-476a-b797-5757a0c526aa', '2023-06-03 16:02:40', '2023-06-03 16:02:40'),
('samaritan@Kenya.co.ke', 'a8c0d2a9d332574951a8e4a0af7d516f', 'Jane', 'Doe', '86e7edd9-9bc9-447b-a4f6-af17ded93978', '2023-06-03 16:02:41', '2023-06-03 16:02:41');



INSERT INTO `Kitambulisho_Collection_Stations` (`operate_registration_date`, `next_license_renew_date`, `city_id`, `staff_user_id`, `name`, `description`, `latitude`, `longitude`, `id`, `created_at`, `updated_at`) VALUES
(NULL, NULL, 'b46115e9-d16c-41a4-b5e3-4e59c55cf8ee', '62de0569-ceb5-476a-b797-5757a0c526aa', 'Kapsoya', NULL, NULL, NULL, '2ec62c4b-f8ea-4a52-b68d-9b06eb7fb927', '2023-06-03 16:06:29', '2023-06-03 16:06:29'),
(NULL, NULL, 'b46115e9-d16c-41a4-b5e3-4e59c55cf8ee', '86e7edd9-9bc9-447b-a4f6-af17ded93978', 'Kenyaree', NULL, NULL, NULL, 'e38b7289-4805-47f6-9d57-9f39ba657292', '2023-06-03 16:06:29', '2023-06-03 16:06:29');


INSERT INTO `reviews` (`user_id`, `station_id`, `description`, `id`, `created_at`, `updated_at`) VALUES
('86e7edd9-9bc9-447b-a4f6-af17ded93978', '2ec62c4b-f8ea-4a52-b68d-9b06eb7fb927', 'hello kitty', 'review_1', '2023-06-03 16:13:19', '2023-06-03 16:13:19');



INSERT INTO `vitambulisho` (`reported_lost_on`, `cleared_on`, `name`, `surname`, `ID_Number`, `ID_found_at_longitude`, `ID_found_at_latitude`, `Birth_District`, `Image_url`, `id`, `created_at`, `updated_at`) VALUES
('2023-06-03 16:07:57', '2023-06-03 16:07:57', 'john', 'Cena', '676767', '55', '55', 'LA', 'localhost/jsc.png', 'john_cena', '2023-06-03 16:07:57', '2023-06-03 16:07:57'),
('2023-06-03 16:07:57', '2023-06-03 16:07:57', 'titus', 'cheserem', '343434', '33.33', '55.55', 'Keiyo', 'localhost/titus.png', 'titus', '2023-06-03 16:07:57', '2023-06-03 16:07:57');



INSERT INTO `Kitambulisho_Collection_Register` (`collection_station_id`, `kitambulisho_id`, `id`) VALUES
('2ec62c4b-f8ea-4a52-b68d-9b06eb7fb927', 'john_cena', 'collector_signoff'),
('2ec62c4b-f8ea-4a52-b68d-9b06eb7fb927', 'titus', 'col_signoff');




INSERT INTO `ID_Collector_SignOff` (`ID_Collector_Register_id`, `status`, `payment_Transaction_code`, `Pay_amount`, `Tax_Charge`, `Tax_Filed`, `id`, `created_at`, `updated_at`) VALUES
('collector_signoff', 'closed', 'sdfsdf', '33.00', '9.00', 'completed', '1343-234234-234234-2342342-234234', '2023-06-03 16:11:44', '2023-06-03 16:11:44');


