CREATE TABLE `Item`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    `user_id` BIGINT NOT NULL,
    `owner_` BIGINT NOT NULL
);
ALTER TABLE
    `Item` ADD PRIMARY KEY `item_id_primary`(`id`);
CREATE TABLE `User`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(255) NOT NULL,
    `items_` BIGINT NOT NULL
);
ALTER TABLE
    `User` ADD PRIMARY KEY `user_id_primary`(`id`);
ALTER TABLE
    `Item` ADD CONSTRAINT `item_user_id_foreign` FOREIGN KEY(`user_id`) REFERENCES `User`(`id`);