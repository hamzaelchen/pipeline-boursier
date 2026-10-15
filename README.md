# Pipeline boursier temps réel

Pipeline de données qui rejoue des cours boursiers comme un flux
temps réel, les transforme et les stocke dans un data lake.

## Objectif
Apprendre et démontrer les bases du data engineering : ingestion,
streaming, transformation, stockage, orchestration.

## Architecture visée
Dataset (CSV) -> Producer Python -> Kafka -> Spark -> S3

## Stack
Python, Kafka, Spark, AWS S3, Docker, PostgreSQL

## Statut
- [ ] Lecture du CSV en Python
- [ ] Producer qui envoie les lignes dans Kafka
- [ ] Transformation avec Spark
- [ ] Stockage sur S3
- [ ] Orchestration avec Airflow

## Auteur
Hamza El Alami, étudiant ingénieur DATA/IA à l'EMSI Casablanca
