In this project, there are three steps:

## collect data
There is a scrapy project in collector directory. It collects data from [quera problemset](https://quera.org/problemset) and store them in a csv file, each row is details of a problem. The csv file of this project is [here](https://drive.google.com/file/d/1eyvUOll3CUkxa6aw2S20AYZlb1FroB0J/view?usp=sharing).

## store collected data in database
In save_data.py, data is read from csv file and written in a sql table.

## use stored data in other projects
Stored data can be used in other projects. In this project, data is used in choose_level.py, where you can choose a difficulty level(Easy/Medium/Hard) and link of problems with choosen difficulty is returned.

