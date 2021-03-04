# interactive clustering

This is the streamlit code.
It is to let non expert users to create clusters, visualize the patterns of each cluster and see the evolution of the clusters the after stratification.
It allows to give different weight to each parameter or group (nutrition, social, etc.)

## Launch up

### Standalone

streamlit run main.py


### Docker


#### Requirements
* [Docker](https://www.docker.com/get-started) running into your machine.
* Port 8501 has to be available in your local machine.

#### Create image
> docker build -t img_interactive_clustering .

#### Run image into container
> docker run -d --rm -p 8501:8501 --name interactive_clustering img_interactive_clustering

#### Access the app through your browser
http://localhost:8501/

#### Stop container
> docker stop interactive_clustering

### The data is missing in git, just in case (Anonimity)
Extract zip file located [here](https://vicomtech.app.box.com/folder/123265650833) into data folder.
