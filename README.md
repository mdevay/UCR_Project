# Visualizing FBI Uniform Crime Reporting Data

## Improving the usability of publicly available data to make informed policy decisions

#### Matthew DeVay

## Exectutive Summary:

FBI UCR/NIBRS data is challenging to work with due to inconsistent formatting, obscure file formats, and complex hierarchies. As such, there is a need for tools to help inform data analysis and policy decisions. This project successfully created a data dashboard to visualize UCR/NIBRS data. Future improvements will attempt to use more granular/raw data to gain additional insights as well as potentially model the affects of policy changes.

## Problem Statement:

Criminal Justice Reform is a top priority for many US jurisdictions. Racial bias, lack of oversight, and qualified immunity help to perpetuate a culture of mistrust between police and the communities they patrol.

Drug charges in particular are an egregious example of this. Despite widespread acceptance by the medical community as therapeutic, and widespread majority popular support for ending prohibition, cannabis remains a schedule I drug. In the meantime, approximately 47% of drug arrests are Black or Latino, despite making up less than 32% of the population, and having similar incidence of usage as whites. Furthermore, nearly 20% of the prison population is incarcerated for drug charges, and drug offenders have high rates of recidivism due to the underlying root cause of addiction.

Drug policy is therefore a particularly appealing target for criminal justice reform: It has popular support, it eliminates or reduces sentencing for crimes that have high racial bias, and would reduce the load on an overcrowded prison system.

Unfortunately, there is a gap in clear, effectively presented data to inform policy changes to ammeliorate these problems. There are few sources of aggregated crime data, the most readily available and well documented being the FBI Uniform Crime Reporting/National Incident Reporting system. Furthermore, that data is published in formats that are challenging to manipulate in a data analysis or modeling context.

The aim of this project is to therefore create a proof of concept dashboard for visualizing UCR data, followed possibly by modeling to develop inferences on the impacts of cannabis decriminalization and legalization. Future iterations of this project may employ raw UCR data as opposed to the Excel summaries in order to take advantage of additional data features.

## Data

Data are prepared by the FBI UCR/NIBRS system. Data are voluntarily submitted to the program by individual agencies/jurisdictions. Data is estimated to cover approximately 80% of the population. Most major metropolitan agencies report, but not all. Most agencies that report are typically inclusive of the data the send, but some only report particularly crimes or categories of crimes.

Data are available as either Excel summary tables or raw "flat files." The raw data contain arrest level information, including demographics, dates, locations, circumstances, etc. The summary tables are aggregations of the arrests, and are significantly less granular and flexible.

## Process:

1. Import and clean data in python via Pandas
2. Amend data with cannabis policy status
3. Create data dashboard with Dash/Plotly
4. Perform EDA and analysis

## Results:

A proof of concept data dashboard was created via Dash/Plotly in python. Code for all data cleaning and the dashboard are included in this repo. Future iterations will use more granular data in order to extract additional insights, as well as model policy changes based on this data.
