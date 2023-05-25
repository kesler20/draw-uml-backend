CREATE TABLE `files`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `filename` VARCHAR(255) NOT NULL,
    `resource_id` VARCHAR(255) NOT NULL,
    `owner_id` INT NOT NULL,
    `size` INT NOT NULL,
    `created_at` DATETIME NOT NULL
);
ALTER TABLE
    `files` ADD PRIMARY KEY(`id`);
CREATE TABLE `notifications`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `description` VARCHAR(255) NOT NULL,
    `title` VARCHAR(255) NOT NULL,
    `short_description` VARCHAR(255) NOT NULL,
    `created_at` DATETIME NOT NULL
);
ALTER TABLE
    `notifications` ADD PRIMARY KEY(`id`);
CREATE TABLE `roles`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(255) NOT NULL
);
ALTER TABLE
    `roles` ADD PRIMARY KEY(`id`);
CREATE TABLE `users`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `username` VARCHAR(255) NOT NULL,
    `email` VARCHAR(255) NOT NULL,
    `role_id` INT NOT NULL,
    `laboratory_id` INT NOT NULL,
    `tutorial_completed` TINYINT(1) NOT NULL,
    `notifications_read` TINYINT(1) NOT NULL
);
ALTER TABLE
    `users` ADD PRIMARY KEY(`id`);
CREATE TABLE `lab_equipments`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `laboratory_id` INT NOT NULL,
    `user_id` INT NOT NULL
);
ALTER TABLE
    `lab_equipments` ADD PRIMARY KEY(`id`);
CREATE TABLE `sensors`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `topic` VARCHAR(255) NOT NULL,
    `lab_equipments_id` INT NOT NULL
);
ALTER TABLE
    `sensors` ADD PRIMARY KEY(`id`);
CREATE TABLE `dashboards`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `resource_id` VARCHAR(255) NOT NULL,
    `author_id` INT NOT NULL,
    `created_at` DATETIME NOT NULL
);
ALTER TABLE
    `dashboards` ADD PRIMARY KEY(`id`);
CREATE TABLE `laboratories`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(255) NOT NULL,
    `location` VARCHAR(255) NOT NULL
);
ALTER TABLE
    `laboratories` ADD PRIMARY KEY(`id`);
CREATE TABLE `process_data_records`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `recording_from` DATETIME NOT NULL,
    `recording_to` DATETIME NOT NULL,
    `sensor_id` INT NOT NULL
);
ALTER TABLE
    `process_data_records` ADD PRIMARY KEY(`id`);
ALTER TABLE
    `sensors` ADD CONSTRAINT `sensors_lab_equipments_id_foreign` FOREIGN KEY(`lab_equipments_id`) REFERENCES `lab_equipments`(`id`);
ALTER TABLE
    `process_data_records` ADD CONSTRAINT `process_data_records_sensor_id_foreign` FOREIGN KEY(`sensor_id`) REFERENCES `sensors`(`id`);
ALTER TABLE
    `files` ADD CONSTRAINT `files_owner_id_foreign` FOREIGN KEY(`owner_id`) REFERENCES `users`(`id`);
ALTER TABLE
    `dashboards` ADD CONSTRAINT `dashboards_author_id_foreign` FOREIGN KEY(`author_id`) REFERENCES `users`(`id`);
ALTER TABLE
    `lab_equipments` ADD CONSTRAINT `lab_equipments_laboratory_id_foreign` FOREIGN KEY(`laboratory_id`) REFERENCES `laboratories`(`id`);
ALTER TABLE
    `users` ADD CONSTRAINT `users_role_id_foreign` FOREIGN KEY(`role_id`) REFERENCES `roles`(`id`);
ALTER TABLE
    `users` ADD CONSTRAINT `users_laboratory_id_foreign` FOREIGN KEY(`laboratory_id`) REFERENCES `laboratories`(`id`);