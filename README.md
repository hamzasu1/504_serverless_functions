# Multi-Cloud-Serverless

I am currently having difficulties pushing files on vs onto my github with my windows pc but it works on my macbook.




## Lab Rules

The lab that I have chosen is fasting glucose.
Normal = Less than 100 mg/dL
Prediabetes = 100 mg/dL to 125 mg/dL
Diabetes = 126 mg/dL or higher than that

Citation
American Diabetes Association. (n.d.). Diabetes Diagnosis & Tests. Retrieved from https://diabetes.org/about-diabetes/diagnosis


## Recording:
https://stonybrook.zoom.us/rec/share/i7XPa8MHIW4036iICDabomQ9zpqAV29Z4dFdYuM5n1zCvUja76MJDVGTKyjmnj9U.KoP_-4LtJhAr9Ykz?startTime=1760839484000
Passcode: dkz5gR3^



Cloud enviornments used were google cloud with a cloud functions gen 2 server. The region was europewest1. The authentication was a public access.
Microsoft azure was also utilized in this assignment. Both versions accept JSON or input labeled "fasting_glucose_mg-dL" and returned a structured
JSON response as either : Normal, Prediabetes, Diabetes. The lab rules above provide the ranges of each value. For deployement, a 
