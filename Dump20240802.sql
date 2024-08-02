-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: project1
-- ------------------------------------------------------
-- Server version	8.0.36

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
-- Table structure for table `countries`
--

DROP TABLE IF EXISTS `countries`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `countries` (
  `countryId` int NOT NULL AUTO_INCREMENT,
  `countryName` varchar(45) NOT NULL,
  PRIMARY KEY (`countryId`)
) ENGINE=InnoDB AUTO_INCREMENT=103 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `countries`
--

LOCK TABLES `countries` WRITE;
/*!40000 ALTER TABLE `countries` DISABLE KEYS */;
INSERT INTO `countries` VALUES (1,'Albania'),(2,'Andorra'),(3,'Argentina'),(4,'Armenia'),(5,'Australia'),(6,'Austria'),(7,'Azerbaijan'),(8,'Bahamas'),(9,'Barbados'),(10,'Belarus'),(11,'Belgium'),(12,'Belize'),(13,'Bolivia'),(14,'Bosnia and Herzegovina'),(15,'Brazil'),(16,'Bulgaria'),(17,'Canada'),(18,'Chile'),(19,'China'),(20,'Colombia'),(21,'Costa Rica'),(22,'Croatia'),(23,'Cyprus'),(24,'Czech Republic'),(25,'Denmark'),(26,'Dominican Republic'),(27,'Ecuador'),(28,'Estonia'),(29,'Eswatini'),(30,'Ethiopia'),(31,'Fiji'),(32,'Finland'),(33,'France'),(34,'Georgia'),(35,'Germany'),(36,'Greece'),(37,'Guatemala'),(38,'Honduras'),(39,'Hungary'),(40,'Iceland'),(41,'India'),(42,'Ireland'),(43,'Italy'),(44,'Japan'),(45,'Kazakhstan'),(46,'Kenya'),(47,'Kosovo'),(48,'Kyrgyzstan'),(49,'Latvia'),(50,'Lesotho'),(51,'Liechtenstein'),(52,'Lithuania'),(53,'Luxembourg'),(54,'Malawi'),(55,'Malta'),(56,'Mauritius'),(57,'Mexico'),(58,'Micronesia'),(59,'Moldova'),(60,'Monaco'),(61,'Montenegro'),(62,'Netherlands'),(63,'New Zealand'),(64,'North Macedonia'),(65,'Norway'),(66,'Panama'),(67,'Paraguay'),(68,'Peru'),(69,'Philippines'),(70,'Poland'),(71,'Portugal'),(72,'Romania'),(73,'Russia'),(74,'Rwanda'),(75,'San Marino'),(76,'Serbia'),(77,'Singapore'),(78,'Slovakia'),(79,'Slovenia'),(80,'South Africa'),(81,'South Korea'),(82,'Spain'),(83,'Sri Lanka'),(84,'Sweden'),(85,'Switzerland'),(86,'Tajikistan'),(87,'Tanzania'),(88,'Thailand'),(89,'Trinidad and Tobago'),(90,'Turkey'),(91,'Uganda'),(92,'Ukraine'),(93,'United Kingdom'),(94,'United States'),(95,'Uruguay'),(96,'Uzbekistan'),(97,'Vietnam'),(98,'Zambia'),(99,'Zimbabwe');
/*!40000 ALTER TABLE `countries` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `likes`
--

DROP TABLE IF EXISTS `likes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `likes` (
  `userId` int NOT NULL,
  `vacationId` int NOT NULL,
  KEY `userId_idx` (`userId`),
  KEY `vacationId_idx` (`vacationId`),
  CONSTRAINT `userId` FOREIGN KEY (`userId`) REFERENCES `users` (`userId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `vacationId` FOREIGN KEY (`vacationId`) REFERENCES `vacations` (`vacationId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `likes`
--

LOCK TABLES `likes` WRITE;
/*!40000 ALTER TABLE `likes` DISABLE KEYS */;
/*!40000 ALTER TABLE `likes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `userId` int NOT NULL AUTO_INCREMENT,
  `firstName` varchar(45) NOT NULL,
  `lastName` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  `password` varchar(250) NOT NULL,
  `roleId` int NOT NULL,
  PRIMARY KEY (`userId`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (24,'super','user','superuser@gmail.com','6196758ed26b20d95c09ad0241008c67ca2d05059547807c91da266a52272d399b60aea3bdccfda8a2433aa52a9cd2e8f7cc7c5c075586a144a4472088d6da4e',1),(32,'normal','user','normaluser@gmail.com','6196758ed26b20d95c09ad0241008c67ca2d05059547807c91da266a52272d399b60aea3bdccfda8a2433aa52a9cd2e8f7cc7c5c075586a144a4472088d6da4e',2);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vacations`
--

DROP TABLE IF EXISTS `vacations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vacations` (
  `vacationId` int NOT NULL AUTO_INCREMENT,
  `vacationInfo` longtext,
  `countryId` int NOT NULL,
  `vacationStart` date NOT NULL,
  `vacationEnd` date NOT NULL,
  `price` int NOT NULL,
  `picName` varchar(450) DEFAULT NULL,
  PRIMARY KEY (`vacationId`),
  KEY `countryId_idx` (`countryId`),
  CONSTRAINT `countryId` FOREIGN KEY (`countryId`) REFERENCES `countries` (`countryId`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=72 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vacations`
--

LOCK TABLES `vacations` WRITE;
/*!40000 ALTER TABLE `vacations` DISABLE KEYS */;
INSERT INTO `vacations` VALUES (51,'The Czech Republic, located in the heart of Europe, is a land of captivating history, vibrant culture, and stunning architecture. Its capital, Prague, is renowned for its beautiful Old Town, the majestic Prague Castle, and the iconic Charles Bridge, often called the \"City of a Hundred Spires\" for its numerous historic buildings.\r\n\r\nOutside Prague, the Czech Republic offers picturesque landscapes ranging from the rolling hills of Moravia to the rugged Bohemian Forest and the tranquil Elbe River. This diverse scenery provides excellent opportunities for outdoor activities and exploration.\r\n\r\nThe country\'s rich cultural heritage is celebrated through traditional music, dance, and festivals throughout the year. Czech cuisine is hearty and flavorful, featuring dishes like goulash, roast pork, and dumplings, often enjoyed with world-famous Czech beer.\r\n\r\nWhether you\'re exploring historic cities, enjoying scenic countryside, or immersing yourself in local culture, the Czech Republic offers an unforgettable experience for every traveler. Discover the charm and beauty of this enchanting country.',24,'2025-03-11','2025-03-14',278,'8c740a68-5777-4660-b825-4e352465ab63.png'),(52,'Spain, located on the Iberian Peninsula, is a country rich in history, culture, and natural beauty. Known for its vibrant cities, picturesque landscapes, and world-famous cuisine, Spain offers a diverse array of experiences for travelers.\r\n\r\nMadrid, the capital city, is a bustling metropolis renowned for its art museums, including the Prado and Reina Sofía, as well as its lively nightlife and historic architecture. Barcelona, with its stunning beaches and the architectural masterpieces of Antoni Gaudí, such as the Sagrada Familia and Park Güell, is another must-visit destination.\r\n\r\nBeyond its cities, Spain boasts beautiful countryside and coastal regions. The rolling hills of Andalusia are dotted with charming white villages, while the rugged coastlines of the Costa Brava and the Balearic Islands offer stunning seaside views and crystal-clear waters.\r\n\r\nSpain\'s cultural heritage is celebrated through its festivals, music, and dance, including the passionate rhythms of flamenco. The country\'s cuisine is equally renowned, with dishes like paella, tapas, and churros offering a taste of its diverse culinary traditions.\r\n\r\nWhether you\'re exploring historic landmarks, relaxing on a beach, or savoring delicious food, Spain is a destination that promises unforgettable experiences. Discover the warmth and charm of this captivating country.',82,'2025-04-17','2025-04-21',305,'b933ca17-377c-44f7-a683-c5ba0f72bb72.png'),(53,'China, located in East Asia, is a vast country known for its rich cultural heritage, diverse landscapes, and rapid modernization. As the world\'s most populous country, it offers a mix of ancient traditions and modern innovations. Iconic landmarks such as the Great Wall of China, the Forbidden City in Beijing, and the Terracotta Warriors in Xi\'an reflect its long history. China\'s diverse geography ranges from the mountainous regions of Tibet to the bustling metropolises of Shanghai and Beijing, as well as picturesque landscapes like the karst mountains in Guilin and the Yangtze River. Chinese cuisine is incredibly varied, with regional specialties like Peking duck, Sichuan spicy dishes, and Cantonese dim sum. The country experiences a wide range of climates, from the cold winters in the north to the tropical conditions in the south. The best times to visit are in the spring and fall, when the weather is generally mild and pleasant. China\'s rich history, vibrant culture, and dynamic cities make it a fascinating destination for travelers.',19,'2024-09-24','2024-10-08',1500,'9010db80-f946-4c84-83ae-cfe7b907ad52.png'),(54,'France, located in Western Europe, is renowned for its rich history, art, cuisine, and diverse landscapes. The country is a cultural hub, home to iconic landmarks such as the Eiffel Tower in Paris, the Château de Versailles, and the historic beaches of Normandy. Paris, the capital, is celebrated for its world-class museums like the Louvre, charming neighborhoods, and vibrant café culture. Beyond Paris, France boasts beautiful regions such as Provence, known for its lavender fields and vineyards; the French Riviera, famous for its glamorous beaches and Mediterranean climate; and the Loire Valley, dotted with stunning châteaux. French cuisine is globally acclaimed, featuring delicacies like croissants, cheeses, wines, and gourmet dishes. The country experiences a temperate climate, with regional variations that offer something for every traveler, from skiing in the Alps to sunbathing on the Côte d\'Azur. The best times to visit are spring and fall, when the weather is pleasant, and the tourist crowds are smaller, providing an ideal setting for exploring the cultural and natural treasures of France.',33,'2024-11-14','2024-11-21',700,'35421ba9-229f-49ee-a884-8e7050ea96d2.png'),(55,'he United States, spanning a vast expanse of North America, is known for its cultural diversity, varied landscapes, and significant global influence. The country offers a wide range of attractions, from bustling cities like New York, Los Angeles, and Chicago, to natural wonders such as the Grand Canyon, Yellowstone National Park, and the Great Smoky Mountains. The U.S. is a melting pot of cultures, reflected in its vibrant arts scene, diverse cuisine, and numerous festivals. Key historical sites include the Statue of Liberty, the White House, and Mount Rushmore. The U.S. experiences a variety of climates, from the temperate regions in the northeast to the tropical climate in Florida and Hawaii, and the arid deserts in the southwest. This diversity means that there are unique experiences available year-round, from skiing in the Rocky Mountains to enjoying the beaches of California and Florida. The country\'s infrastructure and wide range of accommodations make it accessible for travelers of all types. The best time to visit varies by region, but generally, spring and fall are popular for their mild weather and scenic beauty.',94,'2025-05-01','2025-05-29',1020,'c6abdf68-b9e3-4052-9008-41a814e0c7cd.png'),(56,'India, located in South Asia, is a country rich in history, culture, and diversity. Known for its vibrant traditions, ancient architecture, and varied landscapes, India offers a unique blend of the old and the new. The country is home to iconic landmarks such as the Taj Mahal, the temples of Khajuraho, and the forts and palaces of Rajasthan. India\'s geography includes the Himalayan mountain range in the north, vast plains, deserts in the west, and tropical beaches in the south. Each region boasts distinct cultural and culinary traditions, making India a diverse and fascinating destination. Indian cuisine is renowned globally, featuring a wide array of flavors and dishes, from spicy curries to aromatic biryanis. The country\'s festivals, such as Diwali, Holi, and Eid, showcase its rich cultural heritage and are celebrated with great enthusiasm. India\'s climate varies from tropical in the south to temperate in the north, with the monsoon season bringing significant rainfall from June to September. The country\'s bustling cities, serene rural landscapes, and historical sites make it a captivating destination for travelers.',41,'2025-02-01','2025-02-14',988,'6bf0f6a6-dee2-4343-aa09-81376f9fe983.png'),(57,'Italy, located in Southern Europe, is renowned for its rich history, art, culture, and cuisine. The country is a treasure trove of historical landmarks, including the Colosseum in Rome, the canals of Venice, the Renaissance art in Florence, and the ruins of Pompeii. Italy\'s diverse landscapes range from the rolling hills of Tuscany and the picturesque Amalfi Coast to the mountainous regions of the Alps and the Dolomites. Italian cuisine is celebrated worldwide, known for its pasta, pizza, fine wines, and regional specialties like gelato and espresso. The country\'s cultural heritage is showcased in its festivals, fashion, and art, with iconic contributions to painting, sculpture, and architecture. Italy\'s Mediterranean climate varies by region, with hot summers in the south, cooler winters in the north, and mild weather along the coasts. This climate makes Italy a year-round destination, offering a variety of experiences from skiing in the winter to beach holidays in the summer. The country\'s blend of historical, cultural, and natural attractions makes it a favorite destination for travelers.',43,'2024-09-06','2024-09-09',399,'f4ddd5d2-cb40-4cf7-bd05-edef6aada2c2.png'),(58,'Germany is a country located in Central Europe, known for its rich history, cultural heritage, and economic strength. It has a diverse landscape that includes forests, rivers, mountain ranges like the Alps, and bustling cities. Germany is famous for its contributions to art, science, philosophy, and music, with notable figures such as Beethoven, Goethe, and Einstein.\r\n\r\nThe country is a federal parliamentary republic with 16 states, each with its own constitution. Berlin is the capital and largest city, known for its vibrant cultural scene, historical landmarks, and modern architecture. Germany\'s economy is the largest in Europe and one of the strongest in the world, with a strong focus on engineering, automotive industries, and technology.\r\n\r\nGermany is also known for its traditions and festivals, such as Oktoberfest, and its culinary specialties, including sausages, pretzels, and beer. The country is a founding member of the European Union and plays a significant role in global affairs.\r\n\r\n\r\n\r\n\r\n\r\n\r\n',35,'2024-10-31','2024-11-09',681,'1b41b985-d2d9-43bb-bfda-e300b6fcd0ab.png'),(59,'Japan is an island nation in East Asia, known for its rich culture, advanced technology, and beautiful natural landscapes. It consists of four main islands: Honshu, Hokkaido, Kyushu, and Shikoku, along with many smaller islands. The capital city, Tokyo, is one of the world\'s most populous and vibrant cities, known for its modern architecture, shopping, dining, and entertainment.\r\n\r\nJapan has a unique blend of traditional and modern influences. It is famous for its traditional arts like tea ceremonies, calligraphy, and flower arranging, as well as its historical sites, including ancient temples, shrines, and castles. The country also has a rich culinary heritage, with dishes like sushi, ramen, tempura, and sashimi being globally popular.\r\n\r\nThe Japanese landscape is diverse, ranging from mountainous regions and hot springs to coastal areas and cherry blossom-lined streets. Japan experiences four distinct seasons, each offering unique attractions, such as cherry blossoms in spring, vibrant festivals in summer, colorful foliage in autumn, and winter sports in northern regions.\r\n\r\nJapan is known for its technological advancements and innovations in various fields, including electronics, automotive manufacturing, and robotics. The country is also a leader in pop culture, with global influences in anime, manga, fashion, and music.',44,'2024-08-04','2024-10-03',1419,'c8ed3024-4837-4080-b521-c2070e8339eb.png'),(65,'Tajikistan, a captivating gem in Central Asia, is renowned for its breathtaking natural beauty and rich cultural heritage. Dominated by towering mountain ranges, including the majestic Pamirs, it offers a paradise for adventurers and nature enthusiasts. The Pamir Highway, one of the world\'s highest roads, provides an unparalleled journey through spectacular landscapes and traditional villages.\r\n\r\nDushanbe, the capital, is a vibrant city blending modernity with tradition. Its tree-lined avenues, bustling bazaars, and historical monuments, like the National Museum and the Haji Yakoub Mosque, offer a glimpse into the country\'s past and present. The people of Tajikistan are known for their warm hospitality and diverse cultural traditions, with influences from Persian, Russian, and Silk Road heritage.\r\n\r\nTajikistan\'s natural wonders include crystal-clear lakes such as Iskanderkul and Karakul, as well as verdant valleys like the Fann Mountains, ideal for trekking and exploration. The country\'s cuisine, rich in flavors and spices, reflects its diverse cultural tapestry, offering delights such as plov, kebabs, and fresh fruits. Tajikistan is a land of stunning contrasts and enduring traditions, inviting travelers to explore its unspoiled beauty and vibrant cultural life.',86,'2025-02-20','2025-03-03',719,'e673e90b-2016-42e4-8390-4f11cd4d43a7.png'),(69,'The Bahamas, an archipelago comprising around 700 islands and over 2,000 rocks and cays, is situated in the Atlantic Ocean. It lies southeast of Florida and north of Cuba. Known for its stunning beaches with crystal-clear turquoise waters and white sandy shores, the Bahamas is a prime destination for tourists seeking paradise-like getaways.\r\n\r\nNassau, the capital city located on New Providence Island, is a vibrant hub blending modern amenities with colonial charm. It offers attractions such as the Atlantis Paradise Island Resort, historic sites like Fort Charlotte, and lively markets. The Bahamas is also famous for its world-class diving and snorkeling sites, including the Andros Barrier Reef and Thunderball Grotto.\r\n\r\nThe nation\'s rich culture is a tapestry of African, British, and indigenous influences, celebrated through festivals like Junkanoo. The Bahamian economy heavily relies on tourism, but offshore finance also plays a significant role. With its warm climate, friendly locals, and breathtaking landscapes, the Bahamas remains a top choice for travelers worldwide.',8,'2025-08-21','2025-08-23',299,NULL),(71,'Costa Rica, located in Central America, is renowned for its stunning biodiversity and commitment to environmental conservation. Bordered by Nicaragua to the north and Panama to the south, this small country boasts a diverse landscape that includes lush rainforests, pristine beaches on both the Pacific and Caribbean coasts, and active volcanoes such as Arenal and Poás. Costa Rica is a haven for eco-tourists, offering a plethora of activities like zip-lining, surfing, hiking, and wildlife watching.\r\n\r\nThe capital city, San José, is the cultural and economic hub, featuring museums, theaters, and vibrant markets. Costa Rica’s dedication to sustainability is evident in its extensive network of protected areas, including national parks like Corcovado and Tortuguero, which protect unique species such as jaguars, sloths, and sea turtles.\r\n\r\nKnown for its friendly locals, or \"Ticos,\" and a high standard of living, Costa Rica stands out as a beacon of peace and stability in the region. Its emphasis on education and healthcare contributes to its status as one of the happiest countries in the world. Costa Rica\'s motto, \"Pura Vida,\" encapsulates its laid-back, positive lifestyle.\r\n\r\n\r\n\r\n\r\n\r\n\r\n',21,'2026-02-03','2026-02-19',1022,NULL);
/*!40000 ALTER TABLE `vacations` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-08-02 12:40:45
