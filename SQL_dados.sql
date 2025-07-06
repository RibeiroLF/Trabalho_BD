-- MySQL dump 10.13  Distrib 8.0.42, for Win64 (x86_64)
--
-- Host: mysql-controle-ru-controle-ru.k.aivencloud.com    Database: defaultdb
-- ------------------------------------------------------
-- Server version	8.0.35

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
SET @MYSQLDUMP_TEMP_LOG_BIN = @@SESSION.SQL_LOG_BIN;
SET @@SESSION.SQL_LOG_BIN= 0;

--
-- GTID state at the beginning of the backup 
--

SET @@GLOBAL.GTID_PURGED=/*!80000 '+'*/ '98fb272c-59b0-11f0-b544-862ccfb03492:1-133';

--
-- Dumping data for table `bebidas`
--

LOCK TABLES `bebidas` WRITE;
/*!40000 ALTER TABLE `bebidas` DISABLE KEYS */;
INSERT INTO `bebidas` VALUES (1,'Leite Integral'),(2,'Suco de Laranja'),(3,'Suco de Limão'),(4,'Suco de Abacaxi'),(5,'Suco de Uva');
/*!40000 ALTER TABLE `bebidas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `bebidas_fornecedores`
--

LOCK TABLES `bebidas_fornecedores` WRITE;
/*!40000 ALTER TABLE `bebidas_fornecedores` DISABLE KEYS */;
INSERT INTO `bebidas_fornecedores` VALUES (1,1),(2,2),(3,3),(4,4),(5,5);
/*!40000 ALTER TABLE `bebidas_fornecedores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `buffet`
--

LOCK TABLES `buffet` WRITE;
/*!40000 ALTER TABLE `buffet` DISABLE KEYS */;
INSERT INTO `buffet` VALUES (1,'2025-01-01',NULL,'Café da Manhã'),(2,'2025-01-01','2025-03-31','Almoço'),(3,'2025-01-01','2025-03-31','Jantar'),(4,'2025-04-01',NULL,'Almoço'),(5,'2025-04-01',NULL,'Jantar');
/*!40000 ALTER TABLE `buffet` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `buffet_bebidas`
--

LOCK TABLES `buffet_bebidas` WRITE;
/*!40000 ALTER TABLE `buffet_bebidas` DISABLE KEYS */;
INSERT INTO `buffet_bebidas` VALUES (1,1),(2,2),(3,3),(4,4),(5,5);
/*!40000 ALTER TABLE `buffet_bebidas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `buffet_pratos`
--

LOCK TABLES `buffet_pratos` WRITE;
/*!40000 ALTER TABLE `buffet_pratos` DISABLE KEYS */;
INSERT INTO `buffet_pratos` VALUES (1,1),(2,2),(3,3),(4,4),(5,5);
/*!40000 ALTER TABLE `buffet_pratos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `dependentes`
--

LOCK TABLES `dependentes` WRITE;
/*!40000 ALTER TABLE `dependentes` DISABLE KEYS */;
INSERT INTO `dependentes` VALUES (98765432100,'Amim Amou Amado','61912345678'),(98765432101,'Céu Azul do Sol Poente','61912345678'),(98765432102,'Ilegível Inilegível','61912345678'),(98765432103,'Mangelstron','61912345678'),(98765432104,'Tospericagerja','61912345678');
/*!40000 ALTER TABLE `dependentes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `estoque_ingredientes`
--

LOCK TABLES `estoque_ingredientes` WRITE;
/*!40000 ALTER TABLE `estoque_ingredientes` DISABLE KEYS */;
INSERT INTO `estoque_ingredientes` VALUES (1,10),(2,20),(3,30),(4,40),(5,50);
/*!40000 ALTER TABLE `estoque_ingredientes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `fornecedores`
--

LOCK TABLES `fornecedores` WRITE;
/*!40000 ALTER TABLE `fornecedores` DISABLE KEYS */;
INSERT INTO `fornecedores` VALUES (1,'Fornecedor 1','61988887777','2025-01-01',NULL),(2,'Fornecedor 2','61988887777','2025-01-01',NULL),(3,'Fornecedor 3','61988887777','2025-01-01',NULL),(4,'Fornecedor 4','61988887777','2025-01-01',NULL),(5,'Fornecedor 5','61988887777','2025-01-01',NULL);
/*!40000 ALTER TABLE `fornecedores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `funcionarios`
--

LOCK TABLES `funcionarios` WRITE;
/*!40000 ALTER TABLE `funcionarios` DISABLE KEYS */;
INSERT INTO `funcionarios` VALUES (12345678900,'Fulano de Tal','Masculino','1980-01-01','DF','Brasília','Rua 1','Bairro Qualquer','61998765432'),(12345678901,'Siclano','Masculino','1979-05-09','DF','Brasília','Rua 2','Bairro Qualquer Um','61901234567'),(12345678902,'Bestrano','Masculino','1989-05-09','DF','Brasília','Rua 3','Bairro Aleatório','61912345698'),(12345678903,'Fulana','Feminino','1987-02-09','DF','Brasília','Rua 4','Bairro Aleatório','61955558888'),(12345678904,'Siclana','Feminino','1989-06-09','DF','Brasília','Rua 5','Bairro Aleatório','61955557778');
/*!40000 ALTER TABLE `funcionarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `funcionarios_buffet`
--

LOCK TABLES `funcionarios_buffet` WRITE;
/*!40000 ALTER TABLE `funcionarios_buffet` DISABLE KEYS */;
INSERT INTO `funcionarios_buffet` VALUES (12345678901,1),(12345678901,2),(12345678901,3),(12345678901,4),(12345678901,5);
/*!40000 ALTER TABLE `funcionarios_buffet` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `funcionarios_dependentes`
--

LOCK TABLES `funcionarios_dependentes` WRITE;
/*!40000 ALTER TABLE `funcionarios_dependentes` DISABLE KEYS */;
INSERT INTO `funcionarios_dependentes` VALUES (12345678900,98765432100,'2025-01-01',NULL),(12345678901,98765432101,'2025-01-01',NULL),(12345678902,98765432102,'2025-01-01',NULL),(12345678903,98765432103,'2025-01-01',NULL),(12345678904,98765432104,'2025-01-01',NULL);
/*!40000 ALTER TABLE `funcionarios_dependentes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `funcionarios_funcoes`
--

LOCK TABLES `funcionarios_funcoes` WRITE;
/*!40000 ALTER TABLE `funcionarios_funcoes` DISABLE KEYS */;
INSERT INTO `funcionarios_funcoes` VALUES (12345678900,1,'2025-01-01',NULL),(12345678901,2,'2025-01-01',NULL),(12345678902,3,'2025-01-01',NULL),(12345678903,4,'2025-01-01',NULL),(12345678904,5,'2025-01-01',NULL);
/*!40000 ALTER TABLE `funcionarios_funcoes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `funcionarios_situacoes`
--

LOCK TABLES `funcionarios_situacoes` WRITE;
/*!40000 ALTER TABLE `funcionarios_situacoes` DISABLE KEYS */;
INSERT INTO `funcionarios_situacoes` VALUES (12345678900,1,'2025-01-01',NULL),(12345678901,1,'2025-01-01',NULL),(12345678902,1,'2025-01-01',NULL),(12345678903,1,'2025-01-01',NULL),(12345678904,1,'2025-01-01',NULL);
/*!40000 ALTER TABLE `funcionarios_situacoes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `funcoes`
--

LOCK TABLES `funcoes` WRITE;
/*!40000 ALTER TABLE `funcoes` DISABLE KEYS */;
INSERT INTO `funcoes` VALUES (1,'Gerente'),(2,'Atendente'),(3,'Cozinheiro'),(4,'Auxiliar'),(5,'Faxineiro');
/*!40000 ALTER TABLE `funcoes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `ingredientes`
--

LOCK TABLES `ingredientes` WRITE;
/*!40000 ALTER TABLE `ingredientes` DISABLE KEYS */;
INSERT INTO `ingredientes` VALUES (1,'Pão','Unidade'),(2,'Feijão','Quilo'),(3,'Macarrão','Pacote'),(4,'Carne','Quilo'),(5,'Massa de Lasanha','Pacote');
/*!40000 ALTER TABLE `ingredientes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `ingredientes_compra`
--

LOCK TABLES `ingredientes_compra` WRITE;
/*!40000 ALTER TABLE `ingredientes_compra` DISABLE KEYS */;
INSERT INTO `ingredientes_compra` VALUES (1,'2025-01-01',10,100,1,1),(2,'2025-01-01',20,200,2,2),(3,'2025-01-01',30,300,3,3),(4,'2025-01-01',40,400,4,4),(5,'2025-01-01',50,500,5,5);
/*!40000 ALTER TABLE `ingredientes_compra` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `ingredientes_fornecedores`
--

LOCK TABLES `ingredientes_fornecedores` WRITE;
/*!40000 ALTER TABLE `ingredientes_fornecedores` DISABLE KEYS */;
INSERT INTO `ingredientes_fornecedores` VALUES (1,1),(2,2),(3,3),(4,4),(5,5);
/*!40000 ALTER TABLE `ingredientes_fornecedores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `pratos`
--

LOCK TABLES `pratos` WRITE;
/*!40000 ALTER TABLE `pratos` DISABLE KEYS */;
INSERT INTO `pratos` VALUES (1,'Pão com Manteiga','Frutas',NULL),(2,'Feijoada','Torta de Limão',NULL),(3,'Macarronada','Torta Holandesa',NULL),(4,'Churrasco','Bolo de Chocolate',NULL),(5,'Lasanha','Bolo de Morango',NULL);
/*!40000 ALTER TABLE `pratos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `pratos_ingredientes`
--

LOCK TABLES `pratos_ingredientes` WRITE;
/*!40000 ALTER TABLE `pratos_ingredientes` DISABLE KEYS */;
INSERT INTO `pratos_ingredientes` VALUES (1,1),(2,2),(3,3),(4,4),(5,5);
/*!40000 ALTER TABLE `pratos_ingredientes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `situacoes`
--

LOCK TABLES `situacoes` WRITE;
/*!40000 ALTER TABLE `situacoes` DISABLE KEYS */;
INSERT INTO `situacoes` VALUES (1,'Normal'),(2,'Férias'),(3,'Licença Saúde'),(4,'Licença Maternidade'),(5,'Abono');
/*!40000 ALTER TABLE `situacoes` ENABLE KEYS */;
UNLOCK TABLES;
SET @@SESSION.SQL_LOG_BIN = @MYSQLDUMP_TEMP_LOG_BIN;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-07-06 10:51:18
