from config import TABLE_FIN

table_creation = f"""CREATE TABLE IF NOT EXIST `anneurism`.`{TABLE_FIN}` (
  `index` BIGINT NOT NULL AUTO_INCREMENT,
  `uid` TEXT NULL,
  `names` TEXT NULL,
  `birthdate` TEXT NULL,
  `phone` TEXT NULL,
  `address` TEXT NULL,
  PRIMARY KEY (`index`),
  UNIQUE INDEX `new_tablecol_UNIQUE` (`index` ASC) VISIBLE);"""
