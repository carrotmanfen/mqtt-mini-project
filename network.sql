-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Mar 03, 2023 at 03:38 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `network`
--

-- --------------------------------------------------------

--
-- Table structure for table `sensor_data`
--

CREATE TABLE `sensor_data` (
  `Time` text NOT NULL,
  `NodeID` varchar(100) NOT NULL,
  `Humidity` text NOT NULL,
  `Temperature` text NOT NULL,
  `Thermal` mediumtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `sensor_data`
--

INSERT INTO `sensor_data` (`Time`, `NodeID`, `Humidity`, `Temperature`, `Thermal`) VALUES
('2022-11-08 12:08:00', 'Node3', '55.82', '29.16', '31.5,31.6,31.9,32.0,31.6,30.9,31.5,31.4,31.1,31.1,31.2,31.2,31.3,31.2,31.0,31.1,31.5,30.7,31.1,31.2,31.1,30.8,31.1,31.1,31.2,30.9,31.1,31.6,31.4,31.3,31.3,31.3,31.8,31.3,32.0,31.1,32.1,31.3,31.3,31.1,31.4,31.1,31.4,31.4,31.3,30.9,31.3,31.1,31.3,31.1,31.3,30.9,30.8,31.1,31.1,31.0,31.4,31.3,31.3,31.4,31.4,31.1,31.5,31.4,');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
