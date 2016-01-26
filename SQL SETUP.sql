-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema redbeltdb2
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema redbeltdb2
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `redbeltdb2` DEFAULT CHARACTER SET utf8 ;
USE `redbeltdb2` ;

-- -----------------------------------------------------
-- Table `redbeltdb2`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `redbeltdb2`.`users` (
  `id` INT(11) NOT NULL AUTO_INCREMENT COMMENT '',
  `name` VARCHAR(100) NULL DEFAULT NULL COMMENT '',
  `username` VARCHAR(45) NULL DEFAULT NULL COMMENT '',
  `date_hired` DATETIME NULL DEFAULT NULL COMMENT '',
  `pass_hash` VARCHAR(255) NULL DEFAULT NULL COMMENT '',
  `created_at` DATETIME NULL DEFAULT NULL COMMENT '',
  `updated_at` DATETIME NULL DEFAULT NULL COMMENT '',
  PRIMARY KEY (`id`)  COMMENT '')
ENGINE = InnoDB
AUTO_INCREMENT = 3
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `redbeltdb2`.`items`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `redbeltdb2`.`items` (
  `id` INT(11) NOT NULL AUTO_INCREMENT COMMENT '',
  `item` VARCHAR(100) NULL DEFAULT NULL COMMENT '',
  `created_at` DATETIME NULL DEFAULT NULL COMMENT '',
  `updated_at` DATETIME NULL DEFAULT NULL COMMENT '',
  `user_id` INT(11) NOT NULL COMMENT '',
  PRIMARY KEY (`id`, `user_id`)  COMMENT '',
  INDEX `fk_items_users_idx` (`user_id` ASC)  COMMENT '',
  CONSTRAINT `fk_items_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `redbeltdb2`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 9
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `redbeltdb2`.`wishlists`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `redbeltdb2`.`wishlists` (
  `id` INT(11) NOT NULL AUTO_INCREMENT COMMENT '',
  `user_id` INT(11) NOT NULL COMMENT '',
  `item_id` INT(11) NOT NULL COMMENT '',
  PRIMARY KEY (`id`, `user_id`, `item_id`)  COMMENT '',
  INDEX `fk_wishlists_users1_idx` (`user_id` ASC)  COMMENT '',
  INDEX `fk_wishlists_items1_idx` (`item_id` ASC)  COMMENT '',
  CONSTRAINT `fk_wishlists_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `redbeltdb2`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_wishlists_items1`
    FOREIGN KEY (`item_id`)
    REFERENCES `redbeltdb2`.`items` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 11
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
