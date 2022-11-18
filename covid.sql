-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 17, 2022 at 07:10 PM
-- Server version: 10.1.38-MariaDB
-- PHP Version: 7.3.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pythonproj`
--

-- --------------------------------------------------------

--
-- Table structure for table `covid`
--

CREATE TABLE `covid` (
  `ID` int(11) NOT NULL,
  `patientname` varchar(20) NOT NULL,
  `mobile` varchar(12) NOT NULL,
  `email` varchar(50) NOT NULL,
  `address` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `covid`
--

INSERT INTO `covid` (`ID`, `patientname`, `mobile`, `email`, `address`) VALUES
(1, 'deepika', '683734333', 'deepika@gmail.com', 'srivilliputtur'),
(2, 'bala', '685656856', 'bala1401@gmail.com', 'banglore'),
(3, 'uma', '978767656', 'umaneela@gmail.com', 'coimbatore'),
(4, 'kali', '68585787', 'kaliammal@gmail.com', 'srivi'),
(5, 'Muniyandi', '65657878', 'muniyandi@gmail.com', 'srivi'),
(7, 'raja', '876565454', 'raja43@gmail.com', 'rajapalayam'),
(8, 'nandhini', '877665644', 'nandini34@gmail.com', 'sivakasi'),
(10, 'sheela', '765765544', 'sheela@gmail.com', 'sivapuram'),
(11, 'diwana', '765655545', 'diwana@gmail.com', 'chennai'),
(12, 'iliyana', '87665545', 'iliyana@gmail.com', 'madurai'),
(13, 'Shivangi', '854854454', 'shivangikrish@gmail.com', 'chennai'),
(14, 'Sunganya', '6858677554', 'suganya@gmail.com', 'srivi');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `covid`
--
ALTER TABLE `covid`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `covid`
--
ALTER TABLE `covid`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
