ALTER TABLE `curw_fcst`.`run`
DROP FOREIGN KEY `run_ibfk_1`,
DROP FOREIGN KEY `run_ibfk_2`,
DROP FOREIGN KEY `run_ibfk_3`,
DROP FOREIGN KEY `run_ibfk_4`;
ALTER TABLE `curw_fcst`.`run`
ADD CONSTRAINT `run_ibfk_1`
  FOREIGN KEY (`station`)
  REFERENCES `curw_fcst`.`station` (`id`)
  ON DELETE RESTRICT
  ON UPDATE CASCADE,
ADD CONSTRAINT `run_ibfk_2`
  FOREIGN KEY (`source`)
  REFERENCES `curw_fcst`.`source` (`id`)
  ON DELETE RESTRICT
  ON UPDATE CASCADE,
ADD CONSTRAINT `run_ibfk_3`
  FOREIGN KEY (`variable`)
  REFERENCES `curw_fcst`.`variable` (`id`)
  ON DELETE RESTRICT
  ON UPDATE CASCADE,
ADD CONSTRAINT `run_ibfk_4`
  FOREIGN KEY (`unit`)
  REFERENCES `curw_fcst`.`unit` (`id`)
  ON DELETE RESTRICT
  ON UPDATE CASCADE;


ALTER TABLE `curw_fcst`.`data`
DROP FOREIGN KEY `data_ibfk_1`;
ALTER TABLE `curw_fcst`.`data`
ADD CONSTRAINT `data_ibfk_1`
  FOREIGN KEY (`id`)
  REFERENCES `curw_fcst`.`run` (`id`)
  ON DELETE RESTRICT
  ON UPDATE CASCADE;
