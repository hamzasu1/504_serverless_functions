# Multi-Cloud-Serverless



## Zoom Link

https://stonybrook.zoom.us/rec/share/i7XPa8MHIW4036iICDabomQ9zpqAV29Z4dFdYuM5n1zCvUja76MJDVGTKyjmnj9U.KoP_-4LtJhAr9Ykz?startTime=1760839484000
Passcode: dkz5gR3^

This is the video demonstrating utilizing both clouds for this multicloud assignment



## Cloud links

Microsoft azure url : serverless-ajd4gwbeczh8enbp.eastus2-01.azurewebsites.net
Region used: eastus2 (public)
Google cloud url : https://cloud-server-653261614201.europe-west1.run.app/
Region used: europe-west1 (public)

## Overview

This project implements the HTTP serverless accross two clouds- google cloud and microsoft azure. I will be utilized these two
clouds to deploy and test the fasting glucose function based on the American Diabetes reference. The goal was to deploy different 
functions on different cloud platforms

While my Google cloud deployement was successful and produced valid responses, I encountered an issue with Microsoft azure. 
Initially the test run section would even open but it did open in the video. The Python code seemed fine and I had looked it over multiple times.
I Could not identify the issue and tried different making small changes which did not work

## Summary of the tests

The test input would be 

Test #1

"glucose_mg_dl": 95
The output for this would be a status of "normal"


Test #2

"glucose_mg_dl": 130
The output for this would be a status of "abnormal"



## Comparison of the two clouds

I thought gcps cloud was more simple and easier to navigate. I thought azures was a bit more difficult and more troubleshooting. As I stated earlier my test run was not working initially. My google cloud portion was fully functional and was demonstrated in this video.



## Lab Rules

The lab that I have chosen is fasting glucose.

Normal = Less than 100 mg/dL

Prediabetes = 100 mg/dL to 125 mg/dL

Diabetes = 126 mg/dL or higher than that


## Reference

American Diabetes Association. (n.d.). Diabetes Diagnosis & Tests. Retrieved from https://diabetes.org/about-diabetes/diagnosis



## Github problems
I'm not sure with my git commit did not save on when I initially commited this so I redid my readme file and hopefully it commits.
I will try to office hours with Mo to fix my github commiting issues























