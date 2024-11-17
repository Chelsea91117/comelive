-- MySQL dump 10.13  Distrib 8.0.39, for Win64 (x86_64)
--
-- Host: localhost    Database: configg
-- ------------------------------------------------------
-- Server version	8.0.39

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add user',6,'add_user'),(22,'Can change user',6,'change_user'),(23,'Can delete user',6,'delete_user'),(24,'Can view user',6,'view_user'),(25,'Can add ad',7,'add_ad'),(26,'Can change ad',7,'change_ad'),(27,'Can delete ad',7,'delete_ad'),(28,'Can view ad',7,'view_ad'),(29,'Can add booking',8,'add_booking'),(30,'Can change booking',8,'change_booking'),(31,'Can delete booking',8,'delete_booking'),(32,'Can view booking',8,'view_booking'),(33,'Can add review',9,'add_review'),(34,'Can change review',9,'change_review'),(35,'Can delete review',9,'delete_review'),(36,'Can view review',9,'view_review');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_myapp_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_myapp_user_id` FOREIGN KEY (`user_id`) REFERENCES `myapp_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'contenttypes','contenttype'),(7,'comelive','ad'),(8,'comelive','booking'),(9,'comelive','review'),(6,'comelive','user'),(5,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2024-09-17 22:25:43.268040'),(2,'contenttypes','0002_remove_content_type_name','2024-09-17 22:25:43.315827'),(3,'auth','0001_initial','2024-09-17 22:25:43.509157'),(4,'auth','0002_alter_permission_name_max_length','2024-09-17 22:25:43.557619'),(5,'auth','0003_alter_user_email_max_length','2024-09-17 22:25:43.563292'),(6,'auth','0004_alter_user_username_opts','2024-09-17 22:25:43.568278'),(7,'auth','0005_alter_user_last_login_null','2024-09-17 22:25:43.572995'),(8,'auth','0006_require_contenttypes_0002','2024-09-17 22:25:43.575007'),(9,'auth','0007_alter_validators_add_error_messages','2024-09-17 22:25:43.579994'),(10,'auth','0008_alter_user_username_max_length','2024-09-17 22:25:43.583982'),(11,'auth','0009_alter_user_last_name_max_length','2024-09-17 22:25:43.588546'),(12,'auth','0010_alter_group_name_max_length','2024-09-17 22:25:43.605362'),(13,'auth','0011_update_proxy_permissions','2024-09-17 22:25:43.612782'),(14,'auth','0012_alter_user_first_name_max_length','2024-09-17 22:25:43.617782'),(15,'comelive','0001_initial','2024-09-17 22:25:43.919532'),(16,'admin','0001_initial','2024-09-17 22:25:44.039031'),(17,'admin','0002_logentry_remove_auto_add','2024-09-17 22:25:44.045033'),(18,'admin','0003_logentry_add_action_flag_choices','2024-09-17 22:25:44.051374'),(19,'comelive','0002_booking','2024-09-17 22:25:44.204395'),(20,'comelive','0003_alter_booking_end_date_alter_booking_start_date','2024-09-17 22:25:44.242546'),(21,'comelive','0004_alter_booking_status','2024-09-17 22:25:44.249555'),(22,'comelive','0005_alter_booking_end_date_alter_booking_start_date','2024-09-17 22:25:44.303289'),(23,'comelive','0006_review','2024-09-17 22:25:44.419820'),(24,'sessions','0001_initial','2024-09-17 22:25:44.446802');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('kspvbrjmlm9qjuz1ujbkurpn8wzpzdfu','.eJxVjEEOwiAQRe_C2hCQAaYu3XuGZoZBqRpISrsy3l2bdKHb_977LzXSupRx7XkeJ1EnZdXhd2NKj1w3IHeqt6ZTq8s8sd4UvdOuL03y87y7fweFevnWLBzIgyNA9Jx8cIA-cbgaCRGQ7ECCYgGD44TWD2yAj8l6Gw0CRPX-AN3DNxQ:1sqynk:LlLQXmDQp0g8yOlAtbR7qrB1d63ECFQ3c7OOK1IJqrg','2024-10-02 17:49:16.284186');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `myapp_ad`
--

