-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema deliveries
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema deliveries
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `deliveries` DEFAULT CHARACTER SET utf8 ;
USE `deliveries` ;

-- -----------------------------------------------------
-- Table `deliveries`.`Riders`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `deliveries`.`Riders` (
  `idRiders` INT NOT NULL,
  PRIMARY KEY (`idRiders`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `deliveries`.`Orders`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `deliveries`.`Orders` (
  `idOrders` INT NOT NULL,
  `Riders_idRiders` INT NOT NULL,
  PRIMARY KEY (`idOrders`, `Riders_idRiders`),
  INDEX `fk_Orders_Riders_idx` (`Riders_idRiders` ASC) VISIBLE,
  CONSTRAINT `fk_Orders_Riders`
    FOREIGN KEY (`Riders_idRiders`)
    REFERENCES `deliveries`.`Riders` (`idRiders`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
