CREATE TABLE `Items`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    `user_id` BIGINT NOT NULL,
    `owner_` BIGINT NOT NULL
);
ALTER TABLE
    `Items` ADD PRIMARY KEY `items_id_primary`(`id`);
CREATE TABLE `User`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(255) NOT NULL,
    `items_` BIGINT NOT NULL
);
ALTER TABLE
    `User` ADD PRIMARY KEY `user_id_primary`(`id`);
ALTER TABLE
    `Items` ADD CONSTRAINT `items_user_id_foreign` FOREIGN KEY(`user_id`) REFERENCES `User`(`id`);