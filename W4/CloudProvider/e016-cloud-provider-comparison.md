# Exercise: Cloud Provider Research and Comparison

## Overview

In this exercise, you will research and compare the three major cloud providers (AWS, Azure, GCP) with a focus on their data services. This exercise reinforces the cloud computing concepts covered in today's written content.

## Learning Objectives

- Compare cloud provider offerings for data services
- Evaluate trade-offs between different cloud platforms
- Practice structured technical analysis and documentation
- Develop decision-making skills for cloud platform selection

## Exercise Mode: Conceptual (Design/Analysis)

This is a research and analysis exercise. No coding is required.

## The Scenario

Your company is a mid-sized e-commerce retailer planning to migrate their on-premises data infrastructure to the cloud. They need to:

1. Store transactional data from their PostgreSQL database
2. Build a data warehouse for business analytics
3. Process daily batch jobs for inventory management
4. Store product images and customer documents
5. Eventually implement real-time analytics for fraud detection

Leadership has asked you to evaluate AWS, Azure, and GCP and provide a recommendation.

## Deliverables

### Part 1: Service Mapping Matrix (30 minutes)

Create a comparison table mapping the company's needs to specific services from each provider.

| Requirement | AWS Service | Azure Service | GCP Service |
|-------------|-------------|---------------|-------------|
| Managed PostgreSQL | RDS/Aurora | Azure DB | Cloud SQL |
| Data Warehouse | Redshift | Synapse Analytics | BigQuery |
| Batch Processing | AWS Batch | Azure Batch | GCP Batch  |
| Object Storage | S3 | Blob Storage | Cloud Storage |
| Stream Processing | Kinesis | Stream Analytics | Dataflow |

### Part 2: Cost Analysis (30 minutes)

Using each provider's pricing calculator, estimate monthly costs for:

- 500 GB of data warehouse storage
- 10 TB of object storage
- 1000 compute hours per month

| Requirement | AWS Service | Azure Service | GCP Service |
|-------------|-------------|---------------|-------------|
| Calculator Link | [AWS Calculator](https://calculator.aws/#/) | [Azure Calculator](https://azure.microsoft.com/en-us/pricing/calculator/?ef_id=_k_Cj0KCQjwve7NBhC-ARIsALZy9HWoIW6C_bTxz6eEMMFHg1Jrp20JkEXxj8X5Ezq8OVsh4oS9ucllnCMaAtwMEALw_wcB_k_&OCID=AIDcmm83ywnuwb_SEM_k_Cj0KCQjwve7NBhC-ARIsALZy9HWoIW6C_bTxz6eEMMFHg1Jrp20JkEXxj8X5Ezq8OVsh4oS9ucllnCMaAtwMEALw_wcB&utm_source=google&utm_medium=cpc&utm_campaign=23555152752&utm_adgroup=196337746754&utm_term=kwd-310354828215&utm_content=797207936136&gad_source=1&gad_campaignid=23555152752&gbraid=0AAAABCZrPITWzdIlWm4H87GV-n4i1TrY9&gclid=Cj0KCQjwve7NBhC-ARIsALZy9HWoIW6C_bTxz6eEMMFHg1Jrp20JkEXxj8X5Ezq8OVsh4oS9ucllnCMaAtwMEALw_wcB) | [GCP Calculator](https://cloud.google.com/products/calculator?hl=en) |
| 500 GB DW | $12.00 | $11.50 | $11.27 |
| 10 TB Object | $235.52 | $212.99 | $204.70 |
| *1000 Computer hr/mon | $4.20 | $14.00 | $33.58 | 
*not well researched

Document your findings with links to the pricing pages you used.

### Part 3: Recommendation Report (1 hour)

Write a 1-2 page recommendation report that includes:

1. **Executive Summary** (2-3 sentences)
2. **Evaluation Criteria** (list 5 factors you considered)
3. **Provider Comparison** (strengths/weaknesses of each)
4. **Recommendation** (which provider and why)
5. **Migration Considerations** (3 potential challenges)

## Definition of Done

- Completed service mapping matrix with all 15 cells filled
- Cost estimates with documented sources
- Recommendation report with all 5 sections
- Clear, professional writing without jargon overload

## Submission

Save your deliverables as:

- `service-mapping.md` - The comparison table
- `cost-analysis.md` - Cost estimates with sources
- `recommendation-report.md` - Your final recommendation

## Time Estimate

2-3 hours

## Resources

- AWS Pricing Calculator: <https://calculator.aws/>
- Azure Pricing Calculator: <https://azure.microsoft.com/en-us/pricing/calculator/>
- GCP Pricing Calculator: <https://cloud.google.com/products/calculator>
- Written Content: c153-c164 (Cloud Computing)

## Rubric

| Criteria | Points |
|----------|--------|
| Service mapping accuracy | 25 |
| Cost analysis completeness | 25 |
| Recommendation reasoning | 30 |
| Professional presentation | 20 |
| **Total** | **100** |
