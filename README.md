# Automated Notebook Project

The script automatically generates jupyter notebook using the GEO dataset information provided.

### Prerequisites

The script and the jupyter notebook are running on a Docker container. You can learn about Docker and install it here by following the link below:

[Installing Docker](https://docs.docker.com/engine/installation/)

The necessary scripts are provided in folders scripts and gloriiascripts.

### Excel file format

An excel file provided must follow specific formating guidlines. An example of such excel file is provided below.

| sample_gse_id   | platform | control_samples |experimental_samples|
| :---            |     :---:|            ---: |    :---:    |
|GSE86956         | GPL16791 | GSM2310987\|GSM2310988\|GSM2310989|GSM2310993\|GSM2310994\|GSM2310995|
|GSE44461         | GPL11154 | GSM1085736\|GSM1085737\|GSM1085738|GSM1085739\|GSM1085740\|GSM1085741|

You can only provide one set of control and one set of experimental samples; however, the number of samples within the group is not restricted.

### Running the script and generating notebooks

* Run the Docker container

[Running Docker](https://docs.docker.com/engine/reference/commandline/run/)

* If you want to data to persist while using Docker, the folder on the local machine can be mounted to the docker container.

[Mounting Volumes with Docker](https://docs.docker.com/engine/admin/volumes/volumes/#create-and-manage-volumes)

* Open the generate_notebook.ipynb and run the cell by clicking Cells and Run Cells. (Notice that the filename provided is "sample_data.xlsx". You can edit the existing excel file or create a new file with the desired datasets information. You will need to change the filename in the script if using a new file).

* The generated notebooks should appear in the current directory. The notebook are named in the following manner: Automated_Notebook_GSEnumber_platform.ipynb

* If some of the widgets do not show up, click Cells and Run All to reload the cells.

* The notebook can be edited in any desired manner. 


### Automated Notebook Example

An example of the automated notebook can be found [here](http://nbviewer.jupyter.org/github/gnovikov/rna_seq_analysis/blob/master/Automated_Notebook_GSE44461_GPL11154.ipynb).


# Reanalysis of existing RNA-seq datasets deposited to GEO