DROP TABLE IF EXISTS `myapp_ad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_ad` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `description` longtext,
  `state` varchar(50) NOT NULL,
  `city` varchar(50) NOT NULL,
  `address` varchar(150) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `rooms` smallint unsigned NOT NULL,
  `type` varchar(20) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `created_at` date NOT NULL,
  `updated_at` date NOT NULL,
  `owner_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_ad_owner_id_9bbe1d7c_fk_myapp_user_id` (`owner_id`),
  CONSTRAINT `myapp_ad_owner_id_9bbe1d7c_fk_myapp_user_id` FOREIGN KEY (`owner_id`) REFERENCES `myapp_user` (`id`),
  CONSTRAINT `myapp_ad_chk_1` CHECK ((`rooms` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `myapp_ad`
--

LOCK TABLES `myapp_ad` WRITE;
/*!40000 ALTER TABLE `myapp_ad` DISABLE KEYS */;
INSERT INTO `myapp_ad` VALUES (1,'Luxury Apartment in City Center','This luxurious apartment is located in the heart of the city, with stunning views of the skyline. It features 3 spacious bedrooms, 2 bathrooms, and a modern kitchen.','New York','New York City','123 Main St, New York, NY 10001',200.00,2,'Apartment',1,'2024-09-18','2024-09-18',2),(2,'Cozy House in the Suburbs','This charming house is located in a quiet suburban neighborhood, with a beautiful backyard and a short walk to the local park. It features 2 bedrooms, 1 bathroom, and a cozy living room.','California','San Francisco','456 Elm St, San Francisco, CA 94117',190.00,2,'House',1,'2024-09-18','2024-09-18',2),(3,'Studio Apartment in Downtown','This modern studio apartment is located in the heart of downtown, with easy access to public transportation and local amenities. It features a spacious living area, a kitchenette, and a bathroom.','Illinois','Chicago','789 Oak St, Chicago, IL 60607',100.00,1,'Apartment',1,'2024-09-18','2024-09-18',2),(4,'Beach House with Ocean Views','This stunning beach house is located right on the oceanfront, with breathtaking views of the coastline. It features 4 spacious bedrooms, 3 bathrooms, and a large deck perfect for outdoor entertaining.','Florida','Miami Beach','321 Ocean Dr, Miami Beach, FL 33139',300.00,4,'House',1,'2024-09-18','2024-09-18',4),(5,'Luxury Penthouse Apartment','This luxurious penthouse apartment is located on the top floor of a high-rise building, with stunning views of the city skyline. It features 2 spacious bedrooms, 2 bathrooms, and a modern kitchen with high-end appliances.','Texas','Houston','901 Main St, Houston, TX 77002',150.00,2,'Apartment',1,'2024-09-18','2024-09-18',4),(6,'Cozy Cabin in the Woods','This charming cabin is located in a secluded wooded area, perfect for a peaceful getaway. It features 1 bedroom, 1 bathroom, and a cozy living room with a fireplace.','Colorado','Aspen','1234 Mountain Rd, Aspen, CO 81611',100.00,1,'House',1,'2024-09-18','2024-09-18',4);
/*!40000 ALTER TABLE `myapp_ad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `myapp_booking`
--

DROP TABLE IF EXISTS `myapp_booking`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_booking` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `start_date` date NOT NULL,
  `end_date` date NOT NULL,
  `status` varchar(20) NOT NULL,
  `created_at` date NOT NULL,
  `updated_at` date NOT NULL,
  `ad_id` bigint NOT NULL,
  `landlord_id` bigint NOT NULL,
  `renter_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_booking_ad_id_25b1a629_fk_myapp_ad_id` (`ad_id`),
  KEY `myapp_booking_landlord_id_cf5b542d_fk_myapp_user_id` (`landlord_id`),
  KEY `myapp_booking_renter_id_fcb673cd_fk_myapp_user_id` (`renter_id`),
  CONSTRAINT `myapp_booking_ad_id_25b1a629_fk_myapp_ad_id` FOREIGN KEY (`ad_id`) REFERENCES `myapp_ad` (`id`),
  CONSTRAINT `myapp_booking_landlord_id_cf5b542d_fk_myapp_user_id` FOREIGN KEY (`landlord_id`) REFERENCES `myapp_user` (`id`),
  CONSTRAINT `myapp_booking_renter_id_fcb673cd_fk_myapp_user_id` FOREIGN KEY (`renter_id`) REFERENCES `myapp_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `myapp_booking`
--

LOCK TABLES `myapp_booking` WRITE;
/*!40000 ALTER TABLE `myapp_booking` DISABLE KEYS */;
INSERT INTO `myapp_booking` VALUES (1,'2024-09-02','2024-09-07','Confirmed','2024-09-18','2024-09-18',6,4,3),(2,'2024-09-21','2024-09-25','Rejected','2024-09-18','2024-09-18',4,4,3),(3,'2024-08-21','2024-08-27','Confirmed','2024-09-18','2024-09-18',2,2,3),(4,'2024-11-20','2024-11-29','Confirmed','2024-09-18','2024-09-18',1,2,3),(5,'2024-09-19','2024-09-25','Confirmed','2024-09-18','2024-09-18',6,4,5),(6,'2024-09-26','2024-09-28','Confirmed','2024-09-18','2024-09-18',4,4,3),(7,'2024-07-18','2024-07-25','Confirmed','2024-09-18','2024-09-18',2,2,5);
/*!40000 ALTER TABLE `myapp_booking` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `myapp_review`
--

DROP TABLE IF EXISTS `myapp_review`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_review` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `rating` smallint NOT NULL,
  `comment` longtext,
  `created_at` date NOT NULL,
  `ad_id` bigint NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `myapp_review_user_id_ad_id_522790de_uniq` (`user_id`,`ad_id`),
  KEY `myapp_review_ad_id_9336114b_fk_myapp_ad_id` (`ad_id`),
  CONSTRAINT `myapp_review_ad_id_9336114b_fk_myapp_ad_id` FOREIGN KEY (`ad_id`) REFERENCES `myapp_ad` (`id`),
  CONSTRAINT `myapp_review_user_id_9454541e_fk_myapp_user_id` FOREIGN KEY (`user_id`) REFERENCES `myapp_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `myapp_review`
--

LOCK TABLES `myapp_review` WRITE;
/*!40000 ALTER TABLE `myapp_review` DISABLE KEYS */;
INSERT INTO `myapp_review` VALUES (1,5,'Amazing Cabin','2024-09-18',6,3),(2,4,'Friendly landlord, but AC didnt work','2024-09-18',2,3),(3,3,'Problems with AC','2024-09-18',2,5);
/*!40000 ALTER TABLE `myapp_review` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `myapp_user`
--

DROP TABLE IF EXISTS `myapp_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_user` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `email` varchar(254) NOT NULL,
  `name` varchar(20) NOT NULL,
  `is_renter` tinyint(1) NOT NULL,
  `is_landlord` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `myapp_user`
--

LOCK TABLES `myapp_user` WRITE;
/*!40000 ALTER TABLE `myapp_user` DISABLE KEYS */;
INSERT INTO `myapp_user` VALUES (1,'pbkdf2_sha256$870000$JN7WFiN8rWnJiGzAHXmNUS$LF90Gzu1viKXM8IGHl6NSnUhHjwsSgdcxf8JnzSGztc=','latifova_9@mail.ru','',1,1,1,1,1,'2024-09-18 17:48:42.889451','2024-09-18 17:49:16.284186'),(2,'pbkdf2_sha256$870000$eARd3oHcfaE5DrLdd9efvo$SjureFRjOyRV9cxtySMFZlN4NBvxg4mg2bjFd21PJQA=','bob@mail.com','Bob',0,1,1,0,0,'2024-09-18 18:18:29.731048',NULL),(3,'pbkdf2_sha256$870000$wZux7n3wMq4usw6t0c6Ur7$Cca3WKYuy0Uj2KTqvfLEsrxQTSbUn/nBFuIHIcE4OIg=','marley@mail.com','Marley',1,0,1,0,0,'2024-09-18 18:20:44.373892',NULL),(4,'pbkdf2_sha256$870000$bd9oWGV0wjz7Ft9Ana6fIU$P4ILM6xwiIA1iMXDP+aeM50iY90OzA8le+AH4h8TRx8=','david@mail.com','David',0,1,1,0,0,'2024-09-18 18:21:47.848061',NULL),(5,'pbkdf2_sha256$870000$U2Ej6VMW84QY2TzCdqYSXt$WtBIPKVreigZheQHvep4R/CF23gCg1QtDpjbnbJf9D0=','masha@mail.com','Masha',1,0,1,0,0,'2024-09-18 18:22:59.375298',NULL),(6,'pbkdf2_sha256$870000$dQ8WH96Ej0kya6YLtfIe0f$HJI1EwyccdwnlGopze1ZVbb41NEMM4hPaA0BRGDEnhU=','john@mail.com','John',0,1,1,0,0,'2024-09-18 22:18:11.616678',NULL);
/*!40000 ALTER TABLE `myapp_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `myapp_user_groups`
--

DROP TABLE IF EXISTS `myapp_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `myapp_user_groups_user_id_group_id_1ef5feb7_uniq` (`user_id`,`group_id`),
  KEY `myapp_user_groups_group_id_488eb0fb_fk_auth_group_id` (`group_id`),
  CONSTRAINT `myapp_user_groups_group_id_488eb0fb_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `myapp_user_groups_user_id_925f87c5_fk_myapp_user_id` FOREIGN KEY (`user_id`) REFERENCES `myapp_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `myapp_user_groups`
--

LOCK TABLES `myapp_user_groups` WRITE;
/*!40000 ALTER TABLE `myapp_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `myapp_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `myapp_user_user_permissions`
--

DROP TABLE IF EXISTS `myapp_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `myapp_user_user_permissions_user_id_permission_id_13102f46_uniq` (`user_id`,`permission_id`),
  KEY `myapp_user_user_perm_permission_id_4657f93a_fk_auth_perm` (`permission_id`),
  CONSTRAINT `myapp_user_user_perm_permission_id_4657f93a_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `myapp_user_user_permissions_user_id_3f0ef5c3_fk_myapp_user_id` FOREIGN KEY (`user_id`) REFERENCES `myapp_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `myapp_user_user_permissions`
--

LOCK TABLES `myapp_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `myapp_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `myapp_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-09-19 17:23:53
