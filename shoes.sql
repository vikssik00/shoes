-- MySQL dump 10.13  Distrib 8.0.44, for Win64 (x86_64)
--
-- Host: localhost    Database: shoes
-- ------------------------------------------------------
-- Server version	8.0.44

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `category`
--

DROP TABLE IF EXISTS `category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `category` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` enum('Женская обувь','Мужская обувь') NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `category`
--

LOCK TABLES `category` WRITE;
/*!40000 ALTER TABLE `category` DISABLE KEYS */;
INSERT INTO `category` VALUES (1,'Женская обувь'),(2,'Мужская обувь');
/*!40000 ALTER TABLE `category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `goods`
--

DROP TABLE IF EXISTS `goods`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `goods` (
  `article` varchar(20) NOT NULL,
  `name` varchar(45) NOT NULL,
  `description` varchar(200) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `unit_of_measurement` varchar(3) NOT NULL,
  `quantity_in_stock` int NOT NULL,
  `discount` int NOT NULL,
  `photo` varchar(100) NOT NULL,
  `id_producer` int NOT NULL,
  `id_supplier` int NOT NULL,
  `id_category` int NOT NULL,
  PRIMARY KEY (`article`),
  KEY `id_producer_idx` (`id_producer`),
  KEY `id_supplier_idx` (`id_supplier`),
  KEY `id_category_idx` (`id_category`),
  CONSTRAINT `id_category` FOREIGN KEY (`id_category`) REFERENCES `category` (`id`),
  CONSTRAINT `id_producer` FOREIGN KEY (`id_producer`) REFERENCES `producer` (`id`),
  CONSTRAINT `id_supplier` FOREIGN KEY (`id_supplier`) REFERENCES `supplier` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `goods`
--

LOCK TABLES `goods` WRITE;
/*!40000 ALTER TABLE `goods` DISABLE KEYS */;
INSERT INTO `goods` VALUES ('B320R5','Туфли','Туфли Rieker женские демисезонные, размер 41, цвет коричневый',4300.00,'шт.',6,2,'9.jpg',4,1,1),('B431R5','Ботинки','Мужские кожаные ботинки/мужские ботинки',2700.00,'шт.',5,2,'picture.png',4,2,2),('C436G5','Ботинки','Ботинки женские, ARGO, размер 40',10200.00,'шт.',9,15,'picture.png',5,1,1),('D268G5','Туфли','Туфли Rieker женские демисезонные, размер 36, цвет коричневый',99.99,'шт.',12,3,'picture.png',1,2,2),('D329H3','Полуботинки','Полуботинки Alessio Nesca женские 3-30797-47, размер 37, цвет: бордовый',99.99,'шт.',4,4,'8.jpg',1,2,2),('D364R4','Туфли','Туфли Luiza Belly женские Kate-lazo черные из натуральной замши',12400.00,'шт.',5,16,'picture.png',1,1,1),('D572U8','Кроссовки','129615-4 Кроссовки мужские',4100.00,'шт.',6,3,'6.jpg',3,2,2),('E482R4','Полуботинки','Полуботинки kari женские MYZ20S-149, размер 41, цвет: черный',1800.00,'шт.',14,2,'picture.png',1,1,1),('F427R5','Ботинки','Ботинки на молнии с декоративной пряжкой FRAU',99.99,'шт.',12,15,'picture.png',1,1,1),('F572H7','Туфли','Туфли Marco Tozzi женские летние, размер 39, цвет черный',2700.00,'шт.',14,2,'7.jpg',2,1,1),('F635R4','Ботинки','Ботинки Marco Tozzi женские демисезонные, размер 39, цвет бежевый',99.99,'шт.',11,2,'2.jpg',1,1,1),('G432E4','Туфли','Туфли kari женские TR-YR-413017, размер 37, цвет: черный',2800.00,'шт.',15,3,'10.jpg',1,1,1),('G531F4','Ботинки','Ботинки женские зимние ROMER арт. 893167-01 Черный',6600.00,'шт.',9,12,'picture.png',1,1,1),('G783F5','Ботинки','Мужские ботинки Рос-Обувь кожаные с натуральным мехом',5900.00,'шт.',8,2,'4.jpg',3,1,2),('H535R5','Ботинки','Женские Ботинки демисезонные',2300.00,'шт.',7,2,'C:\\Users\\lulun\\PycharmProjects\\shoes\\images\\H535R5.png',1,1,1),('H782T5','Туфли','Туфли kari мужские классика MYZ21AW-450A, размер 43, цвет: черный',4499.00,'шт.',5,4,'3.jpg',1,1,2),('J384T6','Ботинки','B3430/14 Полуботинки мужские Rieker',3800.00,'шт.',16,2,'5.jpg',4,2,2),('J542F5','Тапочки','Тапочки мужские Арт.70701-55-67син р.41',500.00,'шт.',0,13,'picture.png',1,1,2),('K345R4','Полуботинки','407700/01-02 Полуботинки мужские CROSBY',2100.00,'шт.',3,2,'picture.png',6,2,2),('K358H6','Тапочки','Тапочки мужские син р.41',599.00,'шт.',2,20,'picture.png',1,1,1),('L754R4','Полуботинки','Полуботинки kari женские WB2020SS-26, размер 38, цвет: черный',1700.00,'шт.',7,2,'picture.png',1,1,1),('M542T5','Кроссовки','Кроссовки мужские TOFA',2800.00,'шт.',3,18,'picture.png',4,2,2),('N457T5','Полуботинки','Полуботинки Ботинки черные зимние, мех',4600.00,'шт.',13,3,'picture.png',6,1,1),('O754F4','Туфли','Туфли женские демисезонные Rieker артикул 55073-68/37',5400.00,'шт.',18,5,'picture.png',1,1,1),('P764G4','Туфли','Туфли женские, ARGO, размер 38',6800.00,'шт.',15,15,'picture.png',6,1,1),('S213E3','Полуботинки','407700/01-01 Полуботинки мужские CROSBY',2156.00,'шт.',6,3,'picture.png',6,2,2),('S326R5','Тапочки','Мужские кожаные тапочки \"Профиль С.Дали\"',9900.00,'шт.',15,17,'picture.png',6,2,2),('S634B5','Кеды','Кеды Caprice мужские демисезонные, размер 42, цвет черный',5500.00,'шт.',0,2,'picture.png',6,2,2),('T324F5','Сапоги','Сапоги замша Цвет: синий',4699.00,'шт.',5,2,'picture.png',6,1,1),('А112Т4','Ботинки','Женские Ботинки демисезонные kari',4990.00,'шт.',6,3,'1.jpg',1,1,1);
/*!40000 ALTER TABLE `goods` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order`
--

DROP TABLE IF EXISTS `order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order` (
  `number` int NOT NULL AUTO_INCREMENT,
  `date_z` date NOT NULL,
  `date_d` date NOT NULL,
  `code` varchar(10) NOT NULL,
  `status` enum('Завершен','Новый') NOT NULL,
  `id_point_of_issue` int NOT NULL,
  `id_user` int NOT NULL,
  PRIMARY KEY (`number`),
  KEY `id_point_of_issue_idx` (`id_point_of_issue`),
  KEY `id_user_idx` (`id_user`),
  CONSTRAINT `id_point_of_issue` FOREIGN KEY (`id_point_of_issue`) REFERENCES `point_of_issue` (`id`),
  CONSTRAINT `id_user` FOREIGN KEY (`id_user`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order`
--

LOCK TABLES `order` WRITE;
/*!40000 ALTER TABLE `order` DISABLE KEYS */;
INSERT INTO `order` VALUES (1,'2025-02-27','2025-04-20','901','Завершен',1,4),(2,'2022-09-28','2025-04-21','902','Завершен',11,1),(3,'2025-03-21','2025-04-22','903','Завершен',2,2),(4,'2025-02-20','2025-04-23','904','Завершен',11,3),(5,'2025-03-17','2025-04-24','905','Завершен',2,4),(6,'2025-03-01','2025-04-25','906','Завершен',15,1),(7,'2025-02-19','2025-04-26','907','Завершен',3,2),(8,'2025-03-31','2025-04-27','908','Новый',19,3),(9,'2025-04-02','2025-04-28','909','Новый',5,4),(11,'2026-02-22','2026-02-27','910','Новый',30,1);
/*!40000 ALTER TABLE `order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `point_of_issue`
--

DROP TABLE IF EXISTS `point_of_issue`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `point_of_issue` (
  `id` int NOT NULL AUTO_INCREMENT,
  `address` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `point_of_issue`
--

LOCK TABLES `point_of_issue` WRITE;
/*!40000 ALTER TABLE `point_of_issue` DISABLE KEYS */;
INSERT INTO `point_of_issue` VALUES (1,'420151, г. Лесной, ул. Вишневая, 32'),(2,'125061, г. Лесной, ул. Подгорная, 8'),(3,'630370, г. Лесной, ул. Шоссейная, 24'),(4,'400562, г. Лесной, ул. Зеленая, 32'),(5,'614510, г. Лесной, ул. Маяковского, 47'),(6,'410542, г. Лесной, ул. Светлая, 46'),(7,'620839, г. Лесной, ул. Цветочная, 8'),(8,'443890, г. Лесной, ул. Коммунистическая, 1'),(9,'603379, г. Лесной, ул. Спортивная, 46'),(10,'603721, г. Лесной, ул. Гоголя, 41'),(11,'410172, г. Лесной, ул. Северная, 13'),(12,'614611, г. Лесной, ул. Молодежная, 50'),(13,'454311, г.Лесной, ул. Новая, 19'),(14,'660007, г.Лесной, ул. Октябрьская, 19'),(15,'603036, г. Лесной, ул. Садовая, 4'),(16,'394060, г.Лесной, ул. Фрунзе, 43'),(17,'410661, г. Лесной, ул. Школьная, 50'),(18,'625590, г. Лесной, ул. Коммунистическая, 20'),(19,'625683, г. Лесной, ул. 8 Марта'),(20,'450983, г.Лесной, ул. Комсомольская, 26'),(21,'394782, г. Лесной, ул. Чехова, 3'),(22,'603002, г. Лесной, ул. Дзержинского, 28'),(23,'450558, г. Лесной, ул. Набережная, 30'),(24,'344288, г. Лесной, ул. Чехова, 1'),(25,'614164, г.Лесной,  ул. Степная, 30'),(26,'394242, г. Лесной, ул. Коммунистическая, 43'),(27,'660540, г. Лесной, ул. Солнечная, 25'),(28,'125837, г. Лесной, ул. Шоссейная, 40'),(29,'125703, г. Лесной, ул. Партизанская, 49'),(30,'625283, г. Лесной, ул. Победы, 46'),(31,'614753, г. Лесной, ул. Полевая, 35'),(32,'426030, г. Лесной, ул. Маяковского, 44'),(33,'450375, г. Лесной ул. Клубная, 44'),(34,'625560, г. Лесной, ул. Некрасова, 12'),(35,'630201, г. Лесной, ул. Комсомольская, 17'),(36,'190949, г. Лесной, ул. Мичурина, 26');
/*!40000 ALTER TABLE `point_of_issue` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `producer`
--

DROP TABLE IF EXISTS `producer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `producer` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `producer`
--

LOCK TABLES `producer` WRITE;
/*!40000 ALTER TABLE `producer` DISABLE KEYS */;
INSERT INTO `producer` VALUES (1,'Kari'),(2,'Marco Tozzi'),(3,'Рос'),(4,'Rieker'),(5,'Alessio Nesca'),(6,'CROSBY');
/*!40000 ALTER TABLE `producer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `result`
--

DROP TABLE IF EXISTS `result`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `result` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_article` varchar(20) NOT NULL,
  `count` int NOT NULL,
  `id_order` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_article_idx` (`id_article`),
  KEY `id_order_idx` (`id_order`),
  CONSTRAINT `id_article` FOREIGN KEY (`id_article`) REFERENCES `goods` (`article`),
  CONSTRAINT `id_order` FOREIGN KEY (`id_order`) REFERENCES `order` (`number`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `result`
--

LOCK TABLES `result` WRITE;
/*!40000 ALTER TABLE `result` DISABLE KEYS */;
INSERT INTO `result` VALUES (1,'А112Т4',2,1),(2,'F635R4',2,1),(3,'H782T5',1,2),(4,'G783F5',1,2),(5,'J384T6',10,3),(6,'D572U8',10,3),(7,'F572H7',5,4),(8,'D329H3',4,4),(9,'А112Т4',2,5),(10,'F635R4',2,5),(11,'H782T5',1,6),(12,'G783F5',1,6),(13,'J384T6',10,7),(14,'D572U8',10,7),(15,'F572H7',5,8),(16,'D329H3',4,8),(17,'B320R5',5,9),(18,'G432E4',1,9);
/*!40000 ALTER TABLE `result` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `role`
--

DROP TABLE IF EXISTS `role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `role` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name_UNIQUE` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `role`
--

LOCK TABLES `role` WRITE;
/*!40000 ALTER TABLE `role` DISABLE KEYS */;
INSERT INTO `role` VALUES (3,'Авторизированный клиент'),(1,'Администратор'),(2,'Менеджер');
/*!40000 ALTER TABLE `role` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `supplier`
--

DROP TABLE IF EXISTS `supplier`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `supplier` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `supplier`
--

LOCK TABLES `supplier` WRITE;
/*!40000 ALTER TABLE `supplier` DISABLE KEYS */;
INSERT INTO `supplier` VALUES (1,'Kari'),(2,'Обувь для вас');
/*!40000 ALTER TABLE `supplier` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `last_name` varchar(45) NOT NULL,
  `first_name` varchar(45) NOT NULL,
  `patronymic` varchar(45) NOT NULL,
  `login` varchar(50) NOT NULL,
  `password` varchar(45) NOT NULL,
  `id_role` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `login_UNIQUE` (`login`),
  KEY `id_role_idx` (`id_role`),
  CONSTRAINT `id_role` FOREIGN KEY (`id_role`) REFERENCES `role` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'Никифорова','Весения','Николаевна','94d5ous@gmail.com','uzWC67',1),(2,'Сазонов','Руслан','Германович','uth4iz@mail.com','2L6KZG',1),(3,'Одинцов','Серафим','Артёмович','yzls62@outlook.com','JlFRCZ',1),(4,'Степанов','Михаил','Артёмович','1diph5e@tutanota.com','8ntwUp',2),(5,'Ворсин','Петр','Евгеньевич','tjde7c@yahoo.com','YOyhfR',2),(6,'Старикова','Елена','Павловна','wpmrc3do@tutanota.com','RSbvHv',2),(7,'Михайлюк','Анна','Вячеславовна','5d4zbu@tutanota.com','rwVDh9',3),(8,'Ситдикова','Елена','Анатольевна','ptec8ym@yahoo.com','LdNyos',3),(9,'Ворсин','Петр','Евгеньевич','1qz4kw@mail.com','gynQMT',3),(10,'Старикова','Елена','Павловна','4np6se@mail.com','AtnDjr',3);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-02-22 23:23:43
