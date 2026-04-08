# Quick Start Guide

## Setting Up BigQuery Data
1. **Create a Google Cloud Project**: Go to the Google Cloud Console and create a new project.
2. **Enable BigQuery API**: Enable the BigQuery API for your project.
3. **Create a Dataset**: Within BigQuery, create a new dataset to hold your tables.
4. **Load Data**: Load your data into the dataset using the BigQuery UI, CLI, or API.

## Configuring dbt
1. **Install dbt**: If you haven't already, install dbt using pip:
   ```bash
   pip install dbt-bigquery
   ```
2. **Create a dbt Profile**: In your `~/.dbt/profiles.yml` file, add your BigQuery connection settings:
   ```yaml
   your_project:
     target: dev
     outputs:
       dev:
         type: bigquery
         project: your_gcp_project
         dataset: your_dataset
         threads: 1
         keyfile: /path/to/your/service_account.json
   ```
3. **Initialize a dbt Project**: In your terminal, navigate to your project directory and run:
   ```bash
   dbt init your_project_name
   ```

## Running Models
1. **Build Models**: Create `.sql` files in the `models` directory of your dbt project.
2. **Run dbt**: To run your models, execute:
   ```bash
   dbt run
   ```
3. **Check Models**: To test your models, use:
   ```bash
   dbt test
   ```

## Conclusion
Follow these steps to quickly set up your BigQuery data and utilize dbt for your analytics workflow. For more detailed documentation, visit the [dbt documentation](https://docs.getdbt.com/).