-- phpMyAdmin SQL Dump
-- version 5.1.1deb5ubuntu1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jun 12, 2023 at 10:53 PM
-- Server version: 8.0.30-0ubuntu0.22.04.1
-- PHP Version: 8.1.2-1ubuntu2.11

SET FOREIGN_KEY_CHECKS=0;
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `kitambulisho_db`
--
--
-- Dumping data for table `Counties`
--

INSERT INTO `Counties` (`name`, `id`, `created_at`, `updated_at`) VALUES
('Nairobi', '233fcf11-16de-4f98-b2f5-1bbab0374867', '2023-06-03 16:02:19', '2023-06-03 16:02:19'),
('Mombasa', 'a4055bf7-bc5a-4267-8e47-f28164ef5dbe', '2023-06-03 16:02:19', '2023-06-03 16:02:19'),
('Uasin Gishu', 'a67f6549-2490-4f69-8192-94d0497dccc6', '2023-06-03 16:02:19', '2023-06-03 16:02:19');
--
-- Dumping data for table `cities`
--

INSERT INTO `cities` (`name`, `county_id`, `id`, `created_at`, `updated_at`) VALUES
('Huruma', 'a67f6549-2490-4f69-8192-94d0497dccc6', '50b817c0-5c85-4047-add4-e9426c3e1b59', '2023-06-03 16:02:34', '2023-06-03 16:02:34'),
('Langas', 'a67f6549-2490-4f69-8192-94d0497dccc6', 'a85a104f-1c8f-44ed-92d0-7ae779fe7011', '2023-06-03 16:02:35', '2023-06-03 16:02:35'),
('Eldoret', 'a67f6549-2490-4f69-8192-94d0497dccc6', 'b46115e9-d16c-41a4-b5e3-4e59c55cf8ee', '2023-06-03 16:02:34', '2023-06-03 16:02:34');

-- Dumping data for table `users`
--

INSERT INTO `users` (`email`, `password`, `first_name`, `last_name`, `id`, `created_at`, `updated_at`) VALUES
('staff@Kenyaree.co.ke', 'd9d48fcce0c571984f698848d6d35fbf', 'John', 'Connor', '62de0569-ceb5-476a-b797-5757a0c526aa', '2023-06-03 16:02:40', '2023-06-03 16:02:40'),
('samaritan@Kenya.co.ke', 'a8c0d2a9d332574951a8e4a0af7d516f', 'Jane', 'Doe', '86e7edd9-9bc9-447b-a4f6-af17ded93978', '2023-06-03 16:02:41', '2023-06-03 16:02:41');


--
-- Dumping data for table `Kitambulisho_Collection_Stations`
--

INSERT INTO `Kitambulisho_Collection_Stations` (`operate_registration_date`, `next_license_renew_date`, `city_id`, `staff_user_id`, `name`, `description`, `latitude`, `longitude`, `id`, `created_at`, `updated_at`) VALUES
(NULL, NULL, 'b46115e9-d16c-41a4-b5e3-4e59c55cf8ee', '62de0569-ceb5-476a-b797-5757a0c526aa', 'Kapsoya', NULL, NULL, NULL, '2ec62c4b-f8ea-4a52-b68d-9b06eb7fb927', '2023-06-03 16:06:29', '2023-06-03 16:06:29'),
(NULL, NULL, 'b46115e9-d16c-41a4-b5e3-4e59c55cf8ee', '86e7edd9-9bc9-447b-a4f6-af17ded93978', 'Kenyaree', NULL, NULL, NULL, 'e38b7289-4805-47f6-9d57-9f39ba657292', '2023-06-03 16:06:29', '2023-06-03 16:06:29');

--
-- Dumping data for table `reviews`
--

INSERT INTO `reviews` (`user_id`, `station_id`, `description`, `id`, `created_at`, `updated_at`) VALUES
('86e7edd9-9bc9-447b-a4f6-af17ded93978', '2ec62c4b-f8ea-4a52-b68d-9b06eb7fb927', 'hello kitty', 'review_1', '2023-06-03 16:13:19', '2023-06-03 16:13:19');

--

--
-- Dumping data for table `vitambulisho`
--

INSERT INTO `vitambulisho` (`cleared_on`, `name`, `surname`, `ID_Number`, `ID_found_at_longitude`, `ID_found_at_latitude`, `Birth_District`, `Birth_Division`, `Birth_Location`, `Birth_Sub_Location`, `Image_url`, `Signature_url`, `id`, `created_at`, `updated_at`) VALUES
(NULL, 'Libianca', NULL, '9842552', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '04b96d07-45f2-498e-ad28-4d96c953a999', '2023-06-12 22:52:08', '2023-06-12 22:52:08'),
(NULL, 'Bantam', NULL, '4458989', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '85fa7283-7623-4ba9-9bb5-8b374700c3b3', '2023-06-12 22:52:11', '2023-06-12 22:52:11');
SET FOREIGN_KEY_CHECKS=1;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;