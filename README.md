# interactive clustering

The purpose of this app is to analyze the older adult population in the CAPTAIN system using interactive visualization 
techniques. It allows non-expert users to create clusters, visualize their patterns and follow up the evolution of 
those clusters after the stratification. It also allows final users to customize the relevance of every parameter or 
group (nutrition, social, physical, and cognitive).

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

### Public Access

A publicly available version is running in the next url: 
[https://captain-elderly-evolution.herokuapp.com/](https://captain-elderly-evolution.herokuapp.com/)
