CREATE TABLE `chatgpt_qa_corpus` (
  `id` int NOT NULL AUTO_INCREMENT,
  `word` varchar(45) DEFAULT NULL,
  `corpus` varchar(45) DEFAULT NULL,
  `type` varchar(45) DEFAULT NULL,
  `qa_id` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=600786 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

CREATE TABLE `chatgpt_question_answer` (
  `title` text,
  `question` text,
  `reply` text,
  `is_best` int DEFAULT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  `ai_reply` text,
  `is_valid` varchar(45) DEFAULT '0',
  `human_ppl` varchar(45) DEFAULT NULL,
  `ai_ppl` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=144958 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci